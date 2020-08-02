# U1_A4.- Instalación de SQL Server 2014 Express.  
## 1. WS2012.  
### 1.1 Instalación.  
Descargamos la versión *Express* de *SQL-Server* y descomprimimos los archivos de instalación en la ruta deseada.  
![img](./img/001.png)  

Comenzamos la instalación.   
**IMPORTANTE: DEJAR LOS PASOS POR DEFECTO Y MODIFICAR SOLO LO MOSTRADO.***     
![img](./img/002.png)  

Nueva instalación.  
![img](./img/003.png)   

![img](./img/004.png)  

![img](./img/005.png)  

![img](./img/006.png)  

Aquí se recomienda dejarlo en predeterminado. A la hora de conectarlo remótamente, si escogemos la opción predeterminada solo tendremos que espeficar la IP y de la manera que mostramos en la imagen tendriamos que especifar la IP más en nombre de la instancia, quedando algo así `172.18.18.10\SQLEXPRESS`.    
![img](./img/007.png)  

![img](./img/008.png)  

Aquí especificamos el modo mixto y establecemos una contraseña para la conexión.
![img](./img/009.png)  

![img](./img/011.png)  

![img](./img/012.png)  

![img](./img/013.png)  

Una vez finalizada la instalación, abrimos el centro de configuración de *SQL-Server*.
![img](./img/014.png)  

Ahora, descargamos el *SQL-Server Management Studio* de la página oficial.  
![img](./img/015.png)    

Y procedemos a su instalación.  
![img](./img/016.png)  

Este paso puede llegar a durar bastante.  
![img](./img/017.png)   

Una vez instalado, comprobamos su funcionamiento.  
![img](./img/026.png)  

![img](./img/018.png)

### 1.2 Configuración.  
Revisamos que la configuración esté configurada de la siguiente manera.
![img](./img/022.png)   

Permitimos conexiones remotas.
![img](./img/023.png)  

Activamos *login* de *Windows* y *SQL*.
![img](./img/024.png)    

Comprobamos que el usuario "sa" esté habilitado.  
![img](./img/025.png)  

Ahora, nos dirigimos a la herramienta de configuración de *SQL-Server* y habilitamos el puerto 1433 para ofrecer este servicio. También habrá que abrir el puerto en el firewall.   
![img](./img/027.png)   

![img](./img/028.png)

![img](./img/029.png)

Por último, revisar que estas características estén como se muentran en estas capturas para evitar problemas de conexión remota en un futuro.   
![img](./img/030.png)

![img](./img/031.png)  
## 2. Cliente.
### 2.1 Instalación  de SQL-Server Management Studio.  
Seguimos el mismo procedimiento.  
![img](./img/019.png)  

![img](./img/020.png)

Ya para finalizar, comprobamos la conexión, uno de los pasos más complicados de lograr por la cantidad de errores a los que puede estar sujeto.  
![img](./img/023b.png)  

![img](./img/024b.png)
