#! /usr/bin/ruby

if ARGV.size !=1
	puts "Revise que ha escrito el nombre del documento."
	exit
end


filename = ARGV[0]
ficher = `cat #{filename}`
lines = ficher.split("\n")
check_root = `whoami`

if check_root == "root\n"
  lines.each do |u|
    user=u.split(":")
    if user[2] == ""
      puts "#{user[0]} no tiene email."
      next
    end
    if user[4] == "add" 
      if system("id #{user[0]} &> /dev/null") == true
        puts "EL usuario ya existe."
      else
      system("useradd -m #{user[0]} &> /dev/null")
      puts "Usuario #{user[0]} creado."
      end 
    elsif user[4] == "delete"
      if system("id #{user[0]} &> /dev/null") == true
        system("userdel -r #{user[0]} &> /dev/null")
        puts "Usuario #{user[0]} borrado."
      else
        puts "El usuario #{user[0]} no existe."
      end
    end              
  end
else
  puts "Necesita privilegios de superusuario."
  exit
end

