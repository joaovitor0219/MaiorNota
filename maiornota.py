from xml.dom.pulldom import CHARACTERS


escola = input("Qual o nome da escola ? ")
alunos = int(input("Quantos alunos tem na turma ?" ))
contagem = 1
maior_nota = 0
melhor_aluno = CHARACTERS
while contagem <= alunos:
    nome = input("Nome do aluno: ")
    nota = float(input(f"nota de {nome}: "))

    if nota >= maior_nota:
        maior_nota = nota
        melhor_aluno = nome
    contagem = contagem + 1

print(f"A maior nota foi de {melhor_aluno} com a nota de {maior_nota}")
  
    

    