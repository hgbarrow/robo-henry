# -*- coding: utf-8 -*-

import tweepy, time, sys
import newsgrab, wallpapergrab
from twitter_auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# enter information from dev.twitter

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit_notify=False)
roboUser = api.me()
mainAccount = api.get_user(screen_name = 'TechieDudeBro')

def tweetFromFile(filename, delay):
	#Tweet a file line by line with 'delay' seconds between tweets
	file = open(filename, 'r')
	f = file.readlines()
	file.close()
	
	for line in f:
		print 'Tweeting: ' + line
		api.update_status(status=line)
		time.sleep(delay)
		
def printUserTweets(id):
	timeline = api.user_timeline(id = id)
	for tweet in timeline:
		print tweet.text.encode("ascii", errors="ignore")
		print 'ID = ' + str(tweet.id)
	return timeline


def retweetFavoriteLatest(id):
	statuses = api.user_timeline(id = id, count=1)
	tweet = statuses[0]
	if not tweet.retweeted:
		print 'Retweeting and favoriting: ' + tweet.text.encode("ascii", errors="ignore")
		api.create_favorite(tweet.id)
		tweet = api.retweet(tweet.id)
	else:
		print 'I have already retweeted that'
	return tweet
	
def tweetWallpaper(title, filename):
	tweetText = unicode('#PicOfTheDay ') + title
	print unicode('Tweeting: ') + title
	status = api.update_with_media(filename, status = tweetText)
	
	try:
		api.update_profile_banner(filename)
	except TweepError as e:
		print e
	
def tweetLink(title, link):
	tweet = ' '.join([title, link])
	print 'tweeting: ' + tweet
	api.update_status(status = tweet)

def searchTwitter(query):
	max_tweets = 10
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
	return searched_tweets
	
# Tweet Wallpaper
#(title, filename) =  wallpapergrab.grabRandom()
# tweetWallpaper(title, filename)

#tweetWallpaper('wallpaper.jpg', 'Rockefeller View')
#tweet EE times	
#[EETitle, EELink] = newsgrab.getEETimes()
#tweetLink(EETitle, EELink)
