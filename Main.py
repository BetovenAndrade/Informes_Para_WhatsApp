from InformeWhats import InformeWhats
from textwrap import wrap

# Recebendo o texto
texto = input('Cole o texto a ser inserido na imagem: ')

# Limitando a quantidade de caracteres do texto
texto = texto[0:314]

# Definindo largura do texto em caracteres
texto = wrap(texto, width=25)
texto = '\n'.join(texto)

# Centralizando o texto
texto = texto.center(0)

InformeWhats.main(texto)