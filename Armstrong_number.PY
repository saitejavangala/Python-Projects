def is_armstrong_number(num):
    """Checks if a number is an Armstrong number."""

    sum = 0
    order = len(str(num))  # Calculate the number of digits
    for digit in str(num):  # Iterate over the digits of the number
        sum += int(digit) ** order  # Raise each digit to the power of the order and add to the sum
    return sum == num  # Check if the sum equals the original number

num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print("m")  # Indicate that the number is an Armstrong number
else:
    print("b")  # I
           
        
        
   
    


   



