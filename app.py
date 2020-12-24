import sys
import binascii
import tweepy


# APIキー等
api_key=""
api_key_secret=""
access_token=""
access_token_secret=""

# 認証関係
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート用関数
def tweet(tweet_text):
    api.update_status(str(tweet_text))

# ツイートs
text = input("ツイート内容を入力して下さい: ")
text = binascii.hexlify(text.encode('utf-8'))
tweet(str(text).replace('b\'', '').replace('\'', ''))
print(str(text).replace('b\'', '').replace('\'', ''))