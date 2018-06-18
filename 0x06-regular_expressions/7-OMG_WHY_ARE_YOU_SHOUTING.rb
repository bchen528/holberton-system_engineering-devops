#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/[A-Z]/)
  matches.each do |item|
    print item
  end
  puts
end
