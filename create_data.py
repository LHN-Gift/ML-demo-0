# Databricks notebook source
import pandas as pd

# COMMAND ----------

data = {
    'name': ['Nhat', 'Tam', 'N. Anh', 'Q. Anh'],
    'age': [40, 35, 4, 2]
    'pob': ['Hue', 'Saigon', 'Saigon', 'Saigon']
}

df = pd.DataFrame(data=data)

df

# COMMAND ----------

print('Done example data')
