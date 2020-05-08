
from utils import *
from grades_data_processing import grades_data, category_dic, overall_unduplicated_dic, labels_one_list, \
    labels_zero_list, values_one_list, values_zero_list, possible_colors_one, possible_colors_zero
from app import app

# use tooltips for some explanations
# Some modal options under categories

card_content_course = [
    dbc.CardHeader("Overall College Level"),
    dbc.CardBody([
        html.H4("Courses Number", className="card-title"),
        html.H3(str(overall_unduplicated_dic['Course']), className="card-text"),
    ])
]
card_content_student = [
    dbc.CardHeader("Overall College Level"),
    dbc.CardBody([
        html.H4("Students Number", className="card-title"),
        html.H3(str(overall_unduplicated_dic['PIDM']), className="card-text"),
    ])
]
card_content_instructor = [
    dbc.CardHeader("Overall College Level"),
    dbc.CardBody([
        html.H4("Instructor Number", className="card-title"),
        html.H3(str(overall_unduplicated_dic['InstrPIDM']), className="card-text"),
    ])
]
card_content_term = [
    dbc.CardHeader("Overall College Level"),
    dbc.CardBody([
        html.H4("TermCRN Number", className="card-title"),
        html.H3(str(overall_unduplicated_dic['TermCRN']), className="card-text"),
    ])
]
card_content_awards = [
    dbc.CardHeader("Overall College Level"),
    dbc.CardBody([
        html.H4("Awards Number", className="card-title"),
        html.H3(str(overall_unduplicated_dic['Awards']), className="card-text"),
    ])
]

overall_cards = dbc.CardDeck([
    dbc.Card(card_content_course, color="info", inverse=True),
    dbc.Card(card_content_student, color="info", inverse=True),
    dbc.Card(card_content_instructor, color="info", inverse=True),
    dbc.Card(card_content_term, color="info", inverse=True),
    dbc.Card(card_content_awards, color="info", inverse=True),
])

# overall pie chart data processing
overall_dataTrace_one = [{
    "type" : "pie",
    "labels": labels_one_list,
    "values": values_one_list,
    "marker":{"colors": possible_colors_one[:len(values_one_list)]},
}]
overall_dataTrace_zero = [{
    "type" : "pie",
    "labels": labels_zero_list,
    "values": values_zero_list,
    "marker":{"colors": possible_colors_zero[:len(values_zero_list)]},
}]

# set up variables input cards
card_content_Period = html.Div([
    dbc.CardHeader("Period"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Period']])),
            html.Br(),
            dbc.Button("Change values", id="open-body-scroll-AcadYr"),
            dbc.Modal([
                dbc.ModalHeader("Period"),
                dbc.ModalBody([
                    # add AcadYr checklist in ModalBody
                    html.H6("AcadYr: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Period-AcadYr",
                        inline=True,
                    ),
                    html.Br(),
                    # add Term checklist in ModalBody
                    html.H6("Term: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Period-Term",
                        inline=True,
                    ),
                    html.Br(),
                    # add FWS checklist in ModalBody
                    html.H6("FWS: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Period-FWS",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-AcadYr", className="ml-auto")
                )
            ], id="modal-body-scroll-AcadYr", scrollable=True),
        ]),
    ]),
])

card_content_Graduation_Status = [
    dbc.CardHeader("Graduation Status"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Graduation Status']])),
            dbc.Button("Change values", id="open-body-scroll-Graduation-Status"),
            dbc.Modal([
                dbc.ModalHeader("Graduation Status"),
                dbc.ModalBody([
                    # add AwardThatTerm checklist in ModalBody
                    html.H6("AwardThatTerm: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-AwardThatTerm",
                        inline=True,
                    ),
                    html.Br(),
                    # add AwardThatYr checklist in ModalBody
                    html.H6("AwardThatYr: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-AwardThatYr",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Graduation-Status", className="ml-auto")
                )
            ], id="modal-body-scroll-Graduation-Status", scrollable=True),
        ]),
    ])
]

card_content_Grade = [
    dbc.CardHeader("Grade"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Grade']])),
            dbc.Button("Change values", id="open-body-scroll-Grade"),
            dbc.Modal([
                dbc.ModalHeader("Grade"),
                dbc.ModalBody([
                    # add Succ checklist in ModalBody
                    html.H6("Succ: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Grade-Succ",
                        inline=True,
                    ),
                    html.Br(),
                    # add Grade checklist in ModalBody
                    html.H6("GradeGrp: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Grade-GradeGrp",
                        inline=True,
                    ),
                    html.Br(),
                    # add GradeGrp checklist in ModalBody
                    html.H6("Grade: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Grade-Grade",
                        inline=True,
                    ),
                    html.Br(),
                    # add SemGPAx checklist in ModalBody
                    html.H6("SemGPAx: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Grade-SemGPAx",
                        inline=True,
                    ),
                    html.Br(),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Grade", className="ml-auto")
                )
            ], id="modal-body-scroll-Grade", scrollable=True),
        ]),
    ])
]

card_content_Unit = [
    dbc.CardHeader("Unit"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Unit']])),
            html.Br(),
            dbc.Button("Change values", id="open-body-scroll-Unit"),
            dbc.Modal([
                dbc.ModalHeader("Unit"),
                dbc.ModalBody([
                    # add Div checklist in ModalBody
                    html.H6("Div: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Unit-Div",
                        inline=True,
                    ),
                    html.Br(),
                    # add Dept checklist in ModalBody
                    html.H6("Dept: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Unit-Dept",
                        inline=True,
                    ),
                    html.Br(),
                    # add Disc checklist in ModalBody
                    html.H6("Disc: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Unit-Disc",
                        inline=True,
                    ),
                    html.Br(),
                    # add Prog checklist in ModalBody
                    html.H6("Prog: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Unit-Prog",
                        inline=True,
                    ),

                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Unit", className="ml-auto")
                )
            ], id="modal-body-scroll-Unit", scrollable=True),
        ]),
    ])
]

card_content_Course = [
    dbc.CardHeader("Course"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Course']])),
            dbc.Button("Change values", id="open-body-scroll-Course"),
            dbc.Modal([
                dbc.ModalHeader("Unit"),
                dbc.ModalBody([
                    # add Div checklist in ModalBody
                    html.H6("Credit: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Course-Credit",
                        inline=True,
                    ),
                    html.Br(),
                    # add DelMode(Delivery Mode) checklist in ModalBody
                    html.H6("DelMode(Delivery Mode): "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Course-DelMode",
                        inline=True,
                    ),
                    html.Br(),
                    # add PTerm checklist in ModalBody
                    html.H6("PTerm: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Course-PTerm",
                        inline=True,
                    ),
                    html.Br(),
                    # add DelMdType checklist in ModalBody
                    html.H6("DelMdType: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Course-DelMdType",
                        inline=True,
                    ),
                    html.Br(),
                    # add Number checklist in ModalBody
                    html.H6("Number: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Course-Number",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Course", className="ml-auto")
                )
            ], id="modal-body-scroll-Course", scrollable=True),
        ]),
    ])
]

card_content_Faculty = [
    dbc.CardHeader("Faculty"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Faculty']])),
            html.Br(),
            html.Br(),
            dbc.Button("Change values", id="open-body-scroll-Faculty"),
            dbc.Modal([
                dbc.ModalHeader("Faculty"),
                dbc.ModalBody([
                    # add FacCat checklist in ModalBody
                    html.H6("FacCat: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Faculty-FacCat",
                        inline=True,
                    ),
                    html.Br(),
                    # add FT_PT checklist in ModalBody
                    html.H6("FT_PT: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Faculty-FT_PT",
                        inline=True,
                    ),
                    html.Br(),
                    # add FacName checklist in ModalBody
                    html.H6("FacName: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Faculty-FacName",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Faculty", className="ml-auto")
                )
            ], id="modal-body-scroll-Faculty", scrollable=True),
        ]),
    ])
]

card_content_Credits = [
    dbc.CardHeader("Credits"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Credits']])),
            dbc.Button("Change values", id="open-body-scroll-Credits"),
            dbc.Modal([
                dbc.ModalHeader("Credits"),
                dbc.ModalBody([
                    # add FTrmCrAtt checklist in ModalBody
                    html.H6("FTrmCrAtt: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Credits-FTrmCrAtt",
                        inline=True,
                    ),
                    html.Br(),
                    # add SecTrmAtt checklist in ModalBody
                    html.H6("SecTrmAtt: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Credits-SecTrmAtt",
                        inline=True,
                    ),
                    html.Br(),
                    # add SemCrAttx checklist in ModalBody
                    html.H6("SemCrAtt Grouped: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Credits-SemCrAttx",
                        inline=True,
                    ),
                    html.Br(),
                    # add SemCrErnx checklist in ModalBody
                    html.H6("SemCrErn Grouped: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Credits-SemCrErnx",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Credits", className="ml-auto")
                )
            ], id="modal-body-scroll-Credits", scrollable=True),
        ]),
    ])
]

card_content_Education = [
    dbc.CardHeader("Education"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Education']])),
            dbc.Button("Change values", id="open-body-scroll-Education"),
            dbc.Modal([
                dbc.ModalHeader("Education"),
                dbc.ModalBody([
                    # add HSGPAx checklist in ModalBody
                    html.H6("HSGPAx: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-HSGPAx",
                        inline=True,
                    ),
                    html.Br(),
                    # add EDLV checklist in ModalBody
                    html.H6("EDLV: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-EDLV",
                        inline=True,
                    ),
                    html.Br(),
                    # add EGOL checklist in ModalBody
                    html.H6("EGOL: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-EGOL",
                        inline=True,
                    ),
                    html.Br(),
                    # add CTE_Transfer checklist in ModalBody
                    html.H6("CTE_Transfer: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-CTE_Transfer",
                        inline=True,
                    ),
                    html.Br(),
                    # add PT_FT checklist in ModalBody
                    html.H6("PT_FT: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-PT_FT",
                        inline=True,
                    ),
                    html.Br(),
                    # add DevEd checklist in ModalBody
                    html.H6("DevEd: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Education-DevEd",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Education", className="ml-auto")
                )
            ], id="modal-body-scroll-Education", scrollable=True),
        ]),
    ])
]

card_content_Demographic = [
    dbc.CardHeader("Demographic"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Demographic']])),
            html.Br(),
            dbc.Button("Change values", id="open-body-scroll-Demographic"),
            dbc.Modal([
                dbc.ModalHeader("Demographic"),
                dbc.ModalBody([
                    # add AgeGrp checklist in ModalBody
                    html.H6("AgeGrp: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-AgeGrp",
                        inline=True,
                    ),
                    html.Br(),
                    # add Ethnicity Grouped checklist in ModalBody
                    html.H6("Ethnicity Grouped: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-Ethnicity",
                        inline=True,
                    ),
                    html.Br(),
                    # add Gender checklist in ModalBody
                    html.H6("Gender: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-Gender",
                        inline=True,
                    ),
                    html.Br(),
                    # add Resid checklist in ModalBody
                    html.H6("Resid: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-Resid",
                        inline=True,
                    ),
                    html.Br(),
                    # add VET checklist in ModalBody
                    html.H6("VET: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-VET",
                        inline=True,
                    ),
                    html.Br(),
                    # add PELL checklist in ModalBody
                    html.H6("PELL: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Demographic-PELL",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Demographic", className="ml-auto")
                )
            ], id="modal-body-scroll-Demographic", scrollable=True),
        ]),
    ])
]

card_content_Persistence = [
    dbc.CardHeader("Persistence"),
    dbc.CardBody([
        html.Div([
            # add variables/full name if needed
            html.P(' '.join([str(elem) for elem in category_dic['Persistence']])),
            dbc.Button("Change values", id="open-body-scroll-Persistence"),
            dbc.Modal([
                dbc.ModalHeader("Persistence"),
                dbc.ModalBody([
                    # add New_NotNew checklist in ModalBody
                    html.H6("New_NotNew: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Persistence-New_NotNew",
                        inline=True,
                    ),
                    html.Br(),
                    # add NextTrmAtt checklist in ModalBody
                    html.H6("NextTrmAtt: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Persistence-NextTrmAtt",
                        inline=True,
                    ),
                    html.Br(),
                    # add NextYrAtt checklist in ModalBody
                    html.H6("NextYrAtt: "),
                    dbc.Checklist(
                        value=["All"],
                        id="checklist-Persistence-NextYrAtt",
                        inline=True,
                    ),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-body-scroll-Persistence", className="ml-auto")
                )
            ], id="modal-body-scroll-Persistence", scrollable=True),
        ]),
    ])
]

# feedback collapse
collapse = html.Div([
        dbc.Button(
            "Click here to check changes you have made",
            id="collapse-button",
            className="mb-3",
            color="primary",
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody([
                    html.Div(id="Period-checklist-output"),
                    html.Div(id="Graduation-Status-checklist-output"),
                    html.Div(id="Grade-checklist-output"),
                    html.Div(id="Unit-checklist-output"),
                    html.Div(id="Persistence-checklist-output"),
                    html.Div(id="Course-checklist-output"),
                    html.Div(id="Faculty-checklist-output"),
                    html.Div(id="Credits-checklist-output"),
                    html.Div(id="Education-checklist-output"),
                    html.Div(id="Demographic-checklist-output"),
                ])
            ),
            id="collapse",
        ),
])

grades_layout = dbc.Container([
    html.H1("Grades Distribution"),
    html.Div(children=''' Visualization for Enrollments, Awards, Success Rate statistics for students subset.'''),
    html.Hr(),
    # overall college cards for not duplicated statistics
    overall_cards,
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H6("Overall College Level Grade Distribution: "),
            html.Br(),
            dbc.Table.from_dataframe(grades_distribution_groupby(grades_data), striped=True, bordered=True, hover=True,
                                     size='sm')
        ]),
        dbc.Col([
            html.Div([
                dcc.Graph(
                    id='overall-pie-one',
                    figure={
                        'data': overall_dataTrace_one,
                        'layout':{
                            "title": "<b>Overall College Success Grade Distribution<b>",
                            'margin': {'b': 30, 't': 30},
                            "height": 300,
                        }
                    },
                )
            ]),
            html.Div([
                dcc.Graph(
                    id='overall-pie-zero',
                    figure={
                        'data': overall_dataTrace_zero,
                        'layout':{
                            "title": "<b>Overall College non-Success Grade Distribution<b>",
                            'margin': {'b': 30, 't': 30},
                            "height": 300,
                        }
                    },
                )
            ]),
        ]),

    ], align="center"),
    html.Br(),
    html.H6("Please give variables'values within each category you are interested in: (default is all)"),
    html.Br(),
    # variables cards options
    # row1
    dbc.CardDeck([
        dbc.Card(card_content_Period, color="dark", inverse=True),
        dbc.Card(card_content_Graduation_Status, color="dark", inverse=True),
        dbc.Card(card_content_Grade, color="dark", inverse=True),
        dbc.Card(card_content_Unit, color="dark", inverse=True),
        dbc.Card(card_content_Persistence, color="dark", inverse=True),
    ]),
    html.Br(),
    # row2
    dbc.CardDeck([
        dbc.Card(card_content_Course, color="dark", inverse=True),
        dbc.Card(card_content_Faculty, color="dark", inverse=True),
        dbc.Card(card_content_Credits, color="dark", inverse=True),
        dbc.Card(card_content_Education, color="dark", inverse=True),
        dbc.Card(card_content_Demographic, color="dark", inverse=True),
    ]),

    # give feedback for chosen choice
    html.Br(),
    collapse,
    # graphs
    html.Br(),
    html.Div(id="final-feedback-graph")
], fluid=True)


@app.callback(Output("modal-body-scroll-AcadYr", "is_open"),
              [Input("open-body-scroll-AcadYr", "n_clicks"),
               Input("close-body-scroll-AcadYr", "n_clicks")],
              [State("modal-body-scroll-AcadYr", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Graduation-Status", "is_open"),
              [Input("open-body-scroll-Graduation-Status", "n_clicks"),
               Input("close-body-scroll-Graduation-Status", "n_clicks")],
              [State("modal-body-scroll-Graduation-Status", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Grade", "is_open"),
              [Input("open-body-scroll-Grade", "n_clicks"),
               Input("close-body-scroll-Grade", "n_clicks")],
              [State("modal-body-scroll-Grade", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Unit", "is_open"),
              [Input("open-body-scroll-Unit", "n_clicks"),
               Input("close-body-scroll-Unit", "n_clicks")],
              [State("modal-body-scroll-Unit", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Course", "is_open"),
              [Input("open-body-scroll-Course", "n_clicks"),
               Input("close-body-scroll-Course", "n_clicks")],
              [State("modal-body-scroll-Course", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Faculty", "is_open"),
              [Input("open-body-scroll-Faculty", "n_clicks"),
               Input("close-body-scroll-Faculty", "n_clicks")],
              [State("modal-body-scroll-Faculty", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Credits", "is_open"),
              [Input("open-body-scroll-Credits", "n_clicks"),
               Input("close-body-scroll-Credits", "n_clicks")],
              [State("modal-body-scroll-Credits", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Education", "is_open"),
              [Input("open-body-scroll-Education", "n_clicks"),
               Input("close-body-scroll-Education", "n_clicks")],
              [State("modal-body-scroll-Education", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Demographic", "is_open"),
              [Input("open-body-scroll-Demographic", "n_clicks"),
               Input("close-body-scroll-Demographic", "n_clicks")],
              [State("modal-body-scroll-Demographic", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("modal-body-scroll-Persistence", "is_open"),
              [Input("open-body-scroll-Persistence", "n_clicks"),
               Input("close-body-scroll-Persistence", "n_clicks")],
              [State("modal-body-scroll-Persistence", "is_open")],)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(dash.dependencies.Output('checklist-Period-AcadYr', 'options'),
              [dash.dependencies.Input('checklist-Period-AcadYr', 'value')])
def disable_Period_AcadYr_options(chosen_option):
    temp = list(grades_data['AcadYr'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Period-Term', 'options'),
              [dash.dependencies.Input('checklist-Period-AcadYr', 'value'),
               dash.dependencies.Input('checklist-Period-Term', 'value')])
def disable_Period_Term_options(AcadYr_chosen, chosen_option):
    if "All" in AcadYr_chosen:
        temp = list(grades_data['Term'].unique())
    else:
        temp = list(grades_data[grades_data['AcadYr'].isin(AcadYr_chosen)]['Term'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Period-FWS', 'options'),
              [dash.dependencies.Input('checklist-Period-Term', 'value'),
               dash.dependencies.Input('checklist-Period-FWS', 'value')])
def disable_Period_FWS_options(Term_chosen, chosen_option):
    if "All" in Term_chosen:
        temp = list(grades_data['FWS'].unique())
    else:
        temp = list(grades_data[grades_data['Term'].isin(Term_chosen)]['FWS'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-AwardThatTerm', 'options'),
              [dash.dependencies.Input('checklist-AwardThatTerm', 'value')])
def disable_AwardThatTerm_options(chosen_option):
    temp = list(grades_data['AwardThatTerm'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-AwardThatYr', 'options'),
              [dash.dependencies.Input('checklist-AwardThatYr', 'value')])
def disable_AwardThatYr_options(chosen_option):
    temp = list(grades_data['AwardThatYr'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

# Grade part
@app.callback(dash.dependencies.Output('checklist-Grade-Succ', 'options'),
              [dash.dependencies.Input('checklist-Grade-Succ', 'value')])
def disable_Grade_Succ_options(chosen_option):
    temp = list(grades_data['Succ'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Grade-GradeGrp', 'options'),
              [dash.dependencies.Input('checklist-Grade-GradeGrp', 'value'),
               dash.dependencies.Input('checklist-Grade-Succ', 'value')])
def disable_Grade_GradeGrp_options(chosen_option, Succ_option):
    if "All" in Succ_option:
        temp = list(grades_data['GradeGrp'].unique())
    else:
        temp = list(grades_data[grades_data['Succ'].isin(Succ_option)]['GradeGrp'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Grade-Grade', 'options'),
              [dash.dependencies.Input('checklist-Grade-Grade', 'value'),
               dash.dependencies.Input('checklist-Grade-Succ', 'value'),
               dash.dependencies.Input('checklist-Grade-GradeGrp', 'value')])
def disable_Grade_Grade_options(chosen_option, Succ_option, GradeGrp_option):
    if "All" in Succ_option:
        if "All" in GradeGrp_option:
            temp = list(grades_data['Grade'].unique())
        else:
            temp = list(grades_data[grades_data['GradeGrp'].isin(GradeGrp_option)]['Grade'].unique())
    else:
        if "All" in GradeGrp_option:
            temp = list(grades_data[grades_data['Succ'].isin(Succ_option)]['Grade'].unique())
        else:
            temp = list(grades_data[(grades_data['Succ'].isin(Succ_option)) &
                                    (grades_data['GradeGrp'].isin(GradeGrp_option))]['Grade'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Grade-SemGPAx', 'options'),
              [dash.dependencies.Input('checklist-Grade-SemGPAx', 'value')])
def disable_Grade_SemGPAx_options(chosen_option):
    temp = list(grades_data['SemGPAx'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

# Unit part
@app.callback(dash.dependencies.Output('checklist-Unit-Div', 'options'),
              [dash.dependencies.Input('checklist-Unit-Div', 'value')])
def disable_Unit_Div_options(chosen_option):
    temp = list(grades_data['Div'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Unit-Dept', 'options'),
              [dash.dependencies.Input('checklist-Unit-Dept', 'value'),
               dash.dependencies.Input('checklist-Unit-Div', 'value')])
def disable_Unit_Dept_options(chosen_option, Div_option):
    if "All" in Div_option:
        temp = list(grades_data['Dept'].unique())
    else:
        temp = list(grades_data[grades_data['Div'].isin(Div_option)]['Dept'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

# Disc and Prog are both related to Div/Dept
@app.callback(dash.dependencies.Output('checklist-Unit-Disc', 'options'),
              [dash.dependencies.Input('checklist-Unit-Disc', 'value'),
               dash.dependencies.Input('checklist-Unit-Div', 'value'),
               dash.dependencies.Input('checklist-Unit-Dept', 'value')])
def disable_Unit_Disc_options(chosen_option, Div_option, Dept_option):
    if "All" in Div_option:
        if "All" in Dept_option:
            temp = list(grades_data['Disc'].unique())
        else:
            temp = list(grades_data[grades_data['Dept'].isin(Dept_option)]['Disc'].unique())
    else:
        if "All" in Dept_option:
            temp = list(grades_data[grades_data['Div'].isin(Div_option)]['Disc'].unique())
        else:
            temp = list(grades_data[(grades_data['Div'].isin(Div_option)) &
                                    (grades_data['Dept'].isin(Dept_option))]['Disc'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Unit-Prog', 'options'),
              [dash.dependencies.Input('checklist-Unit-Prog', 'value'),
               dash.dependencies.Input('checklist-Unit-Div', 'value'),
               dash.dependencies.Input('checklist-Unit-Dept', 'value')])
def disable_Unit_Prog_options(chosen_option, Div_option, Dept_option):
    if "All" in Div_option:
        if "All" in Dept_option:
            temp = list(grades_data['Prog'].unique())
        else:
            temp = list(grades_data[grades_data['Dept'].isin(Dept_option)]['Prog'].unique())
    else:
        if "All" in Dept_option:
            temp = list(grades_data[grades_data['Div'].isin(Div_option)]['Prog'].unique())
        else:
            temp = list(grades_data[(grades_data['Div'].isin(Div_option)) &
                                    (grades_data['Dept'].isin(Dept_option))]['Prog'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Course-Credit', 'options'),
              [dash.dependencies.Input('checklist-Course-Credit', 'value')])
def disable_Course_Credit_options(chosen_option):
    temp = list(grades_data['Credit'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Course-DelMode', 'options'),
              [dash.dependencies.Input('checklist-Course-DelMode', 'value')])
def disable_Course_DelMode_options(chosen_option):
    temp = list(grades_data['DelMode'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Course-Number', 'options'),
              [dash.dependencies.Input('checklist-Course-Number', 'value')])
def disable_Course_Number_options(chosen_option):
    temp = list(grades_data['Num'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Course-PTerm', 'options'),
              [dash.dependencies.Input('checklist-Course-PTerm', 'value')])
def disable_Course_PTerm_options(chosen_option):
    temp = list(grades_data['PTerm'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Course-DelMdType', 'options'),
              [dash.dependencies.Input('checklist-Course-DelMdType', 'value')])
def disable_Course_DelMdType_options(chosen_option):
    temp = list(grades_data['DelMdType'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Faculty-FacCat', 'options'),
              [dash.dependencies.Input('checklist-Faculty-FacCat', 'value')])
def disable_Faculty_FacCat_options(chosen_option):
    temp = list(grades_data['FacCat'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Faculty-FT_PT', 'options'),
              [dash.dependencies.Input('checklist-Faculty-FT_PT', 'value')])
def disable_Faculty_FT_PT_options(chosen_option):
    temp = list(grades_data['FT_PT'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

# FacName related to category or part_full time
@app.callback(dash.dependencies.Output('checklist-Faculty-FacName', 'options'),
              [dash.dependencies.Input('checklist-Faculty-FacName', 'value'),
               dash.dependencies.Input('checklist-Faculty-FacCat', 'value'),
               dash.dependencies.Input('checklist-Faculty-FT_PT', 'value')])
def disable_Unit_Prog_options(chosen_option, Cat_option, FTPT_option):
    if "All" in Cat_option:
        if "All" in FTPT_option:
            temp = list(grades_data['FacName'].unique())
        else:
            temp = list(grades_data[grades_data['FT_PT'].isin(FTPT_option)]['FacName'].unique())
    else:
        if "All" in FTPT_option:
            temp = list(grades_data[grades_data['FacCat'].isin(Cat_option)]['FacName'].unique())
        else:
            temp = list(grades_data[(grades_data['FacCat'].isin(Cat_option)) &
                                    (grades_data['FT_PT'].isin(FTPT_option))]['FacName'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Credits-FTrmCrAtt', 'options'),
              [dash.dependencies.Input('checklist-Credits-FTrmCrAtt', 'value')])
def disable_Credits_FTrmCrAtt_options(chosen_option):
    temp = list(grades_data['FTrmCrAtt'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Credits-SecTrmAtt', 'options'),
              [dash.dependencies.Input('checklist-Credits-SecTrmAtt', 'value')])
def disable_Credits_SecTrmAtt_options(chosen_option):
    temp = list(grades_data['SecTrmAtt'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Credits-SemCrAttx', 'options'),
              [dash.dependencies.Input('checklist-Credits-SemCrAttx', 'value')])
def disable_Credits_SemCrAttx_options(chosen_option):
    temp = list(grades_data['SemCrAtt Grouped'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Credits-SemCrErnx', 'options'),
              [dash.dependencies.Input('checklist-Credits-SemCrErnx', 'value')])
def disable_Credits_SemCrErnx_options(chosen_option):
    temp = list(grades_data['SemCrErn Grouped'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-HSGPAx', 'options'),
              [dash.dependencies.Input('checklist-Education-HSGPAx', 'value')])
def disable_Education_HSGPAx_options(chosen_option):
    temp = list(grades_data['HSGPAx'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-EDLV', 'options'),
              [dash.dependencies.Input('checklist-Education-EDLV', 'value')])
def disable_Education_EDLV_options(chosen_option):
    temp = list(grades_data['EDLV'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-EGOL', 'options'),
              [dash.dependencies.Input('checklist-Education-EGOL', 'value')])
def disable_Education_EGOL_options(chosen_option):
    temp = list(grades_data['EGOL'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-CTE_Transfer', 'options'),
              [dash.dependencies.Input('checklist-Education-CTE_Transfer', 'value')])
def disable_Education_CTE_Transfer_options(chosen_option):
    temp = list(grades_data['CTE_Transfer'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-PT_FT', 'options'),
              [dash.dependencies.Input('checklist-Education-PT_FT', 'value')])
def disable_Education_PT_FT_options(chosen_option):
    temp = list(grades_data['PT_FT'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Education-DevEd', 'options'),
              [dash.dependencies.Input('checklist-Education-DevEd', 'value')])
def disable_Education_DevEd_options(chosen_option):
    temp = list(grades_data['DevEd'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-AgeGrp', 'options'),
              [dash.dependencies.Input('checklist-Demographic-AgeGrp', 'value')])
def disable_Demographic_AgeGrp_options(chosen_option):
    temp = list(grades_data['AgeGrp'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-Ethnicity', 'options'),
              [dash.dependencies.Input('checklist-Demographic-Ethnicity', 'value')])
def disable_Demographic_Ethnicity_options(chosen_option):
    temp = list(grades_data['Ethnicity'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-Gender', 'options'),
              [dash.dependencies.Input('checklist-Demographic-Gender', 'value')])
def disable_Demographic_Gender_options(chosen_option):
    temp = list(grades_data['Gender'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-Resid', 'options'),
              [dash.dependencies.Input('checklist-Demographic-Resid', 'value')])
def disable_Demographic_Resid_options(chosen_option):
    temp = list(grades_data['Resid'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-VET', 'options'),
              [dash.dependencies.Input('checklist-Demographic-VET', 'value')])
def disable_Demographic_VET_options(chosen_option):
    temp = list(grades_data['VET'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Demographic-PELL', 'options'),
              [dash.dependencies.Input('checklist-Demographic-PELL', 'value')])
def disable_Financial_PELL_options(chosen_option):
    temp = list(grades_data['PELL'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Persistence-New_NotNew', 'options'),
              [dash.dependencies.Input('checklist-Persistence-New_NotNew', 'value')])
def disable_Persistence_New_NotNew_options(chosen_option):
    temp = list(grades_data['New_NotNew'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Persistence-NextTrmAtt', 'options'),
              [dash.dependencies.Input('checklist-Persistence-NextTrmAtt', 'value')])
def disable_Persistence_NextTrmAtt_options(chosen_option):
    temp = list(grades_data['NextTrmAtt'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(dash.dependencies.Output('checklist-Persistence-NextYrAtt', 'options'),
              [dash.dependencies.Input('checklist-Persistence-NextYrAtt', 'value')])
def disable_Persistence_NextYrAtt_options(chosen_option):
    temp = list(grades_data['NextYrAtt'].unique())
    if "All" in chosen_option:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item, "disabled": True} for item in sorted(temp)]
    else:
        result = [{"label": "All", "value": "All"}] + [{"label": item, "value": item} for item in sorted(temp)]
    return result

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# feedback callback functions
@app.callback(dash.dependencies.Output("Period-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Period-AcadYr", "value"),
               dash.dependencies.Input("checklist-Period-Term", "value"),
               dash.dependencies.Input("checklist-Period-FWS", "value")])
def Period_feedback(chosen_value1, chosen_value2, chosen_value3):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("AcadYr", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("Term", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("FWS", chosen_value3)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Period-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Period-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Graduation-Status-checklist-output", "children"),
              [dash.dependencies.Input("checklist-AwardThatYr", "value"),
               dash.dependencies.Input("checklist-AwardThatTerm", "value")])
def Graduation_Status_feedback(chosen_value1, chosen_value2):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("AwardThatYr", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("AwardThatTerm", chosen_value2)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Graduation Status-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Graduation Status-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Grade-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Grade-Succ", "value"),
               dash.dependencies.Input("checklist-Grade-GradeGrp", "value"),
               dash.dependencies.Input("checklist-Grade-Grade", "value"),
               dash.dependencies.Input("checklist-Grade-SemGPAx", "value")])
def Grade_feedback(chosen_value1, chosen_value2, chosen_value3,  chosen_value4):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("Succ", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("GradeGrp", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("Grade", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("SemGPAx", chosen_value4)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Grade-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Grade-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Unit-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Unit-Div", "value"),
               dash.dependencies.Input("checklist-Unit-Dept", "value"),
               dash.dependencies.Input("checklist-Unit-Disc", "value"),
               dash.dependencies.Input("checklist-Unit-Prog", "value")])
def Unit_feedback(chosen_value1, chosen_value2, chosen_value3,  chosen_value4):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("Div", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("Dept", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("Disc", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("Prog", chosen_value4)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Unit-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Unit-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Persistence-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Persistence-New_NotNew", "value"),
               dash.dependencies.Input("checklist-Persistence-NextTrmAtt", "value"),
               dash.dependencies.Input("checklist-Persistence-NextYrAtt", "value")])
def Persistence_feedback(chosen_value1, chosen_value2, chosen_value3):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("New_NotNew", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("NextTrmAtt", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("NextYrAtt", chosen_value3)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Persistence-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Persistence-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Course-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Course-Credit", "value"),
               dash.dependencies.Input("checklist-Course-DelMode", "value"),
               dash.dependencies.Input("checklist-Course-Number", "value"),
               dash.dependencies.Input("checklist-Course-PTerm", "value"),
               dash.dependencies.Input("checklist-Course-DelMdType", "value")])
def Course_feedback(chosen_value1, chosen_value2, chosen_value3, chosen_value4, chosen_value5):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("Credit", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("DelMode", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("Number", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("PTerm", chosen_value4)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value5:
        output_string = template.format("DelMdType", chosen_value5)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Course-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Course-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output('Faculty-checklist-output', 'children'),
              [dash.dependencies.Input('checklist-Faculty-FacName', 'value'),
               dash.dependencies.Input('checklist-Faculty-FacCat', 'value'),
               dash.dependencies.Input('checklist-Faculty-FT_PT', 'value')])
def Faculty_feedback(chosen_value1, chosen_value2, chosen_value3):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("FacName", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("FacCat", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("FT_PT", chosen_value3)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Faculty-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Faculty-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Credits-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Credits-FTrmCrAtt", "value"),
               dash.dependencies.Input("checklist-Credits-SecTrmAtt", "value"),
               dash.dependencies.Input("checklist-Credits-SemCrAttx", "value"),
               dash.dependencies.Input("checklist-Credits-SemCrErnx", "value")])
def Credits_feedback(chosen_value1, chosen_value2, chosen_value3,  chosen_value4):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("FTrmCrAtt", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("SecTrmAtt", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("SemCrAtt Grouped", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("SemCrErn Grouped", chosen_value4)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Credits-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Credits-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Education-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Education-HSGPAx", "value"),
               dash.dependencies.Input("checklist-Education-EDLV", "value"),
               dash.dependencies.Input("checklist-Education-EGOL", "value"),
               dash.dependencies.Input("checklist-Education-CTE_Transfer", "value"),
               dash.dependencies.Input("checklist-Education-PT_FT", "value"),
               dash.dependencies.Input("checklist-Education-DevEd", "value")])
def Education_feedback(chosen_value1, chosen_value2, chosen_value3, chosen_value4, chosen_value5, chosen_value6):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("HSGPAx", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("EDLV", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("EGOL", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("CTE_Transfer", chosen_value4)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value5:
        output_string = template.format("PT_FT", chosen_value5)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value6:
        output_string = template.format("DevEd", chosen_value6)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Education-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Education-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("Demographic-checklist-output", "children"),
              [dash.dependencies.Input("checklist-Demographic-AgeGrp", "value"),
               dash.dependencies.Input("checklist-Demographic-Ethnicity", "value"),
               dash.dependencies.Input("checklist-Demographic-Gender", "value"),
               dash.dependencies.Input("checklist-Demographic-Resid", "value"),
               dash.dependencies.Input("checklist-Demographic-VET", "value"),
               dash.dependencies.Input("checklist-Demographic-PELL", "value")])
def Demographic_feedback(chosen_value1, chosen_value2, chosen_value3, chosen_value4, chosen_value5, chosen_value6):
    output_list = []
    template = "Variable {}, value {} selected."
    if "All" not in chosen_value1:
        output_string = template.format("AgeGrp", chosen_value1)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value2:
        output_string = template.format("Ethnicity", chosen_value2)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value3:
        output_string = template.format("Gender", chosen_value3)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value4:
        output_string = template.format("Resid", chosen_value4)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value5:
        output_string = template.format("VET", chosen_value5)
        output_list.append(html.Div(output_string))
    if "All" not in chosen_value6:
        output_string = template.format("PELL", chosen_value6)
        output_list.append(html.Div(output_string))
    # print or not
    if len(output_list) >= 1:
        output_list = [html.Strong("Demographic-variables have been modified: ")] + output_list
    else:
        output_list = [html.Strong("Demographic-variables keep default values.")]
    return output_list


@app.callback(dash.dependencies.Output("final-feedback-graph", "children"),
              [dash.dependencies.Input("checklist-Period-AcadYr", "value"),
               dash.dependencies.Input("checklist-Period-Term", "value"),
               dash.dependencies.Input("checklist-Period-FWS", "value"),
               dash.dependencies.Input("checklist-AwardThatYr", "value"),
               dash.dependencies.Input("checklist-AwardThatTerm", "value"),
               dash.dependencies.Input("checklist-Grade-Succ", "value"),
               dash.dependencies.Input("checklist-Grade-GradeGrp", "value"),
               dash.dependencies.Input("checklist-Grade-Grade", "value"),
               dash.dependencies.Input("checklist-Grade-SemGPAx", "value"),
               dash.dependencies.Input("checklist-Unit-Div", "value"),
               dash.dependencies.Input("checklist-Unit-Dept", "value"),
               dash.dependencies.Input("checklist-Unit-Disc", "value"),
               dash.dependencies.Input("checklist-Unit-Prog", "value"),
               dash.dependencies.Input("checklist-Persistence-New_NotNew", "value"),
               dash.dependencies.Input("checklist-Persistence-NextTrmAtt", "value"),
               dash.dependencies.Input("checklist-Persistence-NextYrAtt", "value"),
               dash.dependencies.Input("checklist-Course-Credit", "value"),
               dash.dependencies.Input("checklist-Course-DelMode", "value"),
               dash.dependencies.Input("checklist-Course-Number", "value"),
               dash.dependencies.Input("checklist-Course-PTerm", "value"),
               dash.dependencies.Input("checklist-Course-DelMdType", "value"),
               dash.dependencies.Input('checklist-Faculty-FacName', 'value'),
               dash.dependencies.Input('checklist-Faculty-FacCat', 'value'),
               dash.dependencies.Input('checklist-Faculty-FT_PT', 'value'),
               dash.dependencies.Input("checklist-Credits-FTrmCrAtt", "value"),
               dash.dependencies.Input("checklist-Credits-SecTrmAtt", "value"),
               dash.dependencies.Input("checklist-Credits-SemCrAttx", "value"),
               dash.dependencies.Input("checklist-Credits-SemCrErnx", "value"),
               dash.dependencies.Input("checklist-Education-HSGPAx", "value"),
               dash.dependencies.Input("checklist-Education-EDLV", "value"),
               dash.dependencies.Input("checklist-Education-EGOL", "value"),
               dash.dependencies.Input("checklist-Education-CTE_Transfer", "value"),
               dash.dependencies.Input("checklist-Education-PT_FT", "value"),
               dash.dependencies.Input("checklist-Education-DevEd", "value"),
               dash.dependencies.Input("checklist-Demographic-AgeGrp", "value"),
               dash.dependencies.Input("checklist-Demographic-Ethnicity", "value"),
               dash.dependencies.Input("checklist-Demographic-Gender", "value"),
               dash.dependencies.Input("checklist-Demographic-Resid", "value"),
               dash.dependencies.Input("checklist-Demographic-VET", "value"),
               dash.dependencies.Input("checklist-Demographic-PELL", "value")])
def final_graph(period1,period2, period3, AwardThatYr, AwardThatTerm, grade1, grade2, grade3, grade4, Div, Dept, Disc,
                Prog, New_NotNew, NextTrmAtt, NextYrAtt, Credit, DelMode, Number, PTerm, DelMdType, FacName, FacCat,
                FT_PT, FTrmCrAtt, SecTrmAtt, SemCrAttx, SemCrErnx, HSGPAx, EDLV, EGOL, CTE_Transfer, PT_FT, DevEd, AgeGrp,
                Ethnicity, Gender, Resid, VET, PELL):
    temp = grades_data
    # period
    if "All" not in period1:
        temp = temp[temp["AcadYr"].isin(period1)]
    if "All" not in period2:
        temp = temp[temp["Term"].isin(period2)]
    if "All" not in period3:
        temp = temp[temp["FWS"].isin(period3)]
    # Graduation status
    if "All" not in AwardThatYr:
        temp = temp[temp["AwardThatYr"].isin(AwardThatYr)]
    if "All" not in AwardThatTerm:
        temp = temp[temp["AwardThatTerm"].isin(AwardThatTerm)]
    # Grade
    temp = temp[temp["Succ"].notnull()]
    if "All" not in grade1:
        temp = temp[temp["Succ"].isin(grade1)]
    if "All" not in grade2:
        temp = temp[temp["GradeGrp"].isin(grade2)]
    if "All" not in grade3:
        temp = temp[temp["Grade"].isin(grade3)]
    if "All" not in grade4:
        temp = temp[temp["SemGPAx"].isin(grade4)]
    # Unit
    if "All" not in Div:
        temp = temp[temp["Div"].isin(Div)]
    if "All" not in Dept:
        temp = temp[temp["Dept"].isin(Dept)]
    if "All" not in Disc:
        temp = temp[temp["Disc"].isin(Disc)]
    if "All" not in Prog:
        temp = temp[temp["Prog"].isin(Prog)]
    # Persistence
    if "All" not in New_NotNew:
        temp = temp[temp["New_NotNew"].isin(New_NotNew)]
    if "All" not in NextTrmAtt:
        temp = temp[temp["NextTrmAtt"].isin(NextTrmAtt)]
    if "All" not in NextYrAtt:
        temp = temp[temp["NextYrAtt"].isin(NextYrAtt)]
    # Course
    if "All" not in Credit:
        temp = temp[temp["Credit"].isin(Credit)]
    if "All" not in DelMode:
        temp = temp[temp["DelMode"].isin(DelMode)]
    if "All" not in Number:
        temp = temp[temp["Number"].isin(Number)]
    if "All" not in PTerm:
        temp = temp[temp["PTerm"].isin(PTerm)]
    if "All" not in DelMdType:
        temp = temp[temp["DelMdType"].isin(DelMdType)]
    # Faculty
    if "All" not in FacName:
        temp = temp[temp["FacName"].isin(FacName)]
    if "All" not in FacCat:
        temp = temp[temp["FacCat"].isin(FacCat)]
    if "All" not in FT_PT:
        temp = temp[temp["FT_PT"].isin(FT_PT)]
     # Credits
    if "All" not in FTrmCrAtt:
        temp = temp[temp["FTrmCrAtt"].isin(FTrmCrAtt)]
    if "All" not in SecTrmAtt:
        temp = temp[temp["SecTrmAtt"].isin(SecTrmAtt)]
    if "All" not in SemCrAttx:
        temp = temp[temp["SemCrAtt Grouped"].isin(SemCrAttx)]
    if "All" not in SemCrErnx:
        temp = temp[temp["SemCrErn Grouped"].isin(SemCrErnx)]
    # Education
    if "All" not in HSGPAx:
        temp = temp[temp["HSGPAx"].isin(HSGPAx)]
    if "All" not in EDLV:
        temp = temp[temp["EDLV"].isin(EDLV)]
    if "All" not in EGOL:
        temp = temp[temp["EGOL"].isin(EGOL)]
    if "All" not in CTE_Transfer:
        temp = temp[temp["CTE_Transfer"].isin(CTE_Transfer)]
    if "All" not in PT_FT:
        temp = temp[temp["PT_FT"].isin(PT_FT)]
    if "All" not in DevEd:
        temp = temp[temp["DevEd"].isin(DevEd)]
    # Demographic
    if "All" not in AgeGrp:
        temp = temp[temp["AgeGrp"].isin(AgeGrp)]
    if "All" not in Ethnicity:
        temp = temp[temp["Ethnicity"].isin(Ethnicity)]
    if "All" not in Gender:
        temp = temp[temp["Gender"].isin(Gender)]
    if "All" not in Resid:
        temp = temp[temp["Resid"].isin(Resid)]
    if "All" not in VET:
        temp = temp[temp["VET"].isin(VET)]
    if "All" not in PELL:
        temp = temp[temp["PELL"].isin(PELL)]
    # create Filtered dataTrace set
    pie_form = temp.groupby(["Succ", "GradeGrp"])['PIDM'].count().reset_index()
    pie_form['percent'] = pie_form['PIDM']/sum(pie_form['PIDM'])
    pie_form_one = pie_form[pie_form['Succ'] == "Yes"]
    pie_form_zero = pie_form[pie_form['Succ'] == "No"]

    filter_labels_one_list = list(pie_form_one['GradeGrp'])
    filter_values_one_list = list(pie_form_one['percent'])
    filter_labels_one_list, filter_values_one_list = pie_chart_percent_combine(filter_labels_one_list, filter_values_one_list)

    filter_labels_zero_list = list(pie_form_zero['GradeGrp'])
    filter_values_zero_list = list(pie_form_zero['percent'])
    filter_labels_zero_list, filter_values_zero_list = pie_chart_percent_combine(filter_labels_zero_list, filter_values_zero_list)
    Filtered_dataTrace_one = [{
        "type" : "pie",
        "labels": filter_labels_one_list,
        "values": filter_values_one_list,
        "marker":{"colors": possible_colors_one[:len(filter_values_one_list)]},}]

    Filtered_dataTrace_zero = [{
	    "type" : "pie",
	    "labels": filter_labels_zero_list,
	    "values": filter_values_zero_list,
	    "marker":{"colors": possible_colors_zero[:len(filter_values_zero_list)]},}]

    return html.Div([
    	dbc.Row([
	        dbc.Col([
	            html.H6("Filtered Grade Distribution: "),
	            html.Br(),
	            dbc.Table.from_dataframe(grades_distribution_groupby(temp), striped=True, bordered=True, hover=True, size='sm')
	        ]),
	        dbc.Col([
	            html.Div([
	                dcc.Graph(
	                    id='Filtered-pie-one',
	                    figure={
	                        'data': Filtered_dataTrace_one,
	                        'layout':{
	                            "title": "<b>Filtered College Success Grade Distribution<b>",
	                            'margin': {'b': 30, 't': 30},
	                            "height": 300,
	                        }
	                    },
	                )
	            ]),
	            html.Div([
	                dcc.Graph(
	                    id='Filtered-pie-zero',
	                    figure={
	                        'data': Filtered_dataTrace_zero,
	                        'layout':{
	                            "title": "<b>Filtered College non-Success Grade Distribution<b>",
	                            'margin': {'b': 30, 't': 30},
	                            "height": 300,
	                        }
	                    },
	                )
	            ]),
	        ]),
	    ], align="center"),
	])


