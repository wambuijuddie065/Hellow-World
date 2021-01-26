for num in range(100):
    if num%3==0 and num%5==0:
        print("FIZZBUZZ")
        continue
    elif num%3==0:
        print("FIZZ")
        continue
    elif num%5==0:
        print("BUZZ")
        continue
    else:
        print(num)
        
