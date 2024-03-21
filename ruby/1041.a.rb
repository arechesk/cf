n=gets.to_i
s=gets.split.map(&:to_i)
puts s.max-s.min-n+1
