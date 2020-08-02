#!/usr/bin/ruby
##Tabla del 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

puts "La tabla del 7:"  

numbers.each do |number|
  count = 7 * number 
  puts "7 x #{number} = #{count}"
end
