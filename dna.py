import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    subsequence = []
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            subsequence.append(line[1:])
            print(subsequence)
            break

    # TODO: Read DNA sequence file into a variable
    sequence = ''
    with open(sys.argv[2], "r") as file:
        sequence_list = file.read()
        for i in sequence_list:
            sequence = sequence.join(i)
        print(sequence)
        # read using the read() method on the file object.
        # This returns the contents of the file as a string.

    # TODO: Find longest match of each STR in DNA sequence
    max_count = []
    for i in range (len(subsequence[0])):
        max_count.append(longest_match(sequence, subsequence[0][i]))


    # TODO: Check database for matching profiles
    with open(sys.argv[1], "r") as csvfile:
        second_reader = csv.reader(csvfile)
        for line in second_reader:
            if (max_count == line[1:]):
                (print(f"{line[0]} is the match"))
            else:
                print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
