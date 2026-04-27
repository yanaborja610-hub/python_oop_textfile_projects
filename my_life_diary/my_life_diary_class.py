class MyLifeDiary():
    def __init__(self, self.filename="my_life.txt"):
        self.filename = filename
        self.lines = []

    def collect_lines(self):
        print("Write a new journal entry")
        line_number = 1

        while True:
            text = input(f"What's on your mind? {line_number} ").strip()

            if text:
                self.lines.append(text)
                line_number += 1
            else:
                pass

            choice = input("Are there more lines? (yes/no): ").lower().strip()
            if choice != 'yes':
                break
