friends = ['madhu', 'harsha','charan','akhil','hari']
for frnd in friends:
    print(frnd)

print('---------------------------------')
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high = 0
for max in student_scores:
    if max >= high:
        high = max
print(high)
