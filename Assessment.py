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

def main():
	mul_assignment()
	swapping_value(4,5)
	lambda_fun(7)
	f(6)
	keyword_arg(a=1,b='a',c='problem 5')
	num_divisable()


if __name__ == '__main__':
	main()
