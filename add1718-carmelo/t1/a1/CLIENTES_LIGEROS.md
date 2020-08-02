# Clientes Ligeros / LTSP  
___
## 1. Preparación de máquinas.
### 1.1 Tarjetas de red.
Preparación de los adaptadores de red en Virtual Box, tanto como en servidor:

![image](./images/clientes_ligeros/001.png)

![image](./images/clientes_ligeros/002.png)

Como en el cliente:

![image](./images/clientes_ligeros/024.png)

  >Tener en cuenta que el servidor LTSP deberá tener la suficiente RAM para aguantar el  
   número necesario de clientes.  
   *Fórmula orientativa: 1500 + (30 x N_FAT_CLIENTS)  + (300 xN_THIN_CLIENTS)*

### 1.2 Configuración del SO.

> ip a   

![image](./images/clientes_ligeros/004a.png)

> route -n  

![image](./images/clientes_ligeros/005a.png)

> hostname, hosthame -a, hostname -f, uname   

![image](./images/clientes_ligeros/011a.png)

> blkid

![image](./images/clientes_ligeros/011b.png)  

### 1.3 SSH.

Comprobamos si SSH está instalado con con *dpkg -l ssh*.
![image](./images/clientes_ligeros/012b.png)
Por lo tanto, habrá que instalarlo con *apt-get install ssh*.

Creamos los usuarios que se usaran en los clientes LTSP.
![image](./images/clientes_ligeros/013b.png)

Modificamos el archivo de configuración para permitir el acceso *root*.
![image](./images/clientes_ligeros/015a.png)

Y su comprobación con SSH.  
![image](./images/clientes_ligeros/014.png)

___
## 2. LTSP.  
### 2.1 Instalación.  
Instalamos el servicio.
>apt-get install ltsp-server-standalone

![images](./images/clientes_ligeros/017a.png)

Y generamos una imagen del sistema mediante.
>ltsp-build-cliente (para 64bits)  
>ltsp-build-cliente i386 (para 32bits)

![images](./images/clientes_ligeros/018a.png)  

Con VB suele dar un error con las imágenes de 64bits (que veremos más adelante), por lo que me vi forzado a repetir la imagen, pero en su versión de 32bits. AL parecer el problema tiene que ver con la memoria de video virtual que proporciona VB.

Proceso de creación de la ISO.  

![images](./images/clientes_ligeros/019a.png)

### 2.2 Comprobaciones.

>ltsp-info  

![images](./images/clientes_ligeros/020a.png)

En */etc/ltsp/dhcpd.conf* modicamos el rango IP para el DHCP, que en mi caso sería *range 192.168.67.118 192.168.67.218*

Apagamos y reiniciamos el servicio (con un simple *reload* habría bastado).  
![images](./images/clientes_ligeros/021a.png)  

![images](./images/clientes_ligeros/022a.png)

## 3. Cliente.
Arrancamos la máquina desde la red por primera vez y ocurre lo siguiente:  
1º. Me enlaza el cliente con el host pero no carga bien la imagen de 64 bits.  
2º. Genero una imagen de 32 bits que da lugar a un bug gráfico.
![images](./images/clientes_ligeros/023.png)
En mi caso se solucionó aumentando la *vram* de VB y habilitando la aceleración 3D/2D.

Una vez dentro, comprobamos:
>ip a  

![images](./images/clientes_ligeros/025.png)  
> whoami, who, arp, netstat -ntap   

![images](./images/clientes_ligeros/026.png)
