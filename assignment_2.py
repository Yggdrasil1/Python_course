solution_student = []

# Assignment 01:
# a = 5
# b = 0.
# c = a + b
# type(c)

solution_student.append(None)

# Assignment 02:
# a = 5
# b = 3
# c = a // b
# c

solution_student.append(None)

# Assignment 03:
# a = True
# b = False
# (a | (a & b))

solution_student.append(None)

# Assignment 04:
# a = 5
# b = []
# b.append(a)
# a = 7
# b[0]

solution_student.append(None)

# Assignment 05:
# a = [1, 2, 3]
# b = {'list_a': a}
# a.append(4)
# b['list_a']

solution_student.append(None)

# Assignment 06:
# a = [1, 2, 1, 3, 3, 4, 1]
# b = set(a)
# b

solution_student.append(None)

# Assignment 07:
# a = 'glutamat'
# b = a
# b = b + 'e'
# a is b

solution_student.append(None)

# Assignment 08:
# a = (1.3, 7.8)
# b = a + ('glo',)
# b

solution_student.append(None)

# Assignment 09:
# a = 'ananas'
# a.replace('a', 'ana')
# a

solution_student.append(None)

# Assignment 10:
# a = ['x', 9]
# b = (a, 'glob')
# a.append(100)
# b

solution_student.append(None)

# Assignment 11:
# a = {1: 'Finn', 2: 'Jake'}
# a.pop(1)
# 1 in a

solution_student.append(None)

# Assignment 12:
# x = 0
# for i in range(0, 1):
#     x = x + 1
# x

solution_student.append(None)

# Assignment 13:
# a = [1, 2, 3]
# a.append((4, 5))
# if 4 in a:
#     print('YESSA')
# else:
#     print('OH NO')

solution_student.append(None)

# Assignment 14:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = a[3:5]
# b

solution_student.append(None)

# Assignment 15:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []
# for x in a:
#     if x < 5:
#         b.append(True)
#     else:
#         b.append(False)
# c = set(b)
# c

solution_student.append(None)

# Assignment 16:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 0
# for x in a:
#     if x % 2 == 0:
#         b = b + 1
# b

solution_student.append(None)

# Assignment 17:
# a = ['ivo', 'mato', 'jure', 'ante', 'stop', 'marcelo', 'nicola', 'stephan']
# b = []
# for name in a:
#     if name == 'stop':
#         break
#     b.append(name)
# b

solution_student.append(None)

# Assignment 18:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []
# for x in a:
#     if x % 2 == 0:
# 	      continue
#     b.append(x**2)
# b

solution_student.append(None)

# Assignment 19:
# student_points = {'Hans': 91, 'Maria': 75.5, 'Stephan': 53, 'Julia': 89}
# limit = 80
# passed = []
# for student, points in student_points.items():
#     if points >= limit:
#         passed.append(student)
# set(passed)

solution_student.append(None)

# Assignment 20:
# a = [1, 2, 3, 4]
# b = a
# b.append(80)
# a

solution_student.append(None)


if __name__ == '__main__':
    import _pickle
    with open('./solution/solution_2.pkl', 'rb') as solution_file:
        solution_tutors = _pickle.load(solution_file)
    if solution_tutors == solution_student:
        print('Solved!')
    else:
        false_answers = []
        for index, answer in enumerate(solution_student):
            if answer != solution_tutors[index]:
                false_answers.append(str(index + 1))
            else:
                pass
        print('Try Again! Answer(s) for the assignment(s) {} are wrong'.format(', '.join(false_answers)))