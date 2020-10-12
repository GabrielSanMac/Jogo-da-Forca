import random

def main():
	#pegando e ageitando a a palavra para o game
	Palavras = ['folha', 'caderno', 'correia', 'pato', 'carta', 'sentimento', 'calorias', 'cabelo', 'luz', 'som', 'covid', 'concha', 'dinheiro', 'passarinho', 'ceu', 'altura', 'calendario', 'limosine', 'sorvete', 'limite', 'elefante', 'imovel', 'tigre', 'africa', 'brasil', 'belgica', 'musica', 'cantar', 'seriado', 'avestrus', 'limao', 'estados unidos da america', 'emirados arabes', 'ornitorrinco', 'geleira', 'geladeira', 'aquecimento global', 'poluicao', 'mundo', 'nicaragua', 'via lactea', 'mercurio', 'sistema solar', 'terra', 'netuno', 'plutao', 'platao', 'sala de aula', 'escola', 'fogo de artificio', 'roupa', 'banco', 'bone', 'cor', 'hungria', 'russia', 'vladimir putim', 'donald trump', 'governo', 'jair bolsonaro', 'flor', 'flora', 'falna']
	Palavra_Secreta = [letra for letra in random.choice(Palavras)]
	Win_Checker = len(Palavra_Secreta)
	Letras_Usadas = []
	Acertos = []
	Erros = 0
	underline = '_ '
	Printer = []
	for number in range(len(Palavra_Secreta)):
		if Palavra_Secreta[number] == ' ':
			Printer.append(' ')
			Acertos.append(' ')
		elif Palavra_Secreta[number] == '-':
			Printer.append('-')
			Acertos.append('-')
		else:
			Printer.append('_')

	#game:
	print(*Printer)
	while True:
		#check
		print(f"Erros maximos: 6 Erros Atuais do jogador {Erros}")
		Letra = input('Digite uma letra:> ')
		if Letra == '':
			continue	
		if Letra not in Letras_Usadas:
			if Letra not in Palavra_Secreta:
				Erros += 1
			Letras_Usadas.append(Letra)
			for letra in Palavra_Secreta:
				if Letra in letra:
					Acertos.append(Letra)
					print(f'Acertou a letra: {Letra}')
					Printer[Palavra_Secreta.index(Letra)] = Letra
					Palavra_Secreta[Palavra_Secreta.index(Letra)] = '_ '
				else:
					continue
		else:
			print('Letra ja ultilizada')

		print(*Printer)

		if len(Acertos) == Win_Checker:
			print('Você ganhou')
			main()
			break
		elif Erros == 6:
			print('Você Perdeu')
			main()
			break


if __name__ == '__main__':
	main()