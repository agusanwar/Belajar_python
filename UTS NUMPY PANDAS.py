#!/usr/bin/env python
# coding: utf-8

# In[113]:


# Library python import numpy dan pandas
import numpy as np
import pandas as pd 


# Import Dataset
df = pd.read_csv("ds_salaries.csv")

import matplotlib.pyplot as plt
import seaborn as sns


# In[55]:


# untuk menampilkan 17 data pertama pada data set dimulai dari 0-16
df.head(7)


# In[24]:


# dimensi dataframe dalam dataset row dan column
df.shape


# In[21]:


# mengambil data berdasarkan atribute select dictionary index
df['job_title']


# In[22]:


# mengambil data berdasarkan atribute select dictionary index choose index colum
df['job_title'][3]


# In[30]:


#menampilkan column pada dataset
df.columns


# In[34]:


# Untuk memeriksa apakah ada data dengan value null
df.isnull().sum()


# In[56]:


df.isnull().any()


# In[35]:


# untuk cek index beserta barisnya
df.info()


# In[41]:


# untuk cek apakah ada data yang missing
missing_data(df)


# In[47]:


# variabel data yang menyimpan beberapa List untuk membuat DataFrame baru
df = df[["work_year", "job_title", "salary", "salary_currency", "employee_residence","company_location","company_size"]]
df.head()


# In[52]:


# akses index ke-50
df.loc[50]


# In[67]:


# untuk Memeriksa jumlah nilai unik pada setiap kolom
dict = {}
for col in df.columns:
    dict[col] = df[col].value_counts().shape[0]

pd.DataFrame(dict, index=['unique value count']).transpose()


# In[60]:


df.describe()


# In[110]:


# Untuk memisahkan data variable category 
category_columns = ['work_year', 'experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'remote_ratio', 'company_location', 'company_size']
continues_columns = ['salary', 'salary_in_usd']

print('-------------Print Category--------------------')
print("Terdapat data {} pada Category Columns: {}".format(len(category_columns), category_columns))
print('-------------Print Continues--------------------')
print("Terdapat data {} pada Continuous Columns : {}".format(len(continues_columns), continues_columns))


# In[114]:


df[con_cols].describe().transpose()


# In[115]:


# data bar job_title
fig = plt.figure(figsize=(25,25))
gs = fig.add_gridspec(3, 3)


a = fig.add_subplot(gs[2,2])

df_top_feature_values = df[cat_cols[3]].value_counts().reset_index()
df_top_feature_values.columns = ['col_values', 'value_count']
top_values = df_top_feature_values['col_values'].head(9)

sns.countplot(ax=a, data=df[df[cat_cols[3]].isin(top_values)], x=cat_cols[3])
trimmed_xlabels = [s.get_text().replace('Machine Learning', 'ML') for s in ax4.get_xticklabels()]
ax4.set_xticklabels(trimmed_xlabels)
plt.xticks(rotation=10, fontsize=7)


for s in ['right', 'left', 'bottom', 'top']:
    a.spines[s].set_visible(False)
plt.xticks(rotation=20)
plt.show()


# In[116]:


# data matrik korelasi
df_corr = df[con_cols].corr().transpose()

mask = np.triu(np.ones_like(df_corr, dtype=bool))
sns.heatmap(df_corr, annot=True, mask=mask)


# In[ ]:





# In[ ]:




