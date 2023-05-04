#!/usr/bin/env ruby

message = ARGV[0]
from_match = message.match(/from:(\+?\w+)/)
to_match = message.match(/to:(\+?\w+)/)
flags_match = message.match(/flags:([-:0-9]+)/)

from = from_match ? from_match[1] : ''
to = to_match ? to_match[1] : ''
flags = flags_match ? flags_match[1] : ''

puts "#{from},#{to},#{flags}"
