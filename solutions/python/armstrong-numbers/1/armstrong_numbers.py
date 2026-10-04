def is_armstrong_number(number):
    # onumber = number
    # ans = []
    # sum = 0 
    # while number > 0:
    #     ans.append(number % 10)
    #     number = number // 10
    
    # i = len(ans)
    # for n in ans:
    #     sum += n ** i

    # return sum == onumber
    digits = str(number)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == number
    
    