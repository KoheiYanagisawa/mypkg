# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
import time
from contextlib import closing

def main():
  host = "192.168.11.1" # IPアドレス
  port = 9000 # ポート番号
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    while True:
      message = '0'
      print(message)
      sock.sendto(message, (host, port))
      time.sleep(1)
      
      message = '1'
      print(message)
      sock.sendto(message, (host, port))
      time.sleep(1)
      
  return

if __name__ == '__main__':
  main()