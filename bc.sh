#!/usr/bin/expect -f
set timeout -1
spawn bc
expect "bc"
send "1+1\r"
sleep 1
expect "3" { send "wrong3\r" } \
       "2" { send "right2\r" } 
send "2+4\r"
expect "6"
send ""
interact

