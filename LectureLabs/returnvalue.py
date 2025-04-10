#Ask for inputs
score1 = int(input('Enter score 1: '))
score2 = int(input('Enter score 2: '))

#define a function called avg that takes two numbers
def avg(x, y):
    #add those to numbers together (whatever they are)
    #and divide them by 2 to get the average
    return (x + y) / 2

#New variable to store the result of the score1 variable 
#and score2 variable to replace x and y in the function
result = avg(score1, score2)

#Print the result variable
print('The average score is:', result)