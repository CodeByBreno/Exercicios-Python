import pyautogui;
import pandas;
import time;

pyautogui.PAUSE = 1;

#Abre a página no drive
time.sleep(10);
pyautogui.hotkey("ctrl", "t");
time.sleep(5);
pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga");
time.sleep(2);
pyautogui.press("enter");
time.sleep(20);

#Abre a pasta Exportar
pyautogui.click(x=617, y=403, clicks=2)
time.sleep(5);

#Baixa a base de dados
pyautogui.click(x=617, y=403)
pyautogui.click(x=1585, y=251)
pyautogui.click(x=1351, y=787)

#Acessa os dados
tabela = pandas.read_excel(r"C:\Users\Anduin110\Downloads\Vendas - Dez.xlsx");
print(tabela);
