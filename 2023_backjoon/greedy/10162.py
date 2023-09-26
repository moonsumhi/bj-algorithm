BUTTON_TIME = {
    "A" : 300,
    "B" : 60,
    "C" : 10
}

def is_not_available(t):
    return t % 10 != 0

def main():
    t = int(input())
    if is_not_available(t):
        return "-1"
    
    answer = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    for btn_type, second in BUTTON_TIME.items():
        while (t >= second):
            answer[btn_type] += 1
            t -= second
    
    return " ".join(map(str, answer.values()))

if __name__ == "__main__":
    answer = main()
    print(answer)