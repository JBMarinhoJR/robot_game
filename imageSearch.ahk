#NoEnv
#Persistent
#SingleInstance, Force
SetBatchLines, -1
SetTitleMatchMode, 1

; Inclua a biblioteca, assumindo que esteja no mesmo diretório que o script
; Se não estiver, forneça o caminho completo para a biblioteca
#include ShinsImageScanClass.ahk

scan := new ShinsImageScanClass()

SetTimer, ProcurarImagem, 1 ; Define um temporizador para chamar a função ProcurarImagem a cada 500 milissegundos
return

ProcurarImagem:
; Procura pela imagem "seta.png" na tela
variance := 0 ; Define a sensibilidade da correspondência (0 para correspondência exata)
scanDir := 0 ; Define a direção de varredura (0 para padrão)
if (scan.Image("recorte7.png", variance, invX, invY)) {
    MsgBox Encontrou a imagem na posição: X=%invX%, Y=%invY%
} 
return
