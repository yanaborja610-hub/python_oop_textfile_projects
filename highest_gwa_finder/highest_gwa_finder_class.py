class HighestGwaFinder:
    def __init__(self, student_gwa):
        self.student_gwa = student_gwa
        self.gwa_finder = []

    def finding_highest_gwa(self):
        try:
            with open(self.student_gwa, 'r') as file:
                highest_name = " "
                highest_gwa = float("inf")

                for name_gwa in file:
                    name_gwa = name_gwa.strip()
                    name, gwa = name_gwa.split(",")
                    gwa = float(gwa.strip())

                    if gwa < highest_gwa:
                        highest_gwa = gwa
                        highest_name = name.strip()

        except FileNotFoundError:
            print("File not found.")
            return None, None

        return highest_name, highest_gwa