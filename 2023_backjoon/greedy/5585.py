PAID = 1000
COINS = [500, 100, 50, 10, 5, 1]

def main():
    price = int(input())
    change = PAID - price 
    answer = 0

    for coin in COINS:
        while (change >= coin):
            answer += 1
            change -= coin
    
    return answer

if __name__ == "__main__":
    answer = main()
    print(answer)