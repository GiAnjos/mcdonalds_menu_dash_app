#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px


# In[ ]:


# Create the Dash app
app = dash.Dash(__name__,use_pages=True)

# Set up the layout with a single graph
app.layout = html.Div(
    children=[
        
    html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container,    
])    
   
# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server()
#People usually use debug=True but in my case that never worked    


# In[ ]:




