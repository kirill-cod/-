#Импортируем библиотеку os(отвечающую за работу ОС)
import os
#Вводим переменную i для того, чтобы остановить цикл в случае, если файл найден
i = 0
#Печатаем сообщение для ввода названия файла, который необходимо найти
print("Введите название файла(с расширением):")
#Для ввода названия файла
filename = input()
#Перебор файлов, каталогов, файлов в каталогах во время поиска по диску C
for root, dirnames, filenames in os.walk('C:\\'):
        for file in filenames:
         #Условие для определения нужного нам файла
            if file == filename:
                if i == 0:
                 i = i + 1
                #Выводим в консоль найденный путь к файлу
                 print(os.path.join(root, file))
        #Если на диске С файл не найден, переходим к поиску на диске D
        #Перебор файлов, каталогов, файлов в каталогах во время поиска по диску D
        for root, dirnames, filenames in os.walk('D:\\'):
                for file in filenames:
                         #Условие для определения нашего файла
                    if file == filename:
                        
                        if i == 0:
                        
                            i = i + 1
                #Выводим в консоль найденный путь к файлу с диска и каталогов
                            print(os.path.join(root, file))
#Если у нас больше дисков больше, чем C и D, дополняем цикл с указанием других
#существующих дисков

#Запускаем программу
#Вводим название файла test.txt
#Получен результат: D:\\Кирилл\папка\test.txt
