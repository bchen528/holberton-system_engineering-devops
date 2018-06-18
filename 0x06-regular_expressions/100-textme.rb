#!/usr/bin/ruby
ARGV.each do |a|
  match_from = a.scan(/from:(.\w+)/)
  match_to = a.scan(/to:(.\w+)/)
  match_flags = a.scan(/flags:(\S+\w)/)
  matches = match_from + match_to + match_flags
  joined = matches.join(",")
  puts joined
end
