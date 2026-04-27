class IntegerTransformerSystem:
    def __init__(self, filename):
        self.filename = filename
        self.numbers = []
        self.even_squared = []
        self.odd_cubed = []

    def get_user_input(self):
        print("Enter 20 Integers:\n ")

        for i in range(1, 21):
            while True:
                try:
                    numbers = (int(input(f"Enter Number {i}: ")))
                    self.numbers.append(numbers)
                    break

                except ValueError:
                    print("Invalid Input. Please enter an integer")

        with open(self.filename, "w") as file:
            file.write(" ".join(map(str, self.numbers)))

        print("\n Data saved to integers.txt")

    def process_numbers(self):
        for number in self.numbers:
            if number % 2 == 0:
                self.even_squared.append((number, number ** 2))
            else:
                self.odd_cubed.append((number, number ** 3))

    def write_files(self):
        with open("double.txt", "w") as even_file:
            for original_number, even_squared in self.even_squared:
                even_file.write(f"{original_number} -> {even_squared}\n")

        with open("triple.txt", "w") as odd_file:
            for original_number, odd_cubed in self.odd_cubed:
                odd_file.write(f"{original_number} -> {odd_cubed}\n")

    def display_results(self):
        print("\n EVEN NUMBERS (Squared):")
        for original_number, even_squared in self.even_squared:
            print(f"{original_number} -> {even_squared}")

        print("\n ODD NUMBERS (Cubed):")
        for original_number, odd_cubed in self.odd_cubed:
            print(f"{original_number} -> {odd_cubed}")

    def run(self):
        self.get_user_input()
        self.process_numbers()

        self.even_squared.sort(key=lambda x: x[1])
        self.odd_cubed.sort(key=lambda x: x[1])

        self.write_files()
        self.display_results()
        print("Done!")