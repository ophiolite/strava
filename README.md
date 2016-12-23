# Strava Project

This repo is to document explorations with how I can interact with the Strava API for new projects and potentially to assist with the ultrasignup project. Project scoping began Dec. 8, 2016. Basic design delivery goal: 1Q2017. 

# Overarching question:

Can I predict reasonable training paces for athletes based on their Strava data?

Three major categories of paces for first product - easy pace, tempo pace and marathon pace

# Challenges:

Weather - Will pull weather data from weather underground in addition to cross-validating with Garmin temperature data (where available).

Seasonal variations - Seasonality can play a big role in training paces. Projecting this into a time-series model will be a challenge to be faced.

API limitations - To effectively model, I need to have users accept oauth to obtain their data from Strava. To begin modeling, I will need a diverse set of people to agree and store their keys securely in AWS. Strava also limits to 600 requests per day. The request limits may become a challenge as the project progresses.

Modeling challenges - May have to start with a more unsupervised approach to modeling until enough data becomes available to allow for semi-supervised or active machine learning.

Incorporating race data - Ultimately, incorporating race data from a site such as Athlinks, will help better validate race paces and help provide guidance on suggesting goal paces for races of other distances.



