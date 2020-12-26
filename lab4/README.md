## Lab_4: Робота з Docker
1. Для ознайомляння що таке Docker звернувся до [документації](https://docs.docker.com/);
2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустив перевірку версії, виведення допомоги та тестовий імедж:
    ```bash
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    - перенаправив вивід цих команд у файл `my_work.log` та закомітив його до репозиторію.
3. Docker працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи Docker дещо схожа на віртуальні машини. Перш за все створити імедж з якого буде запускатись контейнер. Для цього існує Dockerfile який описує контент імеджу.
4. Для знайомства з Docker створив імедж із Django сайтом зробленим у попередній роботі.
    - Використав команду щоб завантажити базовий імедж з репозиторію:
    ```
    docker pull python:3.8-slim
    docker images
    docker inspect python:3.8-slim
    ```
    - Створив файл з іменем `Dockerfile` скопіював туди вміст такого ж файлу з цього репозиторію;
    - Ознайомився із коментарями та зрозумів структуру написання Dockerfile;
    - Замінив посилання на власний Git репозиторій із веб-сайтом та закомітив даний Dockerfile*
5. Створив власний репозиторій на Docker Hub. Для цього залогінився у власний аккаунт на Docker Hub після чого створив репозиторій [Репозиторій](https://hub.docker.com/r/vasyl1/vasyl4).
6. Виконав білд (build) Docker імеджа та завантажив його до репозиторію: 
    ```
    docker build -t vasyl1/vasyl4:django .
    docker images
    docker push vasyl1/vasyl4:django
    ```
    [Імедж](https://hub.docker.com/layers/vasyl1/vasyl4/django/images/sha256-ac886b58b12d6fe48b63e87539b9e820371e3b53c84b563ed207018b162e3106?context=explore)
    
7. Для запуску веб-сайту виконав команду:
    ```
    docker run -it --name=django --rm -p 8000:8000 vasyl1/vasyl4:django
    ``` 
    - перейшов по адресу `http://127.0.0.1:8000` та переконався що веб-сайт працює;
8. Cтворив Dockerfile.site. Виконав білд (build) Docker імеджа з моніторингом та завантажив його до репозиторію.
    ```
        sudo docker build -t vasyl1/vasyl4:monitoring --file Dockerfile.site . 
        sudo docker images
        sudo docker push vasyl1/vasyl4:monitoring
    ``` 
   Запустив обидва імеджі.
   ```
        sudo docker run -it --rm -p 8000:8000 vasyl1/vasyl4:django
        sudo docker run --net=host --rm -it --volume /home/Beshlei_lab/Lab_4:/app vasyl1/vasyl4:monitoring
   ``` 

9. Після успішного виконання роботи відредагував _README.md_ у цьому репозиторію та зробив pull request.
