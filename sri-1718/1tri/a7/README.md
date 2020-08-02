# Servidor Web Avanzando - Parte I.  
![img](./img/IIS_logo.png)  

(parte II más abajo)
## Proceso y configuración de SSL.
- Comenzamos la práctica creando el los directorios *miEmpresa* y *principal* en `c:\miEmpresa\principal`.  
![img](./img/001.png)  

- Agregamos una zona de búsqueda directa nueva llamada *miEmpresa.com* y agregamos un campo *A* haciendo referencia a la IP *172.18.18.10*.  
![img](./img/002.png)    

 ![img](./img/003.png)   

- Creamos una página Web en el administrador de *IIS*.  
![img](./img/004.png)    

  Y comprobamos (se activó el examen de directorios por error, no hace falta ).
 ![img](./img/006.png)   

- Agregamos al grupo todos dentro de los grupos permitidos, de lo contrario no podremos ver la págiga en el buscador (error de permisos).  
![img](./img/007.png)    

## Creamos el subdominio *pagos*.
- Ahora, creamos un subdominio llamado pagos.
![img](./img/008.png)    

- Cremaos una página web en *IIS* y comprobamos su funcionamiento.  
![img](./img/010.png)    

  ![img](./img/009.png)  

## Agregamos el certificado al subdominio *pagos*.
- Desde IIS, nos dirigimos a certificados del servidor.  
![img](./img/011.png)    

- Seleccionamos *Crear certificado autofirmado*.  
![img](./img/012.png)  

- Modificar enlances.  
![img](./img/014.png)   

- Y rellenamos los campos como se muestran a continuación.  
![img](./img/015.png)   

  ![img](./img/013.png)  

- Quedando algo así (se ha eliminado el http por el puerto 80).  
![img](./img/016.png)    

- Y comrpobamos en el navegador.  
![img](./img/017.png)    


## Creamos el subdominio *tienda*.
- Agregamos un subdomino con un campo *A* en el DNS.  
![img](./img/018.png)   

- Agregamos una página en IIS y la vinculamos al previamente creado subdominio.  
![img](./img/019.png)   

## Agregamos el certificado al subdominio *tienda*.    
- Una vez hecho esto, procedemos a la instalación de *OpenSSL*.  
![img](./img/021.png)   

- Volvemos a los certificados del sevidor y seleccionamos *Crear una solicitud de certificado*.
![img](./img/022.png)    

- Rellenamos los campos de la siguiente maneras y le damos a siguiente.  
![img](./img/023.png)   

- Colocamos estos campos.  
![img](./img/024.png)    

- Y seleccionamos una ruta para exportarlo.  
![img](./img/025.png)    

- Comprobamos su contenido en un bloc de notas.  
![img](./img/026.png)    

- Copiamos este certiciado y lo depositamos en `C:\OpenSSL\bin`.  
![img](./img/027.png)   

- Hecho esto, ejecutamos *OpenSSL.exe* y se abrirá una consola en la cual introduciremos
`genrsa -des3 -out cakey.pem 2048` que generará una clave privada.  
 ![img](./img/028.png)    

- Generamos el certificado digital con `req -new -x509 -key cakey.pem -out cacert.pem -days 365`, rellenando los campos pertinentes.  
![img](./img/029.png)   

- Y creamos el certificado digital para el servidor de IIS con `openssl x509 -req -days 365 -in certreq.txt -CA cacert.pem -CAkey cakey.pem -CAcreateserial -out iis.crt`.  
![img](./img/030.png)   

- Comprobamos que se han generado los archivos especificados.
![img](./img/031.png)    

- Volvemos al administrador de IIS y en certificados del servidor, seleccionamos *Completar solicitud de certificado*.  
![img](./img/032.png)   

- Seleccionamos la ruta en la que se encuentra el certifcado digital generado previamente.  
![img](./img/033.png)   

- Volvemos al subdomino *tienda* y en *Enlances* seleccionamos el certificado ya cargado en el servidor IIS.  
![img](./img/034.png)   

  ![img](./img/035.png)    

- Llegados aquí, toda la configuración ha sido realizada y lo comprobamos de diversas maneras:  
- SSL en servidor.  
![img](./img/036.png)    

- Sin SSL en servidor.  
![img](./img/037.png)   

- SSL en cliente.
![img](./img/038.png)    

- Sin SSL en cliente.  
![img](./img/039.png)    

# Servidor Web Avanzando - Parte II.     
- Creamos un nuevo subdominio.  
![img](./img/iis_parte_2/001.png)     

- Agregamos un nuevo sitio web al servidor de IIS.   
![img](./img/iis_parte_2/002.png)     

- Vamos al directorio y creamos los archivos e index necesarios. Aquí un ejemplo con *empleado2*.  
![img](./img/iis_parte_2/004.png)     

- Volvemos al servidor de IIS y activamos el *examen de direcotiros* y en *autenticación* nos aseguramos que la configuraciguración sea como se muestra en las capturas.  
![img](./img/iis_parte_2/005.png)     

- En cada carpeta.  
![img](./img/iis_parte_2/015.png)     

- En la página web general.  
![img](./img/iis_parte_2/016.png)     

- Y en el servidor.  
![img](./img/iis_parte_2/017.png)  

- Ahora agregamos a los usuarios empleado1, empleado2, empleado3 en Usuarios y equipos de *Active Directory*.     
![img](./img/iis_parte_2/007.png)    

- Y al grupo common.  
![img](./img/iis_parte_2/008.png)   

- Una vez hecho esto, desabilitamos la herencia en todas las carpetas implicadas en la práctica y les asignamos sus respectivos propietarios.  
![img](./img/iis_parte_2/009.png)     

  ![img](./img/iis_parte_2/010.png)     

  ![img](./img/iis_parte_2/011.png)     

  ![img](./img/iis_parte_2/012.png)    

  ![img](./img/iis_parte_2/013.png)     

- Para finalizar, comprobamos que nos pida la contraseña de cada usuario en sus respectivos directorios.  
  ![img](./img/iis_parte_2/014.png)   

  ![img](./img/iis_parte_2/018.png)    

  ![img](./img/iis_parte_2/019.png)    
- Una vez entrado con un usuario dentro de *common*, no hará falta introducir una nueva contraseña.    
![img](./img/iis_parte_2/020.png)    

  ![img](./img/iis_parte_2/021.png)    

  ![img](./img/iis_parte_2/022.png)    

  ![img](./img/iis_parte_2/023.png)    

  ![img](./img/iis_parte_2/024.png)        

Nota: - Revisar el archivo *web-config* en caso de fallo, suele dar problemas de permisos. Una vez modificado, se tomará cierto tiempo.
