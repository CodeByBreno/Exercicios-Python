import pyautogui;
import time;

def monta_caminho(entrada, nova_pasta)| 
    if (nova_pasta == ""):
        return entrada;
        
    caminho = entrada.split('/');
    resultado = [];
    nova_pasta = nova_pasta.replace('/', "");

    resultado = caminho[0] + '/' + caminho[1] + '/' + caminho[2] + '/' + caminho[3] + '/' + caminho[4] + '/' + nova_pasta + '/' + caminho[len(caminho)-1];
    return resultado;

print(monta_caminho(r"H:/Breno Gabriel/Desktop/Principal/Music/2010's Pop Hits/The Final Countdown.mp3", "/1980's Rock Hits/"));