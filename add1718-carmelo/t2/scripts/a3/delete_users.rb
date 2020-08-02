#! /usr/bin/ruby

if ARGV.size !=1
  puts "Revise que ha escrito el nombre del documento."
end

filename = ARGV[0]
user_list = `cat #{filename}`
username = user_list.split("\n")

username.each do |user|
  status = system("id #{user}")
  if status == true
    system("sudo userdel -r #{user} &> /dev/null")
    puts "User borrado."
  else
    puts "No existe #{user}."
  end
end
