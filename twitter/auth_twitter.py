import twitter


def authorize():
    CONSUMER_KEY = 'aCBjyXAOzjj1xQ1G6lIQhBocr'
    CONSUMER_SECRET = 'HnUJSv8Gfei9u1y3l7o7a8vnZZMkMci1UWX8z3ovzRuEGxpy0g'
    OAUTH_TOKEN = '21769507-oogia3xOf48sn96DqV5Mf4qb3a83cevz22242ABeT'
    OAUTH_TOKEN_SECRET = '9TghxlZgwOtP8fila8IPDhywedAAFAJnjjKqcfomnTSnh'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    print twitter_api
    return twitter_api


def getTrending(tapi, woeid):
    trends = tapi.trends.place(_id=woeid)
    print trends


def main():
    tapi = authorize()
    BLORE_WOEID = 23424848
    getTrending(tapi, BLORE_WOEID)
    WORLD_WOEID = 1
    getTrending(tapi, WORLD_WOEID)
    US_WOEID = 23424977
    getTrending(tapi, US_WOEID)

if __name__ == '__main__':
    main()
