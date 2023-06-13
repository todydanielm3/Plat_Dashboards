import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Vetor com os valores da dívida recorrente
divida_recorrente = [
    364000000,
    235000000,
    118000000,
    112000000,
    109000000,
    107500000,
    103600000,
    100200000,
    97600000,
    95508371.18
]

# Vetor com os valores do período
periodo = [
    'abr/21',
    'jan/22',
    'out/22',
    'nov/22',
    'dez/22',
    'jan/23',
    'fev/23',
    'mar/23',
    'abr/23',
    '18/05/2023'
]

valores_maio = [
    43348832.77,
    46761285.23,
    720155.89,
    4678097.29
]

descricao_maio = [
    "Fornecedores com Pagamentos Suspensos e Acompanhados",
    "Parcelamento Tributário",
    "Material de Consumo e Serviços de Terceiros (inclusive acordo judiciais)",
    "Parcelamento Concessionária de Serviços Publicos"
]


# Criação do gráfico de linha com os valores da dívida recorrente ao longo do período
grafico_divida_recorrente = go.Figure(data=go.Scatter(x=periodo, y=divida_recorrente, mode='lines+markers'))

# Atualizar as cores e layout do gráfico de linha
grafico_divida_recorrente.update_traces(marker=dict(color=px.colors.qualitative.Pastel))

grafico_divida_recorrente.update_layout(
    title='Histórico da Dívida IGESDF',
    xaxis_title='Período',
    yaxis_title='Valor (R$)',
    font=dict(
        family='Arial, sans-serif',
        size=14,
        color='#333333'
    ),
    plot_bgcolor='#f2f2f2',
    paper_bgcolor='#ffffff',
    margin=dict(l=40, r=40, t=60, b=40)
)

# Criação do gráfico de pizza
grafico_pizza = go.Figure(data=[go.Pie(
    labels=descricao_maio,
    values=valores_maio,
    textinfo='value+percent',
    hole=0.5,
    insidetextorientation='horizontal',
    texttemplate="%{percent} <br>R$%{value:,.2f}",
    textposition='auto',
    textfont_size=13,
)])

# Atualizar as cores e layout do gráfico de pizza
grafico_pizza.update_traces(marker=dict(colors=px.colors.qualitative.Pastel,
                                        line=dict(color='#000000', width=0)))

valor_formatado = locale.currency(95508371.18, grouping=True, symbol='R$')  # Valor exemplo para ilustração

grafico_pizza.update_layout(
    annotations=[dict(text=valor_formatado, x=0.5, y=0.5, font_size=11, showarrow=False, font_color='black')],
    title='Dívida Atual - Maio 2023',
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    legend=dict(
        orientation="v",
        yanchor="bottom",
        y=0.9,
        xanchor="left",
        x=-0.1
    ),
    plot_bgcolor='lightblue'
)
# Criação do gráfico de barras
grafico_barras = go.Figure(data=go.Bar(x=periodo, y=divida_recorrente,
                                      text=[locale.currency(valor, grouping=True, symbol='R$') for valor in divida_recorrente],
                                      textposition='auto',
                                       textangle=-45))

# Atualizar as cores e layout do gráfico de barras
grafico_barras.update_traces(marker=dict(color=px.colors.qualitative.Pastel))

grafico_barras.update_layout(
    title='',
    xaxis_title='Período',
    yaxis_title='Valor (R$)',
    font=dict(
        family='Arial, sans-serif',
        size=14,
        color='#333333'
    ),
    plot_bgcolor='#f2f2f2',
    paper_bgcolor='#ffffff',
    margin=dict(l=40, r=40, t=60, b=40),
    height=700, # Altura do gráfico
    width=1200 # Largura do gráfico
)

# Criação do layout do dashboard
app = dash.Dash(__name__)


dashboard3_style = {
    'background-color': '#FFFFFF',
    'padding': '10px 10px',
    'margin': '10px 10px',
    'border-radius': '15px',
    'color': '#FFFFFF'  # Texto branco

}

app.layout = html.Div(
    style=dashboard3_style,
    children=[
        html.H1('Composição da dívida do IGESDF',
                style={'color': 'black'}  # Texto branco
                ),
        html.Div(className='row', children=[
            html.Div(className='six columns', children=[
                dcc.Graph(id='grafico-linhas', figure=grafico_divida_recorrente)
            ]),
            html.Div(className='six columns', children=[
                dcc.Graph(id='grafico-barras', figure=grafico_barras)
            ])
        ], style={'display': 'flex'}),

        #grafico de pizza
        html.Div(className='row', children=[
            html.Div(className='six columns', children=[
                dcc.Graph(id='grafico-pizza', figure=grafico_pizza)
            ])
        ]
        )




    ]
)





if __name__ == '__main__':
    # selecionar uma porta específica para rodar o servidor
    app.run_server(debug=True)

