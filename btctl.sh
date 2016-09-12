#!/usr/bin/expect -f
spawn bluetoothctl
expect ""
send "connect 00:00:00:00:0B:00\r"
expect "Attempt to connect to "
sleep 4
expect "connect successful"
expect "$ "
send "quit\r"
