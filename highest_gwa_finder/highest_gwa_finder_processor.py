from highest_gwa_finder_class import HighestGwaFinder

finder = HighestGwaFinder("students_with_their_gwa.txt")
finder.load_students()

while True:
    print("\n===== MENU =====")
    print("1. Show Top Student")
    print("2. Show Top 3 Students")
    print("3. Show All Students")
    print("4. Exit")

    choice = input("Enter choice: ")