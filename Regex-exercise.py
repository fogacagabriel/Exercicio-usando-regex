import re
 
with open('C:/Users/gabri/OneDrive/Documentos/Documento2.txt') as file:
    text = file.read()
print(text)


numbers = list(re.findall('[0-9]+', text))
numeros = list(map(float, numbers))


soma = 0

for i in numeros:
    soma = soma +i
    
print(soma)