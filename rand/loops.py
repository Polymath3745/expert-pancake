def list_sum(list):
    sum = 0
    for num in list:
        sum += num
    
    return sum

def list_prod(list):
    product = 1
    for num in list:
        product *= num
    return product

def max_num(list):
    max = 0
    for num in list:
        if (num > max):
            max = num
    return max


def main():
    nums = [1, 2, 3, 4]
    #print( "sum of numbers in list is: " + str(list_sum(nums)))
    #print("the product of numbers in list is : " + str(list_prod(nums)))
    print("the max number in the list is : " + str(max_num(nums)))




if __name__ == '__main__':
    main()