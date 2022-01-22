from numpy.random import default_rng

def user_float():
    while True:
        try:
            inp = float(input("Value: "))
            if inp <= 0:
                raise Exception("NonPositiveNumber: Enter a positive number")
        except Exception as e:
            print(e)
            continue
        else:
            break
    return(inp)

def user_int():
    while True:
        try:
            inp = int(input("Value: "))
            if inp <= 0:
                raise Exception("NonPositiveNumber: Enter a positive number")
        except Exception as e:
            print(e)
            continue
        else:
            break
    return(inp)

gen = default_rng()
print("Enter the starting price.")
start = user_float()
print("Enter the strike price.")
strike = user_float()
print("Enter the expected volatility in the asset until the expiry date.")
volatility = user_float()
print("Enter the sample size.")
size = user_int()

sample = gen.normal(start, volatility, size)
total_value = 0.0
for i in sample:
    total_value += max(0, i - strike)

price = total_value / size
print("The value of this option is estimated to be: " + str(price))