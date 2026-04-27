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
                self.even_squared.append(number ** 2)
            else:
                self.odd_cubed.append(number ** 3)