'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Recursive backtracking
def generate_phone_numbers(length: int, excluded_digits: list[int]):
    """Generate phone numbers for company employees with the following rules:
        - No consecutive same digits
        - If contains 4, must start with 4
        - Exclude up to 3 digits (passed in)
    """
    allowed_digits = [str(digit) for digit in range(10) if digit not in excluded_digits]
    valid_numbers = []
    
    def backtrack(current_number):
        # Base case (stop condition): complete number generated
        if len(current_number) == length:
            # Filter out numbers that have a 4 but don't start with 4
            if '4' in current_number and not current_number.startswith('4'):
                return
            valid_numbers.append(current_number)
            return
        
        for digit in allowed_digits:
            # Avoid consecutive same digits
            if current_number and current_number[-1] == digit:
                continue
            
            # If first digit is not 4, the rest of the number can't have 4 either
            if len(current_number) == 0:
                if '4' in allowed_digits and digit != '4':
                    digits_without_4 = [d for d in allowed_digits if d != '4']
                    backtrack_without_4(current_number + digit, digits_without_4)
                else:
                    backtrack(current_number + digit)
            else:
                backtrack(current_number + digit)
                
    def backtrack_without_4(current_number, digits_without_4):
        # Base case: complete number generated
        if len(current_number) == length:
            valid_numbers.append(current_number)
            return
        
        for digit in digits_without_4:
            # Avoid consecutive same digits
            if current_number and current_number[-1] == digit:
                continue
            backtrack_without_4(current_number + digit, digits_without_4)
    
    backtrack("")   
    
    print(valid_numbers)
    return valid_numbers
    
    
if __name__ == "__main__":
    # Test case 1: Length 1, smallest example
    print("Test case 1:")
    generate_phone_numbers(1, [])
    print("\n" + "="*50 + "\n")
    
    # Test case 2: Length 2, no exclusions ('_4' removed)
    print("Test case 2:")
    valid_numbers = generate_phone_numbers(2, [])
    assert '14' not in valid_numbers
    print("\n" + "="*50 + "\n")
    
    # Test case 3: Length 2, exclude digit 4 (should allow all since no 4 constraint)
    print("Test case 3:")
    generate_phone_numbers(2, [4])
    print("\n" + "="*50 + "\n")
    
    # Test case 4: Length 3, exclude digit 5
    print("Test case 4:")
    generate_phone_numbers(3, [5])
    print("\n" + "="*50 + "\n")
    
    # Test case 5: Length 3, no exclusions (should handle 4 constraint)
    print("Test case 5:")
    generate_phone_numbers(3, [])
    print("\n" + "="*50 + "\n")
