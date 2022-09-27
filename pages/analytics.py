import dash
from dash import dcc, html, Input, Output,callback
import pandas as pd
import plotly.express as px

mc_menu = pd.read_csv('India_Menu.csv')

line_fig = px.line(data_frame=mc_menu, x='Menu Items', y='Total Sugars (g)', title='Total Sugar per Item')
bar_fig = px.bar(data_frame=mc_menu, x='Menu Items', y='Protein (g)',title='Total Protein per Item')

max_sugar = mc_menu['Total Sugars (g)'].max()
min_sugar = mc_menu['Total Sugars (g)'].min()

max_protein = mc_menu['Protein (g)'].max()
min_protein = mc_menu['Protein (g)'].min()

print(min_sugar)
print(max_protein)
print(min_protein)

mc_logo = ('https://th.bing.com/th/id/R.bd25b8aa0f5c3641790d6c526ea65e4b?rik=6DnUU%2f2uBcOGfw&riu=http%3a%2f%2fwww.pngall.com%2fwp-content%2fuploads%2f4%2fMcdonalds-Logo-PNG-Picture-180x180.png&ehk=e3cUzTVaY01ZtXeqlJ8K23bXnAOVhbiWWhuQKgBcbwg%3d&risl=&pid=ImgRaw&r=0')

#This is the way to call the app inside of a page
dash.register_page(__name__)

#the app was not called so this part is just "layout"
# Set up the layout with a single graph
layout = html.Div(children=[
      
    html.Div(    
        html.Img(src=mc_logo),
        style={'text-align':'center', 'font-size':22}
    ),    
        
    html.Div(    
        # Add a H1
        html.H1("McDonald's Analysis"),
        style={'text-align':'center', 'font-size':22}    
    ),    
        
    # Add an overall text-containing component
    html.Div(
        html.H5(children=[
            # Add the max sugar text
            f"This year, the item with the biggest amount of sugar is Large Fanta Orange with: ", 
            html.B(max_sugar),
            html.B("g"),
            html.Br(),
            ]),
            style={'text-align':'center', 'font-size':22}
    ),    
    html.Br(),
    
    html.Div(
        html.H5(children=[
            # Add the min sugar text
            f"This year, the item with the smallest amount of sugar is L1 Coffee, Coke Zero Can and Vedica Natural Mineral Water with: ", 
            html.B(min_sugar),
            html.B("g"),
            html.Br(),
            ]),
            style={'text-align':'center', 'font-size':22}
    ),
    html.Br(),
    
    html.Div(
        html.H5(children=[
            # Add the min sugar text
            f"This year, the item with the biggest amount of protein is Chunky Chipotle American Burger Chicken with: ", 
            html.B(max_protein),
            html.B("g"),
            html.Br(),
            ]),
            style={'text-align':'center', 'font-size':22}
    ),    
    html.Br(),
    
    html.Div(
        html.H5(children=[
            # Add the min sugar text
            f"This year, the item with the smallest amount of protein is L1 Coffee, Small Coca-Cola, Medium Coca-Cola, Large Coca-Cola, Small Fanta Oragne, Medium Fanta Orange, Large Fanta Oragne, Small Thums-up, Medium Thums-up, Large Thums-up, Small Sprite, Medium Sprite, Large Sprite, Coke Zero Can, Vedica Natural Mineral Water and Maple Syrup with: ", 
            html.B(min_protein),
            html.B("g"),
            html.Br(),
            ]),
            style={'width':'750px', 'margin':'auto','text-align':'center', 'font-size':22}
    ),    
    
    # Add both graphs
    html.H3('Total Sugar per Item'),    
    html.Div(dcc.Graph(
        id='line_graph', 
        figure=line_fig,
        style={'width':'750px', 'margin':'auto'}),
    ),   
    
    html.H3('Total Protein per Item'),
    html.Div(
        dcc.Graph(
            id='bar_graph', 
            figure=bar_fig,
            style={'width':'750px', 'margin':'auto'}),
    ),
    
    html.Br(),
    html.H3('In the dropdown below you can find the items with the biggest and the smallest amount of sugar and protein:'),
    dcc.Dropdown([
        'L1 Coffee', 
        'Small Coca-Cola', 
        'Medium Coca-Cola', 
        'Large Coca-Cola', 
        'Small Fanta Oragne', 
        'Medium Fanta Orange', 
        'Large Fanta Oragne', 
        'Small Thums-up', 
        'Medium Thums-up', 
        'Large Thums-up', 
        'Small Sprite', 
        'Medium Sprite', 
        'Large Sprite', 
        'Coke Zero Can', 
        'Vedica Natural Mineral Water', 
        'Maple Syrup',
        'Chunky Chipotle American Burger Chicken'],
        id='demo-dropdown',
        style={'width':'750px', 'margin':'auto'}
    ),
    html.Div(id='dd-output-container')
            

], style={'text-align':'center', 'font-size':22, 'background-color':'rgb(255, 242, 236)'})  

#the app was not defined so you need to change to @dash
@dash.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'
