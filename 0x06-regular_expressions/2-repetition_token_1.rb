#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/h.t*n/)
  matches.each do |item|
    print item
  end
  puts
end
