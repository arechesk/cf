t = gets.to_i
t.times do
  n = gets.chomp
  puts n.to_i - 10 ** (n.length - 1)
end
