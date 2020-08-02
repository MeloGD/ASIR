<html>
  <head>
    <title>Formulario</title>
  </head>
  <body>
    <form action="ejercicio4.php" method="post">
      <label for="filas">Filas:</label>
      <input type="text" name="filas"/><br>

      <label for="columnas">Columnas:</label>
      <input type="text" name="columnas"/><br>

      <input type="submit" value="Enviar"/>
    </form>
    <table border="1">

      <?php
      if (isset($_POST["filas"]) and isset($_POST["columnas"])) {
        $filas = (float)$_POST["filas"];
        $columnas = (float)$_POST["columnas"];
        $nc = 1;
        $nf = 1;
        if ($filas >= 1 and $columnas >= 1) {
          echo("<p>Tablas y columnas:</p>");
          while ($nf<=$filas) {
            $nf++;
            echo("<tr>");
            while ($nc<=$columnas) {
              $nc++;
              echo("<td>Algo</td>");
            }
            $nc = 1;
            echo("</tr>");
          }
        }
        else{
          echo("Error");
        }
      }
      ?>

    </table>
  </body>
</html>
