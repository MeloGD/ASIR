# Docker.
![img](./img/start.png)

## Comprobación previa.
Comprobamos el kernel con `uname -a` (debe ser 3.10 o superior):    
![](img/26b8c01d.png)  

## Instalación.
Seguiremos los siguientes pasos:  

`zypper in docker              --> Instala docker.`    
![](img/91d0caa7.png)

`systemctl start docker        --> Inicia el servicio / "docker daemon" hace el mismo efecto.`  
![](img/dbb28c67.png)  

`docker version                --> Debe mostrar información del cliente y del servidor.`    
![](img/83148de1.png)   

`usermod -a -G docker USERNAME --> Añade permisos a nuestro usuario.` (Se ha realizado un `id carmelo` para comprobar que esta dentro del grupo *docker*).  
![](img/77d14aa4.png)      

```
* Salir de la sesión y volver a entrar con nuestro usuario.
* Ejecutar con nuestro usuario para comprobar que todo funciona:
```    
`docker images         --> Muestra las imágenes descargadas hasta ahora.`  
![](img/f34e0bc6.png)    

`docker ps -a          --> Muestra todos los contenedores creados.`  
![](img/1495ae07.png)  

`docker run hello-world --> Descarga y ejecuta un contenedor con la imagen hello-world.`  
![](img/d0f4e12b.png)   

`docker images`  
![](img/9a1125ce.png)  

`docker ps -a           --> El contenedor está estado 'Exited'.`  
![](img/68b91c4c.png)  


---

## Configuración de la red

**Habilitar el acceso a la red externa a los contenedores**

Si queremos que nuestro contenedor tenga acceso a la red exterior, debemos
activar la opción IP_FORWARD (`net.ipv4.ip_forward`). Lo podemos hacer en YAST.

* Para openSUSE13.2 (cuando el método de configuracion de red es Wicked).
`Yast -> Dispositivos de red -> Encaminamiento -> Habilitar reenvío IPv4`
* Cuando la red está gestionada por Network Manager, en lugar de usar YaST
debemos editar el fichero `/etc/sysconfig/SuSEfirewall2` y poner `FW_ROUTE="yes"`.
* Para openSUSE Tumbleweed `Yast -> Sistema -> Configuración de red -> Menú de encaminamiento`.  

![](img/6f3be4fe.png)  

Reiniciar el equipo para que se apliquen los cambios.

## Más comandos

Información sobre otros comandos útiles:

* `docker stop CONTAINERID`, parar un contenedor que estaba iniciado.
* `docker start CONTAINERID`, inicia un contenedor que estaba parado.
* `docker attach CONTAINERID`, conecta el terminal actual con el interior de contenedor.
* `docker ps`, muestra los contenedores en ejecución.
* `docker ps -a`, muestra todos los contenedores en ejecución o no.
* `docker rm CONTAINERID`, eliminar un contenedor.
* `docker rmi IMAGENAME`, eliminar una imagen.

---

## Creación manual

Nuestro SO base es OpenSUSE, pero vamos a crear un contenedor Debian8,
y dentro instalaremos Nginx.

## Crear una imagen manualmente
`docker images         --> Vemos las imágenes disponibles localmente.`  
![](img/82ff7a40.png)    

`docker search debian   --> Buscamos en los repositorios de Docker Hub.`  
![](img/fb2e7bd9.png)

`docker pull debian:8   --> Descargamos una imagen debian:8 en local. `   
![](img/63a86941.png)   

`docker images  `  
![](img/aba569ef.png)    

`docker ps -a           --> Vemos todos los contenedores.`  
![](img/3c61bbac.png)  

`docker ps              --> Vemos sólo los contenedores en ejecución.`  
![](img/a3dd9a22.png)    

```  

* Vamos a crear un contenedor con nombre `con_debian` a partir de la
imagen `debian:8`, y ejecutaremos `/bin/bash`:

```
`docker run --name=con_debian -i -t debian:8 /bin/bash`  
![](img/fd6b73c1.png)  

(Estamos dentro del contenedor)  
`root@IDContenedor:/# cat /etc/motd            --> Comprobamos que estamos en Debian.`  
![](img/dd4c0dc5.png)    

`root@IDContenedor:/# apt-get update`  
![](img/43a26b54.png)    

`root@IDContenedor:/# apt-get install -y nginx --> Instalamos nginx en el contenedor.`  
![](img/345cd1af.png)   

`root@IDContenedor:/# apt-get install -y vim   --> Instalamos editor vi en el contenedor.`  
![](img/e608e790.png)  

`root@IDContenedor:/# /usr/sbin/nginx          --> Iniciamos el servicio nginx.`  
![](img/cf6ac09c.png)

`root@IDContenedor:/# ps -ef`    
![](img/9e004732.png)    


```
* Creamos un fichero HTML (`holamundo.html`).
```
`root@IDContenedor:/# echo "<p>Hola nombre-del-alumno</p>" > /var/www/html/holamundo.html`  
![](img/af00803a.png)   

```
* Creamos tambien un script `/root/server.sh` con el siguiente contenido:

#!/bin/bash

echo "Booting Nginx!"
/usr/sbin/nginx &

echo "Waiting..."
while(true) do
  sleep 60
done  
```  
![](img/e2c56e77.png)  

![](img/709adb9a.png)  

Ahora con esto podemos crear la nueva imagen a partir de los cambios que realizamos sobre la imagen base:  


`docker commit 7d193d728925 dvarrui/nginx `  
![](img/660deb94.png)

`docker images`    
![](img/c3833789.png)  


```
> Los estándares de Docker estipulan que los nombres de las imagenes deben
seguir el formato `nombreusuario/nombreimagen`.
> Todo cambio que se haga en la imagen y no se le haga commit se perderá en cuanto se cierre el contenedor.

```
`docker ps`  
![](img/56531207.png)  

`docker stop con_debian  --> Paramos el contenedor.`  
![](img/9fbabd27.png)     

`docker ps`  
![](img/92f63ca3.png)    

`docker ps -a           --> Vemos el contenedor parado.`  
![](img/a2bbe38e.png)    

`docker rm IDcontenedor --> Eliminamos el contenedor.`  
![](img/6627c315.png)      

`docker ps -a`  
![](img/b1bee1ad.png)     

## Crear contenedor con Nginx

Bien, tenemos una imagen con Nginx instalado, probemos ahora la magia de Docker.

Iniciemos el contenedor de la siguiente manera:
```
docker ps
docker ps -a
docker run --name=con_nginx -p 80 -t dvarrui/nginx /root/server.sh
Booting Nginx!
Waiting...
```   
![](img/4264d855.png)   

![](img/278ee21f.png)  

![](img/5a9215ac.png)  

Los mensajes muestran que el script server.sh está en ejecución.
No parar el programa. Es correcto.

> * El argumento `-p 80` le indica a Docker que debe mapear el puerto especificado
del contenedor, en nuestro caso el puerto 80 es el puerto por defecto
sobre el cual se levanta Nginx.
> * El script `server.sh`nos sirve para iniciar el servicio y permanecer en espera.
Lo podemos hacer también con el prgorama `Supervisor`.

Abrimos una nueva terminal.  
`docker ps`, nos muestra los contenedores en ejecución. Podemos apreciar
que la última columna nos indica que el puerto 80 del contenedor está redireccionado a un puerto local `0.0.0.0.:NNNNNN->80/tcp`.    
![](img/89b1e272.png)     

Abrir navegador web y poner URL `0.0.0.0.:NNNNNN`. De esta forma nos conectaremos con el servidor Nginx que se está ejecutando dentro del contenedor.    
![](img/d5c72be5.png)     

Comprobamos también que se muestra el fichero *holamundo.html*:  
![](img/f45cf966.png)    

Paramos el contenedor y lo eliminamos.  
`docker ps`  
![](img/27fba60f.png)    

`docker stop con_nginx`  
![](img/3101b689.png)    

`docker ps`  
![](img/d34d8dcf.png)    

`docker ps -a`  
![](img/b67e79f6.png)  

`docker rm con_nginx`  
![](img/538c13ac.png)

`docker ps -a`  
![](img/ba180947.png)     

> Como ya tenemos una imagen docker, podemos crear nuevos contenedores
cuando lo necesitemos.

---

## Crear un contenedor con `Dockerfile`

Ahora vamos a conseguir el mismo resultado del apartado anterior, pero
usando un fichero de configuración, llamado `Dockerfile`

## Comprobaciones iniciales:

```
docker images
docker ps
docker ps -a
```  
![](img/f0c34112.png)  

![](img/cf04accf.png)     

![](img/bcec0bea.png)  


## Preparar ficheros

Creamos el directorio `/home/nombre-alumno/dockerXX`, y ponemos dentro los siguientes ficheros:
    * Dockerfile
    * holamundo.html
    * server.sh    
![](img/2218b066.png)    


* Crear el fichero `Dockerfile` con el siguiente contenido:  

```
FROM debian:8

MAINTAINER Nombre-del-Alumno 1.0

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y nginx
RUN apt-get install -y vim

COPY holamundo.html /var/www/html
RUN chmod 666 /var/www/html/holamundo.html

COPY server.sh /root
RUN chmod +x /root/server.sh

EXPOSE 80

CMD ["/root/server.sh"]    
```  
![](img/7159a995.png)  

> Los ficheros `server.sh` y `holamundo.html` que vimos en el apartado anterior,
tienen que estar en el mismo directorio del fichero `Dockerfile`.


## Crear imagen desde el `Dockerfile`

El fichero [Dockerfile](./files/Dockerfile) contiene la información necesaria para contruir el contenedor, veamos:

`cd /home/nombre-del-alumno/dockerXX --> Entramos al directorio del Dockerfile.`  
![](img/f2937cb0.png)      

`docker images                       --> Consultamos las imágenes disponibles.`  
![](img/c1785b77.png)    

`docker build -t dvarrui/nginx2 .    --> Construye imagen a partir del Dockefile.`  
![](img/8b5cf087.png)      

`docker images                       --> Debe aparecer nuestra nueva imagen.`  
![](img/13472aec.png)      

## Crear contenedor y comprobar
A continuación vamos a crear un contenedor con el nombre `con_nginx2`,
a partir de la imagen `dvarrui/nginx2`, y queremos que este contenedor
ejecute el programa `/root/server.sh`.  

```
docker run --name=con_nginx2 -p 80 -t dvarrui/nginx2 /root/server.sh
```
Desde otra terminal hacemos `docker ps`, para averiguar el puerto de escucha
del servidor Nginx.
![](img/54fd3c0f.png)  

![](img/1c629874.png)  

Comprobamos en el navegador URL:   
![](img/19cdddae.png)  

Comprobamos en el navegador URL:   
![](img/ee00a45a.png)  

---

# Migrar las imágenes de docker a otro servidor

¿Cómo puedo llevar los contenedores docker a un nuevo servidor?

> Enlaces de interés
>
> * https://www.odooargentina.com/forum/ayuda-1/question/migrar-todo-a-otro-servidor-imagenes-docker-397
> * http://linoxide.com/linux-how-to/backup-restore-migrate-containers-docker/

Creamos una imagen de contenedor:
`docker ps`
![](img/67b51e84.png)  

`docker commit -p CONTAINERID containerXX-backup` grabamos una imagen de nombre "containerXX-backup" a partir del contenedor CONTAINERID.  
![](img/1508522b.png)  

`docker images`comprobamos que se ha creado la imagen "container-backup".  
![](img/dfcf07d0.png)  

Exportamos una imagen docker a fichero:
`docker save -o ~/containerXX-backup.tar containerXX-backup`, guardamos la imagen
"container-backup" en un fichero tar.  
![](img/72c0c2f1.png)  

Importar imagen docker desde fichero:
Nos llevamos el tar a otra máquina con docker instalado, y restauramos.  

`docker load -i ~/containerXX-backup.tar`, cargamos la imagen docker a partir del fichero tar.  
![](img/17592047.png)  

`docker images`, comprobamos que la nueva imagen está disponible.    
![](img/0bae1ab0.png)      
