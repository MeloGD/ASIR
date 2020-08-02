# Triggers.
Creamos la base de datos *banco* y la tabla *cuentas*.  
![img](./img/0001.png)    

Creamos una variable local llamada *saldo* con el valor *0* y a continuación el trigger que irá acumulando en esta variable todos los sueldos de los diferentes números de cuentas (se ha ejecutado un insert como demostración).  
![img](./img/0002.png)  

Y como podemos comprobar, se ha acumulado correctamente.  
![img](./img/0003.png)    

En caso de que la variable local *saldo* se pueda actualizar en caso de borrado, tendremos que ejecutar el trigger de la siguiente manera (se ha ejeuctado un borrado como demostración).  
![img](./img/0004.png)  

Se ha actualizado, correctamente.  
![img](./img/0005.png)
