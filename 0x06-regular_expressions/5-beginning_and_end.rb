#!/usr/bin/ruby
ARGV.each do |a|
  matches = a.scan(/^h.n$/)
  matches.each do |item|
    print item
  end
  puts
end