## Visualisasi menggunakan Google Colab

# Import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Load data
data = pd.read_excel('/content/Data Final.xls')
data

# Descriptive Analysis
# Membuat loop untuk variabel yang ingin diplot
columns_to_plot = ['jenis_kelamin', 'umur', 'pendidikan', 'pekerjaan', 'pernikahan', 'tempat_tinggal', 'pengeluaran'] 

for column in columns_to_plot:
    # Group data and calculate percentages
    grouped_data = data.groupby([column, 'status_merokok'])['status_merokok'].count().reset_index(name='count')
    total_counts = grouped_data.groupby(column)['count'].sum().reset_index(name='total')
    merged_data = pd.merge(grouped_data, total_counts, on=column)
    merged_data['percentage'] = (merged_data['count'] / merged_data['total']) * 100

# Conditional sorting for 'pendidikan' chart
    if column == 'pendidikan':
        categories = ['Tidak sekolah', 'SD', 'SMP', 'SMA/SMK', 'Perguruan Tinggi']
        category_orders_param = {column: categories}  # Store category orders for 'pendidikan'
    else:
        category_orders_param = {}
        
    
    fig = px.bar(merged_data,
                 x=column,
                 y="percentage",
                 color="status_merokok",
                 color_discrete_map={"Merokok": "#616852", "Tidak Merokok/Berhenti Merokok": "#D8C888"},
                 labels={column: "", "status_merokok": ""},
                 text="percentage",
                 category_orders=category_orders_param
                 )

    # Update y-axis to display percentages
    fig.update_yaxes(ticksuffix="%")

    # Update text position, layout, and bar width
    fig.update_traces(texttemplate='%{text:.2f}%', 
                     textposition='inside', 
                     textfont_size=28,  # Mengatur ukuran teks nilai
                     width=0.5  # Mengatur lebar bar (0.5 adalah contoh, sesuaikan sesuai kebutuhan)
                     ) 
    fig.update_layout(
                      width=1400,
                      height=800,
                      uniformtext_minsize=8, 
                      uniformtext_mode='hide',
                      bargap=0.1,# Mengatur jarak antar bar (0.1 adalah contoh, sesuaikan sesuai kebutuhan)
                      yaxis_title='',
                      font=dict(
                          size=28,
                          color="black"
                      ),
                      title_x=0.5,
                      paper_bgcolor='white',
                      plot_bgcolor='white'
                      )
    # Place legend below the chart
    fig.update_layout(
        legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,  # Adjust the y position as needed
        xanchor="center",
        x=0.5
    ))
    fig.show()

