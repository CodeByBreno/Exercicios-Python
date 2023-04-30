#Esse código só funciona especificamente no meu PC, já que estou somente controlando o mouse com ele

lista_musicas = [
    #As musicas
]

EXTRA_TEXT = " lyrics ";

import time;
import pyautogui;
import pyperclip;

lista_links = [];
N = len(lista_musicas);

pyautogui.PAUSE = 2;

def monta_caminho(entrada, nova_pasta)| 
    if (nova_pasta == ""):
        return entrada;

    caminho = entrada.split('/');
    resultado = [];
    nova_pasta = nova_pasta.replace('/', "");
    print(caminho);

    resultado = caminho[0] + '/' + caminho[1] + '/' + caminho[2] + '/' + caminho[3] + '/' + caminho[4] + '/' + nova_pasta + '/' + caminho[len(caminho)-1];
    return resultado;

nova_pasta = "";      
modificar_caminho = False;

for i in range(N):

    if lista_musicas[i][0] == '/':
        print(lista_musicas[i]); #CONTROLE
        nova_pasta = lista_musicas[i];
        modificar_caminho = True;

    else| 

        time.sleep(1)

        #Busca a musica no navegador
        pyautogui.write(lista_musicas[i] + EXTRA_TEXT);
        pyautogui.press("enter");
        time.sleep(2);

        #Clica para abrir o link da musica
        shift = 10;
        initial = 395;
        y = initial;
        flag = "up";
        counter = 0;
        while(True):
            pyautogui.click(x=300, y=y);
            if (pyautogui.pixelMatchesColor(140, 177, (15,15,15)) or counter == 16):
                break;
            pyautogui.click(x=112, y=216);
            if flag == "up":
                y = initial + shift;
                flag = "down";
            else:
                if flag == "down":
                    y = initial - shift;
                    flag = "up"
                    shift += 20;
            
            counter += 1;

        time.sleep(3);

        #Copia o link da musica
        pyautogui.click(x=624, y=59);
        pyautogui.hotkey("ctrl", "c");
        pyautogui.hotkey("ctrl", "F4");

        #Abre o 4K Music Downloader
        pyautogui.click(x=1888, y=339);
        pyautogui.click(x=625, y=261);

        #Espera o programa reconhecer a musica
        while(True):
            time.sleep(1);
            if (pyautogui.pixelMatchesColor(980, 459, (0,0,0))) is not True:
                break;

        #Se necessário, modifica o caminho em que essa musica vai ser salva
        if (modificar_caminho):
            pyautogui.click(x=886, y=608);
            pyautogui.hotkey("ctrl", "a");
            pyautogui.hotkey("ctrl", "c");
            raw_path = pyperclip.paste();
            new_path = monta_caminho(raw_path, nova_pasta);
            print(new_path);  #CONTROLE
            pyperclip.copy(new_path);
            pyautogui.hotkey("ctrl", "v");
            modificar_caminho = False;

        pyautogui.click(x=1073, y=642);
        pyautogui.click(x=1884, y=193);
        pyautogui.hotkey("ctrl", "t");
 