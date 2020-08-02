# Instalación MySQL-Server y PHP-MyAdmin / Ubuntu.
## 1. Instalaciones.
### 1.1 MySQL-Server.
Instalamos desde *apt-get install msyql-server*.
![img](./img/001.png)  

Configuramos una contraseña.  
![img](./img/002.png)  

Reiniciamos el servicio y comprobamos.  
![img](./img/005.png)  

![img](./img/003.png)

Ejecutamos *mysql_secure_installation*. Esto nos permitirá configurar *mysql* con una serie de preguntas referentes a la seguridad del servidor.  
![img](./img/006.png)

### 1.2 MySQL-Workbench.
Instalamos desde *apt-get install msyql-workbench*.
![img](./img/007.png)  

Ejecutamos el programa.  
![img](./img/008.png)   

Creamos un usuario *carmelo-remoto*.
![img](./img/009.png)  

En *settings* clicamos la llave para asignar una ruta de acceso al archivo de configuración.
![img](./img/010.png)

Habilitamos todas las conexiones. Esto es opcional y es recomendable especificar un grupo limitado de IPs.
![img](./img/015.png)    

### 1.3 MySQL-Client.
Instalamos desde *apt-get install msyql-client*.
![img](./img/011.png)  

Y comprobamos la conexión.
![img](./img/016.png)  

### 1.4 PHP-MyAdmin.
Instalamos desde *apt-get install msyql-client*.   
![img](./img/017.png)

Seguimos lo siguintes pasos:    
![img](./img/019.png)

Especificamos la contraseña de *carmelo-remoto*.   
![img](./img/020.png)

![img](./img/022.png)  

MARCAMOS la opción con el espaciador.    
![img](./img/023.png)  

Y comprobamos la conexión.   
![img](./img/024.png)   

![img](./img/025.png)

## 2. Preguntas.
Directorio de instalación base.  
>![img](./img/013.png)  

Directorio del servicio o proceso demonio.  
>![img](./img/014.png)  

Directorio de datos.  
>![img](./img/12.png)  

Fichero de configuración del servidor y su ubicación.  
>![img](./img/026.png)  

¿Quién es el usuario propietario de la instalación?.
>mysql

Aplicar el lenguaje de los mensajes de error  a español, modificando la configuración (indicar el directorio donde se aloja el fichero en español)
>![img](./img/018.png)  
