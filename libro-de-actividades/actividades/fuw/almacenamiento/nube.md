
```
Utilizada en los cursos 201415 y 201314
En el curso 201516 se amplía para usar OpenSUSE13.2
En el curso 201617 se adapta para usar OpenSUSE Leap
```

# 1. Entrega

* Apartado 2:
    * Trabajo individual.
    * Vídeo que muestre la práctica en funcionamiento.
* Apartados 3, 4 y 5:
    * Colaborar con otro compañero.
        * Montar nuestro servidor para que lo use el compañero.
        * Usar el servidor de otro compañero.
    * Entregar un informe de los pasos realizados y el URL del vídeo subido a Youtube

---

# 2. Nube ajena

Almacenamiento en la nube de un proveedor externo.

* Realizar la instalación y configuración de alguna de las siguientes herramientas a elegir por el alumno:
    * DropBox
    * Windows Live Mesh, OneDrive,
    * Ubuntu One, ZumoDrive.
* Realizar una instalación sobre SO Windows y otra sobre GNU/Linux. Mostrar su uso mediante ejemplos.

---

# 3. Nube propia con OwnCloud Server en OpenSUSE Leap

Últimamente se están poniendo de moda servicios de almacenamiento y sincronización
de ficheros en la nube, entre los que destacan Dropbox y Google Drive. Ambas soluciones son cerradas.

Dentro de las soluciones libres disponemos de ownCloud, por el que parece que apuesta Suse, y que utilizan varios proveedores para ofrecer servicios de almacenamiento en la nube con un modelo de negocio freemium, como son OwnCubey GetFreeCloud.

Las fuentes están disponibles para poder instalarlo en máquinas propias o alquiladas,
así como clientes de sincronización para Windows, Linux, Android y próximamente para iOs y Mac.

Para más información [official documentation](https://doc.owncloud.org/).

## 3.1 Instalar OwnCloud

* Vamos a seguir el siguiente [tutorial](https://github.com/iosifidis/owncloud-opensuse-leap).
* Elegir una MV con OpenSUSE Leap para instalar OwnCloud Server.
* Instalamos lo siguientes paquetes:

```
zypper in apache2 mariadb apache2-mod_php5 php5-gd php5-json php5-fpm php5-mysql php5-curl php5-intl php5-mcrypt php5-zip php5-mbstring php5-zlib
```

## 3.2 Create Database

Iniciar el servicio para poder crear la base de datos.

```
systemctl start mysql.service
systemctl enable mysql.service
```

The root password is empty by default. That means that you can press enter and you can use your root user. That's not safe at all. So you can set a password using the command:

`mysqladmin -u root password newpass`

Where newpass is the password you want.
Now you set the root password, create the database.

```
mysql -u root -p
(you'll be asked for your root password)

CREATE DATABASE ocdatabase;
GRANT ALL ON ocdatabase.* TO ocuser@localhost IDENTIFIED BY 'dbpass';
```

* Database user: `ocuser`
* Database name: `ocdatabase`
* Database user password: `dbpass`

## 3.3 PHP changes

* Hacer copia de seguridad del fichero /etc/php5/apache2/php.ini
* Now you should edit the file `/etc/php5/apache2/php.ini` and change the values

```
post_max_size = 50G
upload_max_filesize = 25G
max_file_uploads = 200
max_input_time = 3600
max_execution_time = 3600
session.gc_maxlifetime = 3600
memory_limit = 512M
```

Finalmente habilitar las siguientes extensiones:

```
extension=php_gd2.dll
extension=php_mbstring.dll
```

## 3.4 Apache Configuration

Habilitar los siguientes módulos de Apache. Algunos ya deberían estar habilitados.

```
a2enmod php5
a2enmod rewrite
a2enmod headers
a2enmod env
a2enmod dir
a2enmod mime
```

Iniciar el servicio de Apache.

```
systemctl start apache2.service
systemctl enable apache2.service
```

## 3.5 Instalar ownCloud

Antes de la instalación, crear la carpeta de datos con los permisos adecuados.
Nosotros crearemos el directorio `/opt/owncloud`.

```
mkdir /opt/owncloud-data
chmod -R 0770 /opt/owncloud-data
chown wwwrun /opt/owncloud-data
```

Descargar [OwnCloud](https://owncloud.org/install/). Descomprimir y mover a
la carpeta.

```
wget https://download.owncloud.org/community/owncloud-9.1.1.zip
unzip owncloud-9.1.1.zip
cp -r owncloud /srv/www/htdocs
chown -R wwwrun /srv/www/htdocs/owncloud/
```

Make sure that everything is OK and then delete the folder owncloud and owncloud-9.1.1.zip from the root (user) directory.

* Abrir navegador con URL la IP del servidor owncloud
    * Poner ususario/clave del administrador.
    * El directorio de datos `/opt/owncloud_data`
    * Database user: `ocuser`
    * Database name: `ocdatabase`
    * Database user password: `dbpass`
* Esperar a que termine la instalación.

> * Crear el archivo /srv/www/htdocs/index.html
> * Escribir el nombre del alumno dentro de index.html
> * Con URL localhost accedemos a index.html
> * Con URL localhost/owncloud accedemos a la aplicación OwnCloud

---

## 4 Comprobar vía web

* Hacer una copia de seguridad del fichero de configuración de OwnCloud ( `/srv/www/htdocs/owncloud/config/config.php`).
* Para permitir el acceso desde otros equipos, tenemos que añadir la IP del servidor a las opciones
`trusted_domains` dentro del fichero de configuración `/srv/www/htdocs/owncloud/config/config.php`. Ver ejemplo:

![owncloud-config-php](./files/owncloud-config-php.png)

> **IMPORTANTE**: Revisar bien los cambios que realicemos en el fichero de configuración anterior. Un fallo de sintaxis puede dejar nuestro servidor sin funcionar.

* Hacer captura de pantalla del fichero `/srv/www/htdocs/owncloud/config/config.php`.
* Abrimos un navegador URL: `ip-del-servidor/owncloud`. Ahora debe funcionar el acceso usando la IP.
* Abrimos un navegador web, y ponemos en el URL `http://localhost/owncloud`
* Usamos nuestro usuario/clave administrador.
* Creamos un usuario normal.
* Subiremos algunos archivos al servidor.

---

# 5. OwnCloud Desktop Client

* Ir a una MV con Windows 7.
* Instalar el sofware cliente de OwnCloud.
   * Usar URL http://ip-servidor/owncloud.
* Comprobar cómo se mantienen sincronizados los archivos entre las máquinas.

---

# ANEXO

## A.1 Instalación del servidor OwnCloud para Ubuntu

* [OwnCloud en Debian/Ubuntu](http://hipertextual.com/archivo/2014/10/owncloud/)

## A.2 Instalación del servidor OwnCloud para Debian7

* Añadimos un nuevo repositorio con el paquete que queremos instalar:
    * echo 'deb http://download.opensuse.org/repositories/isv:/ownCloud:/community:/nightly/Debian_7.0/ /' >> /etc/apt/sources.list.d/owncloud.list
* Actualizamos la lista de repositorios: `apt-get up...`
* Instalamos el paquete: `apt-get .... owncloud`

## A.3 Instalación del servidor OwnCloud para Raspberry PI

* [BTSync: Clone Dropbox with a Raspberry Pi and BTSync](http://reustle.io/blog/btsync-pi)
