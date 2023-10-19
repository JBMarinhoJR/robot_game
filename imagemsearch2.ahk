#NoEnv
#SingleInstance, Force
SendMode, Input
SetBatchLines, -1
SetWorkingDir, %A_ScriptDir%
#include ShinsImageScanClass.ahk

; Especifica o caminho da imagem que você está procurando
imagemPath := "C:\caminho\para\sua\imagem.png"

Loop
{
    ; Procura pela imagem na tela
    if (Image(imagemPath, 0.8, invX, invY)) {
        ; Se encontrou a imagem, clique nela
        Click, %invX%, %invY%
        
        ; Exibe um MsgBox com as coordenadas
        MsgBox, Imagem encontrada na posição: X=%invX%, Y=%invY%
        
        ; Aguarda um curto período de tempo antes de continuar a procurar
        Sleep, 1000 ; Espera 1 segundo (1000 milissegundos)
    } else {
        ; Se a imagem não foi encontrada, aguarde antes de tentar novamente
        Sleep, 500 ; Espera meio segundo (500 milissegundos)
    }
}