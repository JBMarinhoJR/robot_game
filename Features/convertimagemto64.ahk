#NoEnv
#SingleInstance, Force
SendMode, Input
SetBatchLines, -1
SetWorkingDir, %A_ScriptDir%

; Caminho para o arquivo da imagem que você deseja converter para Base64
caminhoParaImagem := "C:\Users\Junior\OneDrive\Documentos\robot_game\Features\chapeuteste2.png"

; Função para ler o conteúdo do arquivo como binário
lerArquivoBinario(caminho) {
    FileRead, binario, %caminho%
    return binario
}

; Função para converter binário para Base64 usando uma DLL do Windows
converterParaBase64(binario) {
    VarSetCapacity(base64, 0)
    VarSetCapacity(base64, ((StrLen(binario) + 2) / 3) * 4 + 1)
    dll := DllCall("Crypt32.dll\CryptBinaryToStringA", "ptr", &binario, "uint", StrLen(binario), "uint", 1, "str", base64, "uint*", VarSetCapacity(base64))
    return StrGet(&base64, "UTF-8")
}

; Lê o arquivo como binário
binarioDaImagem := lerArquivoBinario(caminhoParaImagem)

; Converte o binário para Base64
base64String := converterParaBase64(binarioDaImagem)

; Define a string Base64 na área de transferência
Clipboard := base64String

; Notifica o usuário e aguarda a confirmação MCBQAE4ARwA=
MsgBox, A string Base64 foi copiada para a área de transferência. Pressione Ctrl+V para colar.
