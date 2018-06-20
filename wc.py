"""
КРЕСТЬЯНИН
РАЗРАБОТКИЧИКИ: NULLHUMAN, X23006613159, Александр, PINKUNICORN.
Дата: 11.06.2018.
"""
import os
import random
import time
from colored import bg, fg, attr
import dict

clear = lambda: os.system("clear"); #Функция для очистки консоли.
textexit = lambda: print("\n\n\t\t\t\tЧтобы выйти нажмите [0]"); #Функция текста выхода.

            #Переменные
gm = False #Режим бога по умолчанию выключен.
level = 1 #Уровень персонажа.
myheal = 500 #Жизнь персонажа.
mystamina = 150 #Мана персонажа.
money = 150 #Деньги персонажа.
name_person = "notfing" #Имя персонажа, если человек пропустил регистрацию.
war = 0 #Кол-во сражений по умолчанию.

litii = 0 #Переменная для кол-во лития по умолчанию.
berilii = 0 #Кол-во бериллия.
galii = 0 #Кол-во галлия.
indii = 0 #Кол-во индия.
germanii = 0 #Кол-во германия.
vanadii = 0 #Кол-во ванадия.
titan = 0 #Кол-во титана.
molibden = 0 #Кол-во молибдена.


def death(): #Функция смерти персонажа.
    global level;
    global myheal;
    global money;
    global mystamina;
    global name_person;
    global war;
    death = random.randint(0, 1);
    if (death == 0 or death == 1 and money <= 0):
        clear();
        print("%s\t\t\tИгра закончена! Ваш персонаж мёртв.%s" % (fg("red"),attr(0)));
        time.sleep(5);
        level = 0;
        myheal = 500;
        mystamina = 150;
        money = 150;
        war = 0;
        litii = 0
        berilii = 0
        galii = 0
        indii = 0
        germanii = 0
        vanadii = 0
        titan = 0
        molibden = 0
        checkin();
    elif (death == 1):
        clear();
        print("\t\tВам крупно повезло! Ваш персонаж выжил, впредь будте крайне аккуратны.");
        time.sleep(5);
        shop();

def checkin(): #Функция регистрации.
    global name_person;
    clear();
    print("\t\t\t\tДобро пожаловать в игру.")
    time.sleep(2);
    print("\t\tЛюбые совпадения с историческими событиями чистейшая случайность.")
    time.sleep(2);
    print("""%s
     |  /   |--|  |----  |----  ---|---  |       |---|   |   |   |    /|   |   |
     | /    |  |  |      |         |     |       |   |   |   |   |   / |   |   |
     | \    |--|  |----  |         |     |---|   |---|   |---|   |  /  |   |---|
     |  \   |     |      |         |     |   |      /|   |   |   | /   |   |   |
     |   \  |     |----  |----     |     |---|    /  |   |   |   |/    |   |   |
    %s""" % (fg("red"), attr(0)));
    time.sleep(5);
    clear();
    print("\t\t\t\tРегистрация аккаунта.");
    print("%sПожалуйста введите ваш ник: %s" % (fg("blue"), attr(0)));
    del name_person;
    name_person = input("::");
    menu();

def hud(): #Функция показателей персонажа.
    global gm;
    global name_person;
    global myheal;
    global mystamina;
    global money;
    global level
    clear();
    if(myheal <= 0):
        print("%s\t\tВы на грани жизни и смерти! Выпейте зелье!%s" % (fg("red"),attr(0)));
    elif(money <= 0):
        print("%sСледуйте на арену, т.к у вас совсем нету монет.%s" % (fg("red"),attr(0)));
    else:
        print("\t|","Вы",str(name_person), "|", "Ваше ХП:",int(myheal), "|", "Ваша Мана:",int(mystamina), "|", "Деньги :" ,int(money), "|" , "Ваш уровень:", int(level),"|");
        print("\t‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾");

def settings(): #Функция Настроек.
    clear();
    global name_person;
    print ("[1]Сменить имя");
    vod = int(input("::"));
    if(vod == 1):
        print("Введите новое имя :");
        name_person = input("::")
        print("Ваше новое имя выглядит вот так :", name_person);
        time.sleep(3);
        menu();
    if(vod == 7777):
        global myheal;
        global money;
        global mystamina;
        money = money + 7777;
        myheal = myheal + 7777;
        mystamina = mystamina + 7777;
        print("GodMode: ON")
        time.sleep(3);
        menu();
    else:
        print("Вы ввели что-то не то");

def stat(): #Функция статистики персонажа.
    global level;
    global war;
    global myheal;
    global mystamina;
    global money;
    global name_person;
    clear();
    print("%sИнформация о вас: %s" % (fg("yellow"), attr(0)));
    print("\t\t\t________________________________________")
    print("\t\t\t|Вы:", str(name_person));
    print("\t\t\t|ХП:", int(myheal));
    print("\t\t\t|Мана:", int(mystamina));
    print("\t\t\t|У вас:", int(money) , "монет");
    print("\t\t\t|Ваш уровень:", int(level));
    print("\t\t\t|Вы провели", int(war), "сражений.");
    print("\t\t\t‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    textexit();
    question_stat = int(input("::"));
    if (question_stat == 0):
        menu();
    else:
        print("Вы ввели что-то не то.");

def invent(): #Инвентарь.
    global litii
    global berilii
    global galii
    global indii
    global germanii
    global vanadii
    global titan
    global molibden

    clear();
    hud();
    print("У вас", litii , "Кг лития.");
    print("У вас", berilii , "Кг бериллия.");
    print("У вас", galii, "Кг галлия");
    print("У вас", indii, "Кг индия");
    print("У вас", germanii, "Кг германия");
    print("У вас", vanadii, "Кг ванадия");
    print("У вас", titan, "Кг титана");
    print("У вас", molibden, "Кг молибдена");
    textexit();
    question_invent = int(input("::"))
    if (question_invent == 0):
        menu();
    else:
        print("Вы ввели что-то не то");
def shop(): #Функция Магазин.
    global myheal;
    global mystamina;
    global money;
    hud();
    if (myheal <= 50):
        print("%s\t\t\tВам необходимо лечение! Пожалуйста примите зелье.%s" % (fg("red"), attr(0)));
                    #Первый каталог.
    print("\t\t\tВсё необходимое можно купить у нас в магазине!");
    print("[1]Зелье жизни I (+10 ХП)", "%s(20 Монет)%s" % (fg("yellow"), attr(0)));
    print("[2]Зелье жизни II (+30 ХП)", "%s(40 Монет)%s" % (fg("yellow"), attr(0)));
    print("[3]Зелье жизни III (+50 ХП)", "%s(60 Монет)%s" % (fg("yellow"), attr(0)));
    print("[4]Зелье жизни IV (+70 ХП)", "%s(80 Монет)%s" % (fg("yellow"), attr(0)));
    print("[5]Зелье жизни V(+90 ХП)", "%s(120 Монет)%s" % (fg("yellow"), attr(0)));

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

def cave(): #Функция пещеры
    global litii
    global berilii
    global galii
    global indii
    global germanii
    global vanadii
    global titan
    global molibden
    clear();
    print("Спуститься в пещеру? [1]Да [2]Нет");
    print("%sПРЕДУПРЕЖДЕНИЕ: выйти из пещеры можно будет только по истечению времени!%s" % (fg("red"), attr(0)));
    question_cave = int(input("::"));
    if (question_cave == 1):
        if (myheal <= 50):
            shop();
        else:
            b = 0;
            a = random.randint(20, 60);
            while a > b:
                print("\t\tДо прихода в пещеру осталось", a , "Сек.");
                time.sleep(1);
                clear();
                a = a - 1;
            print("%s\t\tВаш персонаж прибыл в пещеру!%s" % (fg("yellow"), attr(0)));
            metall_name = random.choice(dict.metall);
            print("\t\tВаш персонаж начал добычу редкого металла" , metall_name);
            time.sleep(3);
            if (a == 0):
                c = 0
                d = random.randint(20, 70);
                while c < d:
                    print("\t\tПерсонаж бьёт киркой изо всех сил, Пожалуйста ожидайте", d , "Сек.");
                    time.sleep(1);
                    clear();
                    d = d - 1;
            result = random.randint(0,1);
            if (result == 1):
                if (metall_name == "литий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    litii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", litii_kg , "Кг металла", metall_name);
                    litii += litii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "бериллий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    berilii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", berilii_kg , "Кг металла", metall_name);
                    berilii += berilii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "галиий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    galii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", galii_kg , "Кг металла", metall_name);
                    galii += galii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "индий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    indii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", indii_kg , "Кг металла", metall_name);
                    indii += indii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "германий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    germanii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", germanii_kg , "Кг металла", metall_name);
                    germanii += germanii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "ванадий"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    vanadii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", vanadii_kg , "Кг металла", metall_name);
                    vanadii += vanadii_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "титан"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    titan_kg = random.randint(1, 30);
                    print("\t\tВы собрали", titan , "Кг металла", metall_name);
                    titan += titan_kg;
                    time.sleep(3);
                    invent();
                elif(metall_name == "молибден"):
                    print("\t\t%sУспех!%s" % (fg("green"), attr(0)));
                    molibden_kg = random.randint(2, 30);
                    print("\t\tВы собрали", molibden_kg , "Кг металла", metall_name);
                    molibden += molibden_kg;
                    time.sleep(3);
                    invent();
            elif (result == 0):
                print("\t\t%sНеудача!\n\t\tВаш персонаж ничего не собрал%s" % (fg("red"), attr(0)));
                time.sleep(3);
                invent();
    elif (question_cave == 0):
        menu();
    else:
        print("Вы ввели что-то не то.");

def arena(): #Функция Арены.
    global myheal;
    global mystamina;
    global money;
    global level;
    global war;

      #Проверка на кол-во сражений для поднятия лвл'а.
    if (war == 5):
        level = level + 1;
    elif (war == 10):
        level = level + 1;
    elif (war == 15):
        level = level + 1;
    elif (war == 20):
        level = level + 1;
    elif (war >= 50):
        level = level + 1;

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
                shop();
            else:
                war = war + 1;
                print("%s\nВы%s" % (fg("green"), attr(0)), name_person , "%s%s\t\t\t\t[1]Атака%s" % (fg("red"),bg("white"), attr(0)) , "%s\t\t  Противник%s" % (fg("yellow"), attr(0)),random.choice(dict.names_bot));
                print("%sХП%s" % (fg("green"), attr(0)), myheal , "%s%s\t\t\t\t[2]Суперудар%s" % (fg("red"),bg("white"), attr(0)) , "%s\t\t  ХП:%s" % (fg("yellow"), attr(0)), bheal , "\n");
                q_two_arena = int(input("::"));
                if (q_two_arena == 1):
                    bheal = bheal - mydmg;
                    if (bheal <= 0):
                        print("\t\tВы нанесли", mydmg, "Противник,мёртв!");
                    else:
                        print("\t\tВы нанесли", mydmg, "урона.","У противника HP :", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("%s\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.%s" % (fg("red"), attr(0)));
                        death();
                    else:
                        print("\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mydmg >= bheal and myheal >=50):
                        money = money + present;
                        print("%s\t\tПобеда!%s" % (fg("green"), attr(0)));
                        print("\t\tПоздравляю вы победили!!! Ваша награда :",present);
                        time.sleep(4);
                    elif(mydmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        print("\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду :",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mydmg < bheal):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        print("\t\tВы не одалели противника,но он оставил вас в живых.");
                        print("\t\tНаграду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(mydmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        print("\t\tВы не одалели противника,но он оставил вас в живых.");
                        print("\t\tНаграду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mydmg >= bheal):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("%s\t\tПоражение!%s" % (fg("red"), attr(0)));
                        print("\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\tВам плохо выпейте лекарство");
                        time.sleep(3);
                        menu();
                    else:
                        arena();
                elif (q_two_arena == 2):
                    if(mystamina < 50):
                        print("У вас мало сил чтобы использовать суперудар!\nПосетите магазин и купите зелье");
                        time.sleep(3);
                        arena();
                    else:
                        mystamina = mystamina - 50;
                    bheal = bheal - mysuperdmg;
                    if (bheal <= 0):
                        print("\t\tВы нанесли", mysuperdmg, "Противник,мёртв!");
                    else:
                        print("\t\tВы нанесли", mysuperdmg, "урона.","У противника HP :", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("%s\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.%s" % (fg("red"), attr(0)));
                        death();
                    else:
                        print("\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mysuperdmg >= bheal and myheal >=50):
                        money = money + present;
                        print("%s\t\tПобеда!%s" % (fg("green"), attr(0)));
                        print("\t\tПоздравляю вы победили!!! Ваша награда :",present);
                        time.sleep(4);
                    elif(mysuperdmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        print("\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду :",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mysuperdmg < bheal):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        time.sleep(4)
                    elif(mysuperdmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        print("\t\tВы не одалели противника,но он оставил вас в живых. Награду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mysuperdmg >= bheal):
                        money = money + (present/2);
                        print("%s\t\tНичья!%s" % (fg("yellow"), attr(0)));
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("%s\t\tПоражение!%s" % (fg("yellow"), attr(0)))
                        print("\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\tВам плохо выпейте лекарство");
                        time.sleep(3);
                        menu();
                    else:
                        arena();
        elif(question_arena == 0):
            menu();
        else:
            print("Вы ввели что-то не то.");
    arena();

def menu(): #Функция Меню.
    hud();
    global myheal;
    global mystamina;
    global money;
    print("%s\n\n[1]Арена%s" % (fg("red"), attr(0)));
    print("%s[2]Пещера%s" % (fg("red"), attr(0)));
    print("%s[3]Магазин%s" % (fg("green"), attr(0)));
    print("%s[4]Инвентарь%s" % (fg("green"), attr(0)));
    print("%s[5]Статистика%s" % (fg("yellow"), attr(0)));
    print("%s[6]Настройки%s" % (fg("yellow"), attr(0)));
    print("[7]Выход");
    try:
      vod = int(input("\n::")) #Запрос ответа от игрока.
      if(vod == 1):
          arena();
      elif(vod == 2):
          cave();
      elif(vod == 3):
          shop();
      elif(vod == 4):
          invent();
      elif(vod == 5):
          stat();
      elif(vod == 6):
          settings();
      elif (vod == 7):
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
