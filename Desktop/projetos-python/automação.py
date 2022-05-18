
import pyautogui;
import time;
import pyperclip;

link = "https://www.nuinvest.com.br/"
email = " "
senha=" "

pyautogui.PAUSE = 1;
#1 passo abrir navegador na internet 
pyautogui.press("winleft")
pyautogui.write("edge")
pyautogui.press("enter")

#2 acessa o link
pyperclip.copy(link)
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(5)

#clica no login
pyautogui.click(x=2671, y=101);
time.sleep(5)
#clica onde vai por email
pyautogui.click(x=1944, y=322);
pyperclip.copy(email)
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=1825, y=360)
#clica onde vai por a senha
pyautogui.click(x=1896, y=386)
pyperclip.copy(senha)
pyautogui.hotkey("ctrl", "v")
#clica no botão de logar
pyautogui.click(x=1919, y=512)
