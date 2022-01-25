import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    STRs = []
    profiles = []

    # Read in database file - using `with` means we don't have to close the file
    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        # Populate list of Short Tandem Repeats (STRs)
        STRs = reader.fieldnames[1:]
        for row in reader:
            # Add person to profiles
            profiles.append(row)

    # Initialise dictionary for sequence file
    seq_str_count = dict.fromkeys(STRs, 0)

    # Read in sequence file
    with open(sys.argv[2], "r") as sequence_file:
        # Grab first line of txt file
        sequence = sequence_file.readline()
        # Loop over every STR from the database
        for STR in STRs:
            # Update the Sequence STR dictionary with max amount of repeats
            seq_str_count[STR] = longest_match(sequence, STR)

    # Check if any person has same amount of STR repeats as sequence
    for profile in profiles:
        match_count = 0

        for STR in STRs:
            if int(profile[STR]) != seq_str_count[STR]:
                continue
            match_count += 1

        if match_count == len(STRs):
            print(profile['name'])
            exit(0)

    print("No match")
    exit(1)


def longest_match(sequence, subsequence):
    # Returns length of longest run of subsequence in sequence.

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
