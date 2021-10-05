＊ 執行自動更新
1. MCU 須先連上網
2. 程式碼中加入以下敘述：
from My_BoardUpdater import myUpdater
my_updater = myUpdater("MAC address of your MCU")
my_updater.updateAll()  # .update('檔名') 或 .update()


＊ 取消自動更新
from My_BoardUpdater import myUpdater
my_updater = myUpdater("MAC address of your MCU")
my_updater.unsubscribe()


＊ 啟用自動更新
from My_BoardUpdater import myUpdater
my_updater = myUpdater("MAC address of your MCU")
my_updater.subscribe()