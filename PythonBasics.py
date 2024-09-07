msg = "Roll a dice!"
print(msg)

spam_amount = 0
print(spam_amount)

spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want any spam")

#multiple of string
viking_song = "Spam " * spam_amount
print(viking_song)

#type 
print(type(spam_amount))
print(type(viking_song))
print(type(19.55))

#operator
print( 5 + 3)
print( 5 -3 )
print( 5 * 3)
print( 5 / 3)
print( 5 // 3)
print(5 % 3)
print(5 ** 3)
print(-5) 

print( 5 + 3 - 3 * (3 / 3)) # 5 + 0 * 1 = 5
print( 5 + 3 - (3 * 5) // 3) # 8 - 15 // 3 , 8 - 5 , => 3

#min and max functions
print(min(2,1,3))
print(max(2,1,3))

#absolute value
print(abs(32))
print(abs(-32))

#numeric type
print("----- Numberic Type ------")
print(float(10))
print(int(10.12))
print(int('10')+3)
print(float('10.13')+3)


