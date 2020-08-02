<?php
$salario = (float)$_POST["salario"]; 
$edad = (int)$_POST["edad"];
$nombre = $_POST["nombre"];
$apellido = $_POST["apellido"];

if ($salario > 2000) {
	echo "El salario no sufrirá ningun cambio.";
}

elseif ($salario > 1000 and $salario < 2000) {
	if ($edad > 45) {
		$salario = $salario + ($salario * 0.03);
	}
	elseif ($edad < 45) {
		$salario = $salario + ($salario * 0.10);
	}
}	
elseif ($salario < 1000) {
	if ($edad < 30) {
		$salario = 1100;
	}
	elseif ($edad > 30 and $edad < 45) {
		$salario = $salario + ($salario * 0.03); 
	}
	elseif ($edad > 45) {
		$salario = $salario + ($salario * 0.15);
	}
}
echo("$nombre $apellido recibirá $salario euros.");
?>