testhellobot.py
Это приветственный бот для маркетплейса игровых товаров.
Бот нужен только для того, чтобы перевести на сайт пользователя бота. 
После запуска бота кнопкой /start бот ждет нажатия трёх возможных кнопок:
1) Посмотреть предметы CS:GO
2) Найти предмет
3) Поиск ошибочных ордеров
Любое из действий сейчас вызывает только инлайновую кнопку "перейти на сайт", маскируясь под то, что "Всё раскуплено" "что-то пошло не так" и прочее.
На любой присланный текст бот отвечает "Что-то пошло не так, уже сообщил админу. Так что всё что я могу вам сейчас дать это ссылку на наш сайт☺️" с последующей ссылкой на сайт.

Что ещё?
Потенциал у данного проекта большой, можно сделать нормальную машину состояний и активировать поля с поиском ошибочных ордеров по предметам, используя BeautifulSoup и Pandas для анализа.
Через кнопку "найти предмет" можно искать на площадке предмет по названию и сравнивать его стоимость на buff163 и steam. 
В кнопку "Посмотреть предметы" можно зашить популярные предметы, выставленные на продажу в разделе https://buff.163.com/market/csgo#tab=top-bookmarked&page_num=1
