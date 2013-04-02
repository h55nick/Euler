def pali?(num)
 num.to_s != num.to_s.reverse ? false : true
end
n = 0
for i in (100..999).to_a.reverse
  for j in (100..999).to_a.reverse
    num = i * j
    n =  num if pali?(num) && num > n
  end
end
puts n