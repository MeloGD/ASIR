# Servidor DHCP-Windows.
## 1 Intalación DHCP.
### 1.1 Instalación del servicio.
Según iniciamos el servidor nos aparecerá la ventana de administración del servidor. Nos dirigimos a la sección de agregar roles y características.  
![image](./img/001.png)  

Seleccionamos el servidor. En este caso solo disponemos de uno.
![image](./img/002.png)   

Agregamos el rol de DHCP.
![image](./img/003.png)  

Aquí no necesitaríamos hacer nada, dejando las opciones por defecto.   
![image](./img/004.png)  

Comenzamos la instalación del servicio DHCP.   
![image](./img/005.png)  

![image](./img/006.png)  

### 1.2 Configuración DHCP y creación de ámbitos.
Una vez finalizado, desplegamos la pestaña de herramientas y selecionamos DHCP.    
![image](./img/007.png)    

Nos dirigimos a la barra lateral de la izquierda, secundario del ratón y seleccionamos ámbito nuevo.
![image](./img/008.png)  

Seleccionamos un rango IP para el primer *pool* DHCP.  
![image](./img/009.png)  

Agregamos una exclusión.  
![image](./img/010.png)  

Aquí podremos fijar cuanto tiempo va a tardar la tabla *ARP* en reiniciarse. Si a una dirección MAC se le ha dado cierta IP, se le intentará volver a dar la misma.   
![image](./img/011.png)  

Finalizamos y tendremos el ámbito configurado.  
![image](./img/012.png)  

Le asignamos una IP al servidor en la misma red que el *pool* que hemos configurado. Esto no sería necesario en un escenario real ya que se estaría utilizando un router. En esta práctica se están utilizando adaptadores de red en modo "Red Interna" para no descontrolar la red del centro.  
![image](./img/013.png)  

IP del servidor.  
![image](./img/014.png)

IP de la máquina cliente recibida vía DHCP.  
![image](./img/015.png)  

Creamos un nuevo ámbito para comprobar que se hacen los respectivos cambios de *pool* y configuración.
Esta parte ha resultado ser de lo más frustrante. Si desactivamos el 1º ámbito, es muy complicado que haga el cambio
por si mismo, teniendo muchas veces que reiniciar el servidor o incluso borrar el 1º ámbito para que consiga la nueva configuración.
La cosa cambia si estamos en el 2º ámbito, el cual si desactivamos cambiará al primer ámbito sin ningún problema. Supongo que será un error de software al estar usando máquinas virtuales o que no se está utilizando un router.  
![image](./img/023.png)  

Servidor:    
![image](./img/024.png)  

Cliente:    
![image](./img/025.png)  

En este paso se fusionarán los dos ámbitos para crear lo que se conoce como un superámbito. Con esto se puede ahorrar mucho tiempo a la hora de realizar configuraciones nuevas, dado que se pueden configurar varios ámbitos simples al mismo tiempo.  
![image](./img/016.png)  

![image](./img/017.png)    

![image](./img/018.png)  

Lo desactivamos para comprobar que se deja de enviar información a el cliente.  
![image](./img/019.png)

Y funciona.  
![image](./img/020.png)
### 1.3 Reserva.
Por último, con esta opción podremos especificar al servidor IP que una MAC concreta tenga preferencia a la hora de obtener una IP. Lo podremos configurar si desplegamos el servidor y vamos al fichero de "Reserva".
![image](./img/021.png)  

Y efectivamente, el cliente se ha saltado la ip *172.18.18.4*    (que sería la priemera IP del *pool* )  y ha recibido la IP configurada.
![image](./img/022.png)  
