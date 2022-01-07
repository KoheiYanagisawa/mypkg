#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
import time
from contextlib import closing
import rospy
from std_msgs.msg import Int32

def callback(msg):
  host = "192.168.11.1" # IPアドレス
  port = 9000 # ポート番号
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    if(msg.data == 0):
      message = '0'
      print(message)
      sock.sendto(message, (host, port))
    if(msg.data == 1):  
      message = '1'
      print(message)
      sock.sendto(message, (host, port))

def main():
  rospy.init_node('send_signal')
  rospy.Subscriber("/judge_topic", Int32, callback)
  host = "192.168.11.1" # IPアドレス
  port = 9000 # ポート番号
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
      message = '0'
      print(message)
      sock.sendto(message, (host, port))
  rospy.spin()

if __name__ == '__main__':
  main()