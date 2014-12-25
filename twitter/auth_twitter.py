import twitter
import json


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
    return trends


def commonTrends(first, second):
    first_set = set([trend['name'] for trend in first[0]['trends']])
    second_set = set([trend['name'] for trend in second[0]['trends']])

    common = first_set.intersection(second_set)
    return common


def prettyOutput(trends):
    print json.dumps(trends, indent=1)


def main():
    tapi = authorize()
    IND_WOEID = 23424848
    US_WOEID = 23424977
    WORLD_WOEID = 1

    indTrend = getTrending(tapi, IND_WOEID)
    worldTrend = getTrending(tapi, WORLD_WOEID)
    usTrend = getTrending(tapi, US_WOEID)

    common_trend = commonTrends(indTrend, usTrend)
    print "Common Trending between India and US: "
    print common_trend

    print "Common Trends between US and World: "
    common_trend = commonTrends(worldTrend, usTrend)
    print common_trend

if __name__ == '__main__':
    main()
