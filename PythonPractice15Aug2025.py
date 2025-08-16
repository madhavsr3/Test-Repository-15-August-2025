# Define the scores for each subject
grades = {
    "English": 90,
    "Math": 85,
    "Science": 50, "History": 100
}

# Function to convert numeric grade to letter grade
def get_letter_grade(score):
    if score > 95:
        return 'A'
    elif 85 <= score <= 95:
        return 'B'
    else:
        return 'C'

# Calculate and print the grade for each subject
print("Subject Grades:")
for subject, score in grades.items():
    letter_grade = get_letter_grade(score)
    print(f"{subject}: {score}/100 → Grade {letter_grade}")

# Calculate the overall average score
max_score = max(grades.values())

# Get the overall letter grade
overall_grade = get_letter_grade(max_score)

# Print overall result
print("\nOverall Performance:")
print(f"Minimum Score: {max_score:.2f}/100 → Grade {overall_grade}")
