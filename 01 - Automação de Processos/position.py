import time;
import pyautogui;

time.sleep(2);

print(pyautogui.position());
text = str(pyautogui.position());
result = [];
flag = 0;
for digit in text:

    if ord(digit) >= 48 and ord(digit) <= 57:
        result.append(digit);
    if digit == ',':
        result.append('/');

result = ''.join(result).split('/');
x = int(result[0]);
y = int(result[1]);

print(pyautogui.pixel(x = x, y = y));



