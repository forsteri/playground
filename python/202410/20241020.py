# 2024/10/20
# お題: 「FizzBuzz」の拡張版
# 1から100までの数字を順に表示するプログラムを書いてみよう。ただし、以下のルールを適用すること：
# 3の倍数なら「Fizz」と表示する
# 5の倍数なら「Buzz」と表示する
# 7の倍数なら「Bazz」と表示する
# 3と5の倍数なら「FizzBuzz」と表示する
# 3と7の倍数なら「FizzBazz」と表示する
# 5と7の倍数なら「BuzzBazz」と表示する
# 3と5と7の倍数なら「FizzBuzzBazz」と表示する

for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Bazz"
    
    print(output if output else i)

# 不格好なやつ

"""
for i in range(100):
    i = i + 1

    if i % 105 == 0:
        print("FizzBuzzBazz")
    elif i % 35 == 0:
        print("BuzzBazz")
    elif i % 21 == 0:
        print("FizzBazz")
    elif i % 15 == 0:
        print("FizzBuzz")
    elif i % 7 == 0:
        print("Bazz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
"""