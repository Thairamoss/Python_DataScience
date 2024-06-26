# -*- coding: utf-8 -*-
"""regresso linear parte 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18ov_Rovms7QMf0-TQYMtWFesbawOvID4
"""

import statistics as st

#Dados
x=[4,5,6,7,8]
y=[14,25,26,17,8]

def linear_regression(x,y):
  n=len(x)
  media_x=st.mean(x)
  media_y=st.mean(y)
  covariancia=sum((x[i] - media_x)*(y[i] - media_y) for i in range(n))
  variancia=sum((x[i]-media_x)**2 for i in range(n))
  b1=covariancia/variancia
  b0=media_y-b1*media_x
  return b0,b1

intercept, slope = linear_regression(x,y)

print('o coeficiente de inclinação é:', intercept)

print('o coeficiente de inclinação é:', slope)

print('sdmf')