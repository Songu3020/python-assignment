
def number_is_prime(number):
  
    if number < 0:
        number = number * -1

   
    factors = 0
    
    counter = 2

    while(counter<number):
        if number%counter ==0:
            factors+=1
        counter+=1
    if factors==0:
        return True
    return False

