import pandas as pd
from sklearn.model_selection import train_test_split
import os



data = pd.read_csv('NLP-Report-Simplification/expert_fully_aligned.txt', sep='\t', header=None)

train, test = train_test_split(data, test_size=100, random_state=1125)
train, valid = train_test_split(data, test_size=0.2, random_state=1125)

def save(file, file_name):
    with open(f'{file_name}','w') as f:
        for l in file:
            f.write(l+'\n')

PATH = 'NLP-Report-Simplification/resources/datasets/SNUH'
save(train.loc[:,0], os.path.join(PATH,'train.complex'))
save(train.loc[:,1], os.path.join(PATH,'train.simple'))
save(valid.loc[:,0], os.path.join(PATH,'valid.complex'))
save(valid.loc[:,1], os.path.join(PATH,'valid.simple'))
save(test.loc[:,0], os.path.join(PATH,'test.complex'))
save(test.loc[:,1], os.path.join(PATH,'test.simple'))

print('end')