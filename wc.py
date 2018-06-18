#КРЕСТЬЯНИН РАЗРАБОТКИЧИКИ NULLHUMAN, X23006613159 11.06.2018
import os
import random
import time
from termcolor import colored

clear = lambda: os.system("clear"); #Функция для очистки консоли.
textexit = lambda: print("\n\n\t\t\t\tЧтобы выйти нажмите [0]"); #Функция текста выхода.

            #Переменные
myheal = 500;#Жизнь персонажа.
mystamina = 150;#Мана персонажа.
money = 150; #Деньги персонажа.
name_person = "notfing"; #Имя персонажа, если человек пропустил регистрацию.

def checkin(): #Функция регистрации.
    global name_person;
    clear();
    print("\t\t\t\tДобро пожаловать в игру.")
    time.sleep(2);
    print("\t\tЛюбые совпадения с историческими событиями чистейшая случайность.")
    time.sleep(2);
    print(colored("""
     |  /   |--|  |----  |----  ---|---  |       |---|   |   |   |    /|   |   |
     | /    |  |  |      |         |     |       |   |   |   |   |   / |   |   |
     | \    |--|  |----  |         |     |---|   |---|   |---|   |  /  |   |---|
     |  \   |     |      |         |     |   |      /|   |   |   | /   |   |   |
     |   \  |     |----  |----     |     |---|    /  |   |   |   |/    |   |   |
    """, "red"));
    time.sleep(5);
    clear();
    print("\t\t\t\tРегистрация аккаунта.");
    print(colored("Пожалуйста введите ваш ник: ", "blue"));
    del name_person;
    name_person = input("::");
    menu();

def hud(): #Функция показателей персонажа.
    global name_person;
    global myheal;
    global mystamina;
    global money;
    clear();
    if(myheal <= 0):
        print(colored("\t\tВы на грани жизни и смерти! Выпейте зелье!", "red"));
    elif(mystamina <= 0):
        print(colored("\t\tВы слишком уставший! Выпейте зелье!", "red"));
    elif(money <= 0):
        print(colored("Следуйте на арену, т.к у вас совсем нету монет.", "red"));
    else:
        print("\t\tВы",name_person,"Ваше ХП:",myheal,"Ваша Мана:",mystamina,"Деньги :",money);

def arena(): #Функция Арены.
    global myheal;
    global mystamina;
    global money;
    while True:
        present = random.randint(15,5200);#Приз
        bheal = random.randint(300, 560);#Жизнь противника.
        bdmg = random.randint(50, 450);#Урон противника.
        mydmg = random.randint(10,600);#Сила персонажа.
        mysuperdmg = random.randint(100,900);#Супер удар.
        clear();
        hud();
        print("\t\t\tНачать бой [1] Выход в меню [0]");
        question_arena = int(input("\n::"));
        if (question_arena == 1):
            if (myheal <= 50):
                clear();
                print("Вы не можете играть.");
                time.sleep(3);
                menu();
            else:
                print("\t\t\tПротивник","ХП:", bheal )
                print("\t\t\t[1]Атака [2]Суперудар");
                q_two_arena = int(input("::"));
                if (q_two_arena == 1):
                    bheal = bheal - mydmg;
                    if (bheal <= 0):
                        print("Вы нанесли", mydmg, "Противник мёртв!");
                    else:
                        print("Вы нанесли", mydmg, "урона.","У противника HP :", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print(colored("ПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар, который поверг вас.", "red"))
                        print("Отдохните и возвращайтесь в бой");
                    else:
                        print("Вам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mydmg >= bheal and myheal >=50):
                        money = money + present;
                        print(colored("Победа!", "green"));
                        print("Поздравляю вы победили!!!\nВаша награда :",present);
                        time.sleep(4);
                    elif(mydmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print(colored("Ничья!", "yellow"));
                        print("Ваш противник побеждён но вы тоже повреждены.\nВы поделили награду :",present);
                        time.sleep(4);
                    elif(mydmg < bheal and bheal >=50 and myheal <=50):
                        money = money + (present/2);
                        print(colored("Ничья!", "yellow"));
                        print("Вы не одалели противника,но он оставил вас в живых.\n Награду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print(colored("Поражение!", "red"))
                        print("Тебя победили. Ты проиграл.");
                        time.sleep(4);
                    if(myheal <=50):
                        print("Вам плохо выпейте лекарство");
                        time.sleep(3);
                        menu();
                    else:
                        arena();
        elif(question_arena == 0):
            menu();
        else:
            print("Вы ввели что-то не то.");
    arena();

def shop(): #Функция Магазин.
    global myheal;
    global mystamina;
    global money;
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

    if (question_shop == 1):#20
        if(money < 20):
            print("У вас недостаточно Монет")
            time.sleep(3);
            menu();
        else:
            money = money - 40;
            myheal = myheal + 20;
            clear();
            shop();
    elif(question_shop == 2):
        if(money < 40):
            print("У вас недостаточно Монет")
            time.sleep(3);
            menu();
        else:
            money = money - 40;
            myheal = myheal + 30;
            clear();
            shop();
    elif(question_shop == 3):#60
        if(money < 40):
            print("У вас недостаточно Монет")
            time.sleep(3);
            menu();
        else:
            money = money - 60;
            myheal = myheal + 60;
            clear();
            shop();
    elif(question_shop == 4):#80
        if(money < 40):
            print("У вас недостаточно Монет")
            time.sleep(3);
            menu();
        else:
            money = money - 80;
            myheal = myheal + 80;
            clear();
            shop();
    elif(question_shop == 5):#120
        if(money < 40):
            print("У вас недостаточно Монет")
            time.sleep(3);
            menu();
        else:
            money = money - 120;
            myheal = myheal + 120;
            clear();
            shop();
    elif (question_shop == 0):#
        menu();

def settings(): #Функция Настроек.
    clear();

def menu(): #Функция Меню.
    hud();
    global myheal;
    global mystamina;
    global money;
    print(colored("\n\n[1]Арена","red"));
    print(colored("[2]Магазин","green"));
    print(colored("[3]Настройки","blue"))
    print("[4]Выход");
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
          settings();
      elif(vod == 4):
          os.system("exit");
      else:
          print("Такого выбора нету");
          time.sleep(3);
          menu();
    except ValueError:
        print("Вы ввели что-то не то.");
        time.sleep(5);
        menu();

checkin();
