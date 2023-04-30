
c = 0;
soma = 0;

while(c < 10000):
    valor = 1/(2*c+1);
    soma += valor*valor;
    c += 1;
    
print(soma);