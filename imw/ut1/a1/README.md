# 1. ACTIVIDAD SERIES / VIRTUAL HOST

## 1.1 PROCESO
Creamos los directorios y archivos necesarios que se van a cagar en la web. Debo añadir
que más tarde decidí darle estilo con *CSS* y cree una nueva carpeta llamada CSS a nivel de *index.html*.

![image](./img/series/001.png)   

<br>
Nos dirigimos a *sites-available* para crear el archivo de configuración del servidor web *series*. Quedaría de la siguiente manera.

![image](./img/series/002.png)  
<br>
Ahora nos dirigiremos a *sites-enabled* donde tendremos que crear un enlace simbólico al archivo de configuración en cuestión. Sin esto no se podrá acceder a los archivos de la web.

![image](./img/series/003.png)  
<br>
Reiniciamos el servicio para cargar los nuevos cambios.
![image](./img/series/004.png)  
## 2. WEB
Y este sería el resultado final de la página web.
![image](./img/series/005.png)

> Link: http://alu5899.me/series/
