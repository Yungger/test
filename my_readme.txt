＊ 欲執行自動更新, 程式碼中加入以下敘述：
from My_OTA import myOTA
ota = MyOTA()
ota.update('檔名,...')
ota.updateAll()


＊ 關閉自動更新功能
ota.unsubscribe()


＊ 啟用自動更新功能
ota.subscribe()
