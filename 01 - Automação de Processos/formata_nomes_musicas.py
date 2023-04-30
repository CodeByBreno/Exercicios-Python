entrada = open("entrada.txt")
saida = open("saida.txt", "w+")

DIVISOR = '|';
SPACE_AFTER = True;

if entrada is None:
    print("Problemas ao abrir o arquivo");

for each in entrada.readlines():
    counter = 0;
    flag = 0;
    size_line = len(each);

    for digit in each:
        counter += 1;
        if digit == DIVISOR:
            flag = 1;
        if flag == 1:
            break;
    
    result = ["\""];

    if SPACE_AFTER == False:
        counter -= 1;
        
    for i in range(counter+1, size_line-1):
        result.append(each[i]);
    
    result.append("\",");

    frase_objetivo = ''.join(result);
    saida.write(frase_objetivo);
    saida.write("\n");



        