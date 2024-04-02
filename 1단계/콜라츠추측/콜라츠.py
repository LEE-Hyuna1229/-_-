def solution(num):
    run = 0
    while True:
        if num == 1: return run
        
        elif num%2 == 0: num /= 2   
        elif num%2 != 0:num = num*3+1
        run += 1
        if run>500: return -1