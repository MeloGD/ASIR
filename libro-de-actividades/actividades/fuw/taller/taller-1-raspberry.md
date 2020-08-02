# Raspberry PI

## Material

El profesor entregará el siguiente material al alumno:

* Placa Raspberry PI
* Carcasa
* Fuente de alimentación
* Memoria SD
* Adaptador SD-USB
* Cable HDMI

## Taller

El alumno en casa debe hacer lo siguiente:

* Consultar la web de Raspberry PI.
* Instalar el sistema operativo en la memoria SD.
* Conectar Rb a la Tele HDMI, teclado y ratón USB.
* Entrar al sistema y activar el modo gráfico.
* Asegurarse de tener funcionando correctamente el servicio SSH.
* Crear usuario profesor con clave/profesor
* Poner clave profesor al usuario root
* Poner clave profesor al usuario pi
* Apuntar las MACs de los interfaces de red en una etiqueta que se pegará a la carcasa de la Rb.
* Cambiar `/etc/hostname` y poner `rbpiXX`.

---

# ANEXO

Cuando trabajamos desde remoto con la RbPI, vamos a necesitar conocer su IP.
* Podemos definir una IP estática de la forma `172.19.109.RR`, donde RR es el
número qeu identifica la RbPI.
* O también podemos usar los siguientes comandos para localizar la IP del dispositivo
conociendo la MAC.
    * Ejecutar `arp`, si no aparece la MAC que buscamos en la lista, tenemos que
    hacer un barrido.
    * `nmap -Pn 172.19.99.0-254`, escaneo de las máquina desde IP 172.19.109.0 hasta la 172.19.109.254.
    * `arp`
    * `arg | grep MAC-DEL-DISPOSITIVO`

Otra forma de hacer un barrido de IP's:

```
#!/bin/bash
for A in `seq 0 254`
do
  IP="172.19.109.$A"
  echo "Ping a $IP"
  ping $IP -c 1
done
```
