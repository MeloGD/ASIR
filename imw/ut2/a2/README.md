# Wordpress.  
![img](./img/027.png)   

## 1. Instalación.
Comenzamos el proceso de instalación entrando en nuestro previamente configurado mysql.  
![img](./img/001.png)    

Creamos una base de datos llamada *wpdatabase*.  
![img](./img/002.png)  

Creamos un usuario llamado *wpuser@localhost* con contraseña *Testing_1234*, con todos los privilegios sobre la base de datos *wpdatabase*.  
![img](./img/003.png)    

Hecho esto, procedemos a descargar en ``/tmp/`` los ficheros de instalación de *Wordpress*.  
![img](./img/004.png)    

Y los descomprimimos.  
![img](./img/005.png)    

Lo copiamos en ``/usr/share/`` y nos damos cuenta de que el usuario y el grupo están establecidos como ``root``, cosa que habrá que cambiar para que *Wordpress* pueda funcionar correctamente.  
![img](./img/006.png)

Cambiamos el usuario y el grupo a ``www-data``.  
![img](./img/008.png)    

Modificamos copiamos y modificamos *wp-config*, introduciendo los valores de nuestra base de datos de MySql.  
![img](./img/010.png)    

![img](./img/009.png)    

Llegados a este punto, creamos el sitio en *Nginx* con la siguiente configuración.  
![img](./img/011.png)    

![img](./img/015.png)   

![img](./img/013.png)   


Reiniciamos el servicio para cargar la nueva configuración.
![img](./img/014.png)     



Si todo ha salido bien, deberíamos poder entrar a la siguiente página.  
![img](./img/016.png)     

Configuramos el sitio con los siguientes datos.  
![img](./img/017.png)    

Y si aparece esta captura, habremos instalado *Wordpress* correctamente.  
![img](./img/018.png)  

## 2. Links permanentes.  
Entramos con el usuario creado.  
![img](./img/019.png)    

En la zona de ``Ajustes > Enlaces predeterminados`` seleccionamos la opción *Día y nombre*.  
![img](./img/020.png)    

Y en el archivo *wordpress* de *Nginx* añadimos la *location* especificada en la captura y reiniciamos el servicio.  
![img](./img/022.png)    

![img](./img/021.png)    

![img](./img/023.png)    

## 3. Tema.  
En esta pestaña cambiaríamos el tema.  
![img](./img/024.png)    

![img](./img/026.png)  

## 4. Añadir una nueva página.  
En esta pestaña cambiaríamos el tema.
![img](./img/025.png)   

http://wordpress.alu5899.me/estadisticas-wordpress/
