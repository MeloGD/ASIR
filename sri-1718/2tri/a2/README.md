# SMTP
![img](./img/000.jpg)    

## 1. Instalación del servidor SMTP.  
Como siempre, acudimos al *Asistente para agregar roles y características* para instalar nuestro servidor *SMTP*.  
![img](./img/001.png)    

Encontraremos el servicio dentro del *Servidor web (IIS)*.  
![img](./img/002.png)    

Ticamos *Servidor SMTP*.
![img](./img/004.png)    

Verificamos que se instala lo previamente especificado.  
![img](./img/003.png)    

Le damos a instalar y el proceso quedaría finalizado.  
![img](./img/005.png)    

## 2. Configuración.  
Desplegamos el menú de herramientas y seleccionamos *Administrador de Internet Information Services (IIS) 6.0*.  
![img](./img/006.png)    

Una vez dentro, desplegamos el menú de *SMTP* y seleccionamos *Propiedades* para comenzar la configuración.  
![img](./img/007.png)    

Dejamos la configuración como se muestran en las capturas.  
![img](./img/008.png)    

![img](./img/009.png)    

![img](./img/010.png)   

![img](./img/011.png)    

![img](./img/012.png)    

Y en autenticación espeficiamos *Acceso anónimo* para que cualquiera pueada hacer uso del servidor.  
![img](./img/013.png)    

En el DNS, añadimos un campo *CNAME*.  
![img](./img/014.png)    

Y desde el *Administrador de Internet IIS 6.0* agregamos otro alias *email*.
![img](./img/015.png)    

![img](./img/016.png)    

Como información adicional, mostramos la ruta donde se almacenarían los emails.  
![img](./img/017.png)   


## 3. Cliente.  
### 3.1 Anónimo.
En el cliente se ha decidido utilizar *Opera Mail*.  
![img](./img/021.png)    

Una vez dentro, accedemos a *Administrar Cuentas* y revisamos que todas las pestañas tengan la siguiente configuración.  
![img](./img/022.png)    

![img](./img/023.png)    

![img](./img/024.png)    

![img](./img/025.png)    

Llegados aquí, mandamos un correo y comprobamos (En mi caso si se enviaban los correos pero no se quedaban almacenados en el servidor. Fueron necesarias varias pruebas).
![img](./img/026.png)    

![img](./img/027.png)    

### 3.2 Privado.  
Esta vez, volvemos al meno de autenticación.  
![img](./img/010.png)     

Desmarcamos el acceso anónimo y seleccionamos *Autenticación Básica*, lo cual nos pedirá un usuario del dominio para poder hacer uso del servico.  
![img](./img/028.png)    

Ticamos el cifrado TLS.  
![img](./img/029.png)    

Y regresamos al cliente, donde deberemos añadir una cuenta nueva con la configuración mostrada en las capturas.   
   ![img](./img/035.png)   

![img](./img/036.png)    

![img](./img/037.png)      

![img](./img/038.png)    

(Hemos usado el usuario *email* del *Active Directory*.)  
![img](./img/039.png)   

Hecho esto, probamos a mandar un nuevo correo.  
![img](./img/033.png)      

Y como se podrá comprobar, se ha enviado.
![img](./img/034.png)  

---
# hMailServer.    
![img](./img_2/000.png)    

## 1. Instalación.  
Antes de comenzar la instalación de *hMailServer* debemos de desinstalar el *Servidor SMTP* en el *Asistente para quitar roles y características*.  
![img](./img_2/001.png)      

Instalamos *NET Framework 3.5* dado que es necesario para el funcionamiento del nuevo servidor.  
![img](./img_2/005.png)

Hecho esto, procedemos a descargar *hMailServer* desde https://www.hmailserver.com/download e instalamos.  
![img](./img_2/003.png)    

Dejamos esta opción por defecto.  
![img](./img_2/004.png)    

Y ya podríamos ejecutarlo.  
![img](./img_2/006.png)    

![img](./img_2/007.png)    

## 2. Configuración.  
Creamos los dos dominios requeridos para la práctica.  
![img](./img_2/008.png)      

Configuramos la carpeta para las copias de seguridad.  
![img](./img_2/009.png)      

Creamos los dominos en el DNS, con los campos *A*, *CNAME* y *MX*.  
![img](./img_2/013.png)    

![img](./img_2/014.png)    

Testeamos ambos dominios.  
![img](./img_2/010.png)     

![img](./img_2/011.png)     

Creamos un par de usuarios, que serán *prueba1*, *prueba2*, *prueba3* con diferentes opciones entre ellos para probarlos en el cliente.  
![img](./img_2/012.png)    

Por último en el servidor abrimos estos puertos en el firewall (fue necesario en mi caso).  
![img](./img_2/015.png)    

### 2.1 Cliente.  
Finalmente, configuramos *OperaMail* con las nuevas cuentas. A continuación se muestran las configuraciones.  
![img](./img_2/016.png)   

![img](./img_2/017.png)    

![img](./img_2/018.png)    

![img](./img_2/019.png)  

![img](./img_2/020.png)    

Enviamos un correo simple.  
![img](./img_2/021.png)  

Y uno colectivo enviado a *empleados@asir.edu* que lo recibirán tanto *prueba3* como *prueba1*.  
![img](./img_2/022.png)  
