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


if __name__ == '__main__':
	main()
