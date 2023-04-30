#Limpando tudo que já estava no arquivo antes
File1 = open("Entrada.txt","w");
File1.close();

#Abrindo o arquivo novamente, dessa vez para escrever nele
File1 = open("Entrada.txt","a+"); 
#Abrindo com o modo de "apêndice", que adiciona informação no final do arquivo
#(tecnicamente eu poderia abrir com "w+", já ques estou apagando tudo ali no começo mesmo)
#Esse método coloca o ponteiro no final do arquivo
lista_de_coisas = ['Cavalo', 'Sol', 'Iguana', 'Indie', 'Rock', 'Verão', 'Chuva'];

File1.write('Chá de Erva Cidreira\n');

for aux in lista_de_coisas: #escreve com quebras de linha
    File1.write(aux + '\n');

#Lendo o que foi salvo no arquivo
File1.seek(0); #reposiciona o ponteiro de leitura para o início do arquivo
print('Lendo o Arquivo ====================');
for aux in File1.readlines():
    print(aux, end="");