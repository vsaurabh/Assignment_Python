''' 1.) It is possible to do multiple assignments at once ? Give an example of one ?

	Ans.) Yes '''

def mul_assignment():
	'''function for multiple assignments'''
	a,b,c = 1,2,3
	print "problem 1 =>",a,b,c

'''2.) Write simple program to swapping values of 2 variables ?'''

def swapping_value(a,b):
	'''function for swapping values'''
	print "problem 2 =>"
	print "Before swapping=>" , a,b
	a,b = b,a
	print "After swapping=>" , a,b

'''3.) What will be the output of the following program ? : cube = lambda x: x ** 3

	Ans.) when we give any value of x than it will give cube of that number.
    Ex.) x=4 o/p : cube = 64'''
def lambda_fun(x):
    '''function for problem lambda function'''
    cube = lambda x: x ** 3
    print "problem 3 =>", cube(x)

'''4.) What will be the output of the following program?

	Ans.) when we give any value of a than it will give square of that number and assign to x.
	Ex.) a = 6 : o/p : x = 36'''
x = 2
def f(a):
	'''function for problem lambda function'''
	x = a*a
	print "problem 4 =>", x

'''5.) Write program using keyword argument in function ?'''
def keyword_arg(**keyword_argument):
	print "problem 5 =>",len(keyword_argument),keyword_argument

'''6.) Prints the number till 1000 those are diviable by both 3 & 5 ?'''
def num_divisable():
	print "problem 6 =>"
	for i in range(1,1001):
		if i%15==0:
			print i,

'''7.) What will be the output of the following program? l = [i**i for i in range(10) if i%2==0]
	Ans.) this will give list of the square of num which is divisable by 2 up to 10
	[1, 4, 256, 46656, 16777216]'''
def list_com():
	l = [i**i for i in range(10) if i%2==0]
	print "\n problem 7 =>", l

'''8.) What is an argument? Give an one example ?
	Ans.) An argument is a value which we pass when we called a function. Explaination given below '''
def argument_func(*argument):
	print "problem 8 =>"
	argu = [argument]
	for i in argument:
		print i

'''9.) Write program to changes all uppercase letters to lowercase and all lowercase to uppercase using string method ?'''
def string_opration():
	string = 'This is STRING contain lower and UPPERCASE letter'
	print 'problem 9 =>swap UPPER to lower =>', string.swapcase()


'''10.) What is an key and value ? Give an example of each one ?
	Ans.) Key is an unique object in dictionory which has a value, we can search value according to their key. 
	Ex.) {key:value}'''
def key_value():
	d = {5:'value',1:'value1','key3':'value2','dkey':[1,2]}
	print "problem 10 => Keys",d.keys(),'values=>',d.values()
	'''11.) Write the program to sorts keys in dictionary ?'''
	print "problem 11 => Soarted Keys",sorted(d.keys())
	'''12.) wirte the program in dictionary and convert dictionary into list of tuples ?'''
	print "problem 12 => List of tuples", d.items()

'''13.) write the program to unpack item in dictionary ?'''
def unpack_dict():
	a,b,c,d = {'key':'value','key1':'value1','key2':'value2','key4':[1,2]}
	print "problem 13 =>", a,b,c,d

'''14.) what is slice in string ? Give an one example ?
	Ans.) An object usually containing a portion of a sequence or string so when we want only some portion or an ordered portion of a string we use slicing.
	Ex.) string[start:stop:step] '''
def string_slice():
	string = '123456789'
	print "problem 14 =>", string[1:8:2], string[0:8:2], string[::-1]

'''15.) How to remove the whitespace in string in staring and ending place ? Give an one example ?
	Ans.) we remove whitespace by using strip.'''
def remove_whitespace():
	string = '        string containg spaces     '
	print "problem 15 =>",string.strip()
	print string.rstrip(),string.lstrip()

'''16.) What is differnce b/w immutable and mutable object ? Give an one example ?
	Ans.) Immutable object cannot be changed after created, but mutable object can be changed.
	Ex.) tuple is immutable because we can not add or remove new items.
		list is mutable because we can add or remove new items.'''


'''17.) Create a new list is original with three elements ? Assign this list to a new variable as reference ?
		Append a new value into reference ? What is the output for original list ?'''
def list_reference():
	l = ['python','c','ruby']
	new_l = l
	new_l.append('ipython')
	print "problem 17 =>", 'original list =>',l

'''18.) What is IndexError ? Give an one example ?
	ans.) In any sequence there is an index value which represent a perticular position 
	when we give the greter index value which is not present in that case it will through IndexError.'''
def index_error():
	list1 = [1,2,3,4]
	print "problem 18 =>", list1[2]
	try:
		print list1[5]
	except IndexError:
		print "IndexError: because the index value is out of range"


'''19.) What is keyError ? Give an one example ?
	Ans.) keyError is occurred in dictionary when we give the key which is not present in dictionary'''
def key_error():
	dict1 = {1:'python',2:'assessment'}
	print "problem 19 =>", dict1[2]
	try:
		print dict1[3]
	except KeyError:
		print "KeyError: because the key is not in dict1"

'''20.) What will be the output of the following program ?
       for x in [1, 2, 3, 4]:
            print x
        Ans.) 1
			  2
			  3
			  4
       for i  in range(10):
            print i, i*i, i*i*i
		 Ans.)  0,0,0
			    1 1 1
				2 4 8
				3 9 27
				4 16 64
				5 25 125
				6 36 216
				7 49 343
				8 64 512
				9 81 729'''

'''21.) What is the syntax of zip in list ? when we want to iterate over two lists together ?
	Ans.) syntax: zip([list1],[list2]).
			if we want to do opration like equality on same position on both lists,string than we use zip'''
def zip_list():
	list1 = [1,2,3]
	list2 = [4,2,5]
	print "problem 21 =>", zip(list1,list2)
	for a,b in zip(list1,list2):
		if a==b:
			print "a & b equal", a
		else:
			print "a & b unequal", a*b, a+b

'''22.) Write a function reverse to reverse a list. Can you do this without using list slicing ?'''
def reverse_list():
	list1 = [1,2,3,4]
	reversed_list1 = []
	for i in reversed(list1):
		reversed_list1.append(i)
	print "problem 22 =>"
	print "This is original list=>", list1
	print "This is reversed list=>", reversed_list1

'''23.) Write program using join method joins a list of strings.'''
def list_join():
	list_strings = ['This','is','Python','Assessment']
	print "problem 23 =>", ' '.join(list_strings)


def main():
	mul_assignment()
	swapping_value(4,5)
	lambda_fun(7)
	f(6)
	keyword_arg(a=1,b='a',c='problem 5')
	num_divisable()
	list_com()
	argument_func(1,2,3,4,5)
	string_opration()
	key_value()
	unpack_dict()
	string_slice()
	remove_whitespace()
	list_reference()
	index_error()
	key_error()
	zip_list()
	reverse_list()
	list_join()

if __name__ == '__main__':
	main()
