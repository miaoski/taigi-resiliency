# taigi-resiliency
NLP for Taiwanese Hokkien (Tâi-gí) phonological resiliency 計算台語的語音容錯率

## 資料來源
台語有效語音的資料來源是 [信望愛台語輸入法](http://taigi.fhl.net/TaigiIME/), Mac 
的使用者在安裝後，可以在 `~/Library/Input\ Methods/TaigiHakkaIME.app/Contents/Resources/Talmage.db`
找到資料庫的原始檔。資料庫有點髒，所以我手動清理了一下，並把它改成 POJ (白話字) 的拼寫法。

## 檔案說明

- make-syllables.py 把資料從 Talmage.db 讀出來，寫進 syllables.txt
- cvc2array.py 把 cvc.txt 轉成 x,y,z,word 格式的 CSV 輸出
- make-cvc.py  把乾淨的資料從 syllables.txt 讀出來，分出 onset + segment + tone
- cvc.txt	整理過的 onset + segment + tone 的表格

# 版權
程式部份是 GPLv2, 資料部份由於是 信望愛台語輸入法 的衍生物，還在詢問當中。
