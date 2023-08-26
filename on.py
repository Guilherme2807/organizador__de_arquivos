import os

cwd = os.getcwd()

full = os.listdir(cwd)

#verificando se há uma substring em uma string
# 'te' in 'teste'
#criando uma lista que lista remova pastas e arquivos '.py'
files_list = [i for i in full if os.path.isfile(i) and '.py' not in i]


#entendendo qual o tipo de arquivo que tem em minha lista
#porém os arquivos aprecem mais de uma vez, logo preciso criar uma forma que os tipos de arquivos apareçam apenas uma vez, logo uso o comando 'set'
types = list(set([i.split('.')[1] for i in files_list]))

# Para cada tipo de arquivo em tipo, crie uma pasta com o tipe de arquivo
for file_type in types:
    os.mkdir(file_type)


for files in files_list:
    from_path = os.path.join(cwd, files)
    to_path = os.path.join(cwd, files.split('.')[-1], files)
    
    os.replace(from_path, to_path)


