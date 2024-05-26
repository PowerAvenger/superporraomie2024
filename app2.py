import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px

from data import datos






fig=px.bar(datos, x="%_desvio",y="Clasificación", orientation='h', text='%_desvio', title='Clasificación provisional MVPStarPower2024')
fig.update_layout(
    height=1000,
    width=3000,
    
    
    )
fig.update_yaxes(autorange='reversed')
fig.update_xaxes(range=[0, None])
event = st.plotly_chart(fig,use_container_width=True)

