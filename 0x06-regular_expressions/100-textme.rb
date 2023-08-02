#!/usr/bin/env ruby

def extract_textme_info(log_line)
  regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
  match = log_line.match(regex)

  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_line>"
  exit 1
end

extract_textme_info(ARGV[0])
