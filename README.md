## **_Easy image file management_**

#### **_function expression_**
_`rename.py`_
  - 這個 _`.py`_ 檔案會詢問作業的目錄，並將全部於此目錄的圖檔 ( _`.png` , `.jpg`_ ) 的名稱，依照該圖檔寬高重新命名。
  - 若撞名，會依照 _`Windows`_ 批次重新命名的命名規則。


_`createINI.py`_
  - 這個 _`.py`_ 檔案會詢問作業的目錄，讀取該目錄的全部圖檔，並建立一個 _`.ini`_ 檔，檔案格式如下。
```
[Data]
path=
json=
```
  - path是該目錄的 _`abspath`_ 
  - json會儲存一個 _`dict`_ ，詳細資料是 ( _key , value_ ) = ( _"{width}x{height}" , number_ ) ，這是一個圖檔的計數器


_`update.py`_
  - 當 _`createINI.py`_ 建立檔案後，每次呼叫 _`update.py`_ 都會預先讀取該 _`.ini`_ 檔，並在另一個目錄下重新命名該目錄的圖檔，最後執行歸檔。
  - 
