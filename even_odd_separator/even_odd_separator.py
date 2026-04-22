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

processor = EvenOddSeparator("numbers.txt")
processor.process_numbers()
processor.write_even_file()
processor.write_odd_file()