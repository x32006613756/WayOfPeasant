#!/usr/bin/env python3

#Версия для Виндус.

"""
КРЕСТЬЯНИН
РАЗРАБОТКИЧИКИ: NULLHUMAN, X23006613159, Александр, PINKUNICORN.
Дата: 11.06.2018.
"""

import os
import random
import time
import dict

            #Переменные персонажа.
gm = False #Режим бога по умолчанию выключен.
level = 1 #Уровень персонажа.
myheal = 500 #Жизнь персонажа.
mystamina = 150 #Мана персонажа.
money = 150 #Деньги персонажа.
name_person = "notfing" #Имя персонажа, если человек пропустил регистрацию.
war = 0 #Кол-во сражений по умолчанию.
            #Переменные для различных металлов по умолчанию.
litii = 0 #Переменная для кол-во лития по умолчанию.
berilii = 0 #Кол-во бериллия.
galii = 0 #Кол-во галлия.
indii = 0 #Кол-во индия.
germanii = 0 #Кол-во германия.
vanadii = 0 #Кол-во ванадия.
titan = 0 #Кол-во титана.
molibden = 0 #Кол-во молибдена.

clear = lambda: os.system("cls"); #Функция для очистки консоли.
textexit = lambda: print("\n\n\t\t\t\tЧтобы выйти нажмите [0]"); #Функция текста выхода.

def death(): #Функция смерти персонажа.
    global level;
    global myheal;
    global money;
    global mystamina;
    global name_person;
    global war;
    death = random.randint(0, 1);
    if (death == 0 or death == 1 and money <= 0):
        time.sleep(2);
        clear();
        print("\t\t\tИгра закончена! Ваш персонаж мёртв.");
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

def logo(): #Функция лого при запуске.
    clear();
    print("\t\t\t\tДобро пожаловать в игру.");
    time.sleep(2);
    print("\t\tЛюбые совпадения с историческими событиями чистейшая случайность.");
    time.sleep(2);
    print("""
     |  /   |--|  |----  |----  ---|---  |       |---|   |   |   |    /|   |   |
     | /    |  |  |      |         |     |       |   |   |   |   |   / |   |   |
     | \    |--|  |----  |         |     |---|   |---|   |---|   |  /  |   |---|
     |  \   |     |      |         |     |   |      /|   |   |   | /   |   |   |
     |   \  |     |----  |----     |     |---|     / |   |   |   |/    |   |   |
    """);
    time.sleep(5);
    checkin();

def checkin(): #Функция регистрации.
    global name_person
    clear();
    print("\t\t\t\tРегистрация аккаунта.");
    print("Пожалуйста введите ваш ник:");
    del name_person;
    name_person = input("::");
    if (len(name_person) > 10):
        print("Максимум 10 символов.");
        time.sleep(1)
        checkin();
    else:
        menu(); #Функция регистрации.

def hud(): #Функция показателей персонажа.
    global gm;
    global name_person;
    global myheal;
    global mystamina;
    global money;
    global level
    clear();
    if(myheal <= 0):
        print("\t\tВы на грани жизни и смерти! Выпейте зелье!");
    elif(money <= 0):
        print("Следуйте на арену, т.к у вас совсем нету монет.");
    else:
        print("\t|","Вы",str(name_person), "|", "Ваше ХП:",int(myheal), "|", "Ваша Мана:",int(mystamina), "|", "Деньги :" ,int(money), "|" , "Ваш уровень:", int(level),"|");

def faq(): #Функция информации об игре.
    clear();
    hud();
    print('Добро пожаловать в игру под названием "Way Of Peasant"');
    print("Здесь вы можете узнать основы и игры  её тонкости ");
    print("Арена - Используется как добыча денег и поднятия вашего уровня");
    print("Магазин - в магазине вы можете купить зелье здоровья или маны");
    print("Пещера - ещё один вид заработка в игре.\nТут вам предстоит спуститься в пещеру и добывать металл позже продать его в магазине");
    print("Статистика - это место где вы можете узнать информацию о своём персонаже");
    print("Так же ваш персонаж может умереть если его здоровье будет равно нулю !!!НЕ ДОПУСКАЙТЕ ЭТОГО!!!\nПосле того как он умрёт у вас всё обнулится и игра начнётся заного");
    print("В пещере вы можете собрать ничего если ваш персонаж плохо потрудится ");
    print("Если у вас будет мало здоровья то вы не сможете попасть на арену");
    print("Игра будет дорабатываться и обновляться...");
    print("Следите за новостями тут ------> vk.com/wayofpeasant <------");
    print("Разработчики: NULLHUMAN, x32006613756, Александр, PINKUNICORN");
    textexit();
    question_faq = int(input("::"));
    if (question_faq == 0):
        menu();
    else:
        print("Вы ввели что-то не то.");

def settings(): #Функция Настроек.
    clear();
    global name_person;
    print ("[1]Сменить имя");
    textexit();
    question_settings = int(input("::"));
    if(question_settings == 1):
        clear();
        print("Введите новое имя:");
        name_person = input("::");
        if (len(name_person) > 10):
            print("Имя должно иметь не больше 10 символов.");
            time.sleep(1);
            settings();
        else:
            print("Ваше новое имя выглядит вот так:", name_person);
            time.sleep(2);
            menu();
    elif(question_settings == 0):
        menu();
    elif(question_settings == 7777):
        global myheal;
        global money;
        global mystamina;
        money = money + 7777;
        myheal = myheal + 7777;
        mystamina = mystamina + 7777;
        print("GodMode: ON")
        time.sleep(2);
        menu();
    else:
        print("Вы ввели что-то не то.");
    textexit();

def stat(): #Функция статистики персонажа.
    global level;
    global war;
    global myheal;
    global mystamina;
    global money;
    global name_person;
    rank = ("Новичёк","Боец","Освоившийся","Убийца","Ветеран",)
    clear();
    if(level == 1):
        rank = "Новичёк"
    elif(level == 2 or level == 3):
        rank = "Боец"
    elif(level == 4 or level == 5):
        rank = "Освоившийся"
    elif(level == 6 or level == 7):
        rank = "Убийца"
    elif(level == 8 or level == 9):
        rank = "Ветеран"
    else:
        rank = NONE;
    print("Информация о вас: ");
    print("\t\t\t________________________________________")
    print("\t\t\t|Вы:", str(name_person));
    print("\t\t\t|ХП:", int(myheal));
    print("\t\t\t|Мана:", int(mystamina));
    print("\t\t\t|У вас:", int(money) , "монет");
    print("\t\t\t|Ваш уровень:", int(level));
    print("\t\t\t|Вы провели", int(war), "сражений.");
    print("\t\t\t|Ваше звание :",str(rank))
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
    print("\t\tВаш инвентарь:");
    print("\nУ вас", litii , "Кг лития.");
    print("У вас", berilii , "Кг бериллия.");
    print("У вас", galii, "Кг галлия.");
    print("У вас", indii, "Кг индия.");
    print("У вас", germanii, "Кг германия.");
    print("У вас", vanadii, "Кг ванадия.");
    print("У вас", titan, "Кг титана.");
    print("У вас", molibden, "Кг молибдена.");
    textexit();
    question_invent = int(input("::"))
    if (question_invent == 0):
        menu();
    else:
        print("Вы ввели что-то не то.");

def trade(): #Функция торговли металлом.
    global litii
    global berilii
    global galii
    global indii
    global germanii
    global vanadii
    global titan
    global molibden
    global money

    clear();
    hud();
    print("\t\tЦены реального времени:");
    litii_coin = random.randint(100, 150);
    print("\n[1]На 1 кг лития", litii_coin, "Монет.");
    berilii_coin = random.randint(100, 150);
    print("[2]На 1 кг бериллия", berilii_coin, "Монет.");
    galii_coin = random.randint(100, 150);
    print("[3]На 1 кг галлия ", galii_coin, "Монет.");
    indii_coin = random.randint(100, 150);
    print("[4]На 1 кг индия ", indii_coin, "Монет.");
    germanii_coin = random.randint(100, 150);
    print("[5]На 1 кг германия ", germanii_coin, "Монет.");
    vanadii_coin = random.randint(100, 150);
    print("[6]На 1 кг ванадия ", vanadii_coin, "Монет.");
    titan_coin = random.randint(100, 150);
    print("[7]На 1 кг титана ", titan_coin, "Монет.");
    molibden_coin = random.randint(100, 150);
    print("[8]На 1 кг молибдена ", molibden_coin, "Монет.");

    textexit();
    question_trade = int(input("::"));
    if (question_trade == 0):
        menu();
    elif (question_trade == 1):
        if (litii <= 0):
            print("У вас нету лития.");
            time.sleep(1);
            menu();
        else:
            litii = litii - 1;
            money = litii_coin + money;
            trade();
    elif (question_trade == 2):
        if (berilii <= 0):
            print("У вас нету бериллия.");
            time.sleep(1);
            menu();
        else:
            berilii = berilii -1;
            money = berilii_coin + money;
            trade();
    elif (question_trade == 3):
        if (galii <= 0):
            print("У вас нету галия.");
            time.sleep(1);
            menu();
        else:
            galii = galii - 1;
            money = galii_coin + money;
            trade();
    elif (question_trade == 4):
        if (indii <= 0):
            print("У вас нету индия.");
            time.sleep(1);
            menu();
        else:
            indii = indii - 1;
            money = indii_coin + money;
            trade();
    elif (question_trade == 5):
        if (germanii <= 0):
            print("У вас нету германия.");
            time.sleep(1);
            menu();
        else:
            germanii = germanii - 1;
            money = germanii_coin + money;
            trade();
    elif (question_trade == 6):
        if (vanadii <= 0):
            print("У вас нету ванадия.");
            time.sleep(1);
            menu();
        else:
            vanadii = vanadii - 1;
            money = vanadii_coin + money;
            trade();
    elif (question_trade == 7):
        if (titan <= 0):
            print("У вас нету титана.");
            time.sleep(1);
            menu();
        else:
            titan = titan - 1;
            money = titan_coin + money;
            trade();
    elif (question_trade == 8):
        if (molibden <= 0):
            print("У вас нету молибдена.");
            time.sleep(1);
            menu();
        else:
            molibden = molibden - 1;
            money = molibden_coin + money;
            trade();
    else:
        print("Вы ввели что-то не то.");
        time.sleep(1);
        trade();

def shop():#Функция магазина.
    global myheal;
    global mystamina;
    global money;
    hud();
    if (myheal <= 50):
        print("\t\t\tВам необходимо лечение! Пожалуйста примите зелье.");
                    #Первый каталог.
    print("\t\t\tВсё необходимое можно купить у нас в магазине!");
    print("[1]Зелье жизни I (+10 ХП)", "(20 Монет)" , "[6]Зелье силы I (+10 Маны)", "(25 Монет)");
    print("[2]Зелье жизни II (+30 ХП)", "(40 Монет)" , "[7]Зелье силы II (+25 Маны)", "(40 Монет)");
    print("[3]Зелье жизни III (+50 ХП)", "(60 Монет)", "[8]Зелье силы III (+35 Маны)", "(50 Монет)");
    print("[4]Зелье жизни IV (+70 ХП)", "(80 Монет)", "[9]Зелье силы IV (+40 Маны)", "(65 Монет)");
    print("[5]Зелье жизни V(+90 ХП)", "(120 Монет)", "[10]Зелье силы V (+60 Маны)", "(80 Монет)");

    textexit();
    question_shop = int(input("\n::"));

    if (question_shop == 1):#20
        if(money < 20):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 40;
            myheal = myheal + 20;
            clear();
            shop();
    elif(question_shop == 2):
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 40;
            myheal = myheal + 30;
            clear();
            shop();
    elif(question_shop == 3):#60
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 60;
            myheal = myheal + 60;
            clear();
            shop();
    elif(question_shop == 4):#80
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 80;
            myheal = myheal + 80;
            clear();
            shop();
    elif(question_shop == 5):#120
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 120;
            myheal = myheal + 120;
            clear();
            shop();
    elif (question_shop == 6):#20
        if(money < 20):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 25;
            mystamina = mystamina + 10;
            clear();
            shop();
    elif(question_shop == 7):
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 40;
            mystamina = mystamina + 25;
            clear();
            shop();
    elif(question_shop == 8):#60
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 50;
            mystamina = mystamina + 35;
            clear();
            shop();
    elif(question_shop == 9):#80
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 55;
            mystamina = mystamina + 40;
            clear();
            shop();
    elif(question_shop == 10):#120
        if(money < 40):
            print("У вас недостаточно Монет.")
            time.sleep(1);
            menu();
        else:
            money = money - 80;
            mystamina = mystamina + 60;
            clear();
            shop();
    elif (question_shop == 0):#
        menu();

def cave(): #Функция пещеры.
    global litii
    global berilii
    global galii
    global indii
    global germanii
    global vanadii
    global titan
    global molibden
    clear();
    print("Пещера - служит для  добычи разнличных металлов.");
    print("Спуститься в пещеру? [1]Да [0]Нет");
    print("ПРЕДУПРЕЖДЕНИЕ: выйти из пещеры можно будет только по истечению времени!");
    question_cave = int(input("::"));
    if (question_cave == 1):
        if (myheal <= 50):
            shop();
        else:
            b = 0;
            a = random.randint(5, 20);
            while a > b:
                print("\t\tДо прихода в пещеру осталось", a , "Сек.");
                time.sleep(1);
                clear();
                a = a - 1;
            print("\t\tВаш персонаж прибыл в пещеру!");
            metall_name = random.choice(dict.metall);
            print("\t\tВаш персонаж начал добычу редкого металла." , metall_name);
            time.sleep(2);
            if (a == 0):
                c = 0
                d = random.randint(10, 30)
                while (c < d):
                    print("\t\tПерсонаж бьёт киркой изо всех сил, Пожалуйста ожидайте", d , "Сек.");
                    time.sleep(1);
                    clear();
                    d = d - 1;
            result = random.randint(1,2);
            if (result == 1):
                if (metall_name == "литий"):
                    print("\t\tУспех!");
                    litii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", litii_kg , "Кг металла", metall_name);
                    litii += litii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "бериллий"):
                    print("\t\tУспех!");
                    berilii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", berilii_kg , "Кг металла", metall_name);
                    berilii += berilii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "галиий"):
                    print("\t\tУспех!");
                    galii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", galii_kg , "Кг металла", metall_name);
                    galii += galii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "индий"):
                    print("\t\tУспех!");
                    indii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", indii_kg , "Кг металла", metall_name);
                    indii += indii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "германий"):
                    print("\t\tУспех!");
                    germanii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", germanii_kg , "Кг металла", metall_name);
                    germanii += germanii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "ванадий"):
                    print("\t\tУспех!");
                    vanadii_kg = random.randint(1, 30);
                    print("\t\tВы собрали", vanadii_kg , "Кг металла", metall_name);
                    vanadii += vanadii_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "титан"):
                    print("\t\tУспех!");
                    titan_kg = random.randint(1, 30);
                    print("\t\tВы собрали", titan , "Кг металла", metall_name);
                    titan += titan_kg;
                    time.sleep(2);
                    invent();
                elif(metall_name == "молибден"):
                    print("\t\tsУспех!");
                    molibden_kg = random.randint(2, 30);
                    print("\t\tВы собрали", molibden_kg , "Кг металла", metall_name);
                    molibden += molibden_kg;
                    time.sleep(2);
                    invent();
            elif (result == 2):
                print("\t\tНеудача!\n\t\tВаш персонаж ничего не собрал.");
                time.sleep(2);
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
    elif (war >= 25):
        level = level + 1;
    elif (war == 30):
        level = level + 1;
    elif (war == 35):
        level = level + 1;
    elif (war == 40):
        level = level + 1;
    elif (war >= 45):
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
                print("\nВы",  name_person , "\t\t\t\t[1]Атака", "\t\t  Противник" ,random.choice(dict.names_bot));
                print("ХП" , myheal , "\t\t\t\t[2]Суперудар", "\t\t  ХП:", bheal , "\n");
                q_two_arena = int(input("::"));
                if (q_two_arena == 1):
                    bheal = bheal - mydmg;
                    if (bheal <= 0):
                        print("\t\tВы нанесли", mydmg, "Противник,мёртв!");
                    else:
                        print("\t\tВы нанесли", mydmg, "урона.","У противника HP:", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.");
                        death();
                    else:
                        print("\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mydmg >= bheal and myheal >=50 and bheal <=100):
                        money = money + present;
                        print("\t\tПобеда!");
                        print("\t\tПоздравляю вы победили!!! Ваша награда:",present);
                        time.sleep(4);
                    elif(mydmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        print("\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду:",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mydmg < bheal):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        print("\t\tВы не одалели противника,но он оставил вас в живых.");
                        print("\t\tНаграду он поделил с вами: ", present);
                        time.sleep(4);
                    elif(mydmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        print("\t\tВы не одалели противника,но он оставил вас в живых.");
                        print("\t\tНаграду он поделил с вами: ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mydmg >= bheal):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("\t\tПоражение!");
                        print("\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\tВам плохо выпейте лекарство.");
                        time.sleep(2);
                        menu();
                    else:
                        arena();
                elif (q_two_arena == 2):
                    if(mystamina < 50):
                        print("У вас мало сил чтобы использовать суперудар!\nПосетите магазин и купите зелье.");
                        time.sleep(2);
                        arena();
                    else:
                        mystamina = mystamina - 50;
                    bheal = bheal - mysuperdmg;
                    if (bheal <= 0):
                        print("\t\tВы нанесли", mysuperdmg, "Противник,мёртв!");
                    else:
                        print("\t\tВы нанесли", mysuperdmg, "урона.","У противника HP:", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.");
                        death();
                    else:
                        print("\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mysuperdmg >= bheal and myheal >=50):
                        money = money + present;
                        print("\t\tПобеда!");
                        print("\t\tПоздравляю вы победили!!! Ваша награда:",present);
                        time.sleep(4);
                    elif(mysuperdmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        print("\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду:",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mysuperdmg < bheal):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        time.sleep(4)
                    elif(mysuperdmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        print("\t\tВы не одалели противника,но он оставил вас в живых. Награду он поделил с вами: ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mysuperdmg >= bheal):
                        money = money + (present/2);
                        print("\t\tНичья!");
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("\t\tПоражение!")
                        print("\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\tВам плохо выпейте лекарство.");
                        time.sleep(2);
                        menu();
                    else:
                        arena();
        elif(question_arena == 0):
            menu();
        else:
            print("Вы ввели что-то не то.");
            time.sleep(1);
            menu();
    arena();

def menu(): #Функция Меню.
    hud();
    global myheal;
    global mystamina;
    global money;
    print("\n\n[1]Арена");
    print("[2]Пещера");
    print("[3]Магазин");
    print("[4]Торговая лавка");
    print("[5]Инвентарь");
    print("[6]Статистика");
    print("[7]F.A.Q");
    print("[8]Настройки");
    print("[9]Выход");
    try:
      question_menu = int(input("\n::")) #Запрос ответа от игрока.
      if(question_menu == 1):
          arena();
      elif(question_menu == 2):
          cave();
      elif(question_menu == 3):
          shop();
      elif(question_menu == 4):
          trade();
      elif(question_menu == 5):
          invent();
      elif(question_menu == 6):
          stat();
      elif(question_menu == 7):
          faq();
      elif(question_menu == 8):
          settings();
      elif (question_menu == 9):
          os.system("exit");
      else:
          print("Такого выбора нету");
          time.sleep(1);
          menu();
    except ValueError:
        print("Вы ввели что-то не то.");
        time.sleep(1);
        menu();

logo();
input("::");
