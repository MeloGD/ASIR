```
* Práctica creada en el curso 201415
* Actualizada para el curso 201617
```

# iSCSI en Windows 2008 Server

Vamos a montar un iSCSI con Windows Server 2008 64 bits.

*(El siguiente texto está copiado de un enlace de Internet)*

```
Para los que no estén familiarizados con iSCSI, digamos que es una manera de “encapsular”
comandos SCSI en paquetes IP. De esta manera podemos acceder a sistemas de almacenamiento externos usando una red IP en lugar de los tradicionales buses SCSI o los canales de fibra. Es decir, una buena forma de montarnos una SAN.

La solución consta de al menos dos componentes. Un iSCSI Initiator y un Target.
* El initiator es lo que utilizamos en el equipo que va a aceder a esos volumenes,
* y el Target es lo que nos permitirá crear el sistema de almacenamiento compartido,
y el que permitira el acceso a las LUNs que se hayan creado a cada cliente específico.

Generalmente esta tecnología está ya incluida en el propio hardware de los servidores
y de los sistemas SAN, que ofrecen este tipo de conectividad a través de dispositivos multifunción.
Sin embargo esto no excluye que un iniciador software se pueda conectar a un Target hardware o viceversa.

El iSCSI initiator puede descargarse gratuitamente, para Windows XP y Windows server 2003. En Windows Vista y Windows Server 2008 viene ya incluido por defecto. Los iniciadores software son muy útiles en entornos virtualizados, ya que permiten a las máquinas virtuales el acceso a sistemas de tipo SAN mediante tarjetas de red, generalmente dedicadas en el host y en el guest.
```

---

# 1 Preparativos

Necesitamos 2 MV's con Windows Server (Consultar [configuraciones](../../global/configuracion/windows-server.md)).
* MV1: Esta MV actuará de `Initiator`.
    * Con dos interfaces de red.
    * Una en modo puente (172.19.XX.21)
    * la otra en red interna (192.168.XX.21) con nombre `san`.
        * Esta interfaz NO tiene gateway.
* MV2: Esta MV actuará de `Target`.
    * Necesitamos Windows Server 64 bits para poder instalar el software de Target.
    * Con un interfaz de red (192.168.XX.22) en modo red interna `san`.
    * Esta interfaz usa como gateway 192.168.XX.21.
    * Añadir un segundo disco de 800 MB a la MV de VirtualBox.
* Las IP's las pondremos todas estáticas.
* Las IP's de la red interna estarán en el rango 192.168.XX.NN/24.
Donde XX será el número correspondiente al puesto de cada alumno.

---

# 2 Enlaces de interés

* Vídeo de referencia [ES - Crear y conectar recursos iSCSI](https://youtu.be/_77UL2kZEEA).
* Cómo usar un TARGET hardware - [How to use iSCSI target on Windows 2008 server](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Virtualization/How_to_use_iSCSI_Targets_on_a_Windows_Server)
* INITIATOR - [Guía paso a paso del iniciador Windows](https://technet.microsoft.com/es-es/library/ee338476%28v=ws.10%29.aspx)

---

# 3. Iniciador iSCSI

* Poner como identificador iqn del iniciador lo siguiente: `iqn.2017-05.initiatorXXw`

---

# 4. Target iSCSI

* Vídeo de referencia [ES - Crear y conectar recursos iSCSI](https://youtu.be/_77UL2kZEEA).

## 4.1 Instalar el target

* Hay que descargar el software iSCSI Target para instalar en Windows Server 2008.
    * Descargar iSCSI Target 3.3 o superior desde la web de Microsoft.
    * Instalar el software.
    * `C:\iSCSI_target\x64\instalar_target.msi`
* Una vez instalado, vamos a herramientas administrativas -> iSCSI Target

## 4.2 Crear un destino

* Creamos un nuevo destino iSCSI con:
    * Nombre: "alumnoXXdisco01".
    * Descripción: "Nombre completo del alumno y la fecha de hoy"
* Identificador IQN para el target `iqn.2017-05.targetXXw:test`. Esta es la forma de identificar el equipo Initiador que tendrá
permitido el uso del almacenamiento que estamos creando.
    * Nombre IQN del iniciador o también en avanzado podremos poner la dirección IP del Iniciador.

> IMPORTANTE: El iniciador tiene 2 IP's, pero se comunica con el target usando
el interfaz de red de la red interna.

## 4.3 Crear un dispositivo

* Crear disco virtual para el destino iSCSI en `C:\nombre-alumnoXXdisco01.vhd` de tamaño 600 MB.
* Dispositivo -> Botón derecho -> Acceso disco -> Montar.
* Vamos a Administrador del Servidor -> Almacenamiento -> Disco1 (desconectado)
-> Nuevo volumen. Le asignamos letra (`E:`) y le damos formato.
* En este momento podemos guardar ficheros en la unidad `E:`
* Desconectamos el disco.
* Desmontamos el disco.

Ya tenemos el dispositivo de almacenamiento listo para usarlo desde el Iniciador.

* Crear otro destino iSCSI usando el segundo disco (800 MB) de la máquina target.
---

# 5. Configurar Iniciador

* Vídeo de referencia [ES - Crear y conectar recursos iSCSI](https://youtu.be/_77UL2kZEEA).
* Vamos al iniciador. El software Iniciador ya viene preinstalado.
Sólo hay que configurarlo para conectar con el target.
* Destino -> IP del target
* Vamos a `Administrador del Servidor -> Almacenamiento -> Administrador de Discos`
* Ponemos el disco en línea.

Ya tenemos el nuevo almacenamiento disponible en el Iniciador.

---

# 6. Comprobación final

* Desde el Iniciador, montar el nuevo almacenamiento (Letras de unidad `F`, `G`, etc.).
* Guardar ficheros en dichas unidades, de modo que la información que se guarde en ella
se almacenará en el Target remoto.
