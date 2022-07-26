#!/usr/bin/env ruby
puts ARGV[0].scan(/([0-9]{10}|[A-Za-z]+),([0-9]{10}|[A-Za-z]+),(.)/).join
