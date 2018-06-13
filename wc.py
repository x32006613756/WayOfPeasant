import os
import random
import time
from termcolor import colored

clear = lambda: os.system("clear"); #Функция для очистки консоли.
textexit = lambda: print("\n\n\t\t\t\tЧтобы выйти нажмите [0]"); #Функция текста выхода.

            #Переменные
myheal = 500#жизни
mydmg = random.randint(10,760);#Наш персонажа.
bheal = random.randint(50,800);#Жизнь противника.
bdmg = random.randint(5,myheal);#Урон противника
money = 150; #деньги
present = random.randint(15,5400);#Приз после побоища

def hud(): #Функция показателей персонажа.
    global mydmg;
    global myheal;
    global bdmg;
    global bheal;
    global money;
    global present;
    clear();
    if(myheal <= -1):
        myheal = 0
    else:
        myheal = myheal
    print ("\t\t\t\tВаше HP :",myheal,"Деньги :",money);

def arena(): #Функция Арены.
    clear();
    global mydmg;
    global myheal;
    global bdmg;
    global bheal;
    global money;
    global present;
    print("Твоё HP :",myheal,colored("\t\tВраг HP: " ,"red") + colored(bheal, "red"));
    print("\t[1] Обычная атака\n\t[0] Выход в меню");
    varen = int(input());
    if(varen == 1):
        if(myheal <= -1):
            myheal = 0
        else:
            myheal = myheal
        if(bheal <= -1):
            bheal = 0
        else:
            bheal = bheal
        myheal = myheal - bdmg;
        bheal = bheal - mydmg;
    print("Ты нанёс ",mydmg,"У противника HP :",bheal);
    print("Тебе нанесли урона :",bdmg,"Твоё HP :",myheal);
    if(mydmg >= bheal and myheal >=1):
        money = money + present;
    elif(mydmg >=bheal and myheal <=0):
        money = money + present/2;
    elif(mydmg < bheal and bheal >=1 and myheal >= 1):
        money = money + present/2;
    elif(myheal <=0):
        money = money + present/3;
    textexit();
def shop(): #Функция Магазин.
    global mydmg;
    global myheal;
    global bdmg;
    global bheal;
    global money;
    global present;
    hud();
                    #Первый каталог.
    print("\t\t\t\tВсё необходимое можно купить у нас в магазине!");
    print("[1]Зелье жизни I (+10 ХП)", colored("(20 Монет)", "yellow"));
    print("[2]Зелье жизни II (+30 ХП)", colored("(40 Монет)", "yellow"));
    print("[3]Зелье жизни III (+50 ХП)", colored("(60 Монет)", "yellow"));
    print("[4]Зелье жизни IV (+70 ХП)", colored("(80 Монет)", "yellow"));
    print("[5]Зелье жизни V(+90 ХП)", colored("(120 Монет)", "yellow"));

    textexit();
    question_shop = int(input("\n:::"));

    if (question_shop == 1):
        money = money - 20;
        myheal = myheal + 10;
        clear();
        shop();
    elif(question_shop == 2):
        money = money - 40;
        myheal = myheal + 30;
        clear();
        shop();
    elif(question_shop == 3):
        money = money - 60;
        myheal = myheal + 50;
        clear();
        shop();
    elif(question_shop == 4):
        money = money - 80;
        myheal = myheal + 70;
        clear();
        shop();
    elif(question_shop == 5):
        money = money - 120;
        myheal = myheal + 90;
        clear();
        shop();
    elif (question_shop == 0):#
        menu();

def menu(): #Функция Меню.
    hud();
    global mydmg;
    global myheal;
    global bdmg;
    global bheal;
    global money;
    global present;
    print(colored("\n\n[1]Арена","red"));
    print(colored("[2]Магазин","green"));
    print("[3]Выход");
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
      else:
          print("Такого выбора нету");
          time.sleep(3);
          menu();
    except ValueError:
        print("Вы ввели что-то не то.");
        time.sleep(5);
        menu();

menu();
