# This if FS is used to read a content from the "txt" File. Note initially, Mode was in "Read" State.
with open("/Users/admin/Desktop/dup.txt") as file:
    content = file.read()
    print(content)
#  This is used to write the content and create the file and explicitly mentioned MODE name here as "W" for write.

with open("new_file.txt", mode='w') as f:
    f.write("I'm creating the new file using python and writing this content...")


# This FS will be work appened the content from the existing the file.

with open("new_file.txt", mode='a') as e:
    e.write("\nThis line is written and added in append mode!")