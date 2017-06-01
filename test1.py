# Press COMMAND + ENTER to run a single line in the console
print('Welcome to Rodeo!')

# Press CTRL + ENTER with text selected to run multiple lines
# For example, select the following lines
x = 7
x**2
# and remember to press CTRL + ENTER

# Here is an example of using Rodeo:

# Install packages


# Import packages

import numpy as np
import pandas as pd

N = 100
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })
df.head()

# Another example of making a plot:

words=['cat','blue','differentiate']

for w in words[:]:
    print(w,len(w))

    words
