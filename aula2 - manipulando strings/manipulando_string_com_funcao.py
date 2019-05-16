def invertePalavra(palavra):
    """
        Esta função recebe uma frase, inverte toda sua estrutura e mostra apenas a ultima palavra. 
    """
    comprimento = len(palavra)
    palavra_invertida = palavra[::-1]
    nova_palavra = ""

    for letra in palavra_invertida:
        if letra == " ": #quando a letra for igual ao espaço PARE
            break #BREAK para qualquer operação
        else:
            nova_palavra = nova_palavra + letra
        
    return nova_palavra

print("teste 1, frase - 'Amarelo Manga'")
print(invertePalavra("Amarelo Manga"))
print("teste 2, frase - 'Meu pé de laranja lima'")
print(invertePalavra("Meu pé de laranja lima"))
