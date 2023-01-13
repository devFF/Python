# Управление проектором

Данный раздел содержит программу для управления проектором по PJLINK протоколу.
Программа умеет: включать/выключать проектор, узнавать его статус питания, сохранять настройки, 
автоматически добавляться в автозагрузку при запуске компьютера, а также удаляться из нее. 
Интерфейс реализован с использованием библиотеки pysimplegui. Компиляция произведна при помощи pyinstaller в связке с upx.


![Screenshot 1](https://github.com/devFF/FindJob/blob/main/Projects/Projector_control/scr1.PNG?raw=true)
![Screenshot 2](https://github.com/devFF/FindJob/blob/main/Projects/Projector_control/scr2.PNG?raw=true)

## Файлы проекта

[**1. Epson.py**](https://github.com/devFF/FindJob/blob/main/Projects/Projector_control/Epson.py) - исходник.

[**2. Epson.exe**](https://github.com/devFF/FindJob/blob/main/Projects/Projector_control/Epson.exe) - исполняемый файл для win64.

[**3. Epson.spec**](https://github.com/devFF/FindJob/blob/main/Projects/Projector_control/Epson.spec) - конфигурационный файл для компиляции приложения.

## Особенности проекта 

1. Изначально собранный exe-файл был очень тяжелым для столь простой программы и весил 31 Мб. Понятно, что питон это интерпретируемый язык и при его компиляции 
через pyinstaller в один exe-файл собирается не только сам скрипт, но еще и интерпетатор, и все используемые библиотеки. 
Но есть способ значительно уменьшить размер файла. Для этого в чистой системе (виртуалке) создаем папку проекта и виртуальное окружение "python -m venv venv" 
в этой же директории. Затем активируем venv: "venv\Scripts\activate.bat". Устанавливаем все необходимые библиотеки для проекта, в том числе, pyinstaller и 
pypiwin32. Теперь [скачиваем upx](https://github.com/upx/upx/releases) и размещаем его в папке с проектом. Теперь выполняем компиляцию проекта при помощи следующей 
команды: "*pyinstall --noconsole --onefile --upx-dit=Fullpath\upx --icon=icon.ico Epson.py*"





 

