# Collatz_Conjecture_Project
A project that is designed to show the number of iterations for each number (1-100,000 here) and determine the number of iterations of the Collatz conjecture that number needs to get to 1. For a description of the Collatz conjecture, [click here](https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/).

## Process
I started by building the function collatz_test to act as the engine for the scatterplot function. This function is meant to take in any input, determine if the input meets the criteris for the Collatz conjecture, and (if it does) to count the number of iterations necessary to come to 1. Then I built the plotter, which takes in a starting number and an ending number, populates the numbers inbetween to a series in pandas, and graphs both the numbers and the number of iterations from collatz_test. Below is a picture of the resultsfor the numbers 1 through 100,000.

<img src="https://github.com/aadams10046/Collatz_Conjecture_Project/blob/main/Collatz_1_to_100000.png?raw=true" alt="Graph for Collatz Iterations 1-100,000" title="Results">

## Skills Demonstrated
* Python: including seaborn, pandas series, building functions, and mathematical logic

## Full Python Code Below

```python
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
```
