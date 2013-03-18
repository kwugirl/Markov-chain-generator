from twitter import * # why did it have to be this format and not just "import twitter"?
import os

#twitter authentication
MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("KwuDee Markov", "hhMMCNyExowTD1aIuthDAQ", 
                "8Wrjm9QGsgl7yeu1WzeE5MvDwTuHPsBgKSHjok9oM",
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)


t = Twitter(
    auth=OAuth(oauth_token, oauth_secret,
                "hhMMCNyExowTD1aIuthDAQ", 
                "8Wrjm9QGsgl7yeu1WzeE5MvDwTuHPsBgKSHjok9oM")
    )

# Get a particular friend's timeline
t.statuses.friends_timeline(id="kwugirl")