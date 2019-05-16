def invertePalavra(palavra):
    """
        Funcao que retorna parte final da palavra invertida
    """
    comprimento = len(palavra)
    palavra_invertida = palavra[::-1]
    nova_palavra = ""

    for letra in palavra_invertida:

        if letra == " ":
            pass
        else:
            nova_palavra = nova_palavra + letra
        
    return nova_palavra