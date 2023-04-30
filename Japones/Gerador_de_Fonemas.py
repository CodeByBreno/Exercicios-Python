# Gerador de fonemas em dart

import random;

vogais = ['a', 'i', 'u', 'e', 'o', 'n'];
consoantes = ['', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', 'g', 'z', 'd', 'b', 'p'];

N = input('Insira a quantidade de fonemas a serem apresentados : ');
c = 0;
saida = open(r"C:\Users\Anduin110\Desktop\Japones\output.txt", "w+");

if not N.isalnum():
    saida.write('Entrada inválida');
    exit();

for i in range(int(N)):
    flag = False;
    aleat_vogal = random.randint(0, 5);
    if aleat_vogal == 5:
        saida.write(vogais[aleat_vogal] + ' ');
    else:
        aleat_cons = random.randint(0, 14);

        # Casos especiais do 'i'
        if aleat_vogal == 1:
            #saida.write('e1 ');
            if aleat_cons == 2: saida.write('shi ');
            elif aleat_cons == 3: saida.write('chi ');
            elif aleat_cons == 11 or aleat_cons == 12: saida.write('ji ');
            else: flag = True;

        # Casos especiais do 'u'
        if aleat_vogal == 2:
            #saida.write('e2 ');
            if aleat_cons == 3: saida.write('tsu ');
            elif aleat_cons == 5: saida.write('fu ');
            elif aleat_cons == 11 or aleat_cons == 12: saida.write('zu ');
            else: flag = True;

        #saida.write(str(flag) + '  ');

        #Impedindo que os casos que já ocorreram sejam repetidos
        if ((aleat_vogal == 1 or aleat_vogal == 2) and flag == True) or (aleat_vogal != 1 and aleat_vogal != 2):
            # Impedindo os casos 'yi', 'ye', 'wi', 'wu', 'we'
            if not (aleat_cons == 7 and (aleat_vogal == 1 or aleat_vogal == 3) or
                aleat_cons == 9 and (aleat_vogal != 0 or aleat_vogal != 4)):
                #saida.write ('//');
                saida.write(consoantes[aleat_cons] + vogais[aleat_vogal] + ' ');
            else: c -= 1;

    #saida.write(" valor de i : " + str(i) + "\n");
    c += 1;
    if c%10 == 0 and c != 0: saida.write('\n');

