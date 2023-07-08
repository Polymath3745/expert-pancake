def find_max_product(nums):
    max_prod = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] != nums[j]):
                prod = nums[i] * nums[j]
                if (prod > max_prod):
                    max_prod = prod
    return max_prod


def main():
    num_list = [1,2,3,4,5]
    print(find_max_product(num_list))

if __name__ == '__main__':
    main()