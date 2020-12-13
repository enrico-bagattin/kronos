
# KRONOS  ⚡

### Lab of Software Project Development 
## CHECK THE WEATHER! 🌞
The aim of our project is to create a simple software that behaves like a weather app. 
Our software will provide the user data about the current weather and much more for a given city.

**Let's check in detail how it works!**

## Get started! 💻
To run the program, as a prerequisite you should have at least **Python 3.5 version.**

In order to start you have to install the required dependencies: 
```
pip3 install -r requirements.txt
```

**Now you are ready to try our program!**

You can try using our software by writing:
```
python3 main.py Berlin
```

## Functionalities 🛰

When the user has selected the city of interest, our software provides him with a user-friendly, easy readable and good looking table. 

The table lists a lot of interesting information: 

OUTPUT | OUTPUT DESCRIPTION 
------------ | ------------- 
CITY | City selected by the user 
WEATHER| How is the current weather like
TEMPERATURE | Current temperature expressed in celsius degrees 
DESCRIPTION| Weather broader description 
ICON | Weather visual description 
AIR QUALITY| Mean of the most recent air quality levels of the given city 
ICON | Color describing the healthy level with respect to the air quality index


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


## Documentation 📖
Documentation can be opened with: `open sphinx/_build/html/index.html`.
Here you can find the information about the functions you can find in the various modules. 
It has been made with [Sphinx](https://www.sphinx-doc.org/en/master/)


## Data Sources 📁
### APIs
The program based itself on two main API software: 
- **Opencage API:** useful to get geographic coordinates (latitude and longitude) given a specific city name.
- **Current Weather API:** used to get current weather information given specific coordinates. 

### CSV module
In oder to provide our users with further data about the city of interest, we have add a further dataset. 
The dataset includes data collected by the World Health Organization about the air quality mean per year for **10.075 cities** around the world. 
When queried, it reports to the user a **mean of air quality** levels registered in the most recent year. 

> **Note**: If the city is not present in the database, it reports `<n.d.>`.

The air quality is divided in different levels represented in the following table. 

AIR QUALITY INDEX |LEVELS OF HEALTH |COLORS 
------------ | ------------- | -------------
0 to 49 | Healthy | Green 
50 to 150 | Moderate healthy | Orange
151 to 300 | Unhealthy | Red
over 300 | Very unhealthy | Purple 

### Database
The software includes also a database, which keeps track of all the forecasts made by the program. 

The database stored the following variables: 

VARIABLE | VARIABLE DESCRIPTION
------------ | ------------- 
Timestamp | When the research was done
City | The city on which the research has been conducted
Weather | The forecasted weather for the given city
Temperature | The forecasted temperature expressed in celsius degrees 
Icon | The visual representation of the weather 

> **Note**: The database is created automatically when the software is used.

## Testing 🕵️‍♀️
We have tested our air_quality.py module (based on the air quality.csv ) 
and the open_cage.py module. 
You can find both tests in our `kronos_package/tests/`.

To run them from the main folder use:
```
python3 -m unittest -v -b 
```

All tests run correctly. 
 
## Authors 🧑‍🤝‍🧑🧑‍🤝‍🧑
- Bagattin Enrico 
- Bestetti Lucrezia Wally
- Doretto Alessandro 
- Mosele Gianluigi 
- Scarselli Lavinia

## License 
[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)

