#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/^\d{10}/)
  matches.each do |item|
    print item
  end
  puts
end
