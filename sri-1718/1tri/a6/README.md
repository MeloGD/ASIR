# Servidor IIS Windows.
## PDF1.  
Desde agregar roles y características, seguimos el proceso siguiente.  
![img](./img/001.png)  

![img](./img/002.png)  

![img](./img/003.png)  

![img](./img/004.png)  

![img](./img/005.png)  

![img](./img/006.png)  

Y comprobamos que se ve la página por defecto desde el servidor.  
![img](./img/007.png)  

Y el cliente.  
![img](./img/008.png)  

Ahora, nos dirigimos al gestor de DNS y cremaos una zona directa nueva, con un nuevo host y un nuevo alias.  
![img](./img/009.png)  

Volvemos a comprobar servidor.  
![img](./img/010.png)  

Y cliente.  
![img](./img/011.png)  

Ahora, creamos un `index.html` para comprobar que se carga una nueva configuración.  
![img](./img/012.png)  

Volvemos al gestor de DNS y agregamos un *CNAME*.  
![img](./img/013.png)

Y comprobamos su funcionamiento en cliente y servidor.  
![img](./img/014.png)  


Por último, creamos una carpeta en el directorio por defecto y comprobamos si funciona desde cliente y servidor.  
![img](./img/016.png)  

![img](./img/015.png)      

![img](./img/017.png)  

## PDF2.  
Creamos una nueva zona directa, con nuevos *hosts* y *CNAME*.  
![img](./img/018.png)  

Y agregamos un subdominio con un host.
![img](./img/019.png)  

Creamos las páginas necesarias en el gestor de IIS enlanzandolo con el domino ya creado en el DNS, de lo contrario, será como no hacer nada.  
![img](./img/020.png)  

Creamos un par de ficheros para la comprobación.  
![img](./img/021.png)  

![img](./img/022.png)  

Y chequeamos.   
![img](./img/036.png)     

![img](./img/037.png)   

## PDF3.  
Agregamos un entorno virtual a la página web principal de la siguiente manera (por problemas, se cambio el alias a "prueba" en el segundo intento).   
![img](./img/023.png)  

![img](./img/042.png)

Habilitamos el *Examen de directorios* y comprobamos que se han cargado los directorios con sus respectivos index.     
 
![img](./img/038.png)   

![img](./img/040.png)    

Si da problemas, debemos agregar a *Todos* en los permisos del  fichero *web.config* de la siguiente manera.  
![img](./img/041.png)    


Y volvemos a comprobar su funcionamiento en el navegador.    
![img](./img/039.png)

![img](./img/026.png)  

![img](./img/027.png)  

![img](./img/028.png)
