#NoEnv
#SingleInstance, Force
SendMode, Input
SetBatchLines, -1
SetWorkingDir, %A_ScriptDir%

Loop
{
    ; Espera até que a janela do Tibia com o título "Dear John" esteja ativa
    WinWaitActive, Tibia - Dear John
    Sleep, 2000  ; Aguarde 2 segundos para garantir que a janela esteja totalmente carregada

    ; Obtém as coordenadas do canto superior esquerdo e inferior direito da janela ativa
    WinGetPos, x, y, width, height, Tibia - Dear John

    ; Define o caminho da imagem a ser procurada
    imagemParaProcurar := "C:\Users\Junior\OneDrive\Documentos\robot_game\Features\chapeuteste.png"

    ; Procura pela imagem na região da janela ativa do Tibia
    ImageSearch, foundX, foundY, %x%, %y%, % (x + width), % (y + height), %imagemParaProcurar%

    ; Verifica se a imagem foi encontrada
    if (ErrorLevel = 0) {
        MsgBox, Imagem encontrada nas coordenadas X: %foundX% Y: %foundY%
        ; Aguarde um segundo antes de continuar para evitar busca muito rápida
        Sleep, 1000
    } else {
        MsgBox, Imagem não encontrada na janela do Tibia.
        ; Aguarde um segundo antes de tentar novamente
        Sleep, 1000
    }
}
