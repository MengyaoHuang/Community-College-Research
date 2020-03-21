import pandas as pd

courses_path = "C:/Users/TK/Desktop/WCC Dashboard/Courses.xlsx"
Courses_data = pd.read_excel(courses_path)

# summary overall college level data
Courses_data['SuccessPIDM'] = Courses_data['CountOfPIDM'] * Courses_data['Succ']
available_semester_options = ['Fall', 'Sp/Su', 'Winter']
completed_academic_year = list(Courses_data['AcadYr'].unique())