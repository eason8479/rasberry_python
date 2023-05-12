# rasberry_python

## 檔案用途
- manual.py：測試手動模式
- pi_control.py：測試pi的pin腳
- project_for_debug.py：在電腦上測試用的程式
- project_for_pi.py：需要燒進pi的程式
- random_1.py：隨機數測試
- ust_test.py：usb

## pin腳用途
 \ | GPIO2 | GPIO3
---| --- | ---
on | 開門 | 開夾爪
off| 關門 | 關夾爪

![](https://i.imgur.com/DFEKMHD.png)

## scp 傳輸
因為我們的程式碼較多，因此每次都要複製貼上會很浪費時間  
用SCP傳輸會更快

1. 開啟 project_for_pi.py （或你要傳的檔案）所在的資料夾
2. 右鍵，在終端開啟（ios我不確定要怎麼做），運行前
3. 執行下列程式
```
scp project_for_pi.py pi@[pi的ip]:[要存的位置]
```
以下為scp執行例子
```
scp myfile.txt pi@172.20.20.6:/home/pi/
```
4. 完成！

## 代辦清單
- [x] 連接機台  
- [ ] usb存檔  
- [ ] 隨機延遲  
