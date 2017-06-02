import tweepy
# Consumer keys and access tokens, used for OAuth
consumer_key = 'TOcZZ5zcyrseS7fgzxTu7dnLO'
consumer_secret = 'axJ2nYv57CEUZvg3IFz469ECVY3Lmrm9oo7fGKCBmZOlCoW63i'
access_token = '594857569-n3pqqqHMDYWrNXW3SKFSH4wtSeU0TFrq0WsbpT6E'
access_token_secret = 'Bjhw0TZdAuzcX03hupZeNBsigvGzI5o2q3pLb8DnSCMwM'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
    def on_error(self, status_code):
		if status_code == 420:
            	#returning False in on_data disconnects the stream
			print "Rate limit hit threshold"
			return False
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myStream.filter(track=['bitcoin'])

#user = api.me()
 
#print('Name: ' + user.name)
#print('Location: ' + user.location)
#print('Friends: ' + str(user.friends_count)) 
