#!/bin/sh

cleanup() {
  printf '' > $1
}

collect() {
  date +%s >> $1
  echo $2 >> $1
  iw dev wlan-5000mhz station dump >> $1
}

iw dev wlan-2400mhz set txpower fixed 0
cleanup $1
while true; do
  collect $1 $2
  sleep 1
done
