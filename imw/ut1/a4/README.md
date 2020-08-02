# UT1-A4: Sirviendo aplicaciones Php y Python.
## 1. Página Web 1.
### 1.1 Proceso.
Nos dirigimos al directorio `/etc/nginx/sites-available` y creamos un nuevo archivo de configuración para la aplicación de *PHP* con los siguientes parámetros:  
![](img/README-029.png)  
Hay que indicarle que la extención del *index* será *index.php*, crear una *location* para que "lea" los ficheros que acaben en *.php* y en él añadir la ruta al archivo de configuración junto con el *socket* que se encargará de controlar las peticiones de entrada y salida.  

Nos dirigimos a `/etc/nginx/sites-enabled` para activar el archivo de configuración con un enlace simbólico.        
![](img/README-030.png)  

Y recargamos el servicio.  
![](img/README-031.png)  

Por último, subimos el archivo de la activad con el comando *scp archivo host:ruta*   y lo descomprimos en la siguiente carpeta:  
![](img/README-032.png)  

### 1.2 Comprobación.    
Éxito.  php.alu5899.me  
![](img/README-033.png)    

## 2. Página Web 2.
### 2.1 Proceso.
Nos dirigimos al *home* del usuario y buscamos la carpeta oculta de *.virtualenvs* para crear el directorio *now*, que alojará el *socket uwsgi* y los *frameworks* de *python*-*flask*.  
![](img/README-034.png)  

Creamos el entorno virtual con el siguiente comando.
![](img/README-035.png)

Y comprobamos que el entorno virtual funciona.    
![](img/README-036.png)  

Creamos el directorio `/home/alu5899/now/` que contendrá la aplicación escrita en *python*.   
![](img/README-037.png)   

Generamos el fichero *main.py* con el siguiente código.  
![](img/README-038.png)  
Ya tendríamos hecho todo lo que sería la parte de código. Ahora pasaremos a la instalación del *socket* y los *frameworks* necesarios para el funcionamiento de esta *app*.

Activamos el entorno virtual e instalamos *uwsgi* con *pip*.    
![](img/README-039.png)  

Hacemos lo mismo con *flask*.  
![](img/README-040.png)    

Salimos del entorno virtual y creamos el archivo de configuración en *sites-available* con la siguiente configuración (static=css,png...).  
![](img/README-041.png)  

Activamos la página en *sites-enabled*.    
![](img/README-042.png)    

Volvemos a activar el entorno virtual de *now* y lanzamos el comando `uwsgi --socket 0.0.0.0:8080 --protocol=http -w main:app`  para activar en la propia máquina por el puerto 8080 la aplicación de *main.py*.  
![](img/README-043.png)  

Abrimos el navegador y comprobamos rápidamente que ha funcionado.  
![](img/README-044.png)    

### 2.2 Supervisor.
Si queremos que la aplicación sea ofrecida permanentemente tendremos que configurar un supervisor, un servicio que la ofrecerá la web.  
![](img/README-045.png)  

Creamos un *script* en la carpeta *now* que lanzará el servicio.  
![](img/README-049.png)    

Otorgamos permisos de ejecución a el grupo y a otros para que lo puedan ejecutar.   
 ![](img/README-047.png)    

Por último, nos dirimos al directorio `/etc/supervisor/conf.d` y creamos el archivo *now.conf* con la siguiente configuración.  
![](img/0001.png)   

Reiniciamos y comprobamos el estado del nuevo servicio de diversas formas.
![](img/0002.png)   

![](img/0003.png)  

---
### 2.3 Actualización y comprobación.    
Instalamos *pytz* en el entorno virtual de *now*.
![](img/0004.png)    

Y este sería el resultado final si aplicaramos la modificación del código de *main:app* proporcionado en la activad. now.alu5899.me
![](img/0005.png)  
