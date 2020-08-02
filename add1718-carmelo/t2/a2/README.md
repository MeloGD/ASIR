# Puppet.  
![img](./img/000.png)    

## 1. Open Suse.
### 1.1 Instalación y configuración del Master.  
Comenzamos la instalación de *Puppet* con ``sudo zypper install rubygem-puppet-master``.  
![img](./img/001.png)    

Comprobamos el estado del servicio con ``systemctl status puppetmaster.service``.  
![img](./img/002.png)     

Visto esto, lo activamos en el arranque con las opciones de *enable*, lo iniciamos con *start* y volvemos a comprobar su estado.  
![img](./img/003.png)    

Comprobamos que se han creado los directorios de *Puppet*.  
![img](./img/004.png)      

Y creamos los archivos requeridos por la práctica:   
```
mkdir /etc/puppet/files
touch /etc/puppet/files/readme.txt
mkdir /etc/puppet/manifests
touch /etc/puppet/manifests/site.pp
mkdir /etc/puppet/manifests/classes
touch /etc/puppet/manifests/classes/hostlinux1.pp
```    
![img](./img/005.png)    

Quedando los directorios con esta organización.  
![img](./img/009.png)     

En *site.pp* depositamos la siguiente configuración:  
```
import "classes/*"

node default {
  include hostlinux1
}
```   
![img](./img/007.png)      

Y en *hostlinux1*:  
```
class hostlinux1 {
  package { "tree": ensure => installed }
  package { "traceroute": ensure => installed }
  package { "geany": ensure => installed }
}  
```  
![img](./img/008.png)    

Antes de pasar al *Cliente1*, comprobamos que el directorio ``/var/lib/puppet`` tienen a *puppet* como usuario-grupo y que el servicio este funcionando de forma correcta.  
![img](./img/010.png)      

``systemctl status puppetmaster``
![img](./img/011.png)    

``netstat -ntap |grep ruby``
![img](./img/012.png)     

``tail /var/log/puppet/*.log``
![img](./img/013.png)    

Y añadimos una exepción en el *firewall*.  
![img](./img/014.png)    

![img](./img/015.png)  

### 1.2 Instalación y configuración del Cliente1.    
Instalamos con ``sudo zypper install rubygen-puppet``.  
![img](./img/016.png)    

Añadimos las siguientes líneas a ``/etc/puppet/puppet.conf``:  
```[main]
# Definir el host master puppet
server=master18.curso1718
...
[agent]
...
# Desactivar los plugin para este agente
pluginsync=false
```  
![img](./img/017.png)    

Comprobamos que el directorio ``/var/lib/puppet`` tiene como usuario-grupo a *puppet*, el estado del servicio, arrancar y habilitar en el arranque y los servicios de los puertos.  
![img](./img/018.png)    

![img](./img/019.png)    

![img](./img/020.png)   

![img](./img/021.png)    

## 1.3 Certificados.  
Volvemos al master como root, lanzamos `puppet cert list` y podremos ver que el certificado del *Cliente1* aparece.  
![img](./img/022.png)    

Lo aceptamos con `puppet cert sign "cli1alu18.curso1718"`.  
![img](./img/023.png)    

Hecho esto, habrá desaparecido de la lista principal y se habrá registrado en la máquna máster.  
![img](./img/024.png)    

Reiniciamos y comprobamos el estado para comprobar que se ha realizado correctamente.  
![img](./img/025.png)    

---
Vamos al cliente y comprobamos con `puppet agent --test`.  
![img](./img/026.png)    

Y con `puppet agent --server master18.curso1718 --test`.  
![img](./img/027.png)    

No existe fichero de log, por lo tanto, no ha sucedido ninguno.  
![img](./img/028.png)    

## 1.4 Segundo fichero pp.  
Creamos un fichero *hostlinux2* dentro de la ruta `/etc/puppet/manifests/classes`.  
![img](./img/031.png)  

Con el siguiente contenido:  
```
class hostlinux2 {
  package { "tree": ensure => installed }
  package { "traceroute": ensure => installed }
  package { "geany": ensure => installed }

  group { "piratas": ensure => "present", }
  group { "admin": ensure => "present", }

  user { 'barbaroja':
    home => '/home/barbaroja',
    shell => '/bin/bash',
    password => 'poner-una-clave-encriptada',
    groups => ['piratas','admin','root']
  }

  file { "/home/barbaroja":
    ensure => "directory",
    owner => "barbaroja",
    group => "piratas",
    mode => 750
  }

  file { "/home/barbaroja/share":
    ensure => "directory",
    owner => "barbaroja",
    group => "piratas",
    mode => 750
  }

  file { "/home/barbaroja/share/private":
    ensure => "directory",
    owner => "barbaroja",
    group => "piratas",
    mode => 700
  }

  file { "/home/barbaroja/share/public":
    ensure => "directory",
    owner => "barbaroja",
    group => "piratas",
    mode => 755
  }
}
```     
![img](./img/029.png)      

Y *site.pp* :  
```  
import "classes/*"

node default {
  include hostlinux2
}
```  
![img](./img/030.png)      

Reiniciamos y comprobamos el estado.  
![img](./img/032.png)    

En el *Cliente1* comprobamos los nuevos cambios. (Esta captura esta incorrecta, dado que bastaba con un simple reinicio del servicio para forzar la nueva configuración.).
![img](./img/033.png)    

## 2. Windows.  
### 2.1 Master.  
En el *master* creamos el fichero *hostwindows3.pp*.  
![img](./img/036.png)    

Con la siguiente configuración:  
```
class hostwindows3 {
  file {'C:\warning.txt':
    ensure => 'present',
    content => "Hola Mundo Puppet!",
  }
}  
```  
![img](./img/034.png)    

Y *site.pp* :  
```
import "classes/*"

node 'cli1alu42.curso1617' {
  include hostlinux2
}

node 'cli2alu18' {
  include hostwindows3
}
```  
![img](./img/035.png)    

Reiniciamos y comprobamos el estado del servicio.  
![img](./img/037.png)    

Por último, con el comando ``facter`` comprobamos la versión instalada de *Puppet*, necesario para escoger el archivo de instalación correcto en Windows.  
![img](./img/038.png)    

### 2.2 Cliente 2.  
Descargamos la versión deseada desde https://downloads.puppetlabs.com/windows/ e instalamos.  
![img](./img/039.png)    

Una vez instalado, nos dirigimos a `C:\ProgramData\PuppetLabs\puppet\etc\puppet.conf` y lo dejamos de la siguiente manera:  
```
[main]
server=masterXX.curso1718 # Definir el host master
pluginsync=false          # Desactivar los plugin
```  
![img](./img/040.png)  

Reiniciamos la máquina y ejecutamos el *agente de puppet* que generará el certificado.  
![img](./img/Selección_001.png)     

Vamos al master y ejecutamos `puppet cert --list`, donde aparecerá el certificado del cliente si todo ha salido bien.  
![img](./img/Selección_002.png)      

Aceptamos el certificado con `puppet cert sign "cli2alu18"` y reiniciamos el servicios.     
![img](./img/Selección_003.png)     

Volvemos al cliente y ejeuctamos `puppet agent --configprint server` que nos deberá dar la salida *master18.curso1718*.  
![img](./img/Selección_004.png)     

Ejecutamos `puppet agent --server master18.curso1718 --test` para cargar la configuración desde el master.    
![img](./img/Selección_005.png)     

Comprobamos el estado de agente con `puppet agent -t --debug --verbose`.  
![img](./img/Selección_006.png)     

![img](./img/Selección_007.png)     

`facter` Para ver la versión alctual del *agente puppet*.  
![img](./img/Selección_008.png)     

![img](./img/Selección_009.png)     

Vemos la configuración actual del usuario con `puppet resource user carmelo-w10rdd`.  
![img](./img/Selección_010.png)     

Y finalmente `puppet resource file c:\Users:` para ver la configuración puppet de la carpeta.  
![img](./img/Selección_011.png)   

## 3. Hostwindows4.pp .
Probamos la nueva configuración con un nuevo fichero.  
![img](./img/Selección_012.png)  

Sincronizamos.  
![img](./img/Selección_013.png)     

Ha funcionado.  
![img](./img/Selección_014.png)     


## 4. Hostwindows5.pp .
Repetimos los pasos anteriores, pero esta vez se deberá crear un usuario, un fichero y un directorio.
![img](./img/Selección_018.png)       

Forzamos el la configuración.
![img](./img/Selección_016.png)    

Se ha creado el directorio, el fichero...  
![img](./img/Selección_017.png)     

Y el usuario.  
![img](./img/Selección_015.png)     

# Anexo: Problema y solución.
La primera vez que intenté sincronizar la configuración de *puppet*, esta no paraba de fallar. Aparecía el certificado y lo firmarba.  
![img](./img/041.png)    

![img](./img/042.png)      

Pero a la hora de realizar el test, salía el siguiente error.
![img](./img/043.png)     
Usé los comandos sugeridos en la consola, pero ninguno de ellos surtió efecto, a pesar de hacer varios reincios, desactivar firewall etc...  

Como última opción disponible, fui a la ruta de `C:\Usuarios\carmelo-w10rdd\puppet\ssl\certs` donde pude ver que los "en teoría eliminados certificados" todavía seguían ahí, a pesar de haber utilizado los comandos sugeridos y la documentación de *puppet*. Los borré manualmente.
![img](./img/044.png)  

Reinicié la máquina y por fin todo volvió a la normalidad.  
![img](./img/045.png)    
