
# KRONOS  ⚡

### Lab of Software Project Development 
## CHECK THE WEATHER! 🌞
The aim of our project is to create a very simple software that behaves like a weather app. 
Our software will provide the user data about the current weather and much more for a given city.

**Let's check in detail how it works!**

##Get started! 💻
To run the program, as a prerequisite you should have at least **Python 3.5 version.**

In order to start you have to install the required dependencies: 
```
pip3 install -r requirements.txt
```

**Now you are ready to try our program!**

For python 3.8 you can try it using:
```
python3.8 main.py Berlin
```

## Functionalities 🛰

When the user has selected the city of interest, our software provides him with a user-friendly, easy readable and good looking table. 

The table lists a lot of interesting information: 

Output | Output description  
------------ | ------------- 
city | city selected by the user 
weather | how is the current weather like
temperature | current temperature expressed in celsius degrees 
description | weather broader description 
icon | weather visual description 
air quality | mean of the most recent air quality levels of the given city 
icon | a color describing the healthy level with respect to the air quality index


## Command line parameters: 💾
**Positional parameters:** 
- the chosen city.
> **Note**: If you want to insert a city that has a space in the name, you must write for example `<"Abu Dhabi">`.

**Optional parameters:**
- *-v, --verbose* : be more verbose;
- *--version* : show program's version number and exit; 
- *-h, --help* : show this help message and exit;
- *--history N* : history of the previsions. 
> **Note**: *--history N*; the user would be able to specify the number of desired history rows.


##Documentation 📖

## Data Sources 📁
###APIs
The program based itself on two main API software: 
- **Opencage API:** useful to get geographic coordinates (latitude and longitude) given a specific city name.
- **Current Weather API:** used to get current weather information given specific coordinates. 

###CSV module
In oder to provide our users with further data about the city of interest, we have add a further dataset. 
The dataset includes data collected by the World Health Organization about the air quality mean per year for **10.075 cities** around the world. 
When queried, it reports to the user a **mean of air quality** levels registered in the most recent year. 

> **Note**: If the city is not present in the database, it reports `<n.d.>`.

The air quality is divided in different levels represented in the following table. 

Air quality index|Levels of health |Colors 
------------ | ------------- | -------------
0 to 49 | healthy | green 
50 to 150 | moderate healthy | orange
151 to 300 | unhealthy | red
over 300 | very unhealthy | purple 

###Database
The software includes also a database, which keeps track of all the forecasts made by the program. 

The database stored the following variables: 

Variable | Variable description  
------------ | ------------- 
timestamp | when the research was done
city | the city on which the research has been conducted
weather | the forecasted weather for the given city
temperature | the forecasted temperature expressed in celsius degrees 
icon | the visual representation of the weather 


## Testing 🕵️‍♀️


##Authors 
- Bagattin Enrico 
- Bestetti Lucrezia Wally
- Doretto Alessandro 
- Mosele Gianluigi 
- Scarselli Lavinia

##License
[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)

