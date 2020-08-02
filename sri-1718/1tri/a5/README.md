# DNS-UBUNTU.
## 1. Servidor.
### 1.1 Instalación y configuración.
Comenzamos instalando el servidor *DNS* de *bind9*.  
![img](./img/1.png)  

Nos dirigimos al fichero `/etc/resolv.conf` u asignamos la `IP 127.0.0.1` para redirigir el *DNS* a nuestra máquina.  
![img](./img/2.png)  

Luego, vamos a `/etc/bind/named.conf.options` y añadimos los reenviadores.  
![img](./img/3.png)  

Reiniciamos el servicio y comprobamos su funcionamiento tanto en el servidor como en el cliente.  
![img](./img/4.png)  

![img](./img/5.png)  

Ahora, creamos la zona directa e inversa en `/etc/bind/named.conf.local` de la siguiente manera.  
![img](./img/14.png)  

Configuramos la zona directa agregando a los posibles clientes.  
![img](./img/8.png)  

Configuramos la zona inversa agregando a los posibles clientes, en este caso, *isr-carmelo2.miempresa.com* y *imw.miempresa.com*.  
![img](./img/9.png)  

Aquí indica al servidor Linux que el DNS lo otorga él mismo
![img](./img/11.png)

## 2. Creación del servidor esclavo.  
### 2.1 Confiuración.

Clonamos la máquina servidor para que haga de esclavo.  

Empezamos indicando en el miempresa.db del esclavo, quien es el servidor maestro.  
![img](./img/13.png)

Y terminamos añadiendo el `also-notify` en el maestro para mantener los dns sincronizados.  
![img](./img/14.png)

## 3. Cliente.
### 3.1 Master.
Una vez en el cliente, asignamos el nuevo servidor *DNS* y comprobamos si funciona.  
![img](./img/053.png)  

Éxito.  
![img](./img/054.png)

### 3.2 Slave.  
Habiendo apagado la máquina, volvemos a comprobar si el *DNS* maestro está siendo respaldado.  

Éxito.   
 ![img](./img/055.png)
