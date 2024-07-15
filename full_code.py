import re
from zxcvbn import zxcvbn


password_history = ["OldP@ssw0rd", "PrevP@ssw0rd1", "AnotherP@ss2"]


common_passwords = ["123456", "password", "12345678", "qwerty", "12345"]


def calculate_entropy(password):
    import math
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32  # Typical size for special characters
    return len(password) * math.log2(charset_size)

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    not_in_history = password not in password_history
    not_common = password not in common_passwords

    advanced_result = zxcvbn(password)
    score = advanced_result['score']
    suggestions = advanced_result['feedback']['suggestions']
    entropy = calculate_entropy(password)

    if score < 3:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback = {
        "length_criteria": length_criteria,
        "upper_criteria": upper_criteria,
        "lower_criteria": lower_criteria,
        "digit_criteria": digit_criteria,
        "special_criteria": special_criteria,
        "not_in_history": not_in_history,
        "not_common": not_common,
        "advanced_score": score,
        "strength": strength,
        "entropy": entropy,
        "suggestions": suggestions
    }

    return feedback

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

print(f"\nPassword: {password}")
print(f"Strength: {result['strength']}")
print("\nCriteria:")
print(f"  Length: {'Passed' if result['length_criteria'] else 'Failed'}")
print(f"  Uppercase: {'Passed' if result['upper_criteria'] else 'Failed'}")
print(f"  Lowercase: {'Passed' if result['lower_criteria'] else 'Failed'}")
print(f"  Digit: {'Passed' if result['digit_criteria'] else 'Failed'}")
print(f"  Special Character: {'Passed' if result['special_criteria'] else 'Failed'}")
print(f"  Not Recently Used: {'Passed' if result['not_in_history'] else 'Failed'}")
print(f"  Not a Common Password: {'Passed' if result['not_common'] else 'Failed'}")
print(f"\nAdvanced Score: {result['advanced_score']}")
print(f"Entropy: {result['entropy']:.2f} bits")
print("\nSuggestions:")
for suggestion in result['suggestions']:
    print(f"  - {suggestion}")
