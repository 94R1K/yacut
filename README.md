# ___YaCut___

*Проект YaCut - это сервис для укорачивания ссылок. Его задача заключается в том,
чтобы связывать длинные пользовательские ссылки с короткими, которые предлагаются
самим пользователем или предоставляются сервисом.*

## __Ключевые возможности сервиса:__
- Генерация коротких ссылок и связывание их с длинными ссылками
- Перенаправление на исходный адрес при обращении к коротким ссылкам

## __Технологии__
- Python 3.8
- Flask 2.0
- Jinja2 3.0
- SQLAlchemy 1.4

## __Установка__
1. Клонируйте репозиторий и перейдите в него в командной строке:
   ```
   git clone <https://github.com/your_username/YaCut.git>
   cd YaCut
   ```

2. Создайте и активируйте виртуальное окружение:
   ```
   python3 -m venv venv
   ```

   Для Linux/MacOS:
   ```
   source venv/bin/activate
   ```
   Для Windows:
   ```
   venv\Scripts\activate
   ```

3. Установите зависимости из файла requirements.txt:
   ```
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Создайте файл настроек окружения:
   ```
   touch .env
   ```

5. Заполните его следующим образом:
   ```
   FLASK_APP=yacut
   FLASK_ENV=production
   DATABASE_URI=sqlite:///db.sqlite3
   SECRET_KEY=your_secret_key
   ```

6. Запустите приложение:
   ```
   flask run
   ```

7. Откройте браузер и перейдите по адресу [http://localhost:5000](http://localhost:5000).

# ___Об авторе___
Лошкарев Ярослав Эдуардович \
Python-разработчик (Backend) \
Россия, г. Москва \
E-mail: real-man228@yandex.ru

[![VK](https://img.shields.io/badge/Вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/yalluv)
[![TG](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/y4r1kl)