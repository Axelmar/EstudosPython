with open('pi_digits.txt') as file_object:          ### With fecha o arquivo depois que nao for mais necessario acessa-lo
    contents = file_object.read()
    print(contents)


#Lendo dados linha a linha
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


#Criando uma lista de linhas de um arquivo
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#Trabalhando com o conteudo de um arquivo
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Escrevendo dados em um arquivo vazio
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")