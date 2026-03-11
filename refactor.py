import sys
from pathlib import Path

class ComputeStatistics:
    def __init__(self, filename):
        """Initialize with file path and load data once."""
        self.filename = filename
        self.data = self._read_ints()

    def _read_ints(self):
        """Read integers from file and return as list."""
        try:
            return [int(line.strip()) for line in Path(self.filename).read_text().splitlines() if line.strip()]
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found")
            return []
        except ValueError as e:
            print(f"Error: Invalid number format in file - {e}")
            return []

    def count(self):
        return len(self.data)

    def summation(self):
        return sum(self.data)

    def average(self):
        return round(sum(self.data) / len(self.data), 2) if self.data else 0

    def minimum(self):
        return min(self.data) if self.data else None

    def maximum(self):
        return max(self.data) if self.data else None

    def stats(self):
        """Return all statistics in a dictionary."""
        if not self.data:
            return None
        return {
            "total": self.count(),
            "summation": self.summation(),
            "average": self.average(),
            "minimum": self.minimum(),
            "maximum": self.maximum,
        }


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "random_nums.txt"
    cs = ComputeStatistics(filename)

    if cs.data:
        print("The values are:", cs.data)
        print("Total values in file are:", cs.count())
        print("Summation of data is:", cs.summation())
        print("Average of data is:", cs.average())
        print("Minimum value from data is:", cs.minimum())
        print("Maximum value from data is:", cs.maximum())
