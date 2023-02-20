
# Blog with Django


Este proyecto fue desarrollado para cumplir con determinadas consignas y pensado para mostrar algunas propiedades del desarrollo Rest con Django. Su estructura visual no está pulida del todo pero en general cumplimenta con su objetivo el cual pasa mas por el lado del Backend.





![Logo](https://cdn.iconscout.com/icon/free/png-512/django-12-1175186.png?f=avif&w=256)


## INSTALACION

REQUIERE TENER DOCKER DESCARGADO EN SU SISTEMA.


Clonar el repositorio, o bien descargar como un zip 

```bash
  git clone https://github.com/arielgv/Blog_with_dj.git
```

dirigirse a la carpeta

```bash
  cd [proyecto_decargado]
```

Instalar los contenedores. Requiere tener Docker corriendo:

```bash
  docker-compose run web python3 manage.py makemigrations
``` 
Este comando hará que comience a instalar todas las dependencias, al finalizar, se debe de migrar todos los datos a PostgreSql, utilizando el siguiente comando:

```bash
  docker-compose run web python3 manage.py migrate 
```
Al finalizar la migración de datos, ya está todo listo para correr el servidor
```bash
    docker-compose run web python3 manage.py runserver
```
Con esto comenzará a funcionar el servidor de Django utilizando de motor a PostgreSql que ya se encontrará corriendo como una imagen del contenedor.


## Ingresar al blog

Para acceder al programa se debe abrir una ventana del explorador web e ingresar a la direccion http://localhost:8000

## Funcionamiento del Blog :

Al ingresar al blog estará una pagina de inicio en blanco, dirigase al sector superior de la pagina y al hacer click en Register se dirigirá hacia un formulario de registro de usuario 
## Screenshots

![App Screenshot](https://i.imgur.com/Kuujhju.png)

Luego de registrarse y logearse en el sistema, ya estará habilitado para crear sus propios posts !

Multiples usuario pueden crear cuentas y logearse !  No se preocupe por la complejidad del sistema, todo lo desarrolla Django detrás ! junto con la agilidad y las ventajas de un gran motor como lo es Postgresql el cual está corriendo tambien gracias a los contenedores de Docker que automatizaron toda la configuración !

![App Screenshot](https://i.imgur.com/CZkfUzt.png)

Los usuarios que crearon sus posts tienen acceso para editarlos o eliminarlos siempre y cuando sean los autores validados del Post !


![App Screenshot](https://i.imgur.com/wYQYqII.png)

Tambien está a su alcance una simple pero poderosa herramienta de búsqueda y filtrado de los posts, ayudada por módulos de Django, Con solo ingresar una cadena de lo que está buscando, el buscador arrojará resultados si es que lo encuentra !


## API Reference

#### Get all posts

```http
  GET /api/postg/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `queryset` | recibe todos los posts |

#### POST post

```http
  POST /api/postp/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. titulo |
| `content` | `string` | **R** contenido del post |
| `date_posted ` | `date` | **R** TimeStamp del posteo |
| `id_author` | `Int_FK` | **R** numero de index del autor |


```http
  GET /api/profiles/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required** devuelve informacion del usuario 

```http
  GET api/posts/<int:user_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required** devuelve los post del usuario referido


## Running Tests

Para correr los test unitarios de cada Endpoint ejecutar el siguiente comando:

```bash
  python3 manage.py tests
```


## REALIZACION Y EXPLICACION TECNICA DEL CODIGO.

El programa fue realizado empleando imagen de Python 3.10 en la cual se instalaron multiples dependencias entre las que que se encuentran Django 4.1, Django Rest Framework y psycopg2 (postgresql) entre otras. 
 
 Primero se desarrollaron las apps (users & posts) que formarían parte del proyecto, se hace su correspondiente declaración en settings junto con la configuracion de base de datos. Luego los modelos necesarios para que funcione la página , que fueron los modelos de usuario y de posts. 
  Luego de realizar la correspondiente serialización de cada uno, se comenzaron a implementar las propiedades correspondientes de cada item. La clase usuario recibió herencia de User de Django Contrib Auth , el cual ya posee una excelente configuración para validaciones y un conjunto de propiedades que lo hacen bastante seguro y facil de someter a distintos Tests. Lo mismo ocurriría con post para recibir una petición antes tendría que someter al peticionista una autenticación para poder validar. 

  Luego se procedió a realizar las Views, donde se validaría las peticiones, respuestas, request, etcetera. Cada uno cuidadosamente documentado en el codigo y con su debida respuesta HTTP en Status en cada escenario que corresponda. Luego relacionado con su correspondiente Url en el modulo de urls.py

  Por ultimo antes de pasar a la parte de desarrollo visual en templates, se realizaron los correspondientes test unitarios de cada app, por un lado la clase Post revisando cuidadosamente distintos escenarios y ejecutando diversos test facilitados por clases de Django, como así tambien en la clase Users, el cual creaba multiples usuario automaticamente para diversas pruebas. 

  Al finalizar se confeccionaron los templates en donde predominaba un bloque principal de post en donde se optó por un formato clasico donde se mostraban los post en orden descendente segun su fecha de publicación .  Cada Usuario tiene acceso a sus propios posts con derechos individuales de modificacion o eliminacion.

  
  



## Autor

- [@arielgv](https://github.com/arielgv)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/arielgv)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arielgv/)
