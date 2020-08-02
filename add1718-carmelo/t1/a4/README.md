# SAMBA
## 1. Servidor.
### 1.1 Instalación.  
Comprobamos que la configuración es la que se ha pedido.  
![img](./img/001.png)

![img](./img/002.png)  

![img](./img/004.png)  

![img](./img/005.png)    

Añadimos los clientes al fichero `/etc/hosts`.  
![img](./img/006.png)      

Ahora, creamos los siguientes grupos.  
![img](./img/007.png)      

![img](./img/008.png)    

Aquí se ha especificado que este usuario no pueda ejecturar una sesión en una terminal.
![img](./img/009.png)    

Creamos los usuarios para la práctica y los añadimos al grupo (-m para directorio, -G para especificar el grupo).
![img](./img/010.png)    

![img](./img/011.png)    

![img](./img/012.png)    

![img](./img/013.png)  

![img](./img/014.png)    

![img](./img/015.png)    

![img](./img/016.png)    

Creamos las siguientes carpetas con esta estructura.  
![img](./img/017.png)     

![img](./img/018.png)    

Cambiamos los permisos.  
![img](./img/019.png)    

Y hacemos una copia del archivo de configuración de samba.    
![img](./img/020.png)    

### 1.2 Configuración.  
Desde la herramienta Yast accederemos a la característica de *Servidor Samba* para su configuración, siguiendo estos pasos.  
![img](./img/021.png)    

![img](./img/022.png)    

![img](./img/023.png)    

![img](./img/024.png)    

![img](./img/025.png)    

Una vez configurada las características iniciales, habrá que añadir en el fichero de configuración de samba las siguientes opciones para poder usar correctamente las carpetas previamente creadas.
![img](./img/026.png)    

![img](./img/027.png)    

![img](./img/028.png)    

Una vez hecho esto, asignamos una contraseña de acceso al recurso samba a los usuarios previamente creados.  
![img](./img/029.png)    

![img](./img/030.png)    

Paramos, iniciamos y comprobamos la configuración.  
![img](./img/032.png)   

Y lanzamos los últimos comandos de comprobación.  
 ![img](./img/033.png)    

![img](./img/034.png)    

## 2. Cliente Windows.  
### 2.1 Comprobación.
Comprobamos que el fichero hosts contiene al servidor y al primer cliente.  
![img](./img/035.png)    

Comprobamos que se muestras los recursos y que se pueda acceder a ellos.  
![img](./img/036.png)    

![img](./img/037.png)    

![img](./img/038.png)    

![img](./img/039.png)    

El problema está en que si ya hemos accedido a una carpeta e intentamos entrar en otra, no nos dejará; se podría decir que solo acepta una sesión. Para solucionarlo, habría que vaciar "la lista" con el siguiente comando y volver a entrar en la nueva carpeta.  
![img](./img/040.png)    

![img](./img/041.png)    

![img](./img/042.png)    

![img](./img/043.png)    

En el servidor, comprobamos lo siguientes comandos.  
![img](./img/044.png)    

![img](./img/045.png)    

![img](./img/046.png)    

## 3. Cliente Suse.   
### 3.1 Comprobación.
Comprobamos que el ficheros `/etc/hosts` contiene tanto al servidor como al segundo cliente y su ip.  
![img](./img/047.png)  

![img](./img/048.png)     

Comprobamos que se muestran las carpetas y que se pueden acceder a ellas.
![img](./img/049.png)    

![img](./img/050.png)    

![img](./img/051.png)    

![img](./img/052.png)     

Cambiamos los permisos a a la carpeta `public` y comprobamos.
![img](./img/053.png)    

![img](./img/054.png)    

Y realizamos las últimas comprobaciones.  
![img](./img/055.png)   

![img](./img/056.png)  

![img](./img/057.png)  

![img](./img/058.png)  

![img](./img/059.png)  

### 3.2 Montaje y automatización.  
De esta manera, montaremos la carpeta en el cliente, siendo visible desde el equipo sin tener que especificar la ip del servidor. El único incoveniente es que si reiniciamos la máquina, esta se desmontará.
![img](./img/060.png)    

![img](./img/061.png)    

Comprobamos.
![img](./img/062.png)    

![img](./img/063.png)    

![img](./img/064.png)  

![img](./img/065.png)    

Para que se monte de manera automática, habrá que añadir la úitlma línea de esta captura al fichero `/etc/fstab`. Hay que tener bastante cuidado con la sintaxis en este fichero, de lo contrario, el arranque se verá comprometido.  
![img](./img/066.png)    

Por último, reiniciamos y comprobamos con `df -HT`.
![img](./img/067.png)    

## 4. Preguntas.
-¿Las claves de los usuarios en GNU/Linux deben ser las mismas que las que usa Samba?  
No, pueden ser diferentes.  

-¿Puedo definir un usuario en Samba llamado soldado3, y que no exista como usuario del sistema?  
No, para crear un usuario en samba tiene que existir previamente en el sistema.

-¿Cómo podemos hacer que los usuarios soldado1 y soldado2 no puedan acceder al sistema pero sí al samba? (Consultar /etc/passwd)  
Añadiendo el *../bin/false* al final de cada usuario dentro de *passwd*.  

-Añadir el recurso [homes] al fichero smb.conf según los apuntes. ¿Qué efecto tiene?  
Se añade la carpeta *homes*. Hay que tener en cuenta que se tiene que enlazar a un directorio válido.
