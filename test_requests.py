import requests
r = requests.post('http://127.0.0.1:5000/webhook/crypto/binance_future', 
                        json={
                                "ACTION" : "TPSL SHORT",
                                "SYMBOL" : "BTCUSDT",
                                "AMOUNT" : 0.09,
                                "LIMIT" : 35
                        })

print(r.text)