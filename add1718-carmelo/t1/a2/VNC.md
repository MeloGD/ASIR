# VNC-Conexión remota.
## 1. Suse
### 1.1 Configuración y comprobación.
Antes de hacer una conexión remota, debemos ejecutar el siguiente comando en el servidor a conectar, donde habililitaremos el servicio y podremos configurar las contraseñas de acceso.  
Esto también iniciará el servicio vnc. Cada vez que arranquemos el servidor habrá que ejecutar este servicio, de no hacerse la conexión será rechazada.
>vncserver  


![img](./img/003.png)  

Habilitamos también una exepción en el *firewall* para que permita las conexiones VNC. Esto se ha hecho desde *Yast*.  
![img](./img/002.png)  

Lanzamos el programa *vncviewer* desde la consola, el cual nos habrirá una pestaña en la que podremos poner la IP de la máquina a conectar y especificar el puerto, en este caso, el 5901.
![img](./img/001.png)  

 La conexión ha sido un éxito.  
![img](./img/005.png)  

Ahora lo probamos desde la máquina 2 a la máquina 1, realizando los paso anteriores y comprobamos si hay conexión.  
![img](./img/006.png)  

![img](./img/007.png)  

## 2. Windows.
### 2.1 Configuración y comprobación.
Asignamos IPS:

Máquina 1:  
![img](./img/008.png)  

Máquina 2:  
![img](./img/009.png)  

Instalamos *TightVNC*.  
![img](./img/010.png)  

![img](./img/011.png)  

![img](./img/012.png)  

![img](./img/013.png)  

Una vez acabada la instalación, probramos la conexión. Destacar que no ha sido necesario añadir una exepción en el firewall manualmente dado que el instalador te da la opción de añadir esta exepción automáticamente.  
![img](./img/014.png)  

![img](./img/015.png)   

Y ahora, de la máquina 2 a la máquina 1, siguiendo los pasos previos.
![img](./img/016.png)  

![img](./img/017.png)   

## 3. Suse-Windows y viceversa.
No hay ninguna diferencia en especial. Solo tendremos que especificar la IP de la máquina a conectar y el puerto.
![img](./img/018.png)  

![img](./img/019.png)   

![img](./img/020.png)  
