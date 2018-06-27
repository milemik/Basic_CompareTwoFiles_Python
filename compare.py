#!/usr/bin/python3


'''
    Hi there it is a slimple check script
    are two files the same or not?
'''
#take the path of first dir
if1 = input('Enter the path to the first file you want to compare\nsomething like /home/user/documents/file.txt\n')
#take the path of second dir
if2 = input('Enter the path to the second file you want to compare\nsomething like /home/user/documents/file.txt\n')
#opening first dir
file1 = open(if1,'r')
#read first dir
f1 = file1.read()
#open second dir
file2 = open(if2,'r')
#read second dir as f2
f2 = file2.read()
#print content of first dir
print('text of file1 = ' + f1)
#print content of second dir
print('text of file2 = ' + f2)

#check if thay are the same
if f1 == f2:
    #if thay are the same print "File1 is the same as File2"
    print("File1 is same as File2")
    #if thay are not the same
else:
    print("File1 is not the same as File2")





