#Persistent
SetTimer, ProcurarImagem, 1000
return

ProcurarImagem:
; Converta a string Base64 em um bitmap
chapeuteste := "MCBQAE4ARwA="
BitmapFromBase64(BitLock, Type, chapeuteste, B64)
; Procurar pelo bitmap na tela
ImageSearch, foundX, foundY, 0, 0, A_ScreenWidth, A_ScreenHeight, *32 %B64%

; Verificar se a imagem foi encontrada
if (ErrorLevel = 0 && !(foundX = 0 && foundY = 0)) {
    MsgBox, Imagem encontrada nas coordenadas X: %foundX% Y: %foundY%
    ; Execute as ações que você deseja quando a imagem é encontrada aqui
} else {
    ; Execute as ações que você deseja quando a imagem não é encontrada aqui
}
return

BitmapFromBase64(BitLock, Type, B64){
    VarSetCapacity(B64Len, 0)
    , DllCall("Crypt32.dll\CryptStringToBinary", "Ptr", &B64, "UInt", StrLen(B64), "UInt", 0x01, "Ptr", 0, "UIntP", B64Len, "Ptr", 0, "Ptr", 0)
    , VarSetCapacity(B64Dec, B64Len, 0)
    , DllCall("Crypt32.dll\CryptStringToBinary", "Ptr", &B64, "UInt", StrLen(B64), "UInt", 0x01, "Ptr", &B64Dec, "UIntP", B64Len, "Ptr", 0, "Ptr", 0)
    , pStream := DllCall("Shlwapi.dll\SHCreateMemStream", "Ptr", &B64Dec, "UInt", B64Len, "UPtr")
    , DllCall("Gdiplus.dll\GdipCreateBitmapFromStream", "Ptr", pStream, "PtrP", pBitmap)
    , ObjRelease(pStream)
    if Type
    DllCall("Gdiplus.dll\GdipCreateHBITMAPFromBitmap", "UInt", pBitmap, "UInt*", hBitmap, "Int", 0XFFFFFFFF)
    , Gdip_DisposeImage(pBitmap)
    if (BitLock && !Type) {
    Gdip_GetImageDimensions(pBitmap,nWidth,nHeight)
    , Gdip_LockBits(pBitmap,0,0,nWidth,nHeight,nStride,nScan,nBitmapData)
    return Object := {Stride: nStride,Scan: nScan,Width: nWidth,Height: nHeight, Bitmap: (Type ? hBitmap : pBitmap)}
    } Else
    return Type ? hBitmap : pBitmap
    }
