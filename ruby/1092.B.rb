n=gets.to_i
s=gets.split.map(&:to_i).sort!
d=[]
(1..(s.size)/2).each do |i|
    d<<(s[2*i-2]-s[2*i-1]).abs
end
puts d.sum
