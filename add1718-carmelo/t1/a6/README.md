# SERVIDOR DE IMPRESIÓN  
![img](./img/0001.png)  

## Instalación en Windows Server 2012.  
Comenzamos la práctica en el **Administrador del Servidor** y seleccionamos **Agregar roles y características**.  
![img](./img/003.png)    

Le damos a siguiente hasta llegar a la parte de **Seleccionar roles del servidor** y marcamos **Servicios de impresión y documentos**.  
![img](./img/004.png)  

Agregamos la característica.  
![img](./img/005.png)   

Y comprobamos que se ha agregado.  
![img](./img/006.png)    

Aquí nos limitamos a darle a siguiente.  
![img](./img/007.png)    

Ahora, debemos asegurarnos de que en **Servicios de Rol**, tanto **Servidor de impresión** como **Impresión en Internet** deben estar activados.  
![img](./img/008.png)    

Ticamos la opción para reiniciar el servicio.  
![img](./img/009.png)    

Y comenzará el proceso de instalación. Al finzalizar, comprobaremos en esta ventana que todo se ha instalado correctamente.  
![img](./img/010.png)    

## PDF Creator.  
Una vez hecha la instalación del servidor de impresión, descargamos **PDF Creator**, quién acturará de "impresora virtual" en esta práctica.  
![img](./img/011.png)    

Una vez instalado, vamos a **Perfiles>Guardar** donde activaremos la opción de **guardado automático** y **seleccionamos la ruta** donde se guardarán dichos archivos.
![img](./img/012.png)    

Hecho esto, hacemos una simple comprobación imprimiendo un bloc de notas.  
![img](./img/013.png)    

Y comprobamos que se genera el documento PDF.  
![img](./img/014.png)    

## Compartir impresora de manera local.  
Abrimos **Dispositivos e Impresoras** desde el **Panel de Control** o desde el buscador del inicio. Aquí, encontraremos la impresora de **PDF Creator** (la cual debemos compartir con un cliente) y con el secundario, seleccionamos **Propiedades de impresora**.  
![img](./img/015.png)    

En la pestaña de compartir, marcamos **Compartir esta impresora**, **Presentar trabajos de impresion en equipos cliente** y definimos un **nombre** a dicha impresora, en este caso, *PDFcarmelo18*.  
![img](./img/016.png)    

Ahora, vamos a un cliente e introducimos la **ip del servidor en el explorador de archivos**. Si todo ha salido bien, se deberá ver algo así.
![img](./img/017.png)    

Secundario y seleccionamos **Conectar**.  
![img](./img/018.png)    

> Como pequeño parentesis a esta parte, debo comentar que en mi caso me topé con un error de lo más molesto donde la máquina cliente me mostraba este error, denegando todo intento posible de conexión.    
![img](./img/019.png)    
Otro error que me encontré fue relacionado con la importación de drivers en la máquina cliente, pero esto se debía a que el servidor que utilizaba era de 32 bits frente a un cliente de 64 bits.  
Finalmente, repetí esta práctica con un **Windows Server 2012** limpio (el que se estaba usando previamente era importado de otra práctica en el que se había instalado y configurado un **servidor IIS**, el cual también es necesario para el funcionamiento de este servidor de impresión) y un cliente W10 más adelante y este error desapareció, dando a pensar que esta posible configuración es la responsable del desecadenamiento de este error.  


Y si no tenemos ningún problema, instalaremos el controlador y se abrirá la **cola de impresión**.  
![img](./img/020.png)    

![img](./img/021.png)    

![img](./img/022.png)    

LLegados aquí, comprobamos haciendo una impresión **desde el cliente** de un bloc de notas.
![img](./img/023.png)    

Y comprobamos que en la máquina servidor se ha generado un pdf refente al bloc de notas del cliente.  
![img](./img/025.png)      

![img](./img/026.png)    

## Compartir impresora en red o remoto.     
Abrimos un navegador e introducimos `http://ip-servidor/printers` y pedirá un usuario-contraseña para acceder al servidor.  
![img](./img/027.png)      

![img](./img/028.png)    

Vamos propiedades y compiamos el **nombre de red**.
![img](./img/029.png)    

Ahora, vamos a **dispositivos e impresoras** y **agregamos una impresora**.  
![img](./img/030.png)    

Seleccionamos la segunda opción.  
![img](./img/031.png)      

Seleccionamos **La impresora desada no está lista**.  
![img](./img/032.png)    

Y pegamos el **nombre de red copiado previamente**.  
![img](./img/033.png)    

Pedirá un usuario-contraseña de accceso al servidor.  
![img](./img/034.png)    

Le damos a siguiente, filanizamos y comprobamos que se ha agregado correctamente.  
![img](./img/035.png)    

![img](./img/036.png)    

![img](./img/037.png)      

Para comprobar su funcionamiento, paramos la impresora desde el navegador.  
![img](./img/038.png)      

Hacemos una petición de impresión desde el **cliente** y volvemos a activar el servidor de impresión.
![img](./img/039.png)    

Finalmente, comprobamos que el archivo ha llegado correctamente.  
![img](./img/040.png)    

![img](./img/041.png)  
