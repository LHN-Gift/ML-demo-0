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

# COMMAND ----------

data = {
    'name': ['Nhat', 'Tam', 'N. Anh', 'Q. Anh'],
    'professional': ['Data Engineer', 'CEO', 'Boss', 'Boss']
}

career = pd.DataFrame(data=data)

career

# COMMAND ----------

print('Done adding extra data')

# COMMAND ----------

# join two dataframes
# ===================
df = df.merge(career, on='name')
df

# COMMAND ----------

print('Done')
