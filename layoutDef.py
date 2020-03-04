import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from candidates import candidates


candidates = candidates()

def candidateDescribe(candidates):
    """
    Create one column with candidat description in Kandydaci Tab

    Keyword arguments:
    candidates -- dictionary with candidates data > dict('key':['name', 'surname', 'last_seen', 'tv_channel', 'total_views', 'photo_url'])
    """
    dbcCol = ''
    for candidatId in list(candidates.keys()):
        dbcCol = dbcCol + r"""
            dbc.Col(html.Div([ html.H1('{0}'.format(candidates['{1}'][0])), html.H1('{2}'.format(candidates['{3}'][1])), html.H6('{4}'.format(candidates['{5}'][2])),
                dbc.Row([
                        dbc.Col([html.Img(src=candidates['{6}'][-1], width='200px'), html.P('Źródło: {7}'.format(candidates['{8}'][4]))], md='auto' ),
                        dbc.Col(html.Div([html.H5('Statystyki'), 
                                            html.Div(html.B('Ostanio w TV:')),
                                            html.P('{9}\n{10}'.format(candidates['{11}'][3], candidates['{12}'][4])),
                                            html.Div(html.B('Łączny czas antenowy:')),
                                            html.P('{13}'.format(candidates['{14}'][5])),
                                            ]))
                        ])
            ]), md = columnSize),
        """.format('{}',str(candidatId),'{}', str(candidatId), '{}', str(candidatId), str(candidatId), '{}', str(candidatId),'{}', '{}', str(candidatId), str(candidatId), '{}', str(candidatId))
    return dbcCol


def createKandydaciTabLayout(candidates, columnSize = 4):
    """
    
    """
    kandydaciTabLayout = html.Div([
            dbc.Row([
                ### candidateDescribe function result should be past here ###
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['AD'][0])), html.H1('{}'.format(candidates['AD'][1])), html.H6('{}'.format(candidates['AD'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['AD'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['AD'][4]))], md='auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['AD'][3], candidates['AD'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['AD'][5])),
                                            ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['MKB'][0])), html.H1('{}'.format(candidates['MKB'][1])), html.H6('{}'.format(candidates['MKB'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['MKB'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['MKB'][4]))], md='auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['MKB'][3], candidates['MKB'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['MKB'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['SH'][0])), html.H1('{}'.format(candidates['SH'][1])), html.H6('{}'.format(candidates['SH'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['SH'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['SH'][4]))], md='auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['SH'][3], candidates['SH'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['SH'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['RB'][0])), html.H1('{}'.format(candidates['RB'][1])), html.H6('{}'.format(candidates['RB'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['RB'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['RB'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['RB'][3], candidates['RB'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['RB'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['WKK'][0])), html.H1('{}'.format(candidates['WKK'][1])), html.H6('{}'.format(candidates['WKK'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['WKK'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['WKK'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['WKK'][3], candidates['WKK'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['WKK'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['KB'][0])), html.H1('{}'.format(candidates['KB'][1])), html.H6('{}'.format(candidates['KB'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['KB'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['KB'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['KB'][3], candidates['KB'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['KB'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['LS'][0])), html.H1('{}'.format(candidates['LS'][1])), html.H6('{}'.format(candidates['LS'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['LS'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['LS'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['LS'][3], candidates['LS'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['LS'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['PB'][0])), html.H1('{}'.format(candidates['PB'][1])), html.H6('{}'.format(candidates['PB'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['PB'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['PB'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['PB'][3], candidates['PB'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['PB'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['SZ'][0])), html.H1('{}'.format(candidates['SZ'][1])), html.H6('{}'.format(candidates['SZ'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['SZ'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['SZ'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['SZ'][3], candidates['SZ'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['SZ'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
            
                dbc.Col(html.Div([ html.H1('{}'.format(candidates['WP'][0])), html.H1('{}'.format(candidates['WP'][1])), html.H6('{}'.format(candidates['WP'][2])),
                    dbc.Row([
                            dbc.Col([html.Img(src=candidates['WP'][-1], width='200px'), html.P('Źródło: {}'.format(candidates['WP'][4]))], md = 'auto' ),
                            dbc.Col(html.Div([html.H5('Statystyki'), 
                                                html.Div(html.B('Ostanio w TV:')),
                                                html.P('{}\n{}'.format(candidates['WP'][3], candidates['WP'][4])),
                                                html.Div(html.B('Łączny czas antenowy:')),
                                                html.P('{}'.format(candidates['WP'][5])),
                                                ]))
                            ])
                ]), md = columnSize),
                ### ---- END ---- ###
            ])
        ], style = {'margin':'100px'})

    return kandydaciTabLayout
    
def createWyboryWMediachTabLayout(fig1, fig2, fig3, fig4):
    """
    
    """
    wyboryWMediachTabLayout= html.Div([
    html.Div(),
    dbc.Row([
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych dniach tygodnia')], width = 4),
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych porach dnia')], width = 4),
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych stacjach TV')], width = 4),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='fig3PlotId', figure = fig1)], width = 4),
        dbc.Col([dcc.Graph(id='fig4PlotId', figure = fig2)], width = 4),
        dbc.Col([dcc.Graph(id='fig6PlotId', figure = fig3)], width = 4),
        ]),
    dbc.Row(
        dbc.Col([dcc.Graph(id = 'fig7PlotId', figure = fig4)], width = 12)
    )], style = {'margin':'25px'})
    return wyboryWMediachTabLayout

def createToolbar(data):
    DateRanger, BarmodeSelector, TimeRanger = createBarControlComponents(data)
    toolBar = dbc.Card(dbc.Row([dbc.Col([html.Div('Zakres dni'),html.Div(DateRanger)], width = 4),
                    dbc.Col([html.Div('Tryb wykresu słupkowego'),html.P(), html.Div(BarmodeSelector)], width = 2),
                    dbc.Col([html.Div('Zakres godzin', style = {'margin-left': '20px'}), html.P(), html.Div(TimeRanger)], width = 6)], style = {'margin':'10px'}))
    return toolBar            


def createKandydaciWMediachTabLayout(data, fig1, fig2):
    toolBar = createToolbar(data)
    kandydaciWMediachTabLayout = html.Div([
        html.Div(),
        dbc.Row(html.H6('Pasek narzędziowy', style = {'margin-left':'15px'})),
        toolBar,
        dbc.Row([   dbc.Col([html.H5('Mapa ekspozycji kandydatów w stacjach TV', style = {'margin-left':'30px', 'margin-top':'30px'}),dcc.Graph(id='fig2PlotId', figure = fig1)], width = 6),
                    dbc.Col([html.H5('Czas ekspozycji kandydatów w stacjach TV', style = {'margin-left':'30px', 'margin-top':'30px'}), dcc.Graph(id='fig5PlotId', figure = fig2)], width = 6)]),
                    ], style = {'margin':'25px'})
    
    return kandydaciWMediachTabLayout
