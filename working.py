from stravalib.client import Client
import requests

# Authentication Steps:
client = Client()
authorize_url = client.authorization_url(client_id=1234, redirect_uri='http://localhost:8282/authorized')
# Have the user click the authorization URL, a 'code' param will be added to the redirect_uri
# .....

## My clientid = 12454
# Extract the code from your webapp response
code = requests.get('code') # or whatever your framework does
access_token = client.exchange_code_for_token(client_id=12454, client_secret=STRAVA_KEY, code=code)

# Now store that access token somewhere (a database?)
client.access_token = access_token
athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))

# Athletes and Activities
# Currently-authenticated (based on provided token) athlete
# Will have maximum detail exposed (resource_state=3)
#curr_athlete = client.get_athlete()

# Fetch another athlete
#other_athlete = client.get_athlete(123)
# Will only have summary-level attributes exposed (resource_state=2)

# Get an activity
activity = client.get_activity(athlete)
# If activity is owned by current user, will have full detail (resource_state=3)
# otherwise summary-level detail.

# Streams
# Activities can have many streams, you can request n desired stream types
types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]

streams = client.get_activity_streams(123, types=types, resolution='medium')

#  Result is a dictionary object.  The dict's key are the stream type.
if 'altitude' in streams.keys():
    print(streams['altitude'].data)

# Working with units:

activity = client.get_activity(96089609)
assert isinstance(activity.distance, units.quantity.Quantity)
print(activity.distance)
# 22530.80 m

# Meters!?

from stravalib import unithelper

print(unithelper.miles(activity.distance))
# 14.00 mi

# And to get the number:
num_value = float(unithelper.miles(activity.distance))
# Or:
num_value = unithelper.miles(activity.distance).num
