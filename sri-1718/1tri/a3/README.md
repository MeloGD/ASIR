# A3 - DNS Windows Server 2012.
## 1. Configuración.  
### 1.1 Servidor.  
Nos dirigimos  a la herramienta de gestión preinstalada de DNS.  
![img](./img/001.png)    

Desplegamos el dominio y creamos una nueva zona directa.  
![img](./img/002.png)  

Seguimos todos los pasos predefinidos para esta práctica.  
![img](./img/003.png)  

![img](./img/004.png)  

![img](./img/005.png)  

Aquí es importante mencionar que el nombre no contenga  caracteres extraños, como guiones, "@""...(más tarde se cambiaron por puntos).  
![img](./img/006.png)  

![img](./img/007.png)  

![img](./img/008.png)  

Ahora, crearemos una zona invertida, siguiendo la configuración mostrada.  
![img](./img/009.png)  

![img](./img/010.png)  

![img](./img/011.png)  

![img](./img/012.png)   

El siguiente paso de la actividad sería configurar los reenviadores. Para ello tendremos que abrir las propiedas del dominio.  
![img](./img/013.png)  

Y abrir la pestaña de  reenviadores donde agregaremos los servidores DNS.  
![img](./img/014.png)  

En caso de ser verificados, se mostrarán de la siguiente manera:    
![img](./img/015.png)    

![img](./img/016.png)   

De esta manera, habremos configurado un servidor DNS *cache*, ya que este es capaz de redirigir a otros servidores.  Para hacer un *master*, habría que alojar las traducción de nombres e *Ips* en la propia máquina y especificar en la configuración estática del adaptador de red la misma máquina como servidor *DNS*.  ![img](./img/017.png)  

Una breve comprobación en el servidor de si hay internet.  
![img](./img/018.png)    

Como se pedía en la actividad, tenemos que crear un alias. Para ello previamente habrá que crear  un host nuevo o un campo "A".  
![img](./img/023.png)  

Una vez creado el host le podremos asignar un alias.  
![img](./img/025.png)  

Aquí se asignaría un servidor de correo o campo "mx".  
![img](./img/026.png)  

Lo siguiente que se pedía era crear una impresora con un *A* y un *CNAME*.
![img](./img/027.png)    

![img](./img/028.png)

A continuación, creamos un nuevo dominio llamado "Servicios", que contendrá un ftp, una segunda impresora y un equipo administrador.  
![img](./img/029.png)  

![img](./img/030.png)    

![img](./img/031.png)    

![img](./img/032.png)   

## 2. Comprobaciones.
Nos dirigimos a la configuración del adaptador del cliente y redirigimos el servidor *DNS* a nuestro servidor.  
![img](./img/033.png)    

Ya para finalizar, realizamos las últimas comprobaciones con el conmando *nslookup dominio*.  

![img](./img/034.png)    

![img](./img/035.png)   

Para comprobar que la conexión es real, asignamos la *Ip* de *printer* al cliente y volvemos a comprobar.
![img](./img/036.png)    

![img](./img/037.png)    

![img](./img/038.png)    

![img](./img/039.png)    

![img](./img/040.png)  
