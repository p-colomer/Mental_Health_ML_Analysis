# Mental Health
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
- <b>Database.sql:</b> Database
- <b>ML_AgeYearsPrediction_DiffModels.ipynb:</b> ML models to predict the Disability Adjusted Life Years of countries
- <b>Mental_Health_Analysis.pptx:</b> The project presentation slides
- <b>Resources folder:</b> Contains the initial uncleaned data files
- <b>Cleaned_data folder:</b> Contains the cleaned data files
- <b>Website_Code Folder:</b> Contains the webpage created for the project

## Technologies Used

-   Python
-   Pandas
-   Matplotlib
-   Nominatim
-   NumPy
-   SciPy
-   Scikit-Learn
-   Tableau
-   SQL

## Abstract 

Nearly one billion people suffer from a mental health condition. A mental disorder is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour.  It is usually associated with distress or impairment in important areas of functioning.

Using data from Our World in Data[¹](https://ourworldindata.org/mental-health), machine learning was applied to predict the percentage of the population that will suffer a mental health condition in the years 2030 to 2080. These predictions could be used to recognize and develop ways to help the rising amount of people in the population with a mental health condition. Using tableau, we were able to relate the percentage of those with mental health conditions to -----

The results show that anxiety and depression are the most prevalent mental health disorders, and its prevalence its growing steadily.


## Introduction

We can all be "sad" or "blue" at times in our lives. We have all seen movies about the madman and his crime spree, with the underlying cause of mental illness. We sometimes even make jokes about people being crazy or nuts, even though we know that we shouldn't. We have all had some exposure to mental illness, but not many understand or know what it is. **A mental illness can be defined as a health condition that changes a person's thinking, feelings, or behavior (or all three) and that causes the person distress and difficulty in functioning.** As with many diseases, mental illness is severe in some cases and mild in others. Individuals who have a mental illness don't necessarily look like they are sick, especially if their illness is mild. Other individuals may show more explicit symptoms such as confusion, agitation, or withdrawal. There are many different mental illnesses, including depression, schizophrenia, attention deficit hyperactivity disorder (ADHD), autism, and obsessive-compulsive disorder. Each illness alters a person's thoughts, feelings, and/or behaviors in distinct ways.[²](https://www.ncbi.nlm.nih.gov/books/NBK20369/) In this project, we will exploring the prevalence of mental health disorders throughout the world.

According to the World Health Organisation more than 970 million (1 in 8) people live in the world with a mental disorder.[³](https://www.who.int/news-room/fact-sheets/detail/mental-disorders) Most suicides are related to psychiatric disease, with depression, substance use disorders and psychosis being the most relevant risk factors. However, anxiety, personality-, eating-, and trauma-related disorders, as well as organic mental disorders, also contribute.[⁴](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6165520/)

## Goal

Many people hold misconceptions about mental health and through this project we are hoping to address and correct the stigma surrounding mental health.
The goal of this project is to analyse data about countries affected by several mental health disorders including: depression, schizophrenia, bipolar disorder, eating disorders, anxiety, alcohol and drug abuse, in order to predict the percentages of the population that will experience a mental health disorder in future years.

## Data

The data for this project is from Kaggle and was gathered from an article on Our World in Data[¹](https://ourworldindata.org/mental-health) and produced by the Institute for Health Metrics and Evaluation. The data demonstrates that mental health disorders are common everywhere. Improving awareness, recognition, support and treatment for this range of disorders should therefore be an essential focus for global health. 
The data can be found at this website: https://www.kaggle.com/datasets/programmerrdai/mental-health-dataset?select=share-with-mental-or-substance-disorders-by-sex.csv

For this project, data was taken from the years between 1989 and 2019 and consisted of worldwide geospatial coverage.

## Approach

The approach for this project was to create many different model types to see what performs the best and to compare and contrast the different types of models. The modeling effort was done starting with simpler models and moving to more complex models. The models used were SVR, XGBoost, Random Forest, Decision Tree and ANN

## Methods

The way the data was preprocessed with feature engineering, filling missing values, and scaling was done with the goal of increasing accuracy of the models. For each type of model, a model was first trained and fitted with default parameters as a base. The tuned parameters were used to fit the same model using the resampled data for comparison. Performance was compared to the base model of each type, as well as between different model types. 

## Project Flowchart

<img width="667" alt="image" src="https://user-images.githubusercontent.com/111776924/220191858-269df74f-af46-426e-9876-2685d8ed17a5.png">

## Process for choosing Machine Learning Models 

![image](https://user-images.githubusercontent.com/109463488/220934450-593a8114-2062-488a-a7be-078e14e82b67.png)

Correlation Matrix : To assess related parameters 

![image](https://user-images.githubusercontent.com/109463488/220934517-27cdaa73-120f-4968-82bf-ce6e2668da98.png)


Model Results :

![image](https://user-images.githubusercontent.com/109463488/220934621-a8652dc6-0224-4ab5-b469-934117126f98.png)

![image](https://user-images.githubusercontent.com/109463488/220934661-3c2ccdb6-fe09-4810-bb7a-d16066a83fd6.png)

![image](https://user-images.githubusercontent.com/109463488/220934730-78a03c4b-39c0-443f-932a-93838a139ef8.png)

Random Forest: Our choice 
- We tried hyperparameter tunning to get best model fit as well as tried different models to find which algorithm is giving better accuracy. We found that random forest is the better choice amongst all algorithms considering the accuracy along with  factors such as complexity , cost , speed  are taken into account.
- It can handle both categorical and continuous variables.
- It is capable of handling large datasets with high dimensionality. 
- It enhances the accuracy of the model and prevents the overfitting issue
- Robust to outliers 


## Analysis

[Tableau was used](https://public.tableau.com/app/profile/patricia3281/viz/MentalHealthDisorders_16768057524010/MentalHealthDisorders) to analyse the prevalence of mental health disorders acrosss 210 countries, and the years lost due to mental health disorders. 

![image](https://user-images.githubusercontent.com/109463488/220466703-38a5fbd8-27d0-4a3d-824e-1c95d52efefe.png)

![image](https://user-images.githubusercontent.com/109463488/220466820-7fffa506-defe-4fd9-8309-6d41b2607004.png)

One DALY represents the loss of the equivalent of one year of full health. DALYs for a disease or health condition are the sum of the years of life lost to due to premature mortality (YLLs) and the years lived with a disability (YLDs) due to prevalent cases of the disease or health condition in a population.

The countries that have lost more years due to the prevalence of mental health disorders have lost up to 13 years (DALYs), whilst the countries where the prevalence of mental health disorders is lower have only lose around 1 year.

![image](https://user-images.githubusercontent.com/109463488/220469839-79a772d9-f687-46e8-ad76-c4c983543469.png)

The Machine Learning models wewe used to predict the prevalence of the disorders analysed in future years.

![image](https://user-images.githubusercontent.com/109463488/220470197-92e2d27a-8c93-4216-a5b2-24106e12b3a5.png)

![image](https://user-images.githubusercontent.com/109463488/220470255-5fb85c5f-19ec-4411-ace4-d85fe00901fc.png)

## Conclusions

Depression and anxiety are the most prevalent mental health disorders across the world, if the trend continues, in 2090 9% of the world population will suffer anxiety, and 6.5% will suffer depression.

Eating disorders are almost non existant in less developed countries, but they affect people from wealthier countries and its prevalence is growing. By 2090, if nothing is done, 0.5% of the G20 countries will suffer from an eating disorder.

## Future Directions

- <b>Try different models.</b> Predicting mental health disorder prevalency is a complex and multidimensional problem so it is not surprising that it is difficult to model. Perhaps exploring more model types could reveal a strategy that was just right for this task. A neural network, for example, could open up a huge range of possibilities that have not been explored in this project. The downside of neural networks is of course the lack of transparency in what features the model is using to make predictions.

## References

¹**Our World in Data, Mental Health:** https://ourworldindata.org/mental-health

²**National Center for Biotechnology Information, Information About Mental Illness and The Brain:** https://www.ncbi.nlm.nih.gov/books/NBK20369/

³**World Health Organisation Mental Health Overview:** https://www.who.int/news-room/fact-sheets/detail/mental-disorders

⁴**National Center for Biotechnology Informtation, Suicide Risk and Mental Disorders:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6165520/

