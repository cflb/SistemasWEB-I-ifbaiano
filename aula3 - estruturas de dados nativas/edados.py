print("""
	Operações com Listas
	Veja no livro e pesquisem mais sobre o conteúdo na internet
""")
lista = [1,2,3,4]
print("Isto é uma LISTA ==> ", lista)
print("O tamanho da lista é: %s" % len(lista))
#adcionando elemento em uma lista
#Função append (inseri um elemento a lista)
lista.append("novo elemento")
print(lista)
print("O tamanho da lista agora é: %s" % len(lista))

#Removendo um elemento da lista
del lista[0]
print(lista)
print("O tamanho da lista agora é: %s" % len(lista))

#Removendo o ultimo elemento com a função POP
lista.pop()
print(lista)
print("O tamanho da lista agora é: %s" % len(lista))


print("""
	Operações com Tuplas
	Veja no livro e pesquisem mais sobre o conteúdo na internet

	Operações semelhantes as da Lista, contudo as TUPLAS são imutáveis (uma vez que seus elementos foram criados, não é permitido modifica-los)
""")
#
tupla = (1,2,4,5)
print("Isto é uma TUPLA ==> ", tupla)
print("O tamanho da tupla agora é: %s" % len(tupla))

print("Podemos declarar tuplas de algumas formas difrentes, vejamos")
print("Declarar TUPLAS, usando parenteses")
print("Ex. tupla2 = (1,2.0,'casa', True)")
tupla2 = (1,2.0,"casa", True)
print("Resultado: ", tupla2)
print("Declarar TUPLAS, SEM usar parenteses")
print("Ex. tupla3 = 1,2.0,'casa',True")
tupla3 = 1,2.0,"casa", True
print("Resultado: ", tupla3)
print("Declarar TUPLAS, com apenas UM elemento")
print("Se uma variavel for declarada e terminar com uma VIRGULA, esta variável é altomaticamente classificada como uma TUPLA")
print("Ex. tupla4 = 1,")
tupla4 = 1, 
print("Resultado: ", tupla4)


print("""
	Operações com Dicionários
	Veja no livro e pesquisem mais sobre o conteúdo na internet
""")

dic1 = """
aluno = {
	"nome": "Joao",
	"nota": 10.0,
	"disc": "dev web"
}
"""
print("Isto é um dicionário ", dic1)
aluno = {
	"nome": "Joao",
	"nota": 10.0,
	"disc": "dev web"
}
print(aluno)

alunos = [
	{ "nome": "Pedro", "nota": 9.0, "disc": "dev web"},
	{ "nome": "Joao", "nota": 9.0, "disc": "dev web"},
	{ "nome": "maria", "nota": 9.0, "disc": "dev web"},
	{ "nome": "Paulo", "nota": 9.0, "disc": "dev web"},
]
print(alunos)
print(alunos[3]["nome"],alunos[3]["nota"],alunos[3]["disc"])
print("Dicionário é uma estrutura baseada em CHAVE e VALOR, {'chave':'valor'}, mas em ingles {'key':'value'}")
print("Podemos selecionar todas as chaves e todos os valores de forma independente")
print("use as funcões .keys() para selecionar as chaves e .values() para os valores")
print("Vejamos as chaves do dicionario aluno - aluno.keys() ")
print(aluno.keys())
print("Vejamos os valores do dicionario aluno - aluno.values() ")
print(aluno.values())
