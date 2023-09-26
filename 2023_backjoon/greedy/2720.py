COINS = [
    ("QUARTER", 25),
    ("DIME", 10),
    ("NICKEL", 5),
    ("PENNY", 1)
]

def solve(change):
    answer = {
        "QUARTER": 0,
        "DIME": 0,
        "NICKEL": 0,
        "PENNY": 0
    }
    remained = int(change)
    for coin, amount in COINS:
        while (remained >= amount):
            answer[coin] += 1
            remained -= amount

    return answer

def main(t):
    test_cases = [];
    for _ in range(int(t)):
        test_cases.append(input())

    for change in test_cases:
        answer = solve(change)
        print(f"{answer['QUARTER']} {answer['DIME']} {answer['NICKEL']} {answer['PENNY']}")
    


if __name__ == "__main__":
    t = input()
    main(t)
