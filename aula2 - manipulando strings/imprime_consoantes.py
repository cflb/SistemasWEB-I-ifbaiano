vetor_letras = ['b','j','k','a','l','o','i','w','s','p','e', 'r', 'y']

lista_consoantes = ''
lista_vogais = ''
for letra in vetor_letras:
    if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
        lista_vogais += letra            
    else:
        lista_consoantes += letra

print("A quantidade de consoantes é: %s" % len(lista_consoantes))        
print(lista_consoantes)
