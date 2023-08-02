#!/usr/bin/env ruby

def match_beginning_and_end(string)
  regex = /^h.n$/
  match = string.match(regex)
  puts match ? match[0] : ""
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

match_beginning_and_end(ARGV[0])
