import sys
from pathlib import Path


def compute_stats(filename):
    """
    Read numbers from a file and compute statistics.

    Args:
        filename: Path to the file containing numbers (one per line)

    Returns:
        dict: Statistics dictionary with keys: total, summation, average, minimum, maximum
              Returns None if no valid data found
    """
    try:
        numbers = [int(line.strip()) for line in Path(filename).read_text().splitlines() if line.strip()]

        if not numbers:
            print("No data found in file")
            return None

        stats = {
            "total": len(numbers),
            "summation": sum(numbers),
            "average": round(sum(numbers) / len(numbers), 2),
            "minimum": min(numbers),
            "maximum": max(numbers),
        }

        # Print with consistent formatting
        for key, value in stats.items():
            print(f"{key} = {value}")

        return stats

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError as e:
        print(f"Error: Invalid number format in file - {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "random_nums.txt"
    compute_stats(filename)
