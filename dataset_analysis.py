GSE 301: Dataset Management and Basic Analysis System
This program reads numerical and category data from files,
calculates statistics, and saves results to a report file.

# -------------------------------
# Class Definition (OOP Structure)
# -------------------------------
class DataSet:
    def __init__(self, numbers_path, categories_path):
        # File paths for numeric and category data
        self.numbers_path = numbers_path
        self.categories_path = categories_path
        
        # Variables to hold dataset contents
        self.numbers = []
        self.unique_categories = set()
        
        # Variables to store computed statistics
        self.total = 0
        self.mean = 0
        self.minimum = None
        self.maximum = None

    # ----------------------------------
    # Method: Load Data from Text Files
    # ----------------------------------
    def load_data(self):
        # Load numerical data
        try:
            with open(self.numbers_path, "r") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        try:
                            value = float(cleaned)
                            self.numbers.append(value)
                        except ValueError:
                            # Skip non-numeric lines
                            continue
        except FileNotFoundError:
            print("Error: numbers file is missing.")
            return False

        # Check if no valid data was found
        if not self.numbers:
            print("Error: No valid numeric values found.")
            return False

        # Load category data
        try:
            with open(self.categories_path, "r") as cat_file:
                for line in cat_file:
                    self.unique_categories.add(line.strip())
        except FileNotFoundError:
            print("Error: categories file is missing.")
            return False

        return True

    # ----------------------------------------
    # Method: Compute Total, Mean, Min & Max
    # ----------------------------------------
    def compute_statistics(self):
        # Calculate total using a loop and arithmetic operators
        total_value = 0
        for num in self.numbers:
            total_value += num

        # Assign total
        self.total = total_value

        # Compute mean
        count = 0
        for _ in self.numbers:
            count += 1
        self.mean = self.total / count

        # Find minimum and maximum
        self.minimum = self.numbers[0]
        self.maximum = self.numbers[0]
        for num in self.numbers:
            if num < self.minimum:
                self.minimum = num
            if num > self.maximum:
                self.maximum = num

    # ---------------------------------------------
    # Method: Display Results Based on Conditions
    # ---------------------------------------------
    def display_results(self):
        print("----- Data Analysis Results -----")
        print("Total:", self.total)
        print("Average:", self.mean)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)

        # Conditional threshold check
        threshold = 50
        if self.mean > threshold:
            print("Performance Status: High Performance")
        else:
            print("Performance Status: Needs Improvement")

        print("Number of Unique Categories:", len(self.unique_categories))

    # --------------------------------
    # Method: Save Results to Report
    # --------------------------------
    def save_to_report(self, report_file):
        with open(report_file, "w") as out:
            out.write("----- Dataset Analysis Report -----\n")
            out.write(f"Total: {self.total}\n")
            out.write(f"Average: {self.mean}\n")
            out.write(f"Minimum: {self.minimum}\n")
            out.write(f"Maximum: {self.maximum}\n")

            if self.mean > 50:
                out.write("Performance Status: High Performance\n")
            else:
                out.write("Performance Status: Needs Improvement\n")

            out.write(f"Unique Categories: {len(self.unique_categories)}\n")


# -----------------------
# Main Program Execution
# -----------------------
# File names containing data
numbers_file = "data_numbers.txt"
categories_file = "data_categories.txt"
report_file = "analysis_report.txt"

# Create dataset object
data_system = DataSet(numbers_file, categories_file)

# Load dataset
if data_system.load_data():
    # Calculate required statistics
    data_system.compute_statistics()

    # Display results on screen
    data_system.display_results()

    # Save results to file
    data_system.save_to_report(report_file)
    print("Analysis report has been saved.")
