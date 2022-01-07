#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import time
import rospy 
from std_msgs.msg import Int32



def main():
    while not rospy.is_shutdown():
        cap = cv2.VideoCapture(0)
        #撮影した画像
        path_takepic = "/home/"+os.getlogin()+"/catkin_ws/src/mypkg/jpg/takepic.jpg"
        #参照先の画像
        path_base = "/home/"+os.getlogin()+"/catkin_ws/src/mypkg/jpg/base.png"  
        #作成するクレースケール
    
        rospy.init_node('feature_matching')
        pub = rospy.Publisher('judge_topic', Int32, queue_size=10)
        r = rospy.Rate(10) # 10hz
        n = 0
        while True:
            ret, frame = cap.read()
            cv2.imshow("camera",frame)
            key = cv2.waitKey(1)&0xff
            if key == ord('p'):
                cv2.imwrite(path_takepic,frame)
                cv2.imshow(path_takepic,frame)
                time.sleep(2)
                break
        cap.release()
        cv2.destroyAllWindows()


        img1 = cv2.imread(path_base)
        img2 = cv2.imread(path_takepic)

        # A-KAZE検出器の生成
        akaze = cv2.AKAZE_create()                                
    
        # 特徴量の検出と特徴量ベクトルの計算
        kp1, des1 = akaze.detectAndCompute(img1, None)
        kp2, des2 = akaze.detectAndCompute(img2, None)

        # Brute-Force Matcher生成
        bf = cv2.BFMatcher()

        # 特徴量ベクトル同士をBrute-Force＆KNNでマッチング
        matches = bf.knnMatch(des1, des2, k=2)

        ratio = 0.85
        good = []
        for m, n in matches:
            if m.distance < ratio * n.distance:
                good.append([m])
        feature_value = len(good)
        print(feature_value)
        if(feature_value >= 5):
            print("参照データと一致")
            n = 1
            pub.publish(n)
        else:
            print("参照データと一致しません")
            n = 0
            pub.publish(n)

        img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:], None, flags=2)


        cv2.imshow('img', img3)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        r.sleep()

if __name__ == '__main__':
    try:
      main()
    except rospy.ROSInterruptException: 
      pass  

