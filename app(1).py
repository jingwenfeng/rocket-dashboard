from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dummy_factory import DummyRocket

app = Dash(__name__)
rocket = DummyRocket()

# current status
curr_status = 'Power On'
# velocity until
vel_Unit = 'm/s'
# altitude until
alt_Unit = 'm'
# acceleration until
acc_Unit = 'm'
# temperature until
temp_Unit = 'C'
# time series value
time_series = ''

app.layout = html.Div(style={'backgroundColor': '#000', 'margin': '0 0',
        'color': '#fff',  'padding': '5px 5px 5px 5px', 'position': 'absolute', 'top': 0, 'left': 0, 'bottom': 0,
        'right': 0, 'display': 'grid', 'grid-template-columns': '33% 33% 30%',
        'grid-template-rows': '4rem 26rem 3rem 12rem', 'grid-gap': '5px',
        'grid-template-areas': '''
            "span currentState time"
            "charts button span"
            "message map visual"
            span span span '''},
    children=[
        # Current status display module
        html.Div(style={'grid-area': 'currentState', 'grid-row': '1', 'grid-column': '2', 'display': 'flex', 'flex-direction': 'row'},
                 children=[
                     html.H2(children='Current State：'),
                     html.H2(id='currentStatus', children=[curr_status])
                 ]),
        # Time control module
        html.Div(style={'grid-area': 'time', 'grid-row': '1', 'grid-column': '3'},children=[
            html.H3(children='Time Since Launching：'),
            html.P(id='time_controller', children=[time_series])
        ]),
        # Chart rendering module
        html.Div(style={'grid-area': 'charts', 'grid-row': 'span 2', 'grid-column': 'span 2'},
        children=[
            # Set the grid layout
            html.Div(style={'display': 'grid', 'grid-template-columns': '49% 49%', 'grid-template-rows': '13rem 13rem',
            'padding': '5px 5px 5px 5px', 'grid-gap': '10px', 'text-align': 'center',
            'grid-template-areas': ''' 
                "Velocity" "Altitute"
                "Acceleration" "Temperature" '''},
            children=[
                # Velocity graph
                html.Div(style={'grid-area': 'Velocity', 'grid-row': '1', 'grid-column': '1'},
                children=[
                    html.Div(style={'display': 'grid', 'grid-template-columns': '30% 70%', 'grid-template-areas': ''' "text" "graph" '''},
                        children=[
                        html.H3(style={'grid-area': 'text','grid-row': '1', 'grid-column': '1', 'height': '11rem'}, children=[
                            html.H3(children='Velocity:'),
                            html.H4(id='velocity',children=[rocket.time_series_data['Velocity'][-1] if rocket.time_series_data['Velocity'] else 0, vel_Unit])
                        ]),
                        dcc.Graph(id='velocity-chart', style={'grid-area': 'graph', 'grid-row': '1', 'grid-column': '2',
                        'width': '100%', 'height': '100%'})
                    ])
                ]),
                # Altitude graph
                html.Div(style={'grid-area': 'Altitute', 'grid-row': '1', 'grid-column': '2'},
                children=[
                    html.Div(style={'display': 'grid', 'grid-template-columns': '30% 70%', 'grid-template-areas': ''' "text" "graph" '''},
                        children=[
                        html.H3(style={'grid-area': 'text','grid-row': '1', 'grid-column': '1', 'height': '11rem'}, children=[
                            html.H3(children='Altitude:'),
                            html.H4(id='altitude',children=[rocket.time_series_data['Altitude'][-1] if rocket.time_series_data['Altitude'] else 0, alt_Unit])
                        ]),
                        dcc.Graph(id='altitude-chart', style={'grid-area': 'graph', 'grid-row': '1', 'grid-column': '2',
                        'width': '100%', 'height': '100%'})
                    ])
                ]),
                # Acceleration graph
                html.Div(style={'grid-area': 'Acceleration', 'grid-row': '2', 'grid-column': '2'},
                         children=[
                             html.Div(style={'display': 'grid', 'grid-template-columns': '30% 70%',
                                             'grid-template-areas': ''' "text" "graph" '''},
                                      children=[
                                          html.H3(style={'grid-area': 'text', 'grid-row': '1', 'grid-column': '1',
                                                         'height': '12rem'}, children=[
                                              html.H3(children='Acceleration:'),
                                              html.H4(id='acceleration',children=[
                                                  rocket.time_series_data['Acceleration'][-1] if rocket.time_series_data['Acceleration'] else 0, acc_Unit])
                                          ]),
                                          dcc.Graph(id='acceleration-chart',
                                                    style={'grid-area': 'graph', 'grid-row': '1', 'grid-column': '2',
                                                           'width': '100%', 'height': '100%'})
                                      ])
                         ]),
                # Temperature graph
                html.Div(style={'grid-area': 'Temperature', 'grid-row': '2', 'grid-column': '1'},
                         children=[
                             html.Div(style={'display': 'grid', 'grid-template-columns': '30% 70%',
                                             'grid-template-areas': ''' "text" "graph" '''},
                                      children=[
                                          html.H3(style={'grid-area': 'text', 'grid-row': '1', 'grid-column': '1',
                                                         'height': '12rem'}, children=[
                                              html.H3(children='Temperature:'),
                                              html.H4(id='temperature',children=[
                                                  rocket.time_series_data['Temperature'][-1] if rocket.time_series_data['Temperature'] else 0, temp_Unit])
                                          ]),
                                          dcc.Graph(id='temperature-chart',
                                                    style={'grid-area': 'graph', 'grid-row': '1', 'grid-column': '2',
                                                           'width': '100%', 'height': '100%'})
                                      ])
                         ]),
            ])
        ]),
        # Button assembly module
        html.Div(style={'grid-area': 'button', 'grid-row': '2', 'grid-column': '3'}, children=[
            html.Div(style={'border': 'solid 2px', 'margin': '20px 10px 10px 10px'}, children=[
                html.H3(style={'text-align': 'center'},children='Button to change state'),
                dcc.RadioItems(id='buttonState', options=[
                    { 'label': 'Power ON', 'value': 'true' },
                    { 'label': 'Launch Ready', 'value': 'false' }
                ],
                value='true',
                style={'display': 'flex','justify-content': 'space-between',
                    'margin': '1rem 1rem 1rem 1rem', 'fontSize': '20px'})
            ]),
            # Button Unit
            html.Div(style={'border': 'solid 2px', 'margin': '20px 10px 10px 10px'}, children=[
                html.H3(style={'text-align': 'center'},children='Button to Switch Unit'),
                dcc.RadioItems(id='buttonUnit', options=[
                    { 'label': 'Metric Unit', 'value': 'true' },
                    { 'label': 'Imperial Unit', 'value': 'false' }
                ],
                value='false',
                style={'display': 'flex','justify-content': 'space-between',
                    'margin': '1rem 1rem 1rem 1rem', 'fontSize': '20px'})
            ]),
            html.Div(style={'border': 'solid 2px', 'margin': '20px 10px 10px 10px'}, children=[
                html.H3(style={'text-align': 'center'},children='Button to turn on/off camera'),
                dcc.RadioItems(id='buttonCamera', options=[
                    { 'label': 'Camera ON', 'value': 'true' },
                    { 'label': 'Camera OFF', 'value': 'false' }
                ],
                value='false',  
                style={'display': 'flex','justify-content': 'space-between',
                    'margin': '1rem 1rem 1rem 1rem', 'fontSize': '20px'})
            ])
    ]),
        # Message list module
        html.Div(style={'grid-area': 'message', 'grid-row': '4', 'grid-column': '1',
        'border': 'solid 5px'}, children=[
            html.H2(children='Error:'),
            html.Div(id='messageList',children=[
                # Print out the system BUG information here
            ])
        ]),
        # Map module
        html.Div(style={'grid-area': 'map', 'grid-row': '4', 'grid-column': '2',
        'border': 'solid 5px'}, children=[
            html.Div(style={'display': 'grid', 'grid-template-columns': '49% 49%', 'grid-template-rows': '90%',
                            'grid-template-areas': '''
                    "text map " '''}, children=[
                html.Div(style={'grid-area': 'text'}, children=[
                    html.H2(children='GPS Coordinates'),
                    html.H3(children=['N/A','N',';','N/A','W']),
                    html.H3(children=['Number of Linked Satellites: ','N/A']),
                ]),
                html.H2(style={'grid-area': 'map'}, children='Map Component')
            ])
        ]),
        # Real-time communication module
        html.Div(style={'grid-area': 'visual', 'grid-row': '3', 'grid-column': '3','grid-row-end': 'span 2',
        'border': 'solid 5px'}, children=[
            html.Div(id='video',style={'width': '100%', 'height': '90%'}, children=[
                # Insert an offline video resource here, or place a video connection here
                html.Video(
                    id='video-player',
                    controls=True,
                    src='E:\\project\\dash-web\\test.mp4',  # Replace with your local video file path
                    style={'width': '100%', 'height': '100%'}
                )
            ])
        ]),
        dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
    ])

@app.callback(
    [Output('currentStatus', 'children'),
     Output('video-player', 'autoPlay'),
     Output('time_controller', 'children')],
    [Input('buttonState', 'value')]
)

def update_status(state_value):
    if (state_value == 'true'):
        curr_status = 'Power On'
        time_series = 0
        controls = True
    else:
        curr_status = 'Launching'
        time_series = rocket.time_series_data['Time'][4]
        controls = False
    return curr_status, controls, time_series

# Unit button callback function
@app.callback(
    [Output('velocity', 'children'),
     Output('altitude', 'children'),
     Output('acceleration', 'children'),
     Output('temperature', 'children')],
    [Input('buttonUnit', 'value')]
)
def update_until(until_value):
    if (until_value == 'true') :
        vel_Unit = 'Unit'
        alt_Unit = 'Unit'
        acc_Unit = 'Unit'
        temp_Unit = 'Unit'
    else: 
        vel_Unit = 'm/s'
        alt_Unit = 'm'
        acc_Unit = 'm'
        temp_Unit = 'C'
    return vel_Unit, alt_Unit, acc_Unit, temp_Unit

@app.callback(
    [Output('velocity-chart', 'figure'),
     Output('altitude-chart', 'figure'),
     Output('acceleration-chart', 'figure'),
     Output('temperature-chart', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_charts(n):
    data = rocket.time_series_data

    velocity_fig = go.Figure(data=[go.Scatter(x=data['Time'], y=data['Velocity'], mode='lines+markers')])
    velocity_fig.update_layout(title='Velocity vs Time', xaxis_title='Time (s)', yaxis_title='Velocity (m/s)',
                               margin=dict(l=20, r=20, t=40, b=20), height=250)

    altitude_fig = go.Figure(data=[go.Scatter(x=data['Time'], y=data['Altitude'], mode='lines+markers')])
    altitude_fig.update_layout(title='Altitude vs Time', xaxis_title='Time (s)', yaxis_title='Altitude (m)',
                               margin=dict(l=20, r=20, t=40, b=20), height=250)

    acceleration_fig = go.Figure(data=[go.Scatter(x=data['Time'], y=data['Acceleration'], mode='lines+markers')])
    acceleration_fig.update_layout(title='Acceleration vs Time', xaxis_title='Time (s)', yaxis_title='Acceleration (m/s^2)',
                               margin=dict(l=20, r=20, t=40, b=20), height=250)

    temperature_fig = go.Figure(data=[go.Scatter(x=data['Time'], y=data['Acceleration'], mode='lines+markers')])
    temperature_fig.update_layout(title='Temperature vs Time', xaxis_title='Time (s)', yaxis_title='Temperature (C)',
                               margin=dict(l=20, r=20, t=40, b=20), height=250)

    return velocity_fig, altitude_fig, acceleration_fig, temperature_fig

if __name__ == '__main__':
    app.run(debug=True)
