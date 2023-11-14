#perguntar o nome
nome = input("Qual é o seu nome ?")

#tirar o espaço da string e deixar todos os nomes com maiúsculas
nome = nome.strip().title()

#dividir o nome em primeiro nome e sobrenome
primeiro, sobrnome = nome.split(" ")

#dizer ola
print(f"Olá, {primeiro}")