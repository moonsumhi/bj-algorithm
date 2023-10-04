import heapq

def main():
    N = int(input())
    bundles = []
    for _ in range(N):
        heapq.heappush(bundles, int(input()))
    
    total = 0
    while len(bundles) > 1:
        first = heapq.heappop(bundles)
        second = heapq.heappop(bundles)
        new_bundle = first + second
        total += new_bundle
        heapq.heappush(bundles, new_bundle)

    return total

if __name__ == "__main__":
    answer = main()
    print(answer)