# Mental Health - Machine Learning Analysis
![mental_health](https://photographylife.com/wp-content/uploads/2016/06/Mass.jpg)

## Team
-   Farah Hayat
-   Patricia Colomer
-   Prerna Dutt
-   Vivian Nnadozie

## Repository Structure

- <b>README.md:</b> The top level README for reviewers of this project
- <b>Data_Cleaning.ipynb:</b> Complete cleaning of all 5 csv files in jupyter notebook
- <b>ML_Future_Years_Prediction.ipynb:</b> Further exploration of the data to predict the prevalence of mental health disorders in the most affected countries, the G20 countries and the world overall.
- <b>Prediction_Slides:</b> The project presentation slides
- <b>Resources folder:</b> Contains the initial uncleaned data files
- <b>Cleaned_data folder:</b> Contains the cleaned data files

## Technologies Used
-   Python
-   Pandas
-   Matplotlib
-   Nominatim
-   NumPy
-   SciPy
-   Scikit-Learn
-   Tableau

## Abstract 
Nearly one billion people suffer from a mental health condition. A mental disorder is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour.  It is usually associated with distress or impairment in important areas of functioning.

Using data from the [Our World in Data](https://ourworldindata.org/mental-health), machine learning was applied to predict the percentage of the population that will suffer a mental health condition in the 2030 to 2080. These predictions could be used to recognize and develop ways to help the rising amount of people in the population with a mental health condition. Using tableau, we were able to relate the percentage of those with mental health conditions to -----

The results show that ----


## Introduction
We can all be "sad" or "blue" at times in our lives. We have all seen movies about the madman and his crime spree, with the underlying cause of mental illness. We sometimes even make jokes about people being crazy or nuts, even though we know that we shouldn't. We have all had some exposure to mental illness, but not many understand or know what it is. **A mental illness can be defined as a health condition that changes a person's thinking, feelings, or behavior (or all three) and that causes the person distress and difficulty in functioning.** As with many diseases, mental illness is severe in some cases and mild in others. Individuals who have a mental illness don't necessarily look like they are sick, especially if their illness is mild. Other individuals may show more explicit symptoms such as confusion, agitation, or withdrawal. There are many different mental illnesses, including depression, schizophrenia, attention deficit hyperactivity disorder (ADHD), autism, and obsessive-compulsive disorder. Each illness alters a person's thoughts, feelings, and/or behaviors in distinct ways. In this project, we will exploring the prevalence of mental health disorders throughout the world.

According to the World Health Organisation more than 970 million (1 in 8) people live in the world with a mental disorder.[¹](https://www.who.int/news-room/fact-sheets/detail/mental-disorders) Most suicides are related to psychiatric disease, with depression, substance use disorders and psychosis being the most relevant risk factors. However, anxiety, personality-, eating-, and trauma-related disorders, as well as organic mental disorders, also contribute.[²](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6165520/)


In this project we will be analysing the prevalence of mental health disorders across different countries from the 1990s to the 2020s.
We will also be using this data to predict the prevelence mental health disorders across those countries in future years.
We will clean the data using python and combine the DataFrames using SQL. 
We will use the cleaned data to train a ML model that can predict the future prevalence of mental health disorders around the world including: depression, schizophrenia, bipolar disorders, eating disorders, sleeping disorders, etc.
We will then use the analysed data to create visualisations that can better illustrate our findings. 

The analysis will help us derive meaningful conclusions from the data.

## Data Exploration and Cleaning
We have used one dataset from Kaggle: https://www.kaggle.com/datasets/programmerrdai/mental-health-dataset?select=share-with-mental-or-substance-disorders-by-sex.csv

The dataset contains 5 csv files: mental-and-substance-use-as-share-of-disease.csv, prevalence-by-mental-and-substance-use-disorder.csv, prevalence-of-depression-males-vs-females.csv, share-with-mental-and-substance-disorders.csv, share-with-mental-or-substance-disorders-by-sex.csv.

We cleaned up the data by finding and adding the latitudes and longitudes of each country, splitting and deleting columns. 
<img width="437" alt="image" src="https://user-images.githubusercontent.com/111776924/220148685-3a9f17ab-6983-449b-97b8-bf7496149e91.png">

























https://www.who.int/news-room/fact-sheets/detail/mental-disorders
https://ourworldindata.org/mental-health



