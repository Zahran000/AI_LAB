user_name = input("Enter your full name: ")

def analyze_text(text):
    total_chars = len(text)
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    result = {
        "User Name": user_name,
        "Total Characters": total_chars,
        "Uppercase Letters": uppercase_count,
        "Lowercase Letters": lowercase_count,
        "Digits": digit_count
    }
    return result

analysis = analyze_text(user_name)

print("\nText Analysis Result:")
print(analysis)

