# lambda exercise
def fun(n):
    r = lambda x : x * 15
    return r(n)
print(fun(2))


def funn(z):
    return (lambda z : z *15)(z)

print(funn(3))



A= [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_A = sorted(A,key = lambda x: x["make"])

print(sorted_A)

def analyze_scores(scores):
    # Group scores into student score groups of 3
    students = list(map(lambda i: scores[i:i+3], range(0, len(scores), 1)))

    # Total students
    total_students = len(students)

    # Filter valid students using lambda (no 0 in their scores)
    valid_students = list(filter(lambda s: 0 not in s, students))
    num_valid = len(valid_students)

    # Output
    print("Total number of students:", total_students)
    print("Number of students with all valid scores:", num_valid)
    print("Scores of students with only valid scores:", valid_students)

# Example input
scores = [100, 90, 95, 90, 0, 93, 88, 79, 85]
analyze_scores(scores)
