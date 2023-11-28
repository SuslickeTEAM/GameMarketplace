# GameMarketplace
## Установка проекта

1. **Клонирование репозитория:**
    ```bash
    git clone https://github.com/SuslickeTEAM/GameMarketplace.git
    cd GameMarketplace
    ```

2. **Создание виртуальной среды (рекомендуется):**
    ```bash
    python -m venv venv
    ```

3. **Активация виртуальной среды:**
    - Для Windows:
        ```bash
        venv\Scripts\activate
        ```
    - Для Unix или MacOS:
        ```bash
        source venv/bin/activate
        ```

4. **Установка зависимостей:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Настройка базы данных:**
    - Укажите настройки базы данных в файле `settings.py`.
    - Примените миграции:
        ```bash
        python manage.py migrate
        ```

6. **Запуск сервера:**
    ```bash
    python manage.py runserver
    ```

7. **Откройте веб-браузер и перейдите по адресу:**
    ```
    http://localhost:8000/
    ```
