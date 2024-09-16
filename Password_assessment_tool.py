print()
print("A.S Muhammad: PASSWORD ASSESSMENT TOOL")
print()

import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password)
    uppercase_criteria = re.search(r"[A-Z]", password)
    digit_criteria = re.search(r"\d", password)
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}<>]", password)

    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])
    if criteria_met == 5:
        return "strong", "Your password is strong."
    elif 3 <= criteria_met < 5:
        return "Medium", "Your password is medium. Try adding more variety (uppercase, numbers, or special characters)."
    else:
        return "Weak", "Your password is weak. Consider increasing the length and adding numbers, special characters, and both uppercase and lowercase."

def main():
    while True:
        print("\nPassword Strength Assessment Tool")
        password = input("Enter your password: ")
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}")
        print(f"Feedback: {feedback}")
        again = input("Do you want to check another password? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()