#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/hbt{2,5}n/)
  matches.each do |item|
    print item
  end
  puts
end
