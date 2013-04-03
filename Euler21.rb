def dex(n)
  (1..n.to_i).to_a.map!{|a| (n%a == 0) ? a : 0}.inject(&:+).to_i - n
end#sqrt to optimize a bit more.

s = []
(100..10000).to_a.each do |a|
  b = dex(a) #follow logic wpw
  if (dex(b) == a && dex(a) ==b &&  a != b)
    s << a
  end
end
puts s.inject(&:+)