
```
Nuevo Curso 201617
```

# Servidor de actualizaciones con OpenSUSE

Necesitaremos 2 MV con OpenSUSE.
* Un servidor
* Un cliente

---

# 1. Servidor Web

Vamos a necesitar un servidor Web para que los clientes se puedan conectar
con elservidor de actualizaciones usando el protocolo HTTP.

* Ir a la MV servidor de actualizaciones.
* Instalamos el servidor web Apache `zypper in apache2`
* `systemctl enable apache2`, activar apache2 al inicio.
* `systemctl start apache2`, iniciar servicio apache2.
* `systemctl status apache2`, comprobar el estado del servicio apache2.
* Crear el fichero `/srv/www/htdocs/index.html`. Escribimos nuestro nombre dentro.
* Desde la MV cliente abrimos navegador web y ponemos URL `http://ip-del-servidor`,
para comprobar que accedemos vía HTTP a la otra MV.

> Si no se ve la página web, comprobar el cortafuegos en el servidor.
> Ejecutando `nmap -Pn ip-del-servidor` desde el cliente, comprobamos los servicios
abiertos en el servidor.
>
> Para abrir el servicio web en el cortafuegos:
> * `Yast -> Cortafuegos -> Servicios autorizados`, añadir servicio `HHTP Server`

---

# 2. Preparar el repositorio local

* Vamos al servidor
* Crear directorio local `/srv/www/htdocs/repo/nombre-alumnoXX`.

Vamos a descargar algunos paquetes de los repos de OpenSUSE en nuestra máquina local.
* `tree /var/cache/zypp/packages`, vemos una estructura de directorios sin archivos.
* Ejecutar comandos necesarios para descargar sólo los paquetes que queramos y sus dependencias.
Descargar por ejemplo, paquetes geany, nano, dia, nmap y/o ipcalc.
    * `zypper in --download-only PACKAGENAME`, para descargar paquete sin instalarlo,
    cuando el software no está instalado en nuestro sistema local.
    * `zypper -v in -f --download-only PACKAGENAME`, para descargar paquete sin
    instalarlo, cuando el software ya está instalado en nuestro sistema local.
* `tree /var/cache/zypp/packages`, vemos una estructura de directorios con los
archivos de los paquetes descargados.

> Para descargar un repositorio entero podemos usar `wget -r URL-DEL-REPOSITORIO`.
> Pero esto tardaría mucho tiempo.

* Copiar los directorios/ficheros descargados desde la cache de zypper (`/var/cache/zypp/packages`)
al directorio de nuestro repositorio local.
    * Comprobamos `tree /srv/www/htdocs/repo/nombre-alumnoXX/`

Ahora hay que convertir el directorio local en un repositorio.
* Instalar `createrepo`.
* Usar createrepo:
    * `vdir /srv/www/htdocs/repo/nombre-alumnoXX/`, ver estado actual.
    * `createrepo -v /srv/www/htdocs/repo/nombre-alumnoXX/`, crear índices.
        * Tiene que mostrar una lista de todos los paquetes detectados en este repositorio local.
    * `vdir /srv/www/htdocs/repo/nombre-alumnoXX/`, comprobar.

> Se tiene que crear un subcarpeta `repodata` con ficheros xml dentro.

Se pueden compartir los paquetes de este repositorio al resto de equipo de la red
usando diferentes protocolos (http, nfs, ftp/tftp, etc.). Nosotros hemos elegido usar
el protocolo HTTP (Servidor Web).

---

# 3. Cliente del repositorio YAS

* Ir a otra MV OpenSUSE
Comprobar acceso:
* Abrir navegador y poner URL `http://ip-del-servidor/repo/nombre-alumnoXX/repodata/repomd.xml`
    * Debe verse el contenido del fichero XML.

Vamos a añadir nuestro repositorio a esta MV.
* Ir a `Yast -> Repositorios`
* Añadir.
* Seleccionar: HTTP y Descargar archivos de descripción de repositorio
* Siguiente.
* Editar partes de la URL.
    * Nombre de repositorio: `repo-nombre-alumnoXX`
    * Protocolo: HTTP
    * Nombre del servidor: ip-del-servidor
    * Puerto: 80
    * Directorio: `/repo/nombre-alumnoXX/`
    * Autenticación: Anónimo

* Hacer captura de la lista de repositorios que tengan activos.

> En mi caso me aparecen los siguientes:
>
> * OpenSUSE Leap 42.2-Update-Non-Oss,
> * OpenSuse Leap 42.2-Non-Oss
> * OpenSuse Leap 42.2-Oss
> * OpenSuse Leap 42.2-Update

* Deshabilitar(propiedad activar OFF) todos los repositorios.
* Habilitar(propiedad activar ON) sólo el `repo-nombre-alumnoXX`
* Aceptar y cerrar Yast.

---

# 4. Comprobamos el repositorio desde el cliente

* `cat /etc/zypp/repos.d/repo-nombre-alumnoXX.repo`, comprobamos que la configuración
del repositorio nuevo está en este fichero de texto.
* `zypper refresh`, refrescar los repositorios.
* Probar la instalación de algún paquete de nuestro repositorio.
* Probar la instalación de algún paquete que no esté en nuestro repositorio.

---

# ANEXO

> Podríamos haber hecho el paso anterior por comandos
> * Creando el fichero `/etc/zypp/repo.d/repo-nombre-alumnoXX.repo`
> * `zypper addrepo http://hostname/repo alias`
