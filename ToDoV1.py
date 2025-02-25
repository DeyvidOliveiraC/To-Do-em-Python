

lista=[]

def Append_Tasks(Listatarefas=[]):
	for i in Listatarefas:
		with open("Tarefas_Cadastradas.txt","a") as arquivo:
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

def Main():
	Write_Tasks()


Main()






