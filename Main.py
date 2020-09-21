
'''
The purpose of this script will be:

to parse and analyse federal data on nursing home facilities from Data.gov

it will output:

-A list of categories of data available in the raw data
-A dataframe of relevent data averaged by state
-A graph showing the adjusted score mean, expected score mean, and difference between the two sorted by state and ordered by adjusted score.

'''

import pandas as pd


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
get_list = ['Federal Provider Number', 'Provider Name', 'Provider State', 'Provider Zip Code', 'Measure Code',
        'Adjusted Score','Observed Score', 'Expected Score']


df = pd.read_csv('raw_data/Medicare_Claims_Quality_Measures.csv')
df = df.get(get_list)
print(df.dtypes)

df_state_means = pd.DataFrame(columns = ['exp', 'adj', 'dif'], index = states)
for state in states:
    adj = df['Adjusted Score'][df['Provider State'] == state].mean()
    exp = df['Expected Score'][df['Provider State'] == state].mean()
    dif = adj - exp

    df_state_means.loc[state]['adj'] = adj
    df_state_means.loc[state]['exp'] = exp
    df_state_means.loc[state]['dif'] = dif
df_sorted = df_state_means.sort_values(by=['adj'], ascending=False)
print(df_sorted)
ax = df_sorted.sort_values(by=['adj'], ascending=False).plot.bar(figsize = (12,4))
ax.plot


df_ss_hospitalize = df[df['Measure Code'] == 521]
df_ss_outpatient = df[df['Measure Code'] == 522]
df_ls_hospitalize = df[df['Measure Code'] == 551]
df_ls_outpatient = df[df['Measure Code'] == 552]


# In[ ]:
