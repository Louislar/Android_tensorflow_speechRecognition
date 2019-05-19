# Android_tensorflow_speechRecognition

## project
1. android_imageClassification_project: 此為影像分類的專案(為了練習tensorflow mobile)，大部分從網路上參考

2. android_speechRecognition_project: 此為語音辨識的專案，預計使用tensorflo lite，目前正在開發當中

3. project_recognizerIntent_test: 此為利用google提供的recognizer Intent製作的簡易語音轉文字APP

## tool file
1. tensorflow_reBoost: 寫了一個範例，將keras model訓練完成(使用mnist)，並且轉換成tensorflow lite格式，且已經放到手機上測試可以執行(準確度不高)


## 關鍵檔案

1. keras_model_to_tflite.py: 簡單的用兩層DNN train了minst的data, 並且把model儲存成.h5與.tflite的檔案

2. kerasModel_to_pb.py: 將train好的keras model(.h5)轉換成.PB檔案並且能夠用tensorboard查看，

3. tensorflow_pb_to_log.py: 讓.pb檔案能夠恢復成可以用tensorboard查看內部構造的狀態

4. tensorflow_pb_to_tflite.py: 將.pb檔案轉換成.tflite的程式碼，此為tensorflow官方提供
