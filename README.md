Древовидное меню

**Запуск проекта:**

1. Клонируем проект.
2. В терминале пишем docker-compose up -d
3. Готово! Сервер работает по адресу 127.0.0.1:8000

Админ панель находится по эндпоинту /admin/

При запуске контейнера создается супер юзер с данными: логин - admin, пароль - admin

**Эндпоинты:**
1) '/menu/{menu_name}/item/{item_pk}' - получить меню с названием menu_name и с выбранным элементом с id item_pk(элемент должен быть корневым)

2) '/menu?menu_name=example_menu&menu_name=tmp_menu' - получить меню с названиями, перечисленными в GET параметрах, названия которых menu_name(названий меню в GET параметрах может быть неограниченное кол-во)

**Объяснения по принятым мною решений:**

1) В задании написано, что для решения задания нужно использовать только одну библиотеку - Django, это правило соблюдается. Остальные библиотеки в решении задания никак не помогают, пройдусь по каждой библиотеке:
    - psycopg2-binary - для работы с postgresql
    - python-decouple - для работы с .env
    - django-debug-toolbar - для дебага запросов к бд(и для проверяющих и для меня), т.к. нужно делать только один запрос для каждого меню
2) 5 условие задания. Я сделал так, что в качестве выбранного пункта можно было задать только корневой пункт, потому что в случае задания дочернего пункта не очень понятно, что брать в качестве пунктов "над" и "под" (условие 2), пункты из этого же уровня или со всех? Из-за этого было принято такое решение
3) Пункты меню выводятся в порядке возрастания относительно их id