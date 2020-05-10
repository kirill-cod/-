#Устанавливаем модуль для выбора случайного числа
import random
#Устанавливаем модуль для работы со временем
import time
#Устанавливаем модуль для интеграции Python и Postgresql
import psycopg2
#Установим соединение с базой данных
#Заменим значения параметров нашими учетными данными базы данных
conn = psycopg2.connect(
  database="MESSAGES", 
  user="kirill-kod",
  host="192.168.0.105",
  password="dq632004", 
  port="5432")  
#Создаем курсор для выполнения запросов к базе данных
cur = conn.cursor()
#Создаем таблицу, указываем имя таблицы, имена столбцов и тип данных
cur.execute("""CREATE TABLE SENDING MESSANGERS(
               id        INT,
               E-mail    TEXT,
               recipient TEXT,
               content   TEXT
            )""")  
conn.commit()
conn.close()

#Вставляем значения в таблицу
cur.execute("""INSERT INTO SENDING MESSANGERS (id, E-mail, recipient, content)
            VALUES(1, 'salesdirector@mail.ru', 'Сергей Николаевич', 'На товар стоимостью до 300 рублей установить скидку 10%')""")
#Выбираем случайное число из промежутка между 3 и 6 для установки задержки времени между созданием заданий
time.sleep(random.randint(3, 6))
cur.execute("""INSERT INTO SENDING MESSANGERS (id, E-mail, recipient, content)
            VALUES(2, 'staffdirector@mail.ru', 'Ольга Ивановна', 'По итогам работы за май наградить премией лучшего продавца')""")
time.sleep(random.randint(3, 6))
cur.execute("""INSERT INTO SENDING MESSANGERS (id, E-mail, recipient, content)
            VALUES(3, 'buhgalter@mail.ru', 'Татьяна Игоревна', 'Провести ивентаризацию дебиторской задолженности по состоянию на 31.05.2020')""")
time.sleep(random.randint(3, 6))
cur.execute("""INSERT INTO SENDING MESSANGERS (id, E-mail, recipient, content)
            VALUES(4, 'mediadirector@mail.ru', 'Дмитрий Петрович', 'Необходимо заказать рекламный ролик на ТВ в июне')""")
time.sleep(random.randint(3, 6))
cur.execute("""INSERT INTO SENDING MESSANGERS (id, E-mail, recipient, content)
            VALUES(5, 'mickson@mail.ru', 'Николай Григорьевич', 'Направляем Вам коммерческое предложение и предлагаем скидку в размере 5% на оптовые поставки')""")
time.sleep(random.randint(3, 6))

#Создаем очередь запросов и выполняем их
cur.execute("""SELECT id, E-mail, recipient, content
            FROM SENDING MESSANGERS""")
#Извлечение данных 
rows = cur.fetchall()  
#Выполнение заданий на рассылку из очереди
for row in rows:  
   print("ID = {}".format(row[0]))
   print("E-mail = {}".format(row[1]))
   print("RECIPIENT = {}".format(row[2]))
   print("CONTENT = {}".format(row[3]))
   #Устанавливаем определенное время задержки для периодической обработки заданий
   time.sleep(5)

#Получаем результат:
#ID = 1
#E-mail = salesdirector@mail.ru
#RECIPIENT = Сергей Николаевич
#CONTENT = На товар стоимостью до 300 рублей установить скидку 10%
   
#ID = 2
#E-mail = staffdirector@mail.ru
#RECIPIENT = Ольга Ивановна
#CONTENT = По этогам работы за май наградить премией лучшего продавца
   
#ID = 3
#E-mail = buhgalter@mail.ru
#RECIPIENT = Татьяна Игоревна
#CONTENT = Провести ивенторизацию дебиторской задолженности по состоянию на 31.05.2020
   
#ID = 4
#E-mail = mediadirector@mail.ru
#RECIPIENT = Дмитрий Петрович
#CONTENT = Необходимо заказать рекламный ролик на ТВ в июне
   
#ID = 5
#E-mail = mickson@mail.ru
#RECIPIENT = Николай Григорьевич
#CONTENT = Направляем Вам коммерческое предложение и предлагаем скидку в размере 5% на оптовые поставки
