# -*- coding: utf-8 -*-
import cv2
import time

cap = cv2.VideoCapture(0)
#撮影した画像
path_takepic = "../jpg/nomukamo.jpg"
#参照先の画像
path_base = "../jpg/base.jpg"  
#作成するクレースケール
path_gray1 = "../jpg/gray_base.jpg"
path_gray2 = "../jpg/gray_takepic.jpg"

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


img = cv2.imread(path_takepic)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(path_gray1, img_gray)

img = cv2.imread(path_base)
#リサイズ
img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
img_gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(path_gray2, img_gray2)

img1 = cv2.imread(path_gray2)
img2 = cv2.imread(path_gray1)

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
else:
    print("参照データと一致しません")

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:], None, flags=2)


cv2.imshow('img', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
