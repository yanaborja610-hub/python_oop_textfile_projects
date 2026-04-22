from highest_gwa_finder_class import HighestGwaFinder

finder = HighestGwaFinder("students_with_their_gwa.txt")
name, gwa = finder.finding_highest_gwa()

if name:
    print("\nTOP PERFORMING STUDENT")
    print("\nTop Student:", name)
    print(f"GWA: {gwa:.2f}")