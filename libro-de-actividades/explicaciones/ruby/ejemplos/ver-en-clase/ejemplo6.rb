#!/usr/bin/ruby

resultado = `cat carpetas.txt`

asignaturas = resultado.split("\n")

puts asignaturas

system("mkdir curso1516")

asignaturas.each do |nombre|
  system("mkdir curso1516/#{nombre}")
end

puts "Creadas las carpetas"
