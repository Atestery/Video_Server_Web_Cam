#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# import time
# import datetime
# import os
# os.system('clear') - linux.Windows- os.system('CLS').
import os  # Подкл библиотеку , можем выполнять команды в терминале,для определения ip
import shutil #Для удаление каталога с файлами
import time
import threading  # Потоки
import datetime  # определение времени и даты
import os
import smtplib  # для отправки почты
from datetime import datetime
import subprocess #для присвоение переменной результат команды system()
import commands #для проверки даты создания последнего файла функция videosrv()

#Библиотеки для получения списка файлов в папке, использую для проверки записан ли видеофайл
from os import listdir
from os.path import isfile, join



"""
def logwrfile(message):
    try:
        #print("\n -0---0----0---0--0---0--0--")
        from datetime import datetime
        #print(datetime.now())
        #print(message)
        #print("-1-----1-----1-----1-----1---1--")
        # Делаем запись в лог, смотрим командой tail -f /var/log/telebot.log
        # os.system("cat /var/log/telebot.log")
        # chmod -R o+rw /home/sixven
        # chmod -R 777 /home/pi/myprogramming/rasberry/telebot/log/
        # Добавляю дату в название лога, чтобы создавать каждый день новый лог
        # datein = datetime.strftime(datetime.now(), "%Y.%m.%d")
        # file = open('/home/pi/myprogramming/rasberry/telebot/log/telebot.log', 'a')

        #now = datetime.now()
        # Получаем дату для создания папки по названию даты:
        #datein = datetime.strftime(datetime.now(), "%d.%m.%Y")
        #dirpath = datein

        #Тут пишем код на проверку самой папки log
        # Проверяем если папка для лога есть пишем в нее, если ее нет то создаем ее и пишем в нее
        if os.path.exists('/home/pi/myprogramming/videowebcam/logwrfile'):
            #print("Проверка существования папки по пути: /home/pi/myprogramming/videowebcam/log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('/home/pi/myprogramming/videowebcam/logwrfile/' + datein + '.log', 'a')
            #file.write("\n")
            #file.write("\n")
            #file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            #file.write("\n")
            file.write(message)
            file.write("\n")
            #file.write("1-------------------------------------------1")
            #file.write("\n")
            #file.write("\n")
            file.close()
        else:
            # Если такой папки нет то создаем ее и пишем в нее
            os.makedirs('/home/pi/myprogramming/videowebcam/logwrfile')  # Создаю такую папку и пишу в нее
            #print("Создал папку по пути: /home/pi/myprogramming/videoserver/log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('/home/pi/myprogramming/videowebcam/logwrfile/' + datein + '.log', 'a')
            #file.write("\n")
            #file.write("\n")
            #file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            #file.write("\n")
            file.write(message)
            file.write("\n")
            #file.write("1-------------------------------------------1")
            #file.write("\n")
            #file.write("\n")
            file.close()
    except Exception as err:
        log("Сработало Исключение в функции logwrfile.")
        log(str(err))

"""



def log(message):
    try:
        from datetime import datetime
        if os.path.exists('/home/pi/myprogramming/videowebcam/log'):
            #print("Проверка существования папки по пути: /home/pi/myprogramming/videowebcam/log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('/home/pi/myprogramming/videowebcam/log/' + datein + '.log', 'a')
            file.write("\n")
            file.write("\n")
            file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            file.write("\n")
            file.write(message)
            file.write("\n")
            file.write("1-------------------------------------------1")
            file.write("\n")
            file.write("\n")
            file.close()
        else:
            # Если такой папки нет то создаем ее и пишем в нее
            os.makedirs('/home/pi/myprogramming/videowebcam/log')  # Создаю такую папку и пишу в нее
            #print("Создал папку по пути: /home/pi/myprogramming/videoserver/log")
            datein = datetime.strftime(datetime.now(), "%d_%m_%Y")
            file = open('/home/pi/myprogramming/videowebcam/log/' + datein + '.log', 'a')
            file.write("\n")
            file.write("\n")
            file.write("0-------------------------------------------0")
            file.write("\n")
            file.write(str(datetime.now()))
            file.write("\n")
            file.write(message)
            file.write("\n")
            file.write("1-------------------------------------------1")
            file.write("\n")
            file.write("\n")
            file.close()
    except Exception as err:
        log("Сработало Исключение в функции log.")
        log(str(err))



def email(emailmessage):
    try:
        smtpUser = 'кто отправляет@mail.ru'
        smtpPass = 'пароль того кто отправляет'
        toAdd = 'кому отправлять@mail.ru'
        fromAdd = smtpUser
        subject = 'Оповещение!'
        header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
        body = emailmessage
        #print(header + '\n' + body)
        s = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        s.login(smtpUser, smtpPass)
        s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
        s.quit()
    except Exception as err:
        log("Сработало Исключение в функции email.")
        log(str(err))



def contfclrdisk():
    try:
        while True:
            textnamedisk = subprocess.check_output('df -h', shell=True)
            index = textnamedisk.find("/dev/sd")
            index = index + 5  # повышаем индекс до названия диска
            textnamedisk = textnamedisk[index:index + 4]
            output = subprocess.check_output('df -h /dev/' + textnamedisk, shell=True)
            index = output.find("% /media")
            if output[index - 1] != ' ':
                buffer = output[index - 1]
                if output[index - 2] != ' ':
                    buffer = output[index - 2] + output[index - 1]
                    if output[index - 3] != ' ':
                        buffer = output[index - 3] + output[index - 2] + output[index - 1]
            buffer = int(buffer)
            if (buffer > 90):# Если диск занят больше 80% то удаляем старые папки с файлами
                email("Videoserver: Диск занят более 90%, запускается contfclrdisk")
                textnamedisk = subprocess.check_output('df -h', shell=True)
                index = textnamedisk.find("media")
                index = index + 9  # повышаем индекс до названия диска
                textnamedisk = textnamedisk[index:]
                buf = textnamedisk.split('\n')
                textnamedisk = buf[0]
                path = '/media/pi/' + textnamedisk
                name_list = os.listdir(path)
                full_list = [os.path.join(path, i) for i in name_list]
                time_sorted_list = sorted(full_list, key=os.path.getmtime)
                shutil.rmtree(time_sorted_list[0])
                shutil.rmtree(time_sorted_list[1])
                shutil.rmtree(time_sorted_list[2])
                #shutil.rmtree(time_sorted_list[3])
                #shutil.rmtree(time_sorted_list[4])
                email("Videowebcamserver: Удалены старые 3 папки.")
            flaghour = False
            textnamedisk = subprocess.check_output('df -h', shell=True)
            index = textnamedisk.find("media")
            index = index + 9  # повышаем индекс до названия диска
            textnamedisk = textnamedisk[index:]
            buf = textnamedisk.split('\n')
            textnamedisk = buf[0]
            path = '/media/pi/' + textnamedisk
            dirpath = datetime.strftime(datetime.now(), "%d.%m.%Y")
            path = path + '/' + dirpath
            hvideofile = datetime.strftime(datetime.now(), "%H")
            mvideofile = datetime.strftime(datetime.now(), "%M")
            log(dirpath + ' ' + path + ' ' + str(hvideofile) + ' ' + str(mvideofile) + ' ' + textnamedisk)
            if int(mvideofile) > 30:
                if os.path.exists(path):
                    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
                    a = 0
                    while a < len(onlyfiles):
                        clockh = onlyfiles[a]
                        clockh = clockh.split('-')
                        clockh = clockh[1]
                        clockh = clockh.split(':')
                        clockh = clockh[0]
                        if int(clockh) == int(hvideofile):
                            flaghour = True
                            log(str(flaghour))
                            # print("Файл существует")
                        a = a + 1
                    if flaghour == False:
                        log(str(flaghour))
                        # print("Файл не найден. Время файла (час H:): ")
                        # print(hvideofile)
                        email("Файл не найден. Время файла (час H:): " + str(hvideofile))
                        log("Файл не найден. Время файла (час H:): " + str(hvideofile))
                else:
                    # Такой папки нет значит файлы не пишет проверить сервер
                    email("ERROR. Такой папки не существует, необходио проверить сервер: " + path + '/' + dirpath)
                    log("ERROR. Такой папки не существует, необходио проверить сервер: " + path + '/' + dirpath)
            #таймер на 10 минут
            time.sleep(600)
    except Exception as err:
        log("Исключение функция contfclrdisk не сработала, запускаем заново функцию через 60 секунд.")
        log(str(err))
        email("Исключение функция contfclrdisk не сработала, запускаем заново функцию через 60 секунд.")
        email(str(err))
        time.sleep(60)
        log("перезапущена функция contfclrdisk")
        contfclrdisk()



def videosrv():
    try:
        while True:
            now = datetime.now()
            dirpath = datetime.strftime(datetime.now(), "%d.%m.%Y")
            datatextfile = datetime.strftime(datetime.now(), "%d.%m.%Y-%H:%M:%S")
            gettime1 = 60 - now.minute
            gettime1 = gettime1 * 60
            textnamedisk = subprocess.check_output('df -h', shell=True)
            index = textnamedisk.find("media")
            index = index + 9  # повышаем индекс до названия диска
            textnamedisk = textnamedisk[index:]
            buf = textnamedisk.split('\n')
            textnamedisk = buf[0]
            filename = '/media/pi/' + textnamedisk + '/' + dirpath + '/' + datatextfile + '.avi'
            if os.path.exists('/media/pi/' + textnamedisk + '/' + dirpath):
                # Если такая папка существует пишем в нее
                os.system('ffmpeg -t ' + str(gettime1) + ' -f video4linux2 -s 1920x1080 -i /dev/video0 ' + filename)
            else:
                # Если такой папки нет то создаем ее и пишем в нее
                os.makedirs('/media/pi/' + textnamedisk + '/' + dirpath)  # Создаю такую папку и пишу в нее
                #Эта команда для web камеры
                os.system('ffmpeg -t ' + str(gettime1) + ' -f video4linux2 -s 1920x1080 -i /dev/video0 ' + filename)
            os.system('killall -s 9 ffmpeg')
            #Тут делаем проверку на существование записанного файла и определяем его размер
            #Если размер будет меньше то оповестить значит не пишет файл
            if os.path.exists(filename):
                statinfo = os.stat(filename)
                statinfo = statinfo.st_size
                statinfo = statinfo / 1e+6
                statinform = str(statinfo)
                if statinfo < 30.0: #если файл меньше 30 мегабайт
                    email('Файл записан и меньше 30 мегабайт: ' + filename + ' ' + statinform + ' Mb')
                    #logwrfile("Файл записан и  меньше 30 мегабайт: " + filename + ' ' + statinform + ' Mb')
                #else:
                    #logwrfile('Файл записан: ' + filename + ' ' + statinform + ' Mb')
            else:
                email('Файл не записался: ' + filename + ' ' + statinform + ' Mb')
                #logwrfile('Файл не записался: ' + filename + ' ' + statinform + ' Mb')
    except Exception as err:
        log("Исключение функция videosrv не сработала, запускаем заново функцию через 60 секунд.")
        log(str(err))
        #Отправляем лог на емеил чтобы видеть ошибки тут мы увидим например если жесткий диск не монтируется, сломался
        email("Исключение функция videosrv не сработала, запускаем заново функцию через 60 секунд.")
        email(str(err))
        #os.system('sudo killall - s 9 ffmpeg')
        os.system('killall - s 9 ffmpeg')
        time.sleep(60)
        #log(str(err))
        log("перезапущена функция videosrv")
        videosrv()


#Киляем ffmpeg, т.к. он занимает веб камеру
os.system('killall -s 9 ffmpeg')
e1 = threading.Event()
e2 = threading.Event()
#e3 = threading.Event()

t1 = threading.Thread(target=videosrv, name="potok1-videosrv")
t2 = threading.Thread(target=contfclrdisk, name="potok2-contfclrdisk")
#t3 = threading.Thread(target=controlwritedisc, name="potok3-controlwritedisc")
#Задержка запуска потоков, потому что винчестер не успевал примонтироваться
print("Задержка 15 сек. для монтирования винчестера")
time.sleep(15)
# start threads
log("Запуск 1-го и 2-го потоков, старт программы")
t1.start()
t2.start()
#t3.start()
# e1.set() # initiate the first event
# join threads to the main thread
t1.join()
t2.join()
#t3.join()
log("Потоки отключены конец программы")
