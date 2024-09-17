import re

def password_strength(password):
    # Define the strength criteria
    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r'\d', password))
    uppercase_criteria = bool( re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check how many criteria are met
    score = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    # Provide feedback based on score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print(f"Your password is: {strength}")

if __name__ == "__main__":
    main()

