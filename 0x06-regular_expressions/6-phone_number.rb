#!/usr/bin/env ruby

def match_phone_number(string)
  regex = /^\d{10}$/
  match = string.match(regex)
  puts match ? match[0] : ""
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <phone_number>"
  exit 1
end

match_phone_number(ARGV[0])
