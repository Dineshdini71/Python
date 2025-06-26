import pandas as pd
from pandas import concat

# students_score = {
#     'student': ['madhu', 'harsha', 'dinesh', 'bharath'],
#     'score': [56,77, 99, 100]
# }
#
# # for (key, value) in students_score.items():
# #     print(key)
# #     print(value)
# student_DF = pd.DataFrame(students_score)
# print(student_DF)
# {new_key:new_value for (key, value) in dict.items()}
# in pandas we can use like " for (index, row) in student_score.iterrow()" should be like below
# {new_key:new_value for (index, row) in df.iterrow()}

data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for(index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)