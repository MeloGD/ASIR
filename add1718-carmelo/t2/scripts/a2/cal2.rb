#!/usr/bin/ruby

argument = ARGV[0]
content = `cat #{argument}`
lines = content.split("\n")

lines.each do |var|
  fields = var.split
    number1 = fields[0].to_i
    op = fields[1]
    number2 = fields[2].to_i

  if op == "+"
    sum = number1 + number2
    puts sum
  elsif op == "-"
    res = number1 - number2
    puts res
  elsif op == "x"
    mul = number1 * number2
    puts mul
  elsif op == "/"
    div = number1 / number2
    puts div
  else 
   puts "Indroduzca un operando por favor."
  end  
end

