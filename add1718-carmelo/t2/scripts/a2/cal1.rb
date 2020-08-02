#!/usr/bin/ruby
##Tabla del 7

number1 = ARGV[0].to_i
op = ARGV[1]
number2 = ARGV[2].to_i

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


