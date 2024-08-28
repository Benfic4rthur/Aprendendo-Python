#o sep cria um separador diferente do espaço que a virgula usa por default
#usar CRLF com o \n ou \r faz a quebra de linha
#o end define o que vai aparecer no final da linha mas colocar \r\n é inutil pois o padrão é quebra de linha e pula para o proximo
print(12,34,sep='-', end="\r\n")
print(56,78, sep="-")