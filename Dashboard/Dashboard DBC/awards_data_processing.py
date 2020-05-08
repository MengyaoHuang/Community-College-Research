from utils import *
from flask import Flask
#You need to use following line [app Flask(__name__]
app = Flask(__name__)

# Data processing
# awards_path = "C:/Users/TK/Desktop/WCC Dashboard/Awards.xlsx"
awards_path = "/Users/mengyaohuang/Documents/Michigan/WCC Dashboard project/Dataset/Awards.xlsx"

Awards_data = pd.read_excel(awards_path)
del Awards_data['FYr']
del Awards_data['Lyr']
# Modify LMTA and NAST
Awards_data.loc[Awards_data.Prog == "CTLMTA", 'CreditGrpX'] = "LMTA"
Awards_data.loc[Awards_data.Prog == "CTLAM", 'CreditGrpX'] = "LAM"
Awards_data[Awards_data['CreditGrpX'] == "NAST"]

# aggregate table for College Awards in total
award_college = Awards_data.groupby(['AcadYr', 'CreditGrpX'], as_index=True).agg({'CountOfPIDM':'sum'}).reset_index()
award_college = award_college.set_index(['AcadYr', 'CreditGrpX']).unstack(['CreditGrpX']).reset_index()
# fillin NAN values with zero
award_college = award_college.replace('nan', np.nan).fillna(0)
level = award_college.columns.get_level_values(1).astype(str)
columns = ['AcadYr' if x == '' else x for x in level]
award_college.columns = columns
# Modify LAM/LMTA
award_college['LAM/LMTA'] = award_college['LAM'] + award_college['LMTA']
del award_college['LAM']
del award_college['LMTA']

# create available_division_options
available_division_options = list(Awards_data['Div'].unique())

# create completed blank table
complete_df = awards_subset(Awards_data)
complete_df = aggregate_shown_table(complete_df)
complete_year = list(complete_df['AcadYr'].unique())
complete_column = list(complete_df.columns)

blank_table = pd.DataFrame(columns=complete_column)
blank_table['AcadYr'] = complete_year
blank_table = blank_table.fillna(0)




