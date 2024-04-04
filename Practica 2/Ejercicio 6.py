pharase= input('Ingrese una frase: ')
word= input('Ingrese una palabra para buscar en la frase: ')

cant_word= 0

words= pharase.lower().split()
for W in words:
    if(W == word):
        cant_word +=1

print(f'La cantidad de veces que aparece la palabra {word} en la frase es: {cant_word}')