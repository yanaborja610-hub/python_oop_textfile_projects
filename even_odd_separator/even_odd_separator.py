class EvenOddSeparator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.odd_numbers = []
        self.even_numbers = []

    def process_numbers(self):
        with(open(self.numbers, 'r')) as numbers_file:
            for numbers in numbers_file:
                number= int(numbers.strip())
                if number % 2 == 0:
                    self.even_numbers.append(number)
                else:
                    self.odd_numbers.append(number)

    def write_even_file(self):
        self.even_numbers.sort()
        with open('even.txt', 'w') as even_file:
            for numbers in self.even_numbers:
                even_file.write(str(numbers) + '\n')

    def write_odd_file(self):
        self.odd_numbers.sort()
        with open('odd.txt', 'w') as odd_file:
            for numbers in self.odd_numbers:
                odd_file.write(str(numbers) + '\n')

    def display_summary(self):
        print("\nSUMMARY\n")
        print(f"Total Even Numbers:{len(self.even_numbers)}")
        print(f"Total Odd Numbers:{len(self.odd_numbers)}\n")

        minimum_even = min(self.even_numbers)
        minimum_odd = min(self.odd_numbers)

        maximum_even = max(self.even_numbers)
        maximum_odd = max(self.odd_numbers)

        print(f"Minimum Even Number: {minimum_even:<10}Maximum Even Number: {maximum_even}")
        print(f"Minimum Odd Number: {minimum_odd:<11}Maximum Odd Number: {maximum_odd}")