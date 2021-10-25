    def collatz(number):

        if (number % 2) == 0:			# if number % 2 ==0:
            newNumber = number // 2		#print(number // 2)
            print(newNumber)			#return number //2

        elif (number % 2) == 1:			#elif number % 2 == 1:
            newNumber = number * 3 + 1		#result = 3* number + 1
            print(newNumber)			#print(result)
    						#retun result
    print('Enter a number')		
    number = int(input())			#n = input("give me a number")
    collatz(number)				#while n != 1:
						    # n = collatz(int(n))
