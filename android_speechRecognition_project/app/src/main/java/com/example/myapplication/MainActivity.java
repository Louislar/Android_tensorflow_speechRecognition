package com.example.myapplication;

import java.lang.*;
import java.io.File;
import java.io.IOException;

import android.content.pm.PackageManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Environment;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
//import org.tensorflow.contrib.android.TensorFlowInferenceInterface;
//為了錄製音訊
import android.media.MediaRecorder;
import android.media.MediaPlayer;
//為了取得權限
import android.Manifest;
import android.support.v4.app.ActivityCompat;

public class MainActivity extends AppCompatActivity {

    //Load the tensorflow inference library
//    static {
//        System.loadLibrary("tensorflow_inference");
//    }
//    private TensorFlowInferenceInterface tf;


    public TextView text;
    //權限請求代碼，RECORD_AUDIO
    private int AUDIO_PERMISSION_CODE = 1;
    private int EXSTORAGE_PERMISSION_CODE = 2;
    private MediaRecorder mediaRecorder = null;
    private int mediaState = 0;

    //確認權限請求有沒有成功
    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults)
    {
        if(requestCode == AUDIO_PERMISSION_CODE)
        {
            if(grantResults[0] == PackageManager.PERMISSION_DENIED)
            {
                //使用者拒絕權限請求，就結束程式
                System.exit(0);
            }
        }
        if(requestCode == EXSTORAGE_PERMISSION_CODE)
        {
            if(grantResults[0] == PackageManager.PERMISSION_DENIED)
            {
                //使用者拒絕權限請求，就結束程式
                System.exit(0);
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // button 的初始化
        Button button = (Button)findViewById(R.id.button);
        button.setOnClickListener(startChangeText);
        Button record_button = (Button)findViewById(R.id.record_button); //錄音button
        record_button.setOnClickListener(startRecordBtnClick);
        Button stop_record_button = (Button)findViewById(R.id.stopRecordButton); //錄音button
        stop_record_button.setOnClickListener(StopRecordBtnClick);

        // text 的初始化
        text = (TextView)findViewById(R.id.text);

        //請求microphone權限
        //先確認已經有權限了嗎?
        int permission = ActivityCompat.checkSelfPermission(this,
                Manifest.permission.RECORD_AUDIO);
        int permission_exStorage = ActivityCompat.checkSelfPermission(this,
                Manifest.permission.WRITE_EXTERNAL_STORAGE);
        if(permission != PackageManager.PERMISSION_GRANTED)
        {
            //沒有權限就要請求
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.RECORD_AUDIO}, AUDIO_PERMISSION_CODE);
        }
        if(permission_exStorage != PackageManager.PERMISSION_GRANTED)
        {
            //沒有權限就要請求
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, EXSTORAGE_PERMISSION_CODE);
        }

        //tensorflow初始化
        //需要拿到asset manager權限，以及1個已經訓練好的model，XXX.pb檔案
//        tf = new TensorFlowInferenceInterface(getAssets(), );
    }

    private View.OnClickListener startChangeText = new View.OnClickListener(){
        @Override
        public void onClick(View v) {
            System.out.println("button click.");
            changeText();
        }
    };

    //按下開始錄製按鈕
    private View.OnClickListener startRecordBtnClick = new View.OnClickListener(){
        @Override
        public void onClick(View v) {
            System.out.println("record button click.");
            String fileName = "record.amr";
            if(mediaState == 0) {
                try {
                    //會存到download資料夾內，並且會把新錄的覆蓋掉舊錄的
                    System.out.println("*****"+getFilesDir()+"*****");
                    System.out.println("*****"+getExternalCacheDir()+"*****");
                    System.out.println("*****"+Environment.getExternalStorageDirectory()+"*****");
                    File SDCardpath = Environment.getExternalStorageDirectory();//getFilesDir();//getExternalCacheDir();//Environment.getExternalStorageDirectory();
                    File myDataPath = new File(SDCardpath.getAbsolutePath() + "/download");
                    if (!myDataPath.exists()) myDataPath.mkdirs();
                    File recodeFile = new File(SDCardpath.getAbsolutePath()+ "/download/" + fileName);

                    mediaRecorder = new MediaRecorder();

                    //設定音源
                    mediaRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
                    //設定輸出檔案的格式
                    mediaRecorder
                            .setOutputFormat(MediaRecorder.OutputFormat.RAW_AMR);
                    //設定編碼格式
                    mediaRecorder
                            .setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
                    //設定錄音檔位置
                    mediaRecorder
                            .setOutputFile(recodeFile.getAbsolutePath());

                    mediaRecorder.prepare();

                    //開始錄音
                    mediaRecorder.start();

                    //將state改成正在錄音的狀態
                    mediaState = 1;
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }//check media state
            else
            {
                System.out.println("正在撥放了");
            }
        }
    };


    //停止錄音
    private View.OnClickListener StopRecordBtnClick = new View.OnClickListener(){

        @Override
        public void onClick(View v) {
            System.out.println("stop record button clicked");
            if(mediaRecorder != null) {
                mediaRecorder.stop();
                mediaRecorder.release();
                mediaRecorder = null;
                mediaState = 0;
            }
        }
    };

    //更換顯示的字
    private void changeText()
    {
        System.out.println("Call changeText()");
        text.setText("按鈕按下去囉");
//        tf.run();
    }
}
