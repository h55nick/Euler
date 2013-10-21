t = Time.now
inputs = {
  1382049600000 => Time.at(1382049600),
  1382049600 => Time.at(1382049600),
  t => t,
  's' => 's',
  'random text here' => 'random text here',
  344444444444 =>  344444444444,
  1 => 1
}


def format(input)
  if input.to_s.length == 13
    Time.at(input/1000)
  elsif input.to_s.length == 10
    Time.at(input)
  else
    input
  end
end


#Test
inputs.reject{|input,answer| format(input) == answer}.each{|k,v| puts "Error with input: #{k}::(#{k.class}) as it returns #{format(k)}::(#{format(k).class}) when it should return #{v}::(#{v.class})" }