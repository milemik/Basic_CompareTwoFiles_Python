#!/usr/bin/python3


'''
    Hi there it is a slimple check script
    are two files the same or not?
'''
if1 = input('Enter the path to the first file you want to compare\nsomething like /home/user/documents/file.txt\n')
if2 = input('Enter the path to the second file you want to compare\nsomething like /home/user/documents/file.txt\n')

file1 = open(if1,'r')
f1 = file1.read()
file2 = open(if2,'r')
f2 = file2.read()

print('text of file1 = ' + f1)
print('text of file2 = ' + f2)

if f1 == f2:
    print("File1 is same as File2")
else:
    print("File1 is not the same as File2")





