import pygetwindow as gw

# Obtém uma lista de títulos de janelas
titulos_janelas = gw.getAllTitles()

# Lista os títulos das janelas
for titulo in titulos_janelas:
    print(titulo)
