# NoobML
A digital Platform automating Machine Learning Pipeline.  
` Note: The project is still under developement and will be updated soon.`
<br>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About The Project](#about-the-project)
* [Architecture](#architecture)
* [Installations](#installations)


![alt text](./Documentation/full.png)

## About The Project
NoobML is a django web app that allows simple machine learning tasks to be carried out even for the most novice users. The highlight of the project is eliminating the use of code. User can just plug in their dataset and within minutes get predictions and answers to many business questions. We all know how powerful data can be and this is just a stepping stone to elevate business decision making process.  <br> 
![alt text](https://raw.githubusercontent.com/coreprinciple97/coreprinciple97/master/images/pytorch.svg)  &ensp;&ensp;&ensp;
![alt text](https://raw.githubusercontent.com/coreprinciple97/coreprinciple97/18ba183450b3559461d670950d4d127d3935653b/images/django.svg)  &ensp;&ensp;&ensp;
<img title="Python" alt="Python" src="https://raw.githubusercontent.com/coreprinciple97/coreprinciple97/master/images/python.svg" width="50" height="50" />  &ensp;&ensp;&ensp;
<img title="Python" alt="mysql" src="https://raw.githubusercontent.com/coreprinciple97/coreprinciple97/master/images/mysql.svg" width="50" height="50" />  &ensp;&ensp;&ensp;
<img title="Python" alt="Tensorflow" src="https://raw.githubusercontent.com/coreprinciple97/coreprinciple97/master/images/tf.svg" width="50" height="50" />  &ensp;&ensp;&ensp;



## Architecture

The web app is developed in **python** using **Django framework**. Most of the logic is written in python with the help of numerous machine learning libraries such as  **pandas, numpy, matplotlib**. At the core of the project, **Pytorch** was used for training the model.
Some of the models available include:
 * Logistic Regression
 * Random Forest
 * SVM
 * Decision Tree
 * K Means Clustering


## Installations
* Make sure you have python3 installed
* Create a virtual environment
* Source the virtual environment
* Run `pip install -r requirements.txt`
* `cd` to `code/NoobML`
* Run `python manage.py runserver --noreload --nothreading`
* Go to `http://127.0.0.1:8000/read/` (port may be different)

