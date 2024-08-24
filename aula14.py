a = 'A'
b = 'B'
c = 1.254
formato= ' '
print(formato.join([a,b,str(c)])) # posso usar join para juntar os elementos de uma lista usando a variavel mãe como se fosse o separador
formato_format = 'a={} b={} c={:.3f}' .format(a,b,c) # o formato_format vai ser a= {a} b= {b} c= {c} pois estou utilizando o .format
print(formato_format)
string = 'a={:.3f} b={} c={}' # o string aqui vai mostrar o c no A O a no B e o b no C e o {:.3f} vai mostrar 3 casas decimais
string_formatada = string.format(c,a,b)
print(string_formatada)