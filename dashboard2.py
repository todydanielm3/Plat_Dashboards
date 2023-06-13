from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from colorspacious import cspace_converter
import matplotlib as mpl
import plotly.io as pio
import locale



# Create a Dash app
app = Dash(__name__)
app.title = 'Fluxo de Caixa Consolodado de 2022'


# Load the data
df = pd.read_csv('DFC_2022.csv',sep=';',header=0)
d_inv = pd.read_csv('DFC_investimentos_2022.csv',sep=';',header=0)




#preenchendo os valores nulos com zero
df = df.fillna(0)
#print(df.head())

#removendo pontos e virgulas dos valores
df['IGESDF'] = df['IGESDF'].str.replace('.','')
df['IGESDF'] = df['IGESDF'].str.replace(',','.')

#DFC_investimentos
d_inv = d_inv.fillna(0)
d_inv['IGESDF'] = d_inv['IGESDF'].str.replace('.','')
d_inv['IGESDF'] = d_inv['IGESDF'].str.replace(',','.')




#convertendo o tipo de dado da coluna IGESDF para float
df['IGESDF'] = df['IGESDF'].astype(float)
d_inv['IGESDF'] = d_inv['IGESDF'].astype(float)




linhas_interesse = ['SALDO INICIAL','TOTAL DE INGRESSOS','CUSTO COM PESSOAL','CONCESSIONÁRIAS','MATERIAL DE CONSUMO','SERVIÇOS DE TERCEIROS','TOTAL DE DESEMBOLSOS CUSTEIO','SALDO FINAL']

linhas_interesse_inv = ['Repasse SES/DF (BRUTO)',
'Outros Ingressos/Rendimentos Aplicação Financeira',
'Desconto Contratual (METAS)',
'Repasse SES/DF (LÍQUIDO)',
'Bens de Capital',
'Obras',
'Outros Investimentos - Bens de Capital',
'Mobiliários',
'Equipamentos',
'TOTAL DE DESEMBOLSOS INVESTIMENTOS',
'SALDO INVESTIMENTOS',
'SALDO FINAL (CUSTEIO + INVESTIMENTOS)']


df_interesse = df[df['DESCRIÇÃO'].isin(linhas_interesse)]
df_interesse_inv = d_inv[d_inv['DESCRIÇÃO'].isin(linhas_interesse_inv)]


valores_igesdf = df_interesse['IGESDF'].tolist()
valores_igesdf_inv = df_interesse_inv['IGESDF'].tolist()




#criando grafico de barras com os valores da coluna IGESDF com cores
figura1 = px.bar(df_interesse, x=linhas_interesse, y=valores_igesdf, color=valores_igesdf, text=valores_igesdf, labels={'x':'Descrição','y':'Valores em R$'}, title='Fluxo de caixa - 2022')

figura1.update_layout(
    yaxis=dict(
        tickformat="R$",
        tickprefix="R$"
    )
)


#grafico de pizza
figura2 = go.Figure(data=[go.Pie(labels=linhas_interesse, values=valores_igesdf, hole=.3, textinfo='label+percent',
                                 insidetextorientation='horizontal'
                                )])
figura2.update_layout(annotations=[dict(text='Gastos\nIGESDF', x=0.5, y=0.5, font_size=10, showarrow=False)])

figura3 = px.bar(df_interesse_inv, x=linhas_interesse_inv, y=valores_igesdf_inv, color=valores_igesdf_inv,text=valores_igesdf_inv,labels={'x':'Descrição','y':'Valores em R$'},title='Fluxo de caixa em Investimentos ')


#categoria_ordem = ['Celetistas', 'Estatutários', 'Material de Consumo','Serviços de terceiros','Despesas Gerais','Concessionárias']

#graficos Quadro Demonstrativo de Despesas (QDD) - Março 2023

dashboard_style = {
    'background-color': '#FFFFFF',
    'padding': '10px 10px',
    'margin': '10px 10px',
    'border-radius': '15px',
    'color': '#FFFFFF'  # Texto branco

}

# Create the app layout
app.layout = html.Div(
    style=dashboard_style,
    children=[
    html.H1('Fluxo de Caixa - 2022',
            style={'color': 'black'}  # Texto branco
),
    
    html.Div([
        dbc.Col(dcc.Graph(figure=figura1), width=6),

    ])

#    html.Div([
#        dbc.Col(dcc.Graph(figure=figura2), width=6),
#        dbc.Col(dcc.Graph(figure=figura3), width=6),
#
#
#    ],style={'display': 'flex'})
#
])


            

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True,port=8055)
