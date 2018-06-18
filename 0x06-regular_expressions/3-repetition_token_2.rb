#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/h.*tn/)
  matches.each do |item|
    print item
  end
  puts
end
