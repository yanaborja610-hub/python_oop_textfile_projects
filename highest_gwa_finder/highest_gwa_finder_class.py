class HighestGwaFinder:
    def __init__(self, student_gwa):
        self.student_gwa = student_gwa
        self.gwa_finder = []

    def load_students(self):
        with open(self.student_gwa, 'r') as file:
            for line in file:
                line = line.strip()
                name, gwa = line.split(",")
                self.gwa_finder.append((name.strip(), float(gwa)))

    def finding_highest_gwa(self):
        highest_name, highest_gwa = min(self.gwa_finder, key=lambda x: x[1])
        return highest_name, highest_gwa

    def top_three(self):
        sorted_students = sorted(self.gwa_finder, key=lambda x: x[1])
        return sorted_students[:3]

    def display_list_of_students(self):
        return sorted(self.gwa_finder, key=lambda x: x[1])
