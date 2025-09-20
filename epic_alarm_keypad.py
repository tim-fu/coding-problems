'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Brute force / constrained string matching
def is_valid_alarm_code(expected_code, entered_code):
    """Check if entered code is valid - one digit on the alarm keypad may not be working"""
    expected = str(expected_code)
    entered = str(entered_code)
    
    if entered == expected:
        return True
        
    unique_digits = set(expected)
    
    # Remove all occurrences of each digit and see if entered code matches
    for digit_to_remove in unique_digits:
        modified_code = expected.replace(digit_to_remove, "")
        
        if entered == modified_code:
            return True
    
    return False

if __name__ == "__main__":
    print(is_valid_alarm_code("18684", "164"))
    
    expected = "18684"
    test_cases = ["164", "1864", "8684", "186", "684"]
    for entered in test_cases:
        print(f"Expected: {expected}, Entered: {entered}\n", is_valid_alarm_code(expected, entered))