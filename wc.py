"""
КРЕСТЬЯНИН
РАЗРАБОТКИЧИКИ: NULLHUMAN, X23006613159, Александр, Татьяна.
Дата: 11.06.2018.
"""
import os
import random
import time
from colored import bg, fg, attr

clear = lambda: os.system("clear"); #Функция для очистки консоли.
textexit = lambda: print("\n\n\t\t\t\tЧтобы выйти нажмите [0]"); #Функция текста выхода.

            #Переменные
gm = False;
level = 1 #Уровень персонажа.
myheal = 500;#Жизнь персонажа.
mystamina = 150;#Мана персонажа.
money = 150; #Деньги персонажа.
name_person = "notfing"; #Имя персонажа, если человек пропустил регистрацию.
war = 0 #Кол-во сражений по умолчанию.
kgmetall = 0; #Кол-во металла по умолчанию.

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
        print(colored.fg("\t\t\tИгра закончена! Ваш персонаж мёртв.",));
        time.sleep(5);
        level = 0;
        myheal = 500;
        mystamina = 150;
        money = 150;
        war = 0;
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
    print("""%s%s
     |  /   |--|  |----  |----  ---|---  |       |---|   |   |   |    /|   |   |
     | /    |  |  |      |         |     |       |   |   |   |   |   / |   |   |
     | \    |--|  |----  |         |     |---|   |---|   |---|   |  /  |   |---|
     |  \   |     |      |         |     |   |      /|   |   |   | /   |   |   |
     |   \  |     |----  |----     |     |---|    /  |   |   |   |/    |   |   |
    %s""" % (fg("red"),bg("black"), attr(0)));
    time.sleep(5);
    clear();
    print("\t\t\t\tРегистрация аккаунта.");
    print("%s%sПожалуйста введите ваш ник: %s" % (fg("blue"),bg(0), attr(0)));
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
        print("%s%s\t\tВы на грани жизни и смерти! Выпейте зелье!%s" % (fg("red"),bg(0), attr(0)));
    elif(mystamina <= 0):
        print("%s%s\t\tВы слишком уставший! Выпейте зелье!%s" % (fg("red"),bg(0), attr(0)));
    elif(money <= 0):
        print("%s%sСледуйте на арену, т.к у вас совсем нету монет.%s" % (fg("red"),bg(0), attr(0)));
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
    print("%s%sИнформация о вас: %s" % (fg("yellow"),bg("black"), attr(0)));
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
    clear();

def shop(): #Функция Магазин.
    global myheal;
    global mystamina;
    global money;
    hud();
    if (myheal <= 50):
        print("%s%s\t\t\tВам необходимо лечение! Пожалуйста примите зелье.%s" % (fg("red"),bg(0), attr(0)));
                    #Первый каталог.
    print("\t\t\tВсё необходимое можно купить у нас в магазине!");
    print("[1]Зелье жизни I (+10 ХП)", "%s%s(20 Монет)%s" % (fg("yellow"),bg(0), attr(0)));
    print("[2]Зелье жизни II (+30 ХП)", "%s%s(40 Монет)%s" % (fg("yellow"),bg(0), attr(0)));
    print("[3]Зелье жизни III (+50 ХП)", "%s%s(60 Монет)%s" % (fg("yellow"),bg(0), attr(0)));
    print("[4]Зелье жизни IV (+70 ХП)", "%s%s(80 Монет)%s" % (fg("yellow"),bg(0), attr(0)));
    print("[5]Зелье жизни V(+90 ХП)", "%s%s(120 Монет)%s" % (fg("yellow"),bg(0), attr(0)));

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
    global kgmetall;
    clear();
    print("Спуститься в пещеру? [1]Да [2]Нет");
    question_cave = int(input("::"));
    if (question_cave == 1):
        if (myheal <= 50):
            shop();
        else:
            b = 0;
            a = random.randint(10,90);
            while a > b:
                print("До прихода в пещеру осталось", a , "Сек.");
                time.sleep(1);
                clear();
                a = a - 1;
            print("%s%sВаш персонаж прибыл в пещеру!%s" % (fg("yellow"),bg(0), attr(0)));
            metall = ["литий", "бериллий", "галлий", "индий", "германий", "ванадий", "титан", "молибден", "вольфрам"];
            print("%s%sВаш персонаж начал добычу редкого металла%s" % (fg("red"),bg(0), attr(0), random.choice(metall)));
            time.sleep(3);
            if (a == 0):
                c = 0
                d = random.randint(30, 120);
                while c < d:
                    print("Персонаж бьёт киркой изо всех сил, Пожалуйста ожидайте", d , "Сек.");####чел слушай я сделал админ  мод в настр
                    time.sleep(1);
                    clear();
                    d = d - 1;
            result = random.randint(0,1);
            if (result == 1):
                print("%s%sУспех!%s" % (fg("green"),bg(0), attr(0)));
                metall_god = random.randint(1, 30);
                print("Вы собрали", metall_god , "Кг.");
                metall_god = metall_god + kgmetall;
                time.sleep(3);
                menu();
            elif (result == 0):
                print("%s%sНеудача!\nВаш персонаж ничего не собрал%s" % (fg("red"),bg(0), attr(0)));
                time.sleep(3);
                menu();
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
    names_bot = ["Богдан", "Мирослав", "Видогост", "Вратислава", "Всеведа", "Всемила",
       "Всенежа", "Всеслава", "Вторуша", "Вупна", "Вышенега", "Вышеслава", "Вьялица", "Вячеслава",
       "Вящеслава", "Галка", "Годица", "Годна", "Гожа", "Гойка", "Голица", "Голуба", "Горислава",
       "Гореслава", "Гостена", "Гремислава", "Градислава", "Гроздана", "Грёза", "Гроза", "Груша",
       "Гузица", "Даль", "Далина", "Дана", "Данута", "Дарёна", "Дарина", "Даролюба", "Даромила",
       "Дена", "Десислава", "Деснянка", "Дина", "Добрава", "Добринка", "Добромила", "Доброгнева",
       "Добродея", "Добромира", "Добронега", "Добронрава", "Доброслава", "Додола", "Долгождана",
       "Ждислава", "Желана", "Желанья", "Жиромира", "Жилена", "Жула", "Забава", "Зигота", "Загляда",
       "Звенислава", "Зимава", "Зима", "Злата", "Златовласка", "Златоцвета", "Зозуля", "Зорина",
       "Полада", "Полева", "Полеля", "Полонея", "Полуница", "Поляна", "Пороша", "Потана", "Потвора",
       "Прибыслава", "Пригода", "Рада", "Радана", "Радмила", "Радосвета",
       "Радомира", "Радослава", "Радостина", "Радость", "Ракита", "Репка", "Рогнеда", "Родника",
       "Родослава", "Росана", "Ростислава", "Рожа", "Ружица", "Румяна", "Русава", "Русана", "Рута",
       "Светла", "Светлана", "Светогора", "Светозара", "Светолика", "Светослава","Cавина", "Святослава",
       "Святохна", "Селеница", "Селяна", "Сила", "Синеока", "Сияна", "Скрева", "Смеяна", "Смирена",
       "Славолюба", "Славомила", "Славомира", "Славяна", "Сладка", "Собина", "Собислава", "Солоха",
       "Паря", "Пасмур", "Пачемир", "Пачеслав", "Пащек", "Певень", "Пелг", "Пепелюга", "Перван", "Первой", "Первонег", "Первослав", "Первуша",
       "Переверни", "Гора", "Перегуд", "Передслав", "Перемышль", "Перенег", "Переплут", "Перепят", "Пересвет", "Пересмага", "Пересмяк",
       "Переяр", "Переяслав", "Перко", "Перунько", "Перята", "Петун", "Пешка", "Пешок", "ПёсьяСтарость", "Пинай", "Пинещин", "Пискун", "Пирогость",
       "Путисил", "Путьша", "Путята", "Пучна", "Пырей", "Пяст", "Пятак", "Рагоза", "Радей", "Радех", "Радивой", "Радило", "Радим", "Радимир", "Радислав", "Радко", "Радобрат", "Радобой", "Радобуд",
       "Радован", "Радовзор", "Радовид", "Радовит", "Радогой", "Радогорд", "Радогость", "Радожар", "Радожир",
       "Радолюб", "Радом", "Радомил", "Радомир", "Радомысл", "Радонег", "Радосвет", "Радослав", "Радосул", "Радота", "Радотех", "Радочест", "Радош", "Радуж", "Размысл", "Разрывай", "Ковешников",
       "Рябзик", "Рядко", "Ряха", "Садко", "Само", "Самовит", "Самовлад", "Саморад",
       "Славонег", "Славосуд", "Славотех", "Савин", "Славята", "Слинько", "Слободан", "Брагин", "Словута", "Слон", "Слудый", "Смага",
       "Смехн", "Смеян", "Смил", "Смирной", "Смола", "Смолига", "Смык", "Смысл", "Снежко", "Сновид", "Собеслав", "Собигорд",
       "Собидраг", "Собимил", "Собимысл", "Собин", "Собирад", "Соболь", "Собота", "Сова", "Содлилка", "Сокол",
       "Сокольник", "Солнце", "Соловей", "Сомжар", "Сонцеслав", "Сорока", "Сочень", "Спех", "Спирок", "Спитигнев", "Спичак", "Ставок", "Ставр", "Станивук",
       "Станил", "Станило", "Станимир", "Станислав", "Станята", "Старовит", "Старовойт", "Старой", "Старослав",
       "Стуш", "Стырь", "Сувор", "Мидак", "Судибор", "Судивой", "Судимир", "Судислав", "Судиша", "Судор", "Сул",
       "Сулибор", "Суливой", "Сулимир", "Сулислав", "Сулирад", "Сумник", "Суморок", "Суровен", "Сусара",
       "Сухой", "Сухобор", "Суховерх", "Сухослав", "Суш", "Сандаль", "Быков", "Лобанов","LIL PEEP"
       "Сып", "Сыт", "Сябр", "Табомысл", "Таислав", "Талалай", "Талец", "Таргитай", "Тас", "Татомир", "Твердибой", "Твердило", "Твердимир", "Твердин", "Твердислав", "Кизяку", "Иванов", "Твердодраг", "Твердолик", "Твердополк",
       "Твердош", "Твердята", "Творинег", "Творирад", "Творилад", "Творило","Ковешников",
       "Творимир", "Творислав", "Творьян", "Телепень", "Тепло", "Тепта",
       "Ушак", "Ушмян", "Хвалимир", "Хвалибог", "Хвалибор", "Хвалислав", "Хват",
       "Хвилибуд", "Хвост", "Хвороща", "Хвощ", "Хижа", "Хитран","Хвороба",];

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
                print("%s%s\nВы%s" % (fg("green"),bg(0), attr(0)), name_person , "%s%s\t\t\t\t[1]Атака%s" % (fg("red"),bg("white"), attr(0)) , "%s%s\t\t  Противник%s" % (fg("yellow"),bg(0), attr(0)),random.choice(names_bot));
                print("%s%sХП%s" % (fg("green"),bg(0), attr(0)), myheal , "%s%s\t\t\t\t\t[2]Суперудар%s" % (fg("red"),bg("white"), attr(0)) , "%s%s\t\t\t  ХП:%s" % (fg("yellow"),bg(0), attr(0)), bheal , "\n");
                q_two_arena = int(input("::"));
                if (q_two_arena == 1):
                    bheal = bheal - mydmg;
                    if (bheal <= 0):
                        print("\t\t\tВы нанесли", mydmg, "Противник,мёртв!");
                    else:
                        print("\t\t\tВы нанесли", mydmg, "урона.","У противника HP :", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("%s%s\t\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.%s" % (fg("red"),bg(0), attr(0)));
                        death();
                    else:
                        print("\t\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mydmg >= bheal and myheal >=50):
                        money = money + present;
                        print("%s%s\t\t\tПобеда!%s" % (fg("green"),bg(0), attr(0)));
                        print("\t\t\tПоздравляю вы победили!!! Ваша награда :",present);
                        time.sleep(4);
                    elif(mydmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        print("\t\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду :",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mydmg < bheal):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        print("\t\t\tВы не одалели противника,но он оставил вас в живых. Награду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(mydmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        print("\t\t\tВы не одалели противника,но он оставил вас в живых. Награду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mydmg >= bheal):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("%s%s\t\t\tПоражение!%s" % (fg("red"),bg(0), attr(0)));
                        print("\t\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\t\tВам плохо выпейте лекарство");
                        time.sleep(3);
                        menu();
                    else:
                        arena();
                elif (q_two_arena == 2):
                    bheal = bheal - mysuperdmg;
                    if (bheal <= 0):
                        print("\t\t\tВы нанесли", mysuperdmg, "Противник,мёртв!");
                    else:
                        print("\t\t\tВы нанесли", mysuperdmg, "урона.","У противника HP :", bheal);
                    myheal = myheal - bdmg;
                    if  (myheal <= 0):
                        print("%s%s\t\t\tПРЕДУПРЕЖДЕНИЕ: Противник нанёс вам критический удар.%s" % (fg("red"),bg(0), attr(0)));
                        death();
                    else:
                        print("\t\t\tВам нанесли",bdmg ,"урона.","Ваше HP: ", myheal);
                    if(mysuperdmg >= bheal and myheal >=50):
                        money = money + present;
                        print("%s%s\t\t\tПобеда!%s" % (fg("green"),bg(0), attr(0)));
                        print("\t\t\tПоздравляю вы победили!!! Ваша награда :",present);
                        time.sleep(4);
                    elif(mysuperdmg >= bheal and myheal <=50):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        print("\t\t\tВаш противник побеждён но вы тоже повреждены.Вы поделили награду :",present);
                        time.sleep(4);
                    elif(myheal > bdmg and mysuperdmg < bheal):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        time.sleep(4)
                    elif(mysuperdmg < bheal and bheal <=50 and myheal <=50):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        print("\t\t\tВы не одалели противника,но он оставил вас в живых. Награду он поделил с вами : ", present);
                        time.sleep(4);
                    elif(bdmg >= myheal and mysuperdmg >= bheal):
                        money = money + (present/2);
                        print("%s%s\t\t\tНичья!%s" % (fg("yellow"),bg(0), attr(0)));
                        time.sleep(4);
                    elif(myheal <= 0):
                        money = money + (present/5);
                        print("%s%s\t\t\tПоражение!%s" % (fg("yellow"),bg(0), attr(0)))
                        print("\t\t\tТебя победили. Ты проиграл.");
                        time.sleep(4);
                        death();
                    if(myheal <=50):
                        print("\t\t\tВам плохо выпейте лекарство");
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
    print("%s%s\n\n[1]Арена%s" % (fg("red"),bg(0), attr(0)));
    print("%s%s[2]Пещера%s" % (fg("red"),bg(0), attr(0)));
    print("%s%s[3]Магазин%s" % (fg("green"),bg(0), attr(0)));
    print("%s%s[4]Инвентарь%s" % (fg("green"),bg(0), attr(0)));
    print("%s%s[5]Статистика%s" % (fg("yellow"),bg(0), attr(0)));
    print("%s%s[6]Настройки%s" % (fg("yellow"),bg(0), attr(0)));
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

checkin();
