"""

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

"""
import sys

# Brute force
def substring_addition(target_sum: int, digit_string: str):
    digit_list = [int(x) for x in digit_string.split(",")]

    # Try all starting positions
    for start in range(len(digit_list)):
        current_sum = 0

        # Extend window from start position
        for end in range(start, len(digit_list)):
            current_sum += digit_list[end]

            # If we hit the target, substring found
            if current_sum == target_sum:
                print(f"{start}-{end}")  # Print indices of substring
                return

            # If we exceed target, move start of window to the right
            elif current_sum > target_sum:
                break
    
    print(None)
    return
    
# Sliding window
def substring_addition_optimal(target_sum: int, digit_string: str):
    digit_list = [int(x) for x in digit_string.split(",")]
    
    current_sum = 0
    start = 0
        
    for end in range(len(digit_list)):
        current_sum += digit_list[end]
        
        # If exceed target, move start of window to right
        while current_sum > target_sum and start <= end:
            current_sum -= digit_list[start]
            start += 1
        
        if current_sum == target_sum:
            print(f"{start}-{end}")  # Print indices of substring
            return
    
    print(None)
    return

    
if __name__ == '__main__':
    # target_sum = int(sys.argv[1])
    # digit_string = sys.argv[2]
    # substring_addition(target_sum=target_sum, digit_string=digit_string)
    
    target_sum = int(sys.argv[1])
    digit_string = sys.argv[2]
    substring_addition_optimal(target_sum, digit_string)
