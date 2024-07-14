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
