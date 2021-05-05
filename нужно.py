import os
from tkinter import *
import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui



def op_prog(event):
    os.system('cd C:/Users/Степанчик/Desktop/скрипты')
    fill = os.listdir()
    txte = entry.get()
    txte = txte + '.py'
    os.system(txte)
    textik = Text(font='Arial 10')
    textik.pack()
    textik.insert(INSERT, fill)

def pr_google(event):
    driver = webdriver.Chrome(executable_path='C:/Users/Степанчик/Desktop/скрипты/chromedriver.exe')
    element = driver.get('https://google.gik-team.com/')
    element = driver.find_element_by_xpath("/html/body/div[1]/main/form/input")
    txt = entry.get()
    element.send_keys(txt)
    driver.find_element_by_xpath("/html/body/div/main/form/div[1]/button[1]").click()
    driver.find_element_by_xpath("/html/body/div/main/div[3]/div[2]/a[3]").click()

def prost(event):
    requests.get("https://www.google.ru/")
    txt = entry.get()
    print(txt)
    print(requests.post("https://www.google.ru/search?q=" + txt))

def parol(event):
    global pr
    txt = entry.get()
    if txt == 1:
        time.sleep(3)
        pyautogui.typewrite('Nrvbkrf1207')
    elif txt == 2:
        time.sleep(3)
        pyautogui.typewrite('Nrvbkrf@1207')
    elif txt == 3:
        time.sleep(3)
        pyautogui.typewrite('nrvbkrf1207')
    elif txt == 4:
        time.sleep(3)
        pyautogui.typewrite('nrvbkrf@1207')
    else:
        time.sleep(3)
        pyautogui.typewrite('stepan.mokeev160808@gmail.com')





root = Tk()
root.geometry('250x150')
root.title("Полезная прога")
root["bg"] = "gray22"

op_proga = Button(width=10, height=1, text='Открывашка')
op_proga.bind("<Button-1>", op_prog)
op_proga.pack() #это кнопка которая открывайет скрипты

pr_googlee = Button(width=10, height=1, text='норм гуглить')
pr_googlee.bind("<Button-1>", pr_google)
pr_googlee.pack()  #это кнопка которая отправляет в гугл более правильный текст и открывает его

pros = Button(width=10, height=1, text='прост гугл')
pros.bind("<Button-1>", prost)
pros.pack()  #это кнопка которая будет задавть в гугл запрос

prl = Button(width=10, height=1, text='Парольник')
prl.bind("<Button-1>", parol)
prl.pack()

entry = Entry(fg="black", bg="white", width=30)
entry.pack()  #это текстовое поле для написании текста которое будет использывать кнопки

root.mainloop()