import twitter

mytwitteraccount = twitter.Api(consumer_key="hhMMCNyExowTD1aIuthDAQ", 
								consumer_secret="8Wrjm9QGsgl7yeu1WzeE5MvDwTuHPsBgKSHjok9oM", 
								access_token_key="1278575833-6po7q7qgb1qM6QJpM2ptTVhDBfwkUCqqSFJvOgR", 
								access_token_secret="mA6Nzv6Jeun6SmbfY31QkP9e9AyYDdCuCn4Gd8rFBU")

# friends = mytwitteraccount.GetFriends()
# print [u.name for u in friends]

status = mytwitteraccount.PostUpdates('My first API call using Python')