# LDAP    

![img](./img/inicio.jpg)    

## 1. Servidor.  
### 1.1 Configuración.
Establecemos las nuevas relaciones especificadas en la actividad en los ficheros `/etc/hosts` y en `/etc/hostname`.  
![img](./img/001.png)    

![img](./img/002.png)    

Instalamos el paquete `yast2-auth-server`.  
![img](./img/003.png)   

Desde *yast* entramos a "Servicios de red > Servicios de autenticación" e iniciaremos la configuración de *LDAP*. La configuración a seguir se muestra en las capturas siguientes.  
![img](./img/004.png)    

![img](./img/005.png)    

![img](./img/006.png)    

![img](./img/007.png)    

![img](./img/008.png)    

![img](./img/009.png)    

Revisamos que la configuración se ha realizado como era deseada.  
![img](./img/010.png)    

Comprobaciones:  
- slaptest -f /etc/openldap/slapd.conf para comprobar la sintaxis del fichero de configuración.   
![img](./img/011.png)   

- systemctl status slapd, para comprobar el estado del servicio.  
![img](./img/012.png)

- systemctl enable slapd, para activar el servicio automáticamente al reiniciar la máquina.  
![img](./img/013.png)

- nmap -Pn localhost | grep -P '389|636', para comprobar que el servidor LDAP es accesible desde la red.  
![img](./img/014.png)  

- slapcat para comprobar que la base de datos está bien configurada.  
![img](./img/015.png)  

- Instalamos la herramienta *GQ* y la lanzamos para poder realizar la siguiente comprobación.  
![img](./img/016.png)   

  (lanzamos el servicio con el atributo *&* para que sea independiente de la consola)  
  ![img](./img/017.png)   


- Comprobamos que tenemos creadas las unidades organizativas con *GQ*: groups y people.  
![img](./img/018.png)

## 1.2 Creación de usuarios y grupos.
Cambiamos el filtro en las pestañas (en cada pestaña) a *Usuarios LDAP* y agregamos el grupo *bucaneros* con los usuiarios *bucanero1* y *bucanero2*.
![img](./img/019.png)     

Nos pedirá la contraseña del servidor LDAP para hacer el cambio de filtro.  
![img](./img/020.png)   

Aquí estaría el grupo.  
![img](./img/021.png)     

Y aquí los usuarios.  
![img](./img/022.png)    

Volvemos a comprobar en la herramienta previamente instalada *Qp*.  
![img](./img/023.png)     

## 2. Cliente.  
### 2.1 Configuración.
Establecemos las nuevas relaciones especificadas en la actividad en los ficheros `/etc/hosts` y en `/etc/hostname`.  
![img](./img/024.png)       

![img](./img/025.png)       

Instalamos el paquete *yast2-auth-client*.  
![img](./img/026.png)      

Y desde "Yast > LDAP y cliente Kerberos" configuramos la conexión.
![img](./img/027.png)     

Quedando algo así.  
![img](./img/028.png)     

Finalmente problamos la conexión y nos mostrará el siguiente mensaje.  
![img](./img/029.png)     

### 2.2 Comprobaciones.
-`getent passwd bucanero1`  
![img](./img/030.png)     

-`getent group bucaneros`  
 ![img](./img/031.png)  

-`id bucanero1`    
![img](./img/032.png)

-`finger bucanero1`   
![img](./img/033.png)  

-`cat /etc/passwd | grep buncaneros`    
-`cat /etc/group | grep bucanero1`  
![img](./img/034.png)     

-`su pirata21`  
![img](./img/035.png)     

## Anexo: Última comprobación y problema.
Surgió un problema a la hora de reinciar la máquina para realizar la última comprobación dado que esta se quedo congelada en la pantalla de carga del sistema, mostrando múltiples errores.
Se encontró la siguiente solución:
- Usar un CD Live con Knoppix.
- Montamos la unidad afectada haciendo uso del comando *mount*.
- No dirigimos al fichero `/etc/nsswitch.conf` y revisamos que la configuración debe estar como en la captura proporcionada por Kevin.  
![img](./img/036.png)    

- Salimos de Knoppix y reiniciamos la máquina. Si todo ha salido bien, la máquina iniciará como siempre.  

Todavía no se conoce la razón exacta por lo que esto ha ocurrido, pero se baraja la hipótesis de que la manera en la que se cierra Yast afecta la actualización de este archivo, dado que a algunos les había funcionado y a otros no.
