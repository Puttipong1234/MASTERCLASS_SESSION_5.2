import ccxt

# commend --> ctrl + /
# for exchange in ccxt.exchanges:
#         print(exchange)

# get balance from wallet
# identify your wallet 
# api key , api secret (id,pass)

# create instance [กระเป๋าเงินของคุณ]
my_binance_future_wallet = ccxt.binance({
        'apiKey' : "0813c8e8f0ff67b903f4a6ee5bda3bf33ecf93324575aa59b154d049465dfcb0",
        'secret': "79cd1ee2e983d7b3ff99e968d3c08fbd55efe547ad00a33d694901929f4735e2",
        'options' : {
                'defaultType' : 'future'
        }
})

my_binance_future_wallet.set_sandbox_mode(enable=True)

# 1486.5 USDT
future_balance = my_binance_future_wallet.fetch_balance()
my_USDT = future_balance["USDT"]["free"]
print(my_USDT)
# position size 1% portfolio
my_position_size = float(my_USDT) * 0.01
print(my_position_size)

all_asset = future_balance["total"]
for (key , val) in all_asset.items():
        print(key)
        print(val)


# place order 
# margin Risk per trade => 1% => 14.86 USDT
# Stoploss ?? 3% Fix stoploss (previous xx candles low)
# position size margin x leverage
# leverage => 15x
# cross margin , Hedge mode (2 way positions)
# position size / constract price => amount
my_leverage = 15
my_symbol = "BTCUSDT"

current_btc_price = my_binance_future_wallet.fetch_last_prices([my_symbol])
current_btc_price = float(list(current_btc_price.values())[0]["price"])

my_binance_future_wallet.set_leverage(my_leverage,my_symbol)

calculate_amount = my_position_size * my_leverage / current_btc_price
print(calculate_amount)

# เปิด order ประเภท market , limit , stop
# my_binance_future_wallet.create_order(
#         symbol=my_symbol,
#         type="market",
#         side="buy",
#         amount=calculate_amount)

# limit order
# my_binance_future_wallet.create_order(
#         symbol=my_symbol,
#         type="limit",
#         side="buy",
#         price=60,
#         amount=calculate_amount)

all_position = my_binance_future_wallet.fetch_account_positions()

for i in all_position:
        # print(i["info"]["initialMargin"])
        if i["info"]["initialMargin"] != "0":
                print(i["info"]["symbol"])
                print("กำไร ขาดทุน " , i["info"]["unrealizedProfit"])


# f = open("log.txt", "a")
# f.write(str(all_position))
# f.close()

# ปิด order => สวน side ไปอีกทาง

my_binance_future_wallet.create_order(
        symbol=my_symbol,
        type="market",
        side="sell",
        amount=calculate_amount)
