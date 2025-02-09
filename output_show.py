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
