import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.express as px
import datetime
import pandas as pd
from candidates import candidates
from layoutDef import createKandydaciTabLayout
from db_manager import DBManager

conn = DBManager()

SQL_Query = DBManager.query(conn,
    '''select
    timestamp,
    name,
    source
    from most_popular'''
)

data = pd.DataFrame(SQL_Query, columns = ['timestamp', 'name', 'source'])

data['source'] = data['source'].str.upper()
dataTail = data.tail(10)

# Import dictionary with data from candidates.py

candidates = candidates()

# Update dictionary based on database records

for candidatId in list(candidates.keys()):
    try:
        candidates[candidatId][3] = data[data['name']=='{} {}'.format(candidates[candidatId][0], candidates[candidatId][1])]['timestamp'].max()
        if str(candidates[candidatId][3]) == 'NaT':
            candidates[candidatId][3] = ''
        candidates[candidatId][4] = data[data['timestamp']== candidates[candidatId][3]]['source'].values[0]
        candidates[candidatId][5] = datetime.timedelta(seconds = int(data[data['name']=='{} {}'.format(candidates[candidatId][0], candidates[candidatId][1])]['name'].count()))
    except IndexError:
         print("Index Error. Probably the candidat has never appeared")


# set color map for TV station (sources) and candidates

sources_color_map = {"POLSAT":"#FF7F0E", "TVN":"#1F77B4", "TVP":"#17BECF"}

# Data and Figure preparation

# Figure 3 -  CZAS EKSPOZYCJI KANDYDATÓW W POSZCZEGÓLNYCH DNIACH TYGODNIA

weekday_names = {k:v for k,v in zip(range(7), ["pn", "wt", "śr", "cz", "pt", "sb", "nd"])}

fig3Data = data.set_index("timestamp")
fig3Data = fig3Data.groupby([fig3Data.index.weekday, 'source'])["source"].count().rename("agg_seconds").reset_index()
fig3Data["weekday_names"] = fig3Data["timestamp"].map(weekday_names)

fig3Plot = px.bar(
    data_frame = fig3Data,
    x = "weekday_names",
    y = "agg_seconds",
    color = "source",
    color_discrete_map=sources_color_map,
    labels={'weekday_names':'Dzień', "agg_seconds":"Czas ekspozycji [s]", 'source':'Stacja TV'},
)

fig3Plot.update_layout(
    title = None,
    xaxis_title = None,
    yaxis_title = "Czas ekspozycji [s]",
    legend_orientation = 'h',
    legend = dict(x = 0, y = 1.1)
)

# Figure 4 - CAŁKOWITY CZAS EKSPOZYCJI KANDYDATÓW W POSZCZEGÓLNYCH PORACH DNIA

fig4Data = data.set_index("timestamp")
fig4Data = fig4Data.groupby([fig4Data.index.hour, 'source'])["source"].count().rename("agg_seconds").reset_index()
fig4Data.columns = ["hour", 'source', "agg_seconds"]

fig4Plot = px.bar(
    data_frame = fig4Data,
    x = "hour",
    y = "agg_seconds",
    color = 'source',
    color_discrete_map=sources_color_map,
    labels={'hour':'godzina', "agg_seconds":"Czas ekspozycji [s]", 'source':'Stacja TV'}
)

fig4Plot.update_layout(
    title = None,
    xaxis_title = None,
    yaxis_title = "Czas ekspozycji [s]",
    legend_orientation = 'h',
    legend = dict(x = 0, y = 1.1)
)

# Figure 6 - CZAS EKSPOZYCJI KANDYDATÓW W POSZCZEGÓLNYCH STACJACH TV

fig6Data = data.set_index("timestamp").groupby([pd.Grouper(freq="D"), "name", "source"])["source"].count().rename("agg_seconds").reset_index(["name", "source"])
fig6Data = fig6Data.groupby([fig6Data.index, "source"])["agg_seconds"].sum().reset_index(["source"])

fig6Plot = px.bar(
    data_frame = fig6Data, 
    x = fig6Data.index, 
    y = "agg_seconds", 
    color = "source",
    color_discrete_map=sources_color_map,
    labels={'x':'Dzień ekspozycji', "agg_seconds":"czas antenowy [s]", "name":"kandydat", "source":"Stacja TV"}
).for_each_trace(lambda t: t.update(name=t.name.replace("źródło=","")))

fig6Plot.update_layout(
    title = None,
    xaxis_tickformat = '%Y-%m-%d',
    xaxis_title = None,
    yaxis_title = "Czas ekspozycji [s]",
    legend_orientation = 'h',
    legend = dict(x = 0, y = 1.1)
)

# Figure 7 - Mapa ekspozycji kandydatów w TV

fig7Data = data.set_index("timestamp").resample("H").count()
fig7Data["weekday_names"] = fig7Data.index.weekday
fig7Data["hour"] = fig7Data.index.strftime("%H:%M")
fig7Data = pd.pivot_table(
    data = fig7Data, 
    columns = "hour", 
    index = "weekday_names", 
    values = "source", 
    aggfunc = "mean",
)
fig7Data.index = fig7Data.index.map(weekday_names)[::-1]


fig7Plot = go.Figure(
    go.Heatmap(
        z = fig7Data.values,
        x = fig7Data.columns,
        y = fig7Data.index,
        xgap = 3, # this
        ygap = 3, # and this is used to make the grid-like apperance,
        colorscale = "Reds",
        hovertemplate='Godzina: %{x}<br>Dzień: %{y}<br>Śr. czas ekspozycji [s]: %{z}<extra></extra>'
    )
)

fig7Plot.update_layout(
    title = 'Mapa ekspozycji kandydatów w TV, w zależności od dnia tygodnia i pory dnia',
    title_x = 0.5,
    xaxis_title = None,
    yaxis_title = None
)

fig7Plot.update_yaxes(title_font=dict(size=12))


# Figure 2 - MAPA EKSPOZYCJI KANDYDATÓW W STACJACH TV

fig2Data = data.set_index(data['timestamp'])
fig2Data['Time'] = fig2Data.index.hour
fig2Data['Data'] = fig2Data.index.date

fig2Plot = px.scatter(
    fig2Data, 
    x='timestamp', 
    y='name', 
    color = 'source', 
    size_max = 20
)

fig2Plot.update_layout(
    legend_orientation="h", 
    legend = dict(x = 0, y = 1.1)
)



# Figure 5 - CZAS EKSPOZYCJI KANDYDATÓW W STACJACH TV

fig5Data = data.groupby(['name', 'source']).nunique()['timestamp'].sort_values(ascending=False)
fig5Data = fig5Data.reset_index()
fig5Plot = px.bar(fig5Data, color='source', x='name', y='timestamp', barmode='group')
fig5Plot.update_layout(legend_orientation="h", 
                       legend = dict(x = 0, y = 1.15),
                       title = None,
                       xaxis_tickformat = '%Y-%m-%d',
                       xaxis_title = None,
                       yaxis_title = "łączny czas antenowy [s]"
)

####################################
# Bar control tools
####################################

DateRanger = dcc.DatePickerRange(
    id = 'dateRangerId',
    start_date = data['timestamp'].min(), 
    end_date= data['timestamp'].max(),
    calendar_orientation = 'horizontal',
    first_day_of_week = 1,
    min_date_allowed = data['timestamp'].min(),
    max_date_allowed = data['timestamp'].max(),
    minimum_nights=1,
    display_format = 'DD/MM/YYYY'
)

TimeRanger = dcc.RangeSlider(
    id = 'timeRangerId',
    marks = {i:'{}'.format(i) for i in range(0,25)},
    min=0,
    max=24,
    step=1,
    value=[0, 24]
)  

BarmodeSelector = dcc.RadioItems(
    id = 'barmodeSelectorId',
    options=[
        {'label': ' Sterta', 'value': 'stack'},
        {'label': ' Grupowanie', 'value': 'group'}
    ],
    value='stack',
    labelStyle={'display': 'block'}
)  

## cell preparation for Kandydaci-Tab


kandydaci_Tab_row = createKandydaciTabLayout(candidates)

wybory_w_mediach_Tab_row = html.Div([
    html.Div(),
    dbc.Row([
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych dniach tygodnia')], width = 4),
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych porach dnia')], width = 4),
        dbc.Col([html.H5('Całkowity czas ekspozycji kandydatów w poszczególnych stacjach TV')], width = 4),
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(id='fig3PlotId', figure = fig3Plot)], width = 4),
        dbc.Col([dcc.Graph(id='fig4PlotId', figure = fig4Plot)], width = 4),
        dbc.Col([dcc.Graph(id='fig6PlotId', figure = fig6Plot)], width = 4),
        ]),
    dbc.Row(
        dbc.Col([dcc.Graph(id = 'fig7PlotId', figure = fig7Plot)], width = 12)
    )], style = {'margin':'25px'})

kandydaci_w_mediach_Tab_row = html.Div([
    html.Div(),
    dbc.Row(html.H6('Pasek narzędziowy', style = {'margin-left':'15px'})),
    dbc.Card(
        dbc.Row([   
            dbc.Col([html.Div('Zakres dni'),html.Div(DateRanger)], width = 4),
            dbc.Col([html.Div('Tryb wykresu słupkowego'),html.P(), html.Div(BarmodeSelector)], width = 2),
            dbc.Col([html.Div('Zakres godzin', style = {'margin-left': '20px'}), html.P(), html.Div(TimeRanger)], width = 6)], style = {'margin':'10px'})),
    dbc.Row([   
        dbc.Col([html.H5('Mapa ekspozycji kandydatów w stacjach TV', style = {'margin-left':'30px', 'margin-top':'30px'}),dcc.Graph(id='fig2PlotId', figure = fig2Plot)], width = 6),
        dbc.Col([html.H5('Czas ekspozycji kandydatów w stacjach TV', style = {'margin-left':'30px', 'margin-top':'30px'}), dcc.Graph(id='fig5PlotId', figure = fig5Plot)], width = 6)]),
    ], style = {'margin':'25px'})

# function implementation

def dataTableCreate(df):
    dataTable = dash_table.DataTable(wybory,
        id='rawDataTable',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records')) 
    return dataTable

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.LUX])
server = app.server

wstep = html.Div("""Polityczne spory o telewizję publiczną są dowodem na to, że dla polityków nadal pełni ona funkcję istotnego kanału komunikowania politycznego. Należy się zatem spodziewać, że w okresie kampanii prezydenckiej będzie można zauważyć wzmożone zapotrzebowanie na ekspozycję medialną. Obecność w telewizji pozwala bowiem mocniej zaistnieć w świadomości dużej rzeszy potencjalnych wyborców. A to, w połączeniu z pozytywnym przekazem, może decydować — jeśli nie zwycięstwie — to przynajmniej o drugiej turze wyborów.
Analiza medialnej ekspozycji pozwala nie tylko śledzić obecność kandydatów w mediach, ale też daje możliwość określenia ewentualnej linii programowej poszczególnych stacji telewizyjnych.""",
style = {'margin-right':'5px', 'margin-top':'25px', 'text-align':'justify'})

opis_projektu = html.Div("""Projekt polegał na analizie treści obrazów telewizyjnych, nadawanych przez trzy największe stacje w Polsce: TVP (telewizja publiczna), TVN i Polsat (telewizje prywatne). Przez 24 godziny na dobę nasza aplikacja monitorowała treści, które pokazywane były telewidzom. W przypadku, gdy na ekranie pojawił się jeden z kandydatów na prezydenta, w bazie danych zapisywany był rekord z informacją o dniu, godzinie, kandydacie i stacji telewizyjnej, w jakiej się pojawił.
Na podstawie zarejestrowanych w ten sposób danych, internetowa aplikacja generuje interaktywne wykresy, które pozwalają na analizę zebranych informacji. Podzielono je pod kątem obecności konkretnych kandydatów w telewizji oraz ogólnego przekazu wyborczego. Na karcie Kandydaci znajdują się z kolei tekstowe opisy na temat konkretnych kandydatów (kiedy i na jakim kanale pojawił się po raz ostatni, przez ile czasu był eksponowany w wybranych stacjach telewizyjnych oraz (docelowo) screen z ostatniej obecności w mediach).""",
style = {'margin-right':'5px', 'text-align':'justify'})

statementA = html.P("""
     Algorytmy uczenia maszynowego (ML) są rewelacyjnym rozwiązaniem i potrafią zastąpić nas w wielu żmudnych i nudnych pracach. 
     Jednak nie są one wolne od niedoskonałości. Podobnie jest z algorytmem do rozpoznawania twarzy. 
     Z tego powodu można zauważyć, że jeden z kandydatów pojawił się w „M jak Miłość”, choć wcale go tam nie było. 
     Z kolei szczyt medialnej aktywności innego z nich przypada na godziny 23:00 – 3:00. \nChociaż na bieżąco staramy się poprawiać jakość modelu ML, to nigdy nie będziemy w stanie zagwarantować 100% skuteczności.
""", style = {'margin-right':'5px', 'text-align':'justify'})

statementB = html.P("""
     Projekt jest realizowany w poszanowaniu odmienności światopoglądowej każdego człowieka. Nie wspieramy żadnego z komitetów wyborczych. 
""", style = {'margin-right':'5px', 'text-align':'justify'})

statementC = html.P("""
    Podczas realizacji projektu ucierpiało kilka żon i jeden pies ;)
""", style = {'margin-right':'5px', 'text-align':'justify'})


app.layout = html.P([
    html.Img(src = "http://geoscience.pl/wp-content/uploads/2020/02/naglowek.png", width='100%'),
    html.H1('Wybory Prezydenckie 2020',  
            style = {'color':'white','marginTop':-90, 'textAlign': 'center'}),
    html.H5('Medialna ekspozycja kandydatów na urząd prezydenta ',  
            style = {'color':'white','margin-top':25, 'textAlign': 'center'}),                                                 

    dcc.Tabs(id="app-tabs", value= '1', children=[
        dcc.Tab(label = 'Aplikacja', value = '1', children= html.Div([
            dbc.Row([
                dbc.Col([wstep, 
                html.H4('Opis projektu', style = {'margin-top':'20px'}), 
                opis_projektu,
                html.H4('Zastrzeżenie', style = {'margin-top':'20px'}),  
                statementA, 
                statementB, 
                statementC], md = 6),
                dbc.Col([
                    html.H4('Przykładowe rozpoznania twarzy'),
                    html.Img(src = 'http://geoscience.pl/wp-content/uploads/2020/02/screens.jpg', width='100%')], md = 6), 
            ], style = {'margin':'40px'}),
            dbc.Row([dbc.Col([
                html.H4('10 ostatnich wpisów do bazy:'),
                    dash_table.DataTable(
                        id='rawDataTable2', 
                        columns=[{"name": i, "id": i} for i in data.columns],
                        data=dataTail.to_dict('records'),
                        style_cell={'textAlign': 'left'}
                    )], style = {'margin':'60px', 'margin-top':'20px'})
            ])
        ], style = {'margin':25, 'textAlign': 'left'})),

        dcc.Tab(label = 'Kandydaci', value = '3', children = kandydaci_Tab_row),
        dcc.Tab(label = 'Wybory w mediach', value = '4', children = wybory_w_mediach_Tab_row),
        dcc.Tab(label = 'Kandydaci w mediach', value = '5', children = kandydaci_w_mediach_Tab_row),
        dcc.Tab(label = 'Autorzy', value='6', children = html.Div([
            html.P(''),
            html.P(''),
            html.P(''),
            html.H2('Olsztyn @ DataWorkshop Club', style={'margin-top':'150px'}),
            html.H2('Team'),
            html.Div()],
            style = {'margin':25, 
                     'textAlign': 'center'})               )
    ], style = {'width':'100%', 'textAlign': 'center', 'border' : 1})
])


####################
# Callbacks
####################


@app.callback(
    Output('fig5PlotId', 'figure'), 
    [Input('barmodeSelectorId', 'value'), 
    Input('dateRangerId', 'start_date'), 
    Input('dateRangerId', 'end_date'),
    Input('timeRangerId', 'value')]
    )
def change_fig5Plot(mode, start_date, end_date, timeRange):
    dataWorkspace = data.copy().set_index('timestamp')
    dataRange = dataWorkspace.loc[str(start_date):str(end_date)]
    dataRange['Data'] = dataRange.index.date
    dataRange['Time'] = dataRange.index.hour
    dataRange = dataRange[(dataRange['Time']>=timeRange[0]) & (dataRange['Time']<timeRange[1])]
    dataRange = dataRange.reset_index()
    fig5Data = dataRange.groupby(['name', 'source', 'Data']).nunique()['timestamp']
    fig5Data = fig5Data.reset_index()
    if mode == 'group':
        fig5Plot = px.bar(  fig5Data, color='source', 
                            x='name', y='timestamp', barmode='group', 
                            color_discrete_map=sources_color_map, 
                            labels={"name":"kandydat", "source":"Stacja TV"})
        fig5Plot.update_layout( legend_orientation="h", 
                                legend = dict(x = 0, y = 1.15),
                                title = None,
                                xaxis_tickformat = '%Y-%m-%d',
                                xaxis_title = None,
                                yaxis_title = "łączny czas antenowy [s]",)
        return fig5Plot 
    if mode == 'stack':
        fig5Plot = px.bar(  fig5Data, color='source', 
                            x='name', y='timestamp', barmode='stack', 
                            color_discrete_map=sources_color_map, 
                            labels={"name":"Kandydat", "source":"Stacja TV", 'timestamp':'Czas ekspozycji [s]'})
        fig5Plot.update_layout( legend_orientation="h", 
                                legend = dict(x = 0, y = 1.15),
                                title = None,
                                xaxis_tickformat = '%Y-%m-%d',
                                xaxis_title = None,
                                yaxis_title = "łączny czas antenowy [s]")
        return fig5Plot 



@app.callback(
    Output('fig2PlotId', 'figure'), 
    [Input('dateRangerId', 'start_date'), 
    Input('dateRangerId', 'end_date'),
    Input('timeRangerId', 'value')]
    )
def change_fig2Plot(start_date, end_date, value):
    dataWorkspace = data.copy().set_index('timestamp')
    fig2Data = dataWorkspace.loc[str(start_date):str(end_date)]
    fig2Data['Time'] = fig2Data.index.hour
    fig2Data = fig2Data.reset_index()
    fig2Plot = px.scatter(  fig2Data[(fig2Data['Time']>=value[0]) & (fig2Data['Time']<value[1])], 
                            x='timestamp', y='name', color = 'source', color_discrete_map=sources_color_map,  
                            size_max = 20, labels={'timestamp':'Czas', "name":"Kandydat", "source":"Stacja TV"})
    fig2Plot.update_layout(legend_orientation="h", yaxis_title = None, legend = dict(x = 0, y = 1.1))
    return fig2Plot

### Google Analytics walkaround ###
app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-47505587-2"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-47505587-2');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""
### XXX ###


if __name__ == '__main__':
    app.run_server()

