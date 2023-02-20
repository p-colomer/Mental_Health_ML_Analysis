CREATE TABLE Mental_substance_disorders(
Entity VARCHAR NOT NULL,
Code VARCHAR (20),
Year VARCHAR (20)NOT NULL,
Prevalance FLOAT (10)NOT NULL,
Latitude FLOAT (4)NOT NULL,
Longitude FLOAT (4)NOT NULL

);

CREATE TABLE Different_disorders(
Entity VARCHAR NOT NULL,
Year VARCHAR (20)NOT NULL,
Schizophrenia FLOAT NOT NULL,
Bipolar_disorder FLOAT NOT NULL,
Eating_disorder FLOAT (10)NOT NULL,
Anxiety FLOAT NOT NULL,
Drug_usage FLOAT NOT NULL,
Depression FLOAT NOT NULL,
Alcohol FLOAT NOT NULL,
Latitude FLOAT NOT NULL,
Longitude FLOAT NOT NULL
);

SELECT * FROM Different_disorders

CREATE TABLE Prevalance_of_depression_males_vs_female(
Entity VARCHAR NOT NULL,
Code VARCHAR (20),
Year VARCHAR (20)NOT NULL,
Prevalance FLOAT (10)NOT NULL,
Prevalances FLOAT (10)NOT NULL,
Population FLOAT (10)NOT NULL,
Continent VARCHAR (20)NOT NULL,
Latitude FLOAT (4)NOT NULL,
Longitude FLOAT (4)NOT NULL
);
CREATE TABLE Mental_substance_disorders_by_sex(
Entity VARCHAR NOT NULL,
Code VARCHAR (20),
Year VARCHAR (20)NOT NULL,
Prevalance FLOAT (10)NOT NULL,
Prevalances FLOAT (10)NOT NULL,
Population FLOAT (10)NOT NULL,
Continent VARCHAR (20)NOT NULL,
Latitude FLOAT (4)NOT NULL,
Longitude FLOAT (4)NOT NULL,
Num_of_women FLOAT (10)NOT NULL,
Num_of_men FLOAT (10)NOT NULL
);
SELECT * FROM Mental_substance_disorders_by_sex

CREATE TABLE Disabilty_adjusted_life_years(
Entity VARCHAR NOT NULL,
Code VARCHAR (20),
Year VARCHAR (20)NOT NULL,
DALYs FLOAT (10)NOT NULL,
Latitude FLOAT (4)NOT NULL,
Longitude FLOAT (4)NOT NULL
);


SELECT * FROM Disabilty_adjusted_life_years



