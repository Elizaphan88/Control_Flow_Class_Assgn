# Rating students performance 
 
def performance_rating(students_score):
    if students_score >= 80:
        return "Distinction!"  
    elif  60 <= students_score <  80:
        return "Credit!" 
    elif 40 <= students_score < 60:
        return "Fair!" 
    else:
        return "Fail!"

students_score = float(input("Enter student's score: "))
rating = performance_rating(students_score)
print(f"Student's Performance: {rating}") 

# Simple Calculator:

def calculator():
    num1 = float(input("Enter First Number: "))
    operation = input("Enter Operation (+, -, *, /): ")
    num2 = float(input("Enter Second Number: "))
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero is not allowed!"
    else:
        return "Error! Invalid operation!"
    return f"Operation Result: {result}"
Calculation_Result = calculator()
print(Calculation_Result)