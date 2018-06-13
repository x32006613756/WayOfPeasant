import os
import random
import time

clear = lambda: os.system("clear") #Функция для очистки консоли.

            #Переменные
myheal = 500#жизни
mydmg = random.randint(10,760);#Наш персонажа.
bheal = random.randint(50,800);#Жизнь противника.
bdmg = random.randint(5,myheal)#Урон противника
money = 150; #деньги

def hud():
    print ("\t\t\t\tВаше HP :",myheal,"Деньги",money);

def arena(): #Функция Арены.
    clear();

def shop(): #Функция Магазин.
    clear();

def menu(): #Функция Меню.
    clear();
    hud();
    print("\n\n[1]Арена");
    print("[2]Магазин");
    print("[3]Выход");
    print(bheal,bdmg,mydmg)
    try:
      vod = int(input("\n::")) #Запрос ответа от игрока.
      if(vod == 1):
          if(myheal == 0):
            print("Ваше здоровье слишком мало.");
            menu();
          else:
              arena();
      elif(vod == 2):
          shop();
      elif(vod == 3):
          os.system("exit");
      elif(vod == 99):
          print("FUCKED AWESOM KIZARU")
      else:
          print("Такого выбора нету")
          time.sleep(3);
          menu();
    except ValueError:
        print("Вы ввели что-то не то.");
        time.sleep(5);
        menu();

menu();
