# Exchange ที่ 1 มี 6 คู่เทรด แต่ละคู่ราคาไม่เท่ากัน

คู่ที่1 = "EURUSD"
คู่ที่2 = "GBPUSD"

# list , array กลุ่มตัวแปร

list_of_pair = ["EURUSD","GBPUSD","US30","US100","US500","BTCUSD"]

for index , pair in enumerate(list_of_pair): # loop
        print(index)
        print(pair)

print(list_of_pair[0])

# dictionary , Json (javascript object notation) HTTP METHODES

# key : value
# dog : สุนัข
# cat : แมว

dict_01 = { "dog" : "สุนัข" 
           , "cat" : "แมว" 
           , "EURUSD" : 1.22 
           , "GBPUSD" : 1.11}

print(dict_01["dog"])
print(dict_01["EURUSD"])

