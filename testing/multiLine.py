# [OBJETIVE] 
# create a text file and write the items of list 
#       list = [1, 2, 3, 4]
# to that file

# the text file content should look like following

#   1
#   2
#   3
#   4
# 

numbers = [1, 2, 3]

with open ("listNumbers.txt", "w") as f:
    for s in numbers:
        f.write(str(s) + "\n")
