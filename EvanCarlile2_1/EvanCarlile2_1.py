def input_number_of_students():
    # Takes input for the number of students
    number_of_students = int(input('Total number of students: '))
    return number_of_students


def input_scores(number_of_students):
    # Takes input for scores (separated by a space) up to specified number of students
    list_of_scores = []
    while len(list_of_scores) < number_of_students:
        score_input = input(f'Enter {number_of_students} score(s): ').strip()
        if len(score_input.split()) >= number_of_students:
            for scores in score_input.split():
                if len(list_of_scores) < number_of_students:
                    list_of_scores.append(scores)
    return list_of_scores


def scores_list_to_dictionary(list_of_scores):
    # Convert list of scores into a dictionary
    student_scores = {}
    for count, score in enumerate(list_of_scores):
        student_scores[count + 1] = int(score)
    return student_scores


def scores_to_letter_grade(student_scores):
    # Convert scores to letter grade and prints grade
    best_score = max(student_scores.values())
    for student, score in student_scores.items():
        if score >= best_score - 10:
            print(f'Student {student} score is {score} and grade is A')
        elif score >= best_score - 20:
            print(f'Student {student} score is {score} and grade is B')
        elif score >= best_score - 30:
            print(f'Student {student} score is {score} and grade is C')
        elif score >= best_score - 40:
            print(f'Student {student} score is {score} and grade is D')
        else:
            print(f'Student {student} score is {score} and grade is F')


def main():
    number_of_students = input_number_of_students()
    list_of_scores = input_scores(number_of_students)
    student_scores = scores_list_to_dictionary(list_of_scores[:])
    scores_to_letter_grade(student_scores)


if __name__ == '__main__':
    main()
