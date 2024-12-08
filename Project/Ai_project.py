    #setting Basic libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings

warnings.filterwarnings('ignore')

#loading the data 

df = pd.read_excel(r'C:\Users\dell\Desktop\الكليه\3rd year\AI\Project\Datasets\Adult Census Income_Dataset.xlsx')

df.head(10)

