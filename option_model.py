from numpy.random import default_rng

# Returns a positive float inputted by the user
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

# Returns a positive integer inputted by the user
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

# Collects necessary inputs to produce a model
gen = default_rng()
print("Enter the starting price.")
start = user_float()
print("Enter the strike price.")
strike = user_float()
print("Enter the expected volatility in the asset until the expiry date.")
volatility = user_float()
print("Enter the sample size.")
size = user_int()

# Monte Carlo simulation of option using user input and the assumption that future price is distributed normally
sample = gen.normal(start, volatility, size)
total_value = 0.0
for i in sample:
    total_value += max(0, i - strike)

price = total_value / size
print("The value of this option is estimated to be: " + str(price))
