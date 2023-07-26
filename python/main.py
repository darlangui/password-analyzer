import tkinter as tk
import string

class PasswordAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Analyzer")
        self.root.geometry("350x350")
        self.root.configure(bg="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#ffffff")
        frame.pack(pady=20)

        password_label = tk.Label(frame, text="Enter your password:", bg="#ffffff", font=("Nunito", 14))
        password_label.pack()

        self.password_entry = tk.Entry(frame, show="*", font=("Nunito", 14))
        self.password_entry.pack(pady=10)

        self.result_label = tk.Label(frame, text="", bg="#ffffff", font=("Nunito", 14), wraplength=350)
        self.result_label.pack(pady=10)

        analyze_button = tk.Button(frame, text="Analyze", font=("Nunito", 14), command=self.analyze_password)
        analyze_button.pack(pady=10)

        close_button = tk.Button(frame, text="Close", font=("Nunito", 14), command=self.close_window)
        close_button.pack()

    def has_uppercase(self, password):
        return any(char.isupper() for char in password)

    def has_lowercase(self, password):
        return any(char.islower() for char in password)

    def has_digit(self, password):
        return any(char.isdigit() for char in password)

    def has_special_character(self, password):
        return any(char in string.punctuation for char in password)

    def calculate_password_strength(self, password):
        score = 0

        # Check the password length
        if len(password) >= 8:
            score += 1

        # Check if the password contains uppercase, lowercase, digits, and special characters
        if self.has_uppercase(password) and self.has_lowercase(password):
            score += 1
        if self.has_digit(password):
            score += 1
        if self.has_special_character(password):
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
        password = self.password_entry.get()
        if not password:
            self.result_label.config(text="Please enter a password.", fg="red")
            return

        score = self.calculate_password_strength(password)
        strength = self.get_password_strength(score)

        self.result_label.config(text=f"Password strength: {strength}", fg="black")

        if strength in ["Very Weak", "Weak", "Moderate"]:
            self.result_label.config(text=self.result_label.cget("text") + "\nConsider improving your password by adding more characters (uppercase, lowercase, digits, and special characters).", fg="red")
        elif strength == "Strong":
            self.result_label.config(text=self.result_label.cget("text") + "\nGood job! Your password is strong, but you can still improve it by adding more special characters.", fg="orange")
        else:
            self.result_label.config(text=self.result_label.cget("text") + "\nCongratulations! Your password is very strong and secure.", fg="green")

    def close_window(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = PasswordAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
