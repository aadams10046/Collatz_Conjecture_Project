#Importing the necessary libraries for the task
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Defining a function to check that the numbers meet the criteria of the Collatz conjecture, then find the number of iterations of Collatz are necessary
def collatz_test(num):
    if num <= 0:
        print(f'{num} is not a valid input.\nPlease choose a number greater than or equal to 1.')
    elif num == 1:
        return 0
    else:
        collatz_num = 0
        new_num = num
        while new_num != 1:
            if new_num % 2 == 0:
                new_num = int(new_num/2)
                collatz_num += 1
            else:
                new_num = int((new_num*3)+1)
                collatz_num += 1
        return collatz_num

#Defining a function that plots the numbers and the number of iterations for each number from a start_num to an end_num using seaborn
def seaborn_plot(start_num,end_num):
    if int(start_num)<=0 or end_num<=0:
        pass
    else:
        data = pd.DataFrame(data = pd.Series([collatz_test(x) for x in range(start_num, end_num + 1)], [x for x in range(start_num, end_num + 1)]))
        print(data)
        sns.scatterplot(data, palette = 'pastel', legend = [])
        plt.xlabel('Number')
        plt.ylabel('Number of Iterations')
        plt.title('Number vs. Number of Collatz Iterations')
        plt.show()

#Using seaborn_plot to create a scatterplot of the results for numbers 1 through 100000
seaborn_plot(1, 100000)
