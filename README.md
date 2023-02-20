
# Blog with Django


This project was developed to comply with certain guidelines and intended to show some properties of Rest development with Django. Its visual structure is not polished at all but in general it fulfills its objective, which goes more through the Backend side.





![Logo](https://cdn.iconscout.com/icon/free/png-512/django-12-1175186.png?f=avif&w=256)


## INSTALACION

IT REQUIRES TO HAVE DOCKER DOWNLOADED ON YOUR SYSTEM. 


Clone the repository, or download as a zip

```bash
  git clone https://github.com/arielgv/Blog_with_dj.git
```

go to the folder

```bash
  cd [downloaded_project]
```

Install the containers. Requires having Docker running:

```bash
  docker-compose up -d --build
``` 
This command will start installing all dependencies, when finished, all data must be migrated to PostgreSql

Running commands inside Docker is a bit different than a traditional Django project, for example, now to perform the data migration we need to run the following command:

```bash
  docker-compose exec web python manage.py migrate 
```
At the end of the data migration, everything is ready to run the server
```bash
    docker-compose run web python manage.py runserver
```

Now, the Django server will start working using the PostgreSql engine, which will already be running as a container image.



(Alternatively) If you want to create a superuser for administration, just following the same logic of the commands, it should be like this:
"docker-compose exec web python manage.py createsuperuser" (without quotes)


- It is important that when you finish using the page, in the command console press Ctrl + Z to exit back to bash and execute "docker-compose down". to stop the containers.


## Enter the blog

To access the program, you must open a web browser window and enter the address http://localhost:8000

## Funcionamiento del Blog :

When entering the blog there will be a blank home page, go to the upper sector of the page and by clicking on Register you will be redirected to a user registration form.

## Screenshots

![App Screenshot](https://i.imgur.com/Kuujhju.png)

After registering and logging into the system, you will be now ready to create your own posts!

Multiple users can create accounts and login! Don't worry about the complexity of the system, everything is developed by Django behind the scenes! together with the agility and the advantages of a great engine such as Postgresql which is also running in Docker containers with all the automated configuration!

![App Screenshot](https://i.imgur.com/hsVZrSM.png)

The users who created their posts have access to edit or delete them as long as they are the validated authors of the Post! When trying to delete a post a confirmation window will appear to validate it.
The database automates a volume so that each time the container is closed, the information entered into the database is not lost. and then when you run the container again your information is still there!


![App Screenshot](https://i.imgur.com/wYQYqII.png)

A simple but powerful post search and filter tool is also at your fingertips, aided by Django modules. Just enter a string of what you're looking for, and the search engine will return results if it finds it!


## API Reference

#### Get all posts

```http
  GET /api/postg/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `queryset` | returns all posts |

#### POST post

```http
  POST /api/postp/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. post's title |
| `content` | `string` | **R** post's content|
| `date_posted ` | `date` | **R** post's TimeStamp   |
| `id_author` | `Int_FK` | **R** author's index number|


```http
  GET /api/profiles/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required** returns user info (only auth) 

```http
  GET api/posts/<int:user_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required** returns the user's posts


## Running Tests

To run the unit tests of each endpoint, execute the following command:

```bash
  python3 manage.py tests
```


## TECHNICAL REALIZATION AND EXPLANATION OF THE CODE.

The program was made using a Python 3.10 image in which multiple dependencies were installed, among which are Django 4.1, Django Rest Framework and psycopg2 (postgresql) among others.
 
First, the apps (users & posts) that would be part of the project were developed, their corresponding declaration is made in settings along with the database configuration. Then the models necessary for the page to work, which were the user and post models.
After carrying out the corresponding serialization of each one, the corresponding properties of each item began to be implemented. The user class inherited from User from Django Contrib Auth , which already has an excellent configuration for validations and a set of properties that make it quite secure and easy to submit to different tests. The same would happen with post to receive a request before it would have to submit an authentication to the requester to be able to validate.

Then we proceeded to carry out the Views, where the requests, responses, requests, etc. would be validated. Each one carefully documented in the code and with its proper HTTP response in Status in each corresponding scenario. Then related to its corresponding Url in the urls.py module

Finally, before moving on to the visual development part in templates, the corresponding unit tests of each app were carried out, on the one hand, the Post class, carefully reviewing different scenarios and executing various tests provided by Django classes, as well as in the class Users, which created multiple users automatically for various tests.

At the end, the templates were made where a main block of posts predominated, where a classic format was chosen where the posts were displayed in descending order according to their publication date. Each User has access to their own posts with individual rights to modify or delete.

  
  



## Autor

- [@arielgv](https://github.com/arielgv)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/arielgv)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arielgv/)
