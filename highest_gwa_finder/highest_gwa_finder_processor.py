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

    if choice == "1":
        name, gwa = finder.finding_highest_gwa()
        print(f"\nTOP STUDENT:\n{name}: {gwa:.2f}")

    elif choice == "2":
        top_three = finder.top_three()
        print("\nTOP 3 STUDENTS")

        for i, (name, gwa) in enumerate(top_three, start=1):
            print(f"{i}. {name} - {gwa:.2f}")

    elif choice == "3":
        all_students_ranked = finder.display_list_of_students()
        print("\n=== ALL STUDENTS (RANKED) ===")

        for i, (name, gwa) in enumerate(all_students_ranked, start=1):
            print(f"{i}. {name} - {gwa:.2f}")