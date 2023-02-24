#UCID: kb97 - Kush Borikar
#Date: 23rd Feb 2023

class MyCalc:

    def __init__(self):
        self.ans = 0

    def add(self,x,y):
        ans = x + y
        return ans

    def sub(self,x,y):
        ans = x - y      
        return ans
    
    def mul(self,x,y):
        ans = x * y 
        return ans

    def div(self,x,y):
        if y == 0:
            print("Error Division by zero")
            return None
        else:
            ans = x / y 
            return ans

# def handle_negative(string):
#     neg_string = string
#     newString = neg_string.replace("-","")
#     return newString 

def float_check (string):
    #Check if string is composed of only characters
    if string.isnumeric():
        return True

    #Check if string contains decimal and split
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
        #check if user wants to quit
        #splitting input into operator and operands

        if 'q' in user_input:
            print("Exiting Calculator...")
            break

        if len(user_input) != 3:
            print("Error: Invalid input format")
            break
        
        for i in range(len(user_input)):
            if(user_input[i]=="ans"):
                user_input[i] = str(calc.ans)

        num1 = user_input[0]
        operator = user_input[1]
        num2 = user_input[2]

        # if num1[0] == '-':
        #     num1 = handle_negative(num1)
        # if num2[0] == '-':
        #     num2 = handle_negative(num2)    
        
        if not float_check(num1) or not float_check(num2):
            print("Error: Invalid operands - Try Again")       

        else:

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


if __name__ == '__main__':
    main()