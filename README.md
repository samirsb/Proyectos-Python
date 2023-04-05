#Proyecto Final
Página web desarrollada en Python, y sobre el framework de Django. Tematica fotografía. 

##Detalle del funcionamiento de la página web
La página web funciona como portafolio para fotógrafos y a la vez como banco de fotos. 

###Si el usuario no está registrado se tendrán las siguientes vistas / funcionalidades: 

* Página “Inicio” donde se observará una muestra del trabajo del fotógrafo y un pequeño detalle de los servicios ofrecidos para eventos. 
* Página “Sobre mí” donde se podrá leer sobre la historia personal del fotógrafo
* Página “Contacto” donde hay un formulario de 6 inputs para que el usuario pueda ingresar sus datos de contacto y un mensaje en caso de requerir presupuesto o tener una duda.

###Si el usuario se registra en la web se le adicionará a las funcionalidades / vistas mencionadas anteriormente: 
* Página “Stock” donde el usuario podrá filtrar por temática y descargar las fotos que el fotógrafo haya dejado disponibles. El usuario registrado no podrá borrar, modificar ni agregar fotos, solo podrá hacerlo el usuario del fotógrafo.
* Podrá completar, en caso de desearlo,  un perfil de usuario con información personal de sí mismo y también agregar un avatar. 

##Requisitos
Tener previamente instalado Python3 y Django

##Pasos para la ejecución 
1. Clona el repositorio: Puedes clonar el repositorio utilizando el comando git clone en tu terminal o descargando el archivo ZIP desde el enlace del repositorio (https://github.com/samirsb/Proyectos-Python/tree/main/proyectoFinal).
2. Ingresa a la carpeta `ProyectoFinal`
3. Ejecuta el comando `python manage.py runserver` en la terminal
4. Ingresa al link que se observa luego de “Starting development server at”
5. Navega por la web! 
