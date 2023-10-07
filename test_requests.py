import requests
r = requests.post('http://127.0.0.1:5000/webhook/crypto/binance_spot', 
                        json={
                                "ACTION" : "OPEN LONG",
                                "SYMBOL" : "PTT",
                                "AMOUNT" : 200,
                                "LIMIT" : 35
                        })

print(r.text)