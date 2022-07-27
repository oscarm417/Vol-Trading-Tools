from historical_vol import * 
import pandas as pd 
import numpy as np 
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt



def get_vol_data(vol_data):
    minim = vol_data.min()
    maxim = vol_data.max()
    percentile_75 = vol_data.quantile(.75)
    percentile_25 = vol_data.quantile(.25)
    med = vol_data.median()
    vol_stats_dic = {"Max" : maxim,
                     "75 Percentile": percentile_75,
                     "Median":med,
                     "25 Percentile": percentile_25,
                     "Min":minim}
    vol_stats_dic = {k:round(v,2) for k,v in vol_stats_dic.items()}
    return vol_stats_dic
    
def volatility_cone(stock_data,cone_look_backs = [22,44,66,122],\
                    vol_estimation_type = GermanHV,look_back_days = None,\
                    start_date = None, end_date = None
                   ):
    #look back data
    if type(look_back_days) == int:
        data = stock_data[-1*look_back_days:]
    if start_date != None:
        data = stock_data[start_date:end_date]
        
    else:
        cut_off_period = max(cone_look_backs)*2
        data = stock_data.iloc[-1*cut_off_period:]
    vol_stats_table = pd.DataFrame(columns = cone_look_backs)
    vol_data = [vol_estimation_type(data,look_back_window = i) for i in cone_look_backs]
    vol_stats = {i[0] : get_vol_data(i[1]) for i in zip(cone_look_backs,vol_data)}
    vol_stats = pd.DataFrame(vol_stats)
    return vol_stats

def vol_plot(vol):
    fig = px.line(vol.T,symbol = "variable")
    fig.update_layout(title = "Historical Volatility Cone",
                    title_x = .5,
                    xaxis_title = "Days to Option Expiry",
                    yaxis_title = "Realized Vol.",
                    paper_bgcolor="white",
                    legend_title = "Stats",
                    template = "ggplot2")
    return fig