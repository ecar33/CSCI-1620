import re
import csv


def main():
    with open('files/input.txt') as f:
        emails_list = []
        dspam_list = []
        dspam_confidence_total = 0
        emails_d = {}
        for line in f:
            if re.match("^From: ", line):
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
                emails_list.append(match.group(0))
            elif re.match("^X-DSPAM-Confidence", line):
                match = re.search(r'[+-]?([0-9]*[.])?[0-9]+', line)
                dspam_list.append("X-DSPAM-Confidence: " + match.group(0))
                dspam_confidence_total += float(match.group(0))
        for email in emails_list:
            if email not in emails_d:
                emails_d[email] = 1
            else:
                emails_d[email] += 1
        emails_d["TOTAL"] = 27
        emails_d_csv = {"Email": [], "Count": []}

        for key, value in emails_d.items():
            emails_d_csv["Email"].append(key)
            emails_d_csv["Count"].append(value)

    sum_of_confidence = dspam_confidence_total
    average_of_confidence = dspam_confidence_total / len(dspam_list)
    keys = emails_d_csv.keys()

    with open("output.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(keys)
        writer.writerows(zip(*[emails_d_csv[key] for key in keys]))

    with open(r"files\output.txt", 'w') as f:
        for line in dspam_list:
            f.write(f'{line}\n')
        f.write('-------------------------------------------------\n')
        f.write(f"Total dspam confidence = {sum_of_confidence:.2f}\n")
        f.write(f"Average dspam confidence = {average_of_confidence:.2f}\n")


if __name__ == "__main__":
    main()
