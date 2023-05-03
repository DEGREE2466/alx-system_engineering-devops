#!/usr/bin/env ruby

# Use the Oniguruma library for regular expressions
require 'oniguruma'

# Get the argument passed to the script
argument = ARGV[0]

# Define a regular expression pattern to match against the argument
pattern = Oniguruma::ORegexp.new('hello', options: Oniguruma::OPTION_IGNORECASE)

# Use the regular expression to match against the argument
if pattern.match(argument)
  puts "Argument matches pattern!"
else
  puts "Argument does not match pattern."
end
