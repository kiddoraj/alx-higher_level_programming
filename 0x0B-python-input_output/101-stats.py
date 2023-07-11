#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing the counts of different status codes.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))

def process_input():
    """
    Process the input from stdin and compute the metrics.

    Returns:
        None
    """
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            line = line.strip()

            # Parse the line to extract relevant information
            parts = line.split(" ")
            if len(parts) >= 7:
                status_code = parts[5]
                file_size = parts[6]

                # Update the total file size
                total_size += int(file_size)

                # Update the status code count
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    process_input()

