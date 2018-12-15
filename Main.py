import sys

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

from mongo import createMongo, mongoSaver
import datetime
import logging


def dateToString(date):
    return (str(date.year) + '-' + str(date.month) + '-' + str(date.day))


def main():
    logging.basicConfig(filename='out.log', format='%(asctime)s %(message)s')
    db = createMongo()

    dateSince = datetime.datetime(2016, 1, 1)
    endDate = datetime.datetime(2016, 1, 2)
    while dateSince.date() <= endDate.date():
        logging.warning('Get from : ' + str(dateSince))
        dateUntil = dateSince + datetime.timedelta(days=1)
        getTweet(dateSince, dateUntil, db)
        dateSince = dateSince + datetime.timedelta(days=1)


def getTweet(dateSince, dateUntil, db):
    try:
        # Example 1 - Get tweets by username
        res = mongoSaver(db)
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch('warszawa') \
            .setSince(dateToString(dateSince)) \
            .setUntil(dateToString(dateUntil))
        tweets = got.manager.TweetManager.getTweets(tweetCriteria, res)
        logging.warning('Got: ' + str(len(tweets)) + ' from ' + str(dateSince))
    except Exception as error:
        logging.warning('Error: ' + str(error))


if __name__ == '__main__':
    main()
