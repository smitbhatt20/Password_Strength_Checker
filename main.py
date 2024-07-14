import re
from zxcvbn import zxcvbn

# Simulate a password history
password_history = ["OldP@ssw0rd", "PrevP@ssw0rd1", "AnotherP@ss2"]

# Common passwords blacklist
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
