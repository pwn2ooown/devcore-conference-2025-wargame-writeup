# DEVCORE Conference 2025 CTF 磁片密令：聯合作戰 Writeup

## Stage 1

1. 有四種不同的磁片，分別是 Binary 以及 Hex 的形式，把 Binary 以及 Hex 分別組合起來

- Binary 的兩片組出來會是一張 QR code，掃出來是 zip 密碼
- Hex 將兩兩 Byte 反轉合併會得到 zip 檔

因為

```text
0027 0000 001b 0000 4b50 0201 031e 000a
...
```

看到 4b50 聯想到 ASCII 碼為 KP，所以將兩兩 Byte 反轉會得到 PK，是 zip 檔的 Magic Number。

## Stage 2

會進到一個網站，可以一位一位爆破數字密碼，但是一個 Session 猜錯一次就會被鎖起來所以要一直清 cookie。

不然你不想工人智慧的話你抓一下 HTTP Request 會發現它會發 Post Request 並且參數 `c` 是你當下猜的密碼的那個數字，注意到他是看每個 session 猜的順序所以就可以寫爆破的腳本了

## Exploit

QR code 見 `assemble_qrcode.py`

爆破腳本見 `guess.py`

(如果網站下線了就算了)

## Acknowledgement

- [Tony](https://t510599.github.io/)
- [Vincent55](https://vincent55.tw/)
