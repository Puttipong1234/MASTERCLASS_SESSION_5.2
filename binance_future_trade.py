import ccxt
from config import *

exchange = ccxt.binance({
        'apiKey' : BINANCE_FUTURE_API_KEY ,
        'secret' : BINANCE_FUTURE_API_SECRET ,
        'options' : {
                'defaultType' : 'future'
        }
})

exchange.set_sandbox_mode(BINANCE_FUTURE_TESTING) # True => testnet , False => mainnet   

# balance = exchange.fetch_balance(params={"type" : "future","symbols" : "USDT"})
# print(balance['info']['totalWalletBalance'])   
# position_size =  10/100 * float(balance['info']['totalWalletBalance'])
# print("position size for you is : " + str(position_size) + " USDT")

# btc_price = exchange.fetch_mark_ohlcv(symbol="BTCUSDT" , timeframe="1h")
# print(position_size/float(btc_price[-1][4]))

# OPEN LONG
# exchange.create_order(symbol="BTCUSDT",type="market",side="buy",amount=0.1)
# exchange.create_order(symbol="BTCUSDT",type="market",side="sell",amount=0.1)

# exchange.set_leverage(symbol="BTCUSDT",leverage=50)
# exchange.set_margin_mode(symbol="BTCUSDT",marginMode="isolated")

def binance_future_open_long(sym,amount):
        

        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="buy",
                              amount=amount,
                              )

def binance_future_tpsl_long(sym,amount):
        

        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="sell",
                              amount=amount,
                              )


def binance_future_open_short(sym,amount):
        

        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="sell",
                              amount=amount,
                              )

def binance_future_tpsl_short(sym,amount):
        

        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="buy",
                              amount=amount,
                              )