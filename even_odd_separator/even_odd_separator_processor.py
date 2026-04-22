from even_odd_separator import EvenOddSeparator

processor = EvenOddSeparator("numbers.txt")
processor.process_numbers()
processor.write_even_file()
processor.write_odd_file()
processor.display_summary()