# mypkg
  - プログラムを起動しwebカメラで写真を撮ると、撮った写真とあらかじめ登録された画像を比較し、写真の中に登録された画像が含まれていたときに中指を立てます。
  ## 動作環境
  - OS : Ubuntu 18.04 LTS
  - ROS Distribution : Melodic Morenia
  - Python 2.7.17
  - OpenCV 3.2.0
  - Arduino 1.8.13
  ## 使用したもの
  - ESP-WROOM-32
  - 電源用ケーブル micro USB Type-B
  - マイクロサーボ SG90
  - ブレットボード
  - ジャンパ線
  ## 回路
  ![ESP32_servo](https://user-images.githubusercontent.com/76610691/148865314-453b0797-02c0-4e8f-930a-f2fb5840f6a7.jpg)
  ## 実行方法
  ### セットアップ
  #### ROSのセットアップ
  ROSのセットアップは[Ryuich Ueda](https://github.com/ryuichiueda)様の[ロボットシステム学第10回](https://youtu.be/PL85Pw_zQH0)の動画を参考にしました
  #### パッケージのセットアップ
  ```
  cd ~/catkin_ws/src/
  git clone https://github.com/KoheiYanagisawa/mypkg.git
  cd ../
  catkin build
  source ~/.bashrc
  ```
  ESP32についてはArduinoIDEで[こちらのコード](https://github.com/KoheiYanagisawa/mypkg/tree/main/esp32_code)を書き込んでください
  ### 実行
  - 端末を立ち上げ以下のコマンドを入力
  ```
  roslaunch mypkg main.launch
  ```
  - 上のコマンドを実行するとカメラが起動します
  ![image](https://user-images.githubusercontent.com/76610691/148869037-1bb0b7cf-d565-49aa-ae6d-ef1878ad39f9.png)
  - キーボードの[P]を入力することで写真撮影ができ、その後撮影した写真とbase.pngに登録されている画像を比べ結果を出力します
  ![image](https://user-images.githubusercontent.com/76610691/148870033-501e7790-ca82-4104-87f3-83406f48661e.png)
  - 結果が一致していた場合ESP32に信号が送られサーボが動き、中指が立ち上がります
  ![正面中指](https://user-images.githubusercontent.com/76610691/148870284-bd59b9a3-aabb-441a-b1b0-ff7f3b2ce91e.jpg)
  ## 実際に動かした動画
  https://youtu.be/5n7cQr-E7A8
  ## ライセンス
  - This repository is licensed under the []()
