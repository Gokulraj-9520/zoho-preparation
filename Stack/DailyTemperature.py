def dailyTemperatures(T):
    n = len(T)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result


if __name__ == "__main__":
    temperatures = list(map(int,input().split()))
    print("Input:", temperatures)
    print("Output:", dailyTemperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
