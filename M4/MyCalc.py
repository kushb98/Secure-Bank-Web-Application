#UCID: kb97 - Kush Borikar
#Date: 23rd Feb 2023

class MyCalc:

    def __init__(self):
        self.ans = 0
        #UCID: kb97 - Kush Borikar
        #Date: 23rd Feb 2023
        #this initializes the value of ans to 0    

    def add(self,x,y):
        ans = x + y
        return ans
        #this function performs the addition operation on operands
        # UCID: kb97 - Kush Borikar
        #Date: 23rd Feb 2023  

    def sub(self,x,y):
        ans = x - y      
        return ans
        #this function performs the substraction operation on operands
        # UCID: kb97 - Kush Borikar
        #Date: 23rd Feb 2023 
    
    def mul(self,x,y):
        ans = x * y 
        return ans
        #this function performs the multiplication operation on operands
        # UCID: kb97 - Kush Borikar
        #Date: 23rd Feb 2023 

    def div(self,x,y):
        if y == 0:
            print("Error Division by zero")
            return None
        else:
            ans = x / y 
            return ans
        #this function performs the division operation on operands and also handles division by 0 
        # UCID: kb97 - Kush Borikar
        #Date: 23rd Feb 2023

def float_check (string):
    #Check if string is composed of only characters
    # UCID: kb97 - Kush Borikar
    #Date: 23rd Feb 2023
    if string.isnumeric():
        return True

    #Check if string contains decimal point and split
    # UCID: kb97 - Kush Borikar
    #Date: 23rd Feb 2023
    parts = string.split('.')
    if len(parts) == 2 and parts[0].isnumeric() and parts[1].isnumeric():
        return True

    if string.startswith('-'):
        return float_check(string[1:])    

    return False        

def main():
    calc = MyCalc() 
    while True:
        #ask for user input
        user_input = input("Enter a valid equation (e.g. 2 * 3) or Enter 'q' to quit : ").split()
        #splitting input into operator and operands

        #check if user wants to quit
        if 'q' in user_input:
            print("Exiting Calculator...")
            break

        #check if user has entered valid expression
        if len(user_input) != 3:
            print("Error: Invalid input format, Please check correct input format in input prompt")
            break
        
        #if user wants to use previous answer to perform a new expression, this function will handle it
        for i in range(len(user_input)):
            if(user_input[i]=="ans"):
                user_input[i] = str(calc.ans)

        for i in range(len(user_input)):
            if(user_input[i]=="-ans"):
                user_input[i] = str((calc.ans) * (-1))
                #user_input = str(calc.ans)           

        #assign input elements to variables
        num1 = user_input[0]
        operator = user_input[1]
        num2 = user_input[2]  
        
        #this will check if the entred operands are in valid format or not 
        if not float_check(num1) or not float_check(num2):
            print("Error: Invalid operands - Try Again")       

        else:
            #convert operands to float for arithmetic functions
            num1 = float(num1)
            num2 = float(num2)


            #performing calculations
            if operator == '+' :
                calc.ans=calc.add(num1,num2)

            elif operator == '-' :
                calc.ans=calc.sub(num1,num2)

            elif operator == '*' :
                calc.ans=calc.mul(num1,num2)

            elif operator == '/' :
                calc.ans=calc.div(num1,num2)  

            else:
                print("Error - Invalid Operator")
                continue

            if calc.ans == -0.0:
                calc.ans = 0.0

            print("Answer:" , calc.ans)


#calling main function
if __name__ == '__main__':
    main()