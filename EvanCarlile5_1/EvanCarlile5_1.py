import re
import csv
import os.path


def main():
    # Enter input file name and check if it exists
    user_input_file_name = 'files//' + input("Input file name: ").strip()
    while True:
        try:
            with open(user_input_file_name, 'r'):
                break
        except FileNotFoundError:
            print("File does not exist!")
            user_input_file_name = 'files//' + input("Input file name: ").strip()

    # Enter output file name and if it does ask to overwrite
    user_output_file_name = 'files//' + input("Output file name: ").strip()
    choice = ''
    while os.path.isfile(user_output_file_name) and choice != 'y':
        choice = input('Overwrite existing file (y/n): ').strip().lower()
        while True:
            if choice == 'y':
                break
            elif choice == 'n':
                user_output_file_name = 'files//' + input("New output file name: ").strip()
                break
            else:
                choice = input("Enter (y/n): ").strip().lower()

    # Search through each line in input file and grab emails, commit numbers, and confidence numbers
    with open(user_input_file_name) as f:
        emails = []
        commit_numbers = []
        confidence_numbers = []

        for line in f:
            if re.match("^From: ", line):
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
                emails.append(match.group(0))
            elif re.match("^Subject: ", line):
                match = re.search(r'r+[0-9]+', line)
                commit_numbers.append(match.group(0))
            elif re.match("^X-DSPAM-Confidence", line):
                match = re.search(r'[+-]?([0-9]*[.])?[0-9]+', line)
                confidence_numbers.append(match.group(0))

        headers = ["Email", "Subject", "Confidence"]

    # Writes csv file using lists of emails, commit numbers, and confidence numbers
    with open(user_output_file_name, "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(zip(emails, commit_numbers, confidence_numbers))
    print("Data stored!")


if __name__ == "__main__":
    main()
