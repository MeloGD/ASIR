```
* Práctica utilizada en los cursos 201213, 201314, 201415
* Actualizada para el curso 201516
```

# Almacenamiento NAS con OpenSUSE

* Trabajar de forma individual.
* Entregar informe con capturas de pantalla.

---

# 0. Definición de Wikipedia

El almacenamiento conectado en red, Network Attached Storage (NAS), es el nombre
dado a una tecnología de almacenamiento dedicada a compartir la capacidad de almacenamiento de un computador (servidor) con computadoras personales o servidores clientes a través de una red (normalmente TCP/IP), haciendo uso de un sistema operativo optimizado para dar acceso con los protocolos CIFS, NFS, FTP o TFTP.

Los sistemas NAS son dispositivos de almacenamiento a los que se accede desde los equipos a través de protocolos de red (normalmente TCP/IP). También se podría considerar un sistema NAS a un servidor (Microsoft Windows, Linux, etcétera) que comparte sus unidades por red, pero la definición suele aplicarse a sistemas específicos.

Los protocolos de comunicaciones NAS están basados en archivos por lo que el cliente solicita el archivo completo al servidor y lo maneja localmente, por lo que están orientados a manipular una gran cantidad de pequeños archivos. Los protocolos usados son protocolos de compartición de archivos como Network File System (NFS) o Microsoft Common Internet File System (CIFS).

Muchos sistemas NAS cuentan con uno o más dispositivos de almacenamiento para incrementar su capacidad total. Frecuentemente, estos dispositivos están dispuestos en RAID (Redundant Arrays of Independent Disks) o contenedores de almacenamiento redundante.

---

# 1. Prepara la máquina y los discos

Enlaces de interés:
* Montar en una MV con OpenSUSE el servicio Samba
(Consultar [configuración](../../global/configuracion/opensuse.md).
* Consultar vídeo [SAMBA Management with YaST on SUSE](https://youtu.be/Zh3J-HUYDY4?list=PL3E447E094F7E3EBB)

Normalmente los NAS usan un disco a parte para guardar los datos. Y para mayor
seguridad usan un almacenamiento en RAID1 o RAID5.
Vamos a usar el entorno gráfico Yast para crear RAID1.

* Ir a MV OpenSUSE NAS
* Configurar hostname con `nasXX`.
* Añadimos 2 discos de tamaño 500 MB a la MV VirtualBox.
* Iniciamos la MV.
* Ir a `Yast -> Particionador`.
* Crear un RAID1 con los 2 discos.
* Montar el RAID1 en la ruta `/mnt/nas`.
* Comprobamos la configuración de los discos:
    * `df -hT` debemos ver los discos montados en la ruta.
    * `fdisk -l`
    * `cat /proc/mdstat`

---

# 2. Instalar y configurar Samba

* Instalar y configurar un servidor Samba (desde Yast por ejemplo o con zypper).

![nas-opensuse-yast-samba.png](./files/nas-opensuse-yast-samba.png)

> Samba es un software que permite que el equipo se comunique
usando el protocolo SMB/CIFS típico de las redes Windows.

* Ir a MV OpenSUSE NAS.
* Configurar Servidor Samba con:
    * Grupo de trabajo: `curso1617`
    * Sin controlador de Dominio
    * Inicio del servicio: `durante el arranque`
    * Puerto abierto en el cortafuegos
    * Nombre de Host NetBios: `nasXX`

## 2.1 Crear recurso compartido (I)

Grupos y usuarios del sistema:
* En el sistema, crear el grupo `hobbitsXX`.
* Añadir los usuarios `frodoXX` y `bilboXX`

En el sistema de ficheros:
* Crear la carpeta `/mnt/nas/lacomarcaXX.d`
* Con permisos de lectura/navegación para todos.
* Con permisos de escritura/lectura/navegación para el grupo `hobbitsXX`.

Configuración el recurso compartido en Samba:
* Usar `Yast -> Samba Server` para crear recursos compartido (SMB/CIFS)
en la ruta anterior, con el nombre `lacomarcaXX`.
* Heredar ACLS
* `path = /mnt/nas/lacomarcaXX.d`
* `valid users = @hobbitsXX` (Los usuarios de este grupo pueden acceder al recurso)
* `read only = No`

Veamos una imagen de ejemplo, donde los valores de la imagen no se corresponden
con lo que se pide en la práctica.
![nas-samba-share.png](./files/nas-samba-share.png)

## 2.2 Crear recurso compartido (II)

Grupos y usuarios del sistema:
* En el sistema, crear el grupo `humanosXX`
* Añadir los usuarios `gandalfXX` y `aragornXX`

En el sistema de ficheros:
* Crear la carpeta `/mnt/nas/mordorXX.d`
* Con permisos de lectura/navegación para todos.
* Con permisos de escritura/lectura/navegación para el grupo `humanosXX`.

Configuración el recurso compartido en Samba:
* Crear recursos compartido (SMB/CIFS) en dicha ruta, con el nombre `mordorXX`.
* Heredar ACLS
* `path = /mnt/nas/mordorXX.d`
* `valid users = gandalfXX, frodoXX` (Estos usuarios pueden acceder al recurso)
* `read only = Yes`

## 2.3 Comprobar

* Poner también clave en Samba para los usuarios: `frodoXX`, `bilboXX`,
`gandalfXX` y `aragornXX`.
    * `smbpasswd -a USUARIO` para poner clave del usuario en samba.
    * `smbpasswd -e USUARIO` para activar el usuario en samba.
* Reiniciar el servicio:
    * `systemctl stop smb`
    * `systemctl start smb`
    * `systemctl status smb`
* Comprobar la configuración por comandos.
    * `cat /etc/samba/smb.conf`
    * `testparm`
* `netstat -untap`, comprobar el servicio desde la máquina local.
* En el cortafuegos autorizar servicios "Cliente SAMBA" y "Servidor SAMBA".

> Actualizar el sistema `zypper update` en caso de error.

---

# 3. Comprobar desde un cliente OpenSUSE

* Ir a MV cliente OpenSUSE.
* En el cortafuegos autorizar servicio "Cliente SAMBA".
* Comprobar el acceso al servidor NAS desde otra máquina con todos los
usuarios, y todos los recursos.
* Comprobaciones desde el cliente:
    * Ejecutando `smbtree` en OpenSUSE veremos todos los recursos compartidos de red.
    * Ejecutando `smbclient -L ip-servidor-samba`, comprobamos que aparecen correctamente
    los nombres de los recursos compartidos de nuestra máquina Samba Server.

* Comprobar acceso a las carpetas compartidas (incluir captura de pantalla).
* `netstat -untap`, comprobar que hay una conexión establecidad con el servidor.

> * En el explorador de archivos, pulsar CTRL+L para que nos aparezca casilla para URL
> * Podemos encontrar la MV más rápido poniendo `smb://ip-del-servidor` en la búsqueda de red.

---

# 4. Comprobar desde un cliente Windows 7

* Ir a MV cliente Windows 7.
* Comprobar acceso a las carpetas compartidas (incluir captura de pantalla).

> Podemos encontrar la MV más rápido poniendo `\\ip-del-servidor` en la búsqueda de red.

* `net use` para comprobar sesiones de red abiertas.
* `netstat`, comprobar que hay una conexión establecidad con el servidor.

> * Después de cada conexión se quedan guardada la información en el cliente Windows (Ver comando net use).
> * Para cerrar las conexión SMB/CIFS que ha realizado el cliente al servidor, usamos el comando: `C:>net use * /d /y`.
