from datetime import datetime

class MyLifeDiary:
    def __init__(self, filename="my_life.txt"):
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

    def save_text_to_file(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, "a") as file:
            file.write(f"\n Entry on {timestamp}\n")
            file.write("-" * 40 + "\n")

            for i, line in enumerate(self.lines, start = 1):
                file.write(f"{i}. {line}\n")

        print(f"\n Entry saved to {self.filename}!")

    def read_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if content.strip():
                    print("\nPast Entries\n")
                    print(content)

                else:
                    print("\nNo Entries\n")

        except FileNotFoundError:
            print("\nFile is empty\n")
