import string

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    return any(char in string.punctuation for char in password)

def calculate_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if has_uppercase(password) and has_lowercase(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special_character(password):
        score += 1

    return score

def get_password_strength(score):
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    score = calculate_password_strength(password)
    strength = get_password_strength(score)

    print(f"Password strength: {strength}")

    if strength in ["Very Weak", "Weak", "Moderate"]:
        print("Consider improving your password by adding more characters (uppercase, lowercase, digits, and special characters).")
    elif strength == "Strong":
        print("Good job! Your password is strong, but you can still improve it by adding more special characters.")
    else:
        print("Congratulations! Your password is very strong and secure!")

if __name__ == "__main__":
    main()
