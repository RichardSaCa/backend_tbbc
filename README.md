**BACKEND PRUEBA TÉCNICA:**

1. El backend fue desarrollado con fastApi, utiliza una base de datos relacional mysql.

1. Se desarrolló con una arquitectura en capas, el archivo main.py se usa como controlador donde se reciben y envían peticiones hacia el backend, este controlador depende del servicio el cual se encarga de toda la lógica del negocio (operaciones matemáticas, algoritmos complejos, etc...), asi mismo el servicio depende de repository el cual se encarga de hacer peticiones a la base de datos. Este arquitectura permite estructurar muy bien el código para facilitar mantenimiento y brindar eficiencia en el funcionamiento.

1. Para correr en local se debe tener instalado python en su version 3.12 o mayor

1. Una vez el proyecto este descargado iniciar el entorno virtual de python con los siguientes comandos:
	- python -m venv venv
	- ./venv/Scripts/activate

1. Posteriormente instalar todas las dependencias del proyecto con el comando:
	- pip install -r ./requirements.txt

1. Para correr el proyecto usar el comando
	- uvicorn main:app

1. Se debe crear un archivo .env para la base base de datos con la siguiente informacion:

	MYSQL_HOST=host de base de datos
	MYSQL_USER=usuario
	MYSQL_PASSWORD=contraseña
	MYSQL_DATABASE=nombre de base de datos

1. La base de datos contiene una tabla:

	https://drive.google.com/file/d/1IORo1-Q1mfIjqVgYTvKtOPmwiFxynt7z/view?usp=sharing

1. El api quedará desplegada en la url: http://localhost:8000

1. fastapi facilita documentación de los endpoints a traves de la url: 
http://localhost:8000/docs

1. Se realizó el desligue en producción usando Docker. Se crea la imagen con el Dockerfile, esta imagen se sube a github y en EC2 de aws se descarga para crear el contenedor el cual se encuentra desplegado en la siguiente url:

	http://3.148.114.153:8000

1. Para la documentación con fastapi revisar la url, donde se encuentran los endpoints:

	http://3.148.114.153:8000/docs

