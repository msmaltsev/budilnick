# budilnick
alarm clock for mac

1) "applescript_budilnick.txt": запускает три окна google chrome:
  1.1) страница с онлайн-радио (ссылка случайно выбирается из файла radio.txt)
  1.2) страница с погодой (ссылка случайно выбирается из файла weather.txt); страница помещается на левую половину экрана (при условии, что разрешение экрана - 1366x768)
  1.3) страница с картой пробок (ссылка случайно выбирается из файла traffic.txt); страница помещается на правую половину экрана (при условии, что разрешение экрана - 1366x768)
  
2) "open_as.py": 
  2.1) собирает ссылки из файлов radio.txt, weather.txt, traffic.txt; при наличии нескольких ссылок в каждом из файлов случайно выбирает одну.
  2.2) считывает текстовые данные на языке applescript из файла applescript_budilnick.txt; подставляет ссылки из п.2.1 в эти данные
  2.3) запускает applecript из п.2.2
  
Запуск осуществляется из командной строки:
$ python3 open_as.py

Выход не предусмотрен; предполагается, что пользователь сам закрывает страницы браузер google chrome.
