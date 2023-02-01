import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

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

seaborn_plot(1, 100000)