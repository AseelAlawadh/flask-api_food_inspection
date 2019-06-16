Capstone Project : Food inspection vaiolation [Repo](https://github.com/AseelAlawadh/food_inspections) 

### Dataset Brief Description: 
This dataset contains information from inspections of restaurants in Chicago from January 1, 2013 to April 30, 2019.

### Description:
This information is derived from inspections of restaurants in Chicago from January 1, 2013 to April 30, 2019. Inspections are performed by staff from the Chicago Department of Public Health’s Food Protection Program. Inspections are done using a standardized procedure. The results of the inspection are inputted into a database, then reviewed and approved by a State of Illinois Licensed Environmental Health Practitioner (LEHP). A subset of data elements are extracted from this database and downloaded into this data portal. 

### Problem Statment:
The aim of this project is to have a predictive model would help by optimize restaurant health inspections for city also reduce the violations of restaurants and contamination of food by taking the impact of the region and the census of housing and whether the restaurant succeed in not taking any violation and what is the probability and seriousness of the violation that will be done.


### Executive summary:
We analyzed the data of food violations for restaurants in Chicago  considering 3 factors numbers of crime, and community area. Our goal in the project is to determine the number of crimes and weather conditions. Whether the two conditions are related to making the restaurant take any number of violations.

We noticed that the area is an impact for the violations, so based on that we could predict the rate of violation of the restaurant.

### REQUIREMENTS:
- `Pytohn`: [install](https://www.python.org/downloads/release/python-365/)
- `pip3`:  [install](https://pip.pypa.io/en/stable/)
- `Jupyter` : [link](https://jupyter.org)
- `Numbpy` : [link](https://www.numpy.org)
- `Pandas` : [link](https://pandas.pydata.org)
- `Seaborn` : [link](https://seaborn.pydata.org)
- `Matplotlib` : [link](https://matplotlib.org)
- `Scipy` : [link](https://www.scipy.org)
- `imblearn.over_sampling: SMOTE` : The classes targeted will be over-sampled or under-sampled to achieve an equal number of sample with the majority or minority class. [link](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html)
- `XGboost` : is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. [link](https://xgboost.readthedocs.io)


### Challenges: 
- Time: the preiod of time by getting the dataset and start doing the project was short (a week) from submitting the project.
- Researsh: as part of being a data engineer is to have a good insight of undertanding and doing the reasearch on data was short also.



### Food api:
Write a simple Rest API with Python Flask in order to have the infomration from Api. The api contains 2 modules: 

- Food.
- Resturant: this module contains the information of resturant (area, location, commuity .. etc) also will contain the prediction model and the api will start giveing the result of prediction (`Pass`, `Pass w/Condition`, `Fail`). 

#### install project:
- `Pytohn`: [install](https://www.python.org/downloads/release/python-365/)
- `pip3`:  [install](https://pip.pypa.io/en/stable/)
- `Flask` :  >=1.0,<2.0 [install](http://flask.pocoo.org)
- `SQLAlchemy` : [install](https://www.sqlalchemy.org)
- `Flask Restplus`: [install](https://flask-restplus.readthedocs.io/en/stable/)
- `joblib`: for reading the model [install](https://joblib.readthedocs.io)


### Deliverables: 
The project contains modules can be communicate with predict model. also ready to comunicate with Database and geting respnse from the Api as Json.

### Food Dashboard:[Repo](https://github.com/AseelAlawadh/food_inspection_dashboard)
Write a simple Dashboard to communicate and fetch the data from Rest API.

#### install project:
 - `npm`: [install](https://www.npmjs.com)
 - `node`: [install](https://nodejs.org/en/) 
 - `Angular`: [install](https://angular.io)

### Deliverables: 
the project still in initial state of building the dashboard.

### Acknowledgements:
The Dataset Brief Description has been copied from [FOOD INSPECTION FORECASTING](https://chicago.github.io/food-inspections-evaluation/). also I would like to mention this research was conducted by Aseel Alawadh as part of General Assempply program (DSI) with support from DSI Instructors.I would especially like to thank Khaled Alresheed, Androw , Esra for their efforts in deomnstrate and help for understanding the data to have the predictive model. 
