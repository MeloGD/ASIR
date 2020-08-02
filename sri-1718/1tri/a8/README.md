# FTP SRD
## Windows.
![img](img/000.jpg)   
### FTP 1.
Comenzamos la práctica agregando el rol FTP de la siguiente manera:  
![img](./img/001.png)   

Seguimos la configuración que se muestra en las capturas:  
![img](./img/002.png)      

![img](./img/003.png)    

![img](./img/004.png)    

En el administrador de DNS, agregamos un host llamado *ftp*, para que dicho servicio pueda ser abierto desde *ftp.pruebasrd.edu*.  
![img](./img/007.png)  

Una vez asignado el DNS, nos dirigimos a IIS.  
![img](./img/005.png)  

Agregamos un sitio *FTP*.
![img](./img/006.png)  

Introducimos el nombre del sitio FTP creado en el DNS y asiganamos toda la unidad de *C:\*.  
![img](./img/008.png)    

Dejamos la configuración como se muestra en las siguientes capturas.  
![img](./img/009.png)    

![img](./img/010.png)  

Comprobamos que la configuración se ha realizado de la manera deseada.  
![img](./img/011.png)  

![img](./img/012.png)  

Y que sea accesible desde el propio servidor.  
![img](./img/013.png)  

Y cliente, ya sea desde el navegador o el cliente *WinCp*.  
![img](./img/014.png)  

![img](./img/015.png)    

![img](./img/016.png)  


### FTP 2.
Creamos el segundo host para el nuevo *ftp*, quedando como *ftp2.pruebasrd.edu*.  
![img](./img/017.png)    

En ISS, agregamos el sitio *FTP* con la siguiente configuración.  
![img](./img/018.png)  

![img](./img/019.png)  

![img](./img/020.png)  

Y comprobamos desde el servidor.  
![img](./img/021.png)  

![img](./img/022.png)  

Y desde el cliente a través de *WinCp*.  
![img](./img/023.png)  

![img](./img/024.png)  

### FTP 3.
Finalmente, agregamos el nuevo sitio *ftp* a través de *ftp3.pruebasrd.edu*, con la siguiente configuración.  
![img](./img/025.png)  

![img](./img/026.png)  

![img](./img/027.png)  

![img](./img/028.png)  

Y comprobamos si funciona la conexión anónima.  
![img](./img/029.png)  

![img](./img/030.png)    

## Ubuntu - Linux.  
### Siguiendo los pasos pedidos en la práctica...
Instalamos ssh.  
![img](./img/031.png)    

Creamos los usuarios *B2* como administrador y *Jefri* como usuario estándar.
![img](./img/033.png)  

![img](./img/034.png)  

Y hacemos una conexión ssh desde el cliente al servidor con el usuario *B2*.  
![img](./img/032.png)   

Hacemos otra conaxión ssh, pero esta vez con permisos de ejecución para lanzar el programa *geany* en el cliente.  
![img](./img/035.png)  

![img](./img/036.png)  

Llegados a este punto, realizamos una conexión *sftp* de la misma manera que hariamos una con *ssh*.  
![img](./img/037.png)  

En otra terminal, comprobamos el contenido del *home* de *b2*.  
![img](./img/038.png)    

Y desde el cliente, hacemos un *get prueba.txt* para obtener dicho archivo.  
![img](./img/039.png)  

Y comprobamos en el *home* del cliente.  
![img](./img/040.png)  

En esta captura se muestra como se subiría un archivo con *scp*.  
![img](./img/041.png)    

Instalamos *ProFTPd*, un servidor *FTP* altamente personalizable, en modo independiente.  
![img](./img/043.png)  

![img](./img/042.png)  

Este sería el archivo principal de configuración. Todo el significado de su sintaxis se puede encontrar en este link:  
http://www.proftpd.org/docs/howto/ConfigFile.html  
![img](./img/044.png)    

![img](./img/045.png)    

Por último, comprobamos una conexión ftp. En esta captura se cometió el error de especificar el usuario, dando así un error de conexión. En ftp basta con espeficiar la ip al principio, y luego preguntará por usuario y clave.  
![img](./img/046.png)  
