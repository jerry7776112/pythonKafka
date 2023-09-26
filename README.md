# pythonKafka
## 專案說明
### 專案名稱: Python & Kafka & 餐點訂單分散式系統設計
**詳情請參閱[pythonKafka.pdf](https://github.com/jerry7776112/pythonKafka/blob/main/pythonKafka.pdf)**
### 實作說明
* 使用Python & Kafka 模擬設計一個高擴展性的食物訂單系統
每件重要的事情皆為一個獨立事件，例如下訂單和確認訂單
* 實作專注於系統的設計並不會撰寫前端程式，會以迴圈的方式模擬訂單產生
* 系統優勢:
如果任何前端或後端系統出現問題，資料不會遭受任何遺失，因為每項功能皆為各自獨立

### Flow
![flow](https://github.com/jerry7776112/pythonKafka/blob/main/flow/flow.png "flow")
### 專案架構
```
Hierarchy
---------------
pythonkafka
├── analytics.py (計算訂單數及收入)
├── docker-compose.yml
├── email.py (信箱資訊)
├── order_backend.py (訂單資訊)
├── requirements.txt (使用套件)
├── transaction.py (交易資訊)
```

### 前置準備
* Docker下載安裝
* ```pip install –r requirement.txt```

### 實務知識
* 分散式系統設計
* python & kafka 應用
* docker
