import os

lista=[]

def Append_Tasks(Listatarefas=[]):
	for i in Listatarefas:
		with open(f"Tarefas_Cadastradas.txt","a") as arquivo:
			arquivo.write(f"{i}\n")
			arquivo.close()

def Write_Tasks():
	global lista
	while True:
		tarefa=str(input("Digite uma tarefa a ser realizada: "))
		lista.append(tarefa)
		esc=str(input("Deseja cadastrar outra tarefa?[S/N]")).strip().upper()[0]
		if esc=='N':
			break
	Append_Tasks(lista)
	lista.clear()


def List_Tasks():
	global lista
	with open("Tarefas_cadastradas.txt") as arquivo:
		line=arquivo.readline()
		while line:
			lista.append(line)
			line=arquivo.readline()
		arquivo.close()

def Show_Tasks():
	count=1
	with open("Tarefas_Cadastradas.txt","r") as arquivo:
		for c in arquivo:
			if c.isspace()==False:
				print(f"{count}->{c}")
				count+=1
		arquivo.close()

def Delete_Tasks(task):
	global lista
	List_Tasks()
	lista.pop(task)
	os.remove("Tarefas_Cadastradas.txt")
	Append_Tasks(lista)

def Main():
	Write_Tasks()
	Delete_Tasks(1)
	Show_Tasks()


Main()





