# Usuarios Y privilegios MYSQL.
1. Ejecuta MySQL Workbench y activar la base de datos 'Jardinería'. En caso de que no dispongas de ella, puedes generarla con el script SQL que hay en el moodle. Abrir una nueva ventana de consulta y realizar las siguientes acciones mediante órdenes SQL.  

2. Crear un usuario llamado “alumno” que tenga acceso a las tablas CLIENTES, EMPLEADOS, PRODUCTOS desde cualquier lugar.  

3. Crear un usuario llamado “profesor” que tenga permiso de lectura a toda la base de datos desde localhost.  

4. Comprueba la creación y las características de estos nuevos usuarios consultando la tabla mysql.user.  

5. Establecer nuevas conexiones a la instancia de BD con los usuarios 'alumno' y 'profesor' y comprobar sus niveles de acceso respectivo sobre las diferentes tablas de la BD 'jardineria'.   

6. Modifica la contraseña de 'alumno'. Comprobar la conexión con la nueva contraseña.  

7. Modifica el host desde donde pueda acceder el alumno a una dirección IP determinada (del propio servidor o un cliente). Soluciona los problemas que pueda presentar esta modificación.  

8. Comprueba que el usuario alumno puede conectar sólo desde la máquina con la IP asignada.  

9. Vuelve a la ventana de root y concede derechos de consulta al usuario alumno sobre la tabla PEDIDOS. Comprueba, mediante una nueva conexión del usuario 'alumno' que tiene este nuevo acceso.  

10. Crear un usuario llamado “profesor_cli” con los privilegios de 'profesor' y, también, los privilegios de inserción y borrado en la tabla CLIENTES.  

11. Conecta como 'profesor_cli' y comprueba sus privilegios sobre las diferentes tablas de 'jardineria'.  

12. Crear un usuario llamado “administrador” que tenga todos los privilegios a todas las bases de datos de nuestro servidor mysql. Este administrador no tendrá la posibilidad de dar privilegios.  

13. Crear un usuario llamado “superadmin” con los privilegios anteriores y con posibilidad de conceder privilegios a otros usuarios.  

14. Quitar los privilegios al usuario “profesor_cli” para actualizar la tabla CLIENTES.  

15. Eliminar todos los privilegios al usuario 'profesor'.  

16. Actualizar los privilegios.  

17. Muestra los privilegios de usuario 'profesor'.  

18. Consulta todos los usuarios existentes.  
