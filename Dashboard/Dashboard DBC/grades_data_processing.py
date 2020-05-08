import pandas as pd
from utils import pie_chart_percent_combine

# grades_path = "C:/Users/TK/Desktop/WCC Dashboard/grades.csv"
grades_path = "/Users/mengyaohuang/Documents/Michigan/WCC Dashboard project/Dataset/grades.csv"
grades_data = pd.read_csv(grades_path)

# rename some variables
grades_data.columns = ['Ethnicity' if x=='Ethx' else x for x in grades_data.columns]
grades_data.columns = ['SemCrAtt Grouped' if x=='SemCrAttx' else x for x in grades_data.columns]
grades_data.columns = ['SemCrErn Grouped' if x=='SemCrErnx' else x for x in grades_data.columns]

# exclude UA category
grades_data = grades_data[grades_data['UA'] != 1]
grades_data = grades_data[grades_data['FTrmCrAtt'].notnull()]
grades_data['PIDM_Term'] = grades_data['PIDM'].astype(str) + " " + grades_data['Term'].astype(str)

# overall not duplicated numbers
overall_unduplicated_dic = {}
overall_unduplicated_dic['Course'] = len(grades_data[grades_data['Course'].notnull()]['Course'].unique())
overall_unduplicated_dic['PIDM'] = len(grades_data[grades_data['PIDM'].notnull()]['PIDM'].unique())
overall_unduplicated_dic['InstrPIDM'] = len(grades_data[grades_data['InstrPIDM'].notnull()]['InstrPIDM'].unique())
overall_unduplicated_dic['TermCRN'] = len(grades_data[grades_data['TermCRN'].notnull()]['TermCRN'].unique())
overall_unduplicated_dic['Awards'] = len(grades_data[grades_data['AwardThatTerm'] == 1]['PIDM_Term'].unique())

# set up category dictionary
category_dic = {}
category_dic['Period'] = ["AcadYr", "Term", "FWS"]
category_dic['Graduation Status'] = ["AwardThatYr", "AwardThatTerm"] # Yr-e.g 2018-19: 201809/201901/201905
category_dic['Grade'] = ["Succ", "GradeGrp", "Grade", "SemGPAx"]
category_dic['Unit'] = ["Div", "Dept", "Disc", "Prog"]
category_dic['Course'] = ["Credit", "DelMode", "Number", "PTerm", "DelMdType"]
category_dic['Faculty'] = ["FacCat", "FacName", "FT_PT"] # FT_PT: full time or part time instructor
category_dic['Credits'] = ["FTrmCrAtt", "SecTrmAtt", "SemCrAtt Grouped", "SemCrErn Grouped"]
category_dic['Education'] = ["HSGPAx", "EDLV", "EGOL", "CTE_Transfer", "PT_FT", "DevEd"] # PT_FT: 12 credits
category_dic['Demographic'] = ["AgeGrp", "Ethnicity",  "Gender", "Resid", "VET", "PELL"]
category_dic['Persistence'] = ["New_NotNew", "NextTrmAtt", "NextYrAtt"]

# RENAME: Modify the name for some options
grades_data['AwardThatTerm'] = grades_data['AwardThatTerm'].replace(0, "No")
grades_data['AwardThatTerm'] = grades_data['AwardThatTerm'].replace(1, "Yes")
grades_data['AwardThatYr'] = grades_data['AwardThatYr'].replace(0, "No")
grades_data['AwardThatYr'] = grades_data['AwardThatYr'].replace(1, "Yes")
grades_data['Succ'] = grades_data['Succ'].replace(0, "No")
grades_data['Succ'] = grades_data['Succ'].replace(1, "Yes")
grades_data['Succ'] = grades_data['Succ'].fillna("blanks")
grades_data['FacCat'] = grades_data['FacCat'].fillna("blanks")
grades_data['FT_PT'] = grades_data['FT_PT'].fillna("blanks")
grades_data['FacName'] = grades_data['FacName'].fillna("blanks")
grades_data['SecTrmAtt'] = grades_data['SecTrmAtt'].fillna("blanks")
grades_data['SemCrAtt Grouped'] = grades_data['SemCrAtt Grouped'].replace("?", "blanks")
grades_data['SemCrErn Grouped'] = grades_data['SemCrErn Grouped'].replace("Missing", "blanks")
grades_data['EDLV'] = grades_data['EDLV'].fillna("blanks")
grades_data['EGOL'] = grades_data['EGOL'].fillna("blanks")
grades_data['CTE_Transfer'] = grades_data['CTE_Transfer'].fillna("blanks")
grades_data['DevEd'] = grades_data['DevEd'].fillna("blanks")
grades_data['Ethnicity'] = grades_data['Ethnicity'].fillna("blanks")
grades_data['NextTrmAtt'] = grades_data['NextTrmAtt'].replace(0, "No")
grades_data['NextTrmAtt'] = grades_data['NextTrmAtt'].replace(1, "Yes")
grades_data['NextYrAtt'] = grades_data['NextYrAtt'].replace(0, "No")
grades_data['NextYrAtt'] = grades_data['NextYrAtt'].replace(1, "Yes")
grades_data['PELL'] = grades_data['PELL'].replace(0, "No")
grades_data['PELL'] = grades_data['PELL'].replace(1, "Yes")


# data processing for overall college pie charts
overall_pie_form = grades_data.groupby(["Succ", "GradeGrp"])['PIDM'].count().reset_index()
overall_pie_form['percent'] = overall_pie_form['PIDM']/sum(overall_pie_form['PIDM'])
overall_pie_form_one = overall_pie_form[overall_pie_form['Succ'] == "Yes"]
overall_pie_form_zero = overall_pie_form[overall_pie_form['Succ'] == "No"]

labels_one_list = list(overall_pie_form_one['GradeGrp'])
values_one_list = list(overall_pie_form_one['percent'])
labels_one_list, values_one_list = pie_chart_percent_combine(labels_one_list, values_one_list)

labels_zero_list = list(overall_pie_form_zero['GradeGrp'])
values_zero_list = list(overall_pie_form_zero['percent'])
labels_zero_list, values_zero_list = pie_chart_percent_combine(labels_zero_list, values_zero_list)

# possible colors to use for pie charts
# https://digitalsynopsis.com/design/minimal-web-color-palettes-combination-hex-code/
# https://digitalsynopsis.com/design/beautiful-color-palettes-combinations-schemes/
# ["#4b3832", "#854442", "#3c2f2f", "#fff4e6", "#be9b7b"]
possible_colors_zero = ["#96ceb4", "#ffeead", "#ff6f69", "#ffcc5c", "#1e1f26"]
possible_colors_one = ["#E5FCC2", "#9DE0AD", "#45ADA8", "#547980", "#594F4F"]
