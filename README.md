# Image-Upload-In-Django-
This repo show you how to upload images 

<div align="center"><h1>  Djanog - Image upload scripts </h1> </div>
<div align="center"> In this repo, I show you. How to upload image in django project app. </div>


Usage
-------
You can clone the project and run the following command to install: 

```bash
$ git clone https://github.com/rahulcs754/Image-Upload-In-Django-.git
```

*I consider, You have already installed virtualenv and pip.*

*First of all, create a virtualenv in a working directory*

```bash
$ virtualenv virtualenv_name
```
* or In window, run following command 

```bash
$ python -m virtualenv virtualenv_name
```

*after that you have to activate virtualenv machine by using the below command*

In linux
--------
```bash
$ source virtualenv_name/bin/activate
```
In Windows
------------
```bash
$ source virtualenv_name/Scripts/activate
```


 Installing list of dependencies to file
----------------------------------------

Change directory where requirements.txt file exists

```bash
pip install -r requirements.txt
```

create database  .
-----------------
```bash
$ python manage.py migrate
```

 create admin username and password
------------------------------------
```bash
$ python manage.py createsuperuser
```

run main file 
-------------
```bash
$ python manage.py runserver
```

*Note  : Make sure you cd into the *clone* folder before performing the command above.*


Stack
------
python3



