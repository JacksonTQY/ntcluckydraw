import pandas as pd
import numpy as np
import sys

col_name = 'names'

df = pd.read_csv("NTC_participants.csv")

consolation = df.sample(n=10, replace=False)

#print(consolation)

print('Consolation prize winners are: ')
print(consolation[col_name].to_string(index=False, header=False))

remaining = df.loc[~(df.names.isin(consolation[col_name]))]

user_input = ''

user_input = input('Continue to third prize? (Y/N) ')

if user_input.lower()=='n':
    sys.exit()

user_input = ''

while user_input.lower()!='y':
    third_prize = remaining.sample(n=1, replace=False)
    print('The third prize goes to: ' + third_prize.iloc[0][col_name])
    remaining = remaining.loc[~(remaining.names.isin(third_prize[col_name]))]
    user_input = input('Continue to second prize? (Y/N) ')
    if user_input.lower()=='n':
        print('Seems like ' + third_prize.iloc[0][col_name] + ' is not here so ...')
    
user_input = ''

while user_input.lower()!='y':
    second_prize = remaining.sample(n=1, replace=False)
    print('The second prize goes to: ' + second_prize.iloc[0][col_name])
    remaining = remaining.loc[~(remaining.names.isin(second_prize[col_name]))]
    user_input = input('Continue to first prize? (Y/N) ')
    if user_input.lower()=='n':
        print('Seems like ' + second_prize.iloc[0][col_name] + ' is not here so ...')
    
user_input = ''

while user_input.lower()!='y':
    first_prize = remaining.sample(n=1, replace=False)
    print('The first prize goes to: ' + first_prize.iloc[0][col_name])
    remaining = remaining.loc[~(remaining.names.isin(first_prize[col_name]))]
    user_input = input('Continue to end the prize giving ceremony? (Y/N) ')
    if user_input.lower()=='n':
        print('Seems like ' + first_prize.iloc[0][col_name] + ' is not here so ...')
    
