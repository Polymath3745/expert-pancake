def find_max_element(nums):
    max = 0
    for num in range(len(nums)):    
        if(nums[num] > max):
            max = nums[num]
    return max

def main():
    nums = [1,2,3,4]
    result = find_max_element(nums)
    print(result)

if __name__ == '__main__':
    main() 