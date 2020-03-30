# make some preparation for packages
# package use
import requests
import urllib
import urllib.request
import time
import re

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import copy
import datetime
from collections import Counter

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

from courses_data_processing import completed_academic_year

# create functions for Awards subset extraction plots
def awards_subset(dataset_, div_list=[], dept_list=[], prog_list=[]):
    # given input should be in list for filtering
    temp = dataset_
    if len(div_list) >= 1:
        temp = temp[temp['Div'].isin(div_list)]
    if len(dept_list) >= 1:
        temp = temp[temp['Dept'].isin(dept_list)]
    if len(prog_list) >= 1:
        temp = temp[temp['Prog'].isin(prog_list)]
    return temp

# show tables in html
def generate_table(dataframe, left_margin_str, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))],
        style={"marginLeft": str(left_margin_str)+"px", 'overflow': 'scroll'},
    )

# try to modify award_college dataset into figure data type
def figure_data_modify(award_college_):
    # return a list of dictionary for multiple line plots
    award_college_column = list(award_college_.columns)
    data_list = []
    for i in range(1, len(award_college_column)):
        temp_dic = {'mode': 'lines+markers', 'marker': {'size': 12}, 'x': list(award_college_['AcadYr'])}
        temp_dic['name'] = award_college_column[i]
        temp_dic['y'] = list(award_college_[temp_dic['name']])
        # give text and customdata info
        temp_dic['text'] = [ temp_dic['x'][j] + " " + temp_dic['name'] + " " + str(temp_dic['y'][j]) for j in range(len(temp_dic['x']))]
        temp_dic['customdata'] = ['c.' + str_ for str_ in temp_dic['text']]
        # append
        data_list.append(temp_dic)
    return data_list

# Aggregate any given table into award_college format
def aggregate_shown_table(data_to_aggregate):
    # here data_to_aggregate is related to specific Div/Dep/Prog
    temp = data_to_aggregate.groupby(['AcadYr', 'CreditGrpX'], as_index=True).agg({'CountOfPIDM':'sum'}).reset_index()
    temp = temp.set_index(['AcadYr', 'CreditGrpX']).unstack(['CreditGrpX']).reset_index()
    temp = temp.replace('nan', np.nan).fillna(0)
    level = temp.columns.get_level_values(1).astype(str)
    columns = ['AcadYr' if x == '' else x for x in level]
    temp.columns = columns
    try:
        temp['LAM/LMTA'] = temp['LAM'] + temp['LMTA']
        del temp['LAM']
        del temp['LMTA']
    except:
        temp = temp
    return temp

# create functions for Courses subset extraction plots
# Here num list contains string
def courses_subset(dataset_, div_list=[], dept_list=[], disc_list=[], num_list=[], sect_list=[], term_list=[]):
    # given input should be in list for filtering
    temp = dataset_
    if len(div_list) >= 1:
        temp = temp[temp['Div'].isin(div_list)]
    if len(dept_list) >= 1:
        temp = temp[temp['Dept'].isin(dept_list)]
    if len(disc_list) >= 1:
        temp = temp[temp['Disc'].isin(disc_list)]
    if len(num_list) >= 1:
        temp = temp[temp['Num'].isin(num_list)]
    if len(sect_list) >= 1:
        temp = temp[temp['Sect'].isin(sect_list)]
    if len(term_list) >= 1:
        temp = temp[temp['Term'].isin(term_list)]
    return temp

# Aggregate any given table into shown format
def aggregate_shown_table_enroll_succ(data_to_aggregate, completed_academic_year_ = completed_academic_year):
    # here data_to_aggregate is related to specific Div/Dep/Disc/Num/Section
    # Dont drop NA for Enrollment data
    temp_enroll = data_to_aggregate.groupby(['AcadYr', 'FWS'], as_index=True).agg({'CountOfPIDM': 'sum'}).reset_index()
    temp_enroll = temp_enroll.set_index(['AcadYr', 'FWS']).unstack(['FWS']).reset_index()
    temp_enroll = temp_enroll.replace('nan', np.nan).fillna(0)
    level = temp_enroll.columns.get_level_values(1).astype(str)
    columns = ['AcadYr' if x == '' else x for x in level]
    temp_enroll.columns = columns

    # Drop NA for Success Rate data
    temp_success = data_to_aggregate.dropna()
    temp_success = temp_success.groupby(['AcadYr', 'FWS'], as_index=True).agg(
        {'CountOfPIDM': 'sum', 'SuccessPIDM': 'sum'}).reset_index()
    temp_success = temp_success.set_index(['AcadYr', 'FWS']).unstack(['FWS']).reset_index()
    temp_success = temp_success.replace('nan', np.nan).fillna(0)
    level0 = temp_success.columns.get_level_values(0).astype(str).tolist()
    level1 = temp_success.columns.get_level_values(1).astype(str).tolist()
    level_all = [level0[i] + level1[i] for i in range(len(level0))]
    temp_success.columns = level_all
    # fill in missing year enrollment records with zero
    # set up a blank table
    success_blank_table = pd.DataFrame(columns=level_all)
    success_blank_table['AcadYr'] = completed_academic_year_
    success_blank_table = success_blank_table.fillna(0)
    temp_success = pd.concat([temp_success, success_blank_table]).drop_duplicates()
    temp_success = temp_success.fillna(0).groupby("AcadYr").sum().reset_index()

    # calculate and aggregate results
    temp_result = pd.DataFrame()
    temp_result['AcadYr'] = temp_enroll['AcadYr']
    try:
        temp_result['Fall(E)'] = temp_enroll['Fall']
    except:
        pass
    try:
        temp_result['Winter(E)'] = temp_enroll['Winter']
    except:
        pass
    try:
        temp_result['Sp/Su(E)'] = temp_enroll['Sp/Su']
    except:
        pass
    # fill in missing year enrollment records with zero
    # set up a blank table
    complete_courses_table_column = list(temp_result.columns)
    courses_blank_table = pd.DataFrame(columns=complete_courses_table_column)
    courses_blank_table['AcadYr'] = completed_academic_year_
    courses_blank_table = courses_blank_table.fillna(0)

    temp_result = pd.concat([temp_result, courses_blank_table]).drop_duplicates()
    temp_result = temp_result.fillna(0).groupby("AcadYr").sum().reset_index()

    try:
        temp_result['Fall(SR)'] = temp_success['SuccessPIDMFall'] / temp_success['CountOfPIDMFall']
        temp_result[['Fall(SR)']] = temp_result[['Fall(SR)']].applymap(lambda x: "{0:.1f}%".format(x * 100))
        # replace all "nan%" with "--"
        temp_result[['Fall(SR)']] = temp_result[['Fall(SR)']].replace("nan%", "--")
    except:
        pass
    try:
        temp_result['Winter(SR)'] = temp_success['SuccessPIDMWinter'] / temp_success['CountOfPIDMWinter']
        temp_result[['Winter(SR)']] = temp_result[['Winter(SR)']].applymap(lambda x: "{0:.1f}%".format(x * 100))
        # replace all "nan%" with "--"
        temp_result[['Winter(SR)']] = temp_result[['Winter(SR)']].replace("nan%", "--")
    except:
        pass
    try:
        temp_result['Sp/Su(SR)'] = temp_success['SuccessPIDMSp/Su'] / temp_success['CountOfPIDMSp/Su']
        temp_result[['Sp/Su(SR)']] = temp_result[['Sp/Su(SR)']].applymap(lambda x: "{0:.1f}%".format(x * 100))
        # replace all "nan%" with "--"
        temp_result[['Sp/Su(SR)']] = temp_result[['Sp/Su(SR)']].replace("nan%", "--")
    except:
        pass
    return temp_result

# Aggregate any given table into shown format - for grades specifically
def aggregate_shown_table_enroll_succ_grades(data_to_aggregate, FacNameOrNot = True):
    # here data_to_aggregate is related to specific course
    # FacName indicates show or not show Faculty name - default hide
    if FacNameOrNot:
        rename_column = ['Sect', 'CRN', 'FacName', '(E)', '(SR)']
        temp_df_enroll_succ = data_to_aggregate.groupby(['Sect'], as_index=True).agg(
            {'CRN': 'min', 'FacName': 'min','CountOfPIDM': 'sum', 'SuccessPIDM': 'sum'}).reset_index()
    else:
        # hide faculty name column
        rename_column = ['Sect', 'CRN', '(E)', '(SR)']
        temp_df_enroll_succ = data_to_aggregate.groupby(['Sect'], as_index=True).agg(
            {'CRN': 'min', 'CountOfPIDM': 'sum', 'SuccessPIDM': 'sum'}).reset_index()
    # enrollment and success rate table
    temp_df_enroll_succ['SuccessPIDM'] = temp_df_enroll_succ['SuccessPIDM'] / temp_df_enroll_succ['CountOfPIDM']
    temp_df_enroll_succ[['SuccessPIDM']] = temp_df_enroll_succ[['SuccessPIDM']].applymap(lambda x: "{0:.1f}%".format(x * 100))
    temp_df_enroll_succ.columns = rename_column
    # grade distribution table
    temp_df_grade = data_to_aggregate.groupby(['Sect', 'GradeZ'], as_index=True).agg({'CountOfPIDM': 'sum'}).reset_index()
    temp_df_grade = temp_df_grade.set_index(['Sect', 'GradeZ']).unstack(['GradeZ']).reset_index()
    temp_df_grade = temp_df_grade.replace('nan', np.nan).fillna(0)
    level = temp_df_grade.columns.get_level_values(1).astype(str)
    columns = ['Sect' if x == '' else x for x in level]
    temp_df_grade.columns = columns
    # combine and show
    frames = [temp_df_enroll_succ, temp_df_grade]
    result = pd.concat(frames, axis=1)
    result = result.loc[:, ~result.columns.duplicated()]
    return result
