# Vagrant  
![img](./img/Vagrant.png)    

## 1. Instalación.    
Instalamos Vagrant mediante `apt-get install vagrant` (no se puede mostrar una captura de este paso ya que se hizo en la máquina real).  

Creamos el directorio *mivagrant18* y ejecutamos `vagrant init` para generar el archivo de configuración *Vagrantfile*.  
![img](./img/001.png)    

Agregamos la ca caja con `vagrant box add micaja18_ubuntu_precise32.box`.
![img](./img/002.png)      

Y comprobamos que se ha agregado la caja con `vagrant box list`.  
![img](./img/003.png)    

Eliminamos todos los comentarios, dado que estos no son necesarios y dificultan la lectura del archivo.   
![img](./img/004.png)     

Dejando solo la línea de *config.vm.box* como se muestra en la captura.  
![img](./img/005.png)    


## 2. Configuración.
Levantamos la máquina con `vagrant up`.  
![img](./img/006.png)    

Probamos que se puede establecer una conexión mediante ssh.  
![img](./img/007.png)     

Y comprobamos que *Vagrantfile* sigue en el mismo directorio a pesar de estar en un entorno virtual.  
![img](./img/008.png)     

Una vez hecho esto, procedemos a intarlar *apache2*.  
![img](./img/009.png)    

Redirigimos el puerto en *Vagrantfile* usando `config.vm.network :forwarded_port, host: 4567, guest: 80`, como se muestra en la captura.  
![img](./img/010.png)    

Recargamos el servicio de vagrant con `vagrant reload`.  
![img](./img/011.png)    

Llegados aquí, realizamos las siguientes comprobaciones:  
- `nmap -p 4500-4600 localhost, debe mostrar 4567/tcp open tram`.  
![img](./img/013.png)    
- `netstat -ntap, debe mostrar tcp 0.0.0.0:4567 0.0.0.0:* ESCUCHAR`.  
![img](./img/014.png)    

- `172.0.0.1:4567` desde un navegador.  
![img](./img/015.png)      

## 3. Suministro - Ejecución de Scripts.  
Paramos la máquina con `vagrant halt`.  
![img](./img/016.png)    

Y destruimos la máquina con `vagrant destroy`.   
![img](./img/017.png)    


Creamos el script con la siguiente configuración.  
```console
#!/usr/bin/env bash

apt-get update
apt-get install -y apache2
rm -rf /var/www
ln -fs /vagrant /var/www
echo "<h1>Actividad de Vagrant</h1>" > /var/www/index.html
echo "<p>Curso201516</p>" >> /var/www/index.html
echo "<p>Nombre-del-alumno</p>" >> /var/www/index.html
```   
![img](./img/018.png)    

Asignamos permisos de ejecución al script.
![img](./img/019.png)    

Introducimos `config.vm.provision :shell, :path => "install_apache.sh"` en *Vagrantfile*.  
![img](./img/020.png)    

Levantamos la máquina.  
![img](./img/021.png)   

Y comrpobamos en un navegador con la misma dirección.  
![img](./img/022.png)    

![img](./img/023.png)    

### Puppet.    
Volvemos al *Vagrantfile* e introducimos el siguiente código.  
```console
Vagrant.configure(2) do |config|
  ...
  config.vm.provision "puppet" do |puppet|
    puppet.manifest_file = "default.pp"
  end
 end
```  
![img](./img/024.png)    

Creamos el directorio *manifest* y dentro el fichero *default.pp* con:  
```console
package { 'nmap':
  ensure => 'present',
}
```
![img](./img/025.png)    

![img](./img/026.png)    

Recargamos el servicio.
![img](./img/027.png)    

Y ejecutamos `vagrant provision` para cargar la nueva configuración.  
![img](./img/028.png)    


## 4. Caja personalizada.  
## Máquina Virtual.  
Comprobamos que *openssh* está instalado.  
![img](./img/029.png)      

Creamos usuario *vagrant*, con permisos *root*. También modificamos ambas contraseñas (root y normal) a "vagrant".  
![img](./img/045.png)

Añadiemos también `vagrant ALL=(ALL) NOPASSWD: ALL` al fichero `/etc/sudoers`.  
![img](./img/046.png)    

Ejecutamos `wget https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub -O .ssh/authorized_keys`.  
![img](./img/032.png)    

Nos aseguramos de fijar los permisos de *.ssh/* y *authorized_keys* a 700-600 respectivamente.  
![img](./img/047.png)    

Antes de salir de la máquina virtutal, comprobamos la versión que esta instalada de *GuestAditions* con `modinfo vboxguest`.  
![img](./img/038.png)    

## Máquina Real.   
Creamos el directorio y ejecutamos `vagrant init` para crear el Vagrantfile.  
![img](./img/039.png)      

Ejecutamos `VBoxManage list vms` para averiguar el nombre de la máquina que acabamos de configurar.  
![img](./img/048.png)    

Una vez localizado, ejecutamos `vagrant package --base ubuntu_vagrant` para crear la caja o fichero *package.box*.  
![img](./img/049.png)    

Comprobamos que se ha generado la caja con `vagrant box list`.  
![img](./img/050.png)   

![img](./img/051.png)    

Cambios en *Vagrantfile* el nombre de la máquina por el actual *ubuntu_vagrant*.  
![img](./img/052.png)    

Finalmente, lanzamos `vagrant up` para ejecutar la máquina y la debería de haber conectado. En mi caso, me dio un problema con las claves de ssh que no logré solucionar (se repitió este último paso unas tres veces sin éxito).  
![img](./img/053.png)  
