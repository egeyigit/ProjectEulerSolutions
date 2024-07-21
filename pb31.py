def count_ways_to_make_200():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    ways = [0] * (target + 1)
    ways[0] = 1  # There is one way to make 0 pence (using no coins)

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

# Call the function and print the result
number_of_ways = count_ways_to_make_200()
print(number_of_ways)