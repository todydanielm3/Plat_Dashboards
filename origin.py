import dash
import dash_html_components as html
from dash.dependencies import Output, Input
from dashboard1 import app as dashboard1_app
from dashboard2 import app as dashboard2_app
from dashboard3 import app as dashboard3_app
from dashboard4 import app as dashboard4_app

# Criação do aplicativo Dash
app = dash.Dash(__name__)
app.title = 'IGESDF'

# Estilo dos botões
button_style = {
    'display': 'inline-block',
    'margin': '10px',
    'padding': '15px 30px',
    'font-size': '20px',
    'text-align': 'center',
    'text-decoration': 'none',
    'border-radius': '4px',
    'background-color': '#00BFFF',  # Azul claro
    'color': '#FFFFFF',  # Texto branco
    'cursor': 'pointer'
}

# Layout com os botões dos dashboards e fundo personalizado
app.layout = html.Div(
    style={
        'background-color': '#4169E1',  # Azul escuro
        'border-radius': '30px',
        'padding': '60px',
        'text-align': 'center',
    },
    children=[
        html.H1(
            'Transparência - IGESDF',
            style={'color': '#FFFFFF'}  # Texto branco
        ),
        html.Div(
            style={'margin-bottom': '20px'},
            children=[
                html.Button('Gráficos Dados Financeiros - 1º Quadrimestre 2023', id='dashboard1-button', n_clicks=0, style=button_style),
                html.Button('Fluxo de Caixa - 2022', id='dashboard2-button', n_clicks=0, style=button_style),
                html.Button('Quadro de Composição de Dívidas', id='dashboard3-button', n_clicks=0, style=button_style),
                html.Button('QDD Consolidado', id='dashboard4-button', n_clicks=0, style=button_style),
                html.Button('Voltar', id='back-button', n_clicks=0, style=button_style)
            ]
        ),
        html.Div(id='dashboard-content')
    ]
)

# Variável de estado para rastrear o dashboard atual
current_dashboard = None

# Callback para exibir os dashboards
@app.callback(
    Output('dashboard-content', 'children'),
    [Input('dashboard1-button', 'n_clicks'),
     Input('dashboard2-button', 'n_clicks'),
     Input('dashboard3-button', 'n_clicks'),
     Input('dashboard4-button', 'n_clicks'),
     Input('back-button', 'n_clicks')
     ],
    prevent_initial_call=True
)
def render_dashboard(n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks_back):
    global current_dashboard

    if n_clicks_back > 0:
        current_dashboard = None # Retorna ao dashboard inicial

    elif n_clicks4 > 0:
        current_dashboard = dashboard4_app.layout
    
    elif n_clicks3 > 0:
        current_dashboard = dashboard3_app.layout
    
    elif n_clicks2 > 0:
        current_dashboard = dashboard2_app.layout
    
    elif n_clicks1 > 0:
        current_dashboard = dashboard1_app.layout

    return current_dashboard


if __name__ == '__main__':
    app.run_server(debug=True)

