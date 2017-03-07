import twitter
import pickle
from pathlib import Path

consumer_key = 'B8wAGC920QYKPl7ivFSLu1bDj'
consumer_secret = 'RPiyW9BpVRldlvXnQuRy2jVosKJxpnbHecYGtL5u5Sx3tllAEB'
access_token = '838329122-pQUHuiSRqQ9MnXer7clyzVgQPSIIKUo56jLbzBmn'
access_token_secret = 'CMWwMm3n62lhx51MIor3SKhd5yLQ0IAfO2IgxOyeq9lAD'


def get_trump_tweets():
    '''Gets Trump tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('trumptwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('trumptwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@realDonaldTrump', 'trumptwitters.pickle',
                        '796315640307060738')


def get_clinton_tweets():
    '''Gets Clinton tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('clintontwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('clintontwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@HillaryClinton', 'clintontwitters.pickle',
                        '796390484084215808')


def get_malley_tweets():
    '''Gets Martin O'Malley tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('malleytwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('malleytwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@MartinOMalley', 'malleytwitters.pickle',
                        '796261181006761984')


def get_bernie_tweets():
    '''Gets Bernie Sanders' tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('bernietwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('bernietwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@SenSanders', 'bernietwitters.pickle',
                        '796785451713593344')


def get_cruz_tweets():
    '''Gets Ted Cruz's tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('cruztwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('cruztwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@tedcruz', 'cruztwitters.pickle',
                        '796263241890439169')


def get_kasich_tweets():
    '''Gets John Kasich's tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('kasichtwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('kasichtwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@JohnKasich', 'kasichtwitters.pickle',
                        '796033355036983301')


def retrieve_tweets(name, filename, idnum):
    '''Retrieves tweets from the given screen name that were published
    before the given id from the twitter API and stores them in the
    given file'''

    api = twitter.Api(consumer_key, consumer_secret,
                      access_token,
                      access_token_secret)

    tweets = api.GetUserTimeline(screen_name=name, count=199, max_id=idnum)
    for status in tweets:
        # Print the ID and the date published for each Tweet
        print(status.id)
        print(status.created_at)
    tweets = [s.text for s in tweets]
    # Save data to a file
    f = open(filename, 'wb')
    pickle.dump(tweets, f)
    f.close()


get_trump_tweets()
get_clinton_tweets()
get_cruz_tweets()
get_bernie_tweets()
get_malley_tweets()
get_kasich_tweets()
