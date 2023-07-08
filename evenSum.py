def calculate_even_sum(n):
    even_nums = []
    for i in range(n+1):
        if (i % 2 == 0):
            even_nums.append(i)
    return sum(even_nums)


def main():
    result = calculate_even_sum(10)
    print(result)

if __name__ == '__main__':
    main()