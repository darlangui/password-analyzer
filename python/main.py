import string

class PasswordAnalyzer:
    def __init__(self):
        self.password = None

    def has_uppercase(self):
        return any(char.isupper() for char in self.password)

    def has_lowercase(self):
        return any(char.islower() for char in self.password)

    def has_digit(self):
        return any(char.isdigit() for char in self.password)

    def has_special_character(self):
        return any(char in string.punctuation for char in self.password)

    def calculate_password_strength(self):
        score = 0

        # Check the password length
        if len(self.password) >= 8:
            score += 1

        # Check if the password contains uppercase, lowercase, digits, and special characters
        if self.has_uppercase() and self.has_lowercase():
            score += 1
        if self.has_digit():
            score += 1
        if self.has_special_character():
            score += 1

        return score

    def get_password_strength(self, score):
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

    def analyze_password(self):
        self.password = input("Enter your password (or type 'exit' to quit): ")
        while self.password.lower() != "exit":
            score = self.calculate_password_strength()
            strength = self.get_password_strength(score)
            print("--------------------------------------------------------------------------------------------------------------------\n")
            print(f"Password strength: {strength}")

            if strength in ["Very Weak", "Weak", "Moderate"]:
                print("Consider improving your password by adding more characters (uppercase, lowercase, digits, and special characters).\n")
            elif strength == "Strong":
                print("Good job! Your password is strong, but you can still improve it by adding more special characters.\n")
            else:
                print("Congratulations! Your password is very strong and secure.\n")

            print("--------------------------------------------------------------------------------------------------------------------")
            self.password = input("Enter your password (or type 'exit' to quit): ")


def main():
    password_analyzer = PasswordAnalyzer()
    password_analyzer.analyze_password()


if __name__ == "__main__":
    main()
