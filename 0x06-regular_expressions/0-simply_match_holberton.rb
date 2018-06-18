#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/Holberton/)
  matches.each do |item|
    print item
  end
  puts
end
