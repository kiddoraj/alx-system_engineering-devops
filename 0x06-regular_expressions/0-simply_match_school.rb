#!/usr/bin/env ruby

def match_school(string)
  regex = /School/
  match = string.scan(regex).join
  puts match
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

match_school(ARGV[0])
