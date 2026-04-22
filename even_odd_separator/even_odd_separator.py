class EvenOddSeparator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.odd_numbers = []
        self.even_numbers = []

    def process_numbers(self):
        with(open(self.numbers, 'r')) as numbers_file:
            for numbers in numbers_file:
                numbers = numbers.strip()
                if number % 2 == 0:
                    self.even_numbers.append(numbers)
                else:
                    self.odd_numbers.append(numbers)