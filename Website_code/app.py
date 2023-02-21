import xgboost as xgb
import streamlit as st
import pandas as pd
import pickle

#Loading up the Regression model we created
with open('model_pickle','rb') as f:
  model=pickle.load(f)


#Caching the model for faster loading
@st.cache_data 


# Define the prediction function
def predict(country_index, Year, Schizophrenia, Bipolar_disorder, Eating_disorder, Anxiety, drug_usage, depression, alcohol, latitude, longitude):
    #Predicting mental health
    
    prediction = model.predict(pd.DataFrame([[country_index, Year, Schizophrenia, Bipolar_disorder,Eating_disorder, Anxiety, drug_usage, depression, alcohol, latitude, longitude]], columns=['Country', 'Year', 'Schizophrenia', 'Bipolar_disorder','Eating_disorder', 'Anxiety', 'drug_usage','depression', 'alcohol','latitude','longitude']))
    return prediction



country_name=['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'G20', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North America (WB)', 'North Korea', 'North Macedonia', 'Northern Ireland', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Asia (WB)', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wales', 'Western Pacific Region (WHO)', 'World', 'Yemen', 'Zambia', 'Zimbabwe']
year=[1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023]

st.markdown("<h1 style='text-align: center; color: white;'>Mental Health Predictor</h1>", unsafe_allow_html=True)
st.image("""img.jpg""")
st.header('Enter the characteristics of the Mental Health:')
country = st.selectbox('Country name:', country_name)
country_index=country_name.index(country)
Year = st.selectbox('year:', year)
Schizophrenia = st.number_input('Schizophrenia:')
Bipolar_disorder = st.number_input('Bipolar_disorder:')
Eating_disorder = st.number_input('Eating_disorder:')
Anxiety = st.number_input('Anxiety:')
drug_usage = st.number_input('drug_usage:')
depression = st.number_input('depression:')
alcohol = st.number_input('alcohol:')
latitude = st.number_input('latitude:')
longitude = st.number_input('longitude:')

if st.button('Predict AgeYears_lost'):
    value = predict(country_index, Year, Schizophrenia, Bipolar_disorder,Eating_disorder, Anxiety, drug_usage, depression, alcohol,latitude, longitude)
    st.success(f'The predicted AgeYears_lost7 is {value[0]:.2f}')