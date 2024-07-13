# Predict the next word in a sentence
In this project we will be working on text dataset which is a book written by Plato - The Republic. We preprocess the data into a more usable format and train our Deep Learning LSTM model. This model is based on Neural Net-Architecture and provides very high performance on sequence based datasets as it has a feedback structure helping the model remember sequence of data input and the changes that are happening. Then we create a django project which becomes our base website that will be hosted on AWS.
LSTM networks were designed specifically to overcome the long-term dependency problem faced by recurrent neural networks RNNs (due to the vanishing gradient problem). LSTMs have feedback connections which make them different to more traditional feedforward neural networks. This property enables LSTMs to process entire sequences of data (e.g. time series) without treating each point in the sequence independently, but rather, retaining usefull information about previous data in the sequence to help with the processing of new data points.
Django is a free and open source web application framework written in Python. It includes advanced functionality like authentication support, management and admin panels, contact forms, comment boxes, file upload support, and more. In other words, if you were creating a website from scratch you would need to develop these components yourself. By using this framework instead, these components are already built, you just need to configure them properly to match your site.

# THE STEP 
1. create a virtual environment.
2. install django version-3.2.0
3. create a project : django-admin startproject <project_name>
4. cd into project.
5. create an app: python manage.py startapp <app_name>
6. setting up the setting.py inside project directory.
7. run the command to initialize the tables: python manage.py migrate.
run the command: python manage.py runserver.

->When creating your private key using puttyGen, check the "save private key",
I might have mistakenly said the public key.

btw you need pycharm hehe







