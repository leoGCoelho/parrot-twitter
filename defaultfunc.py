import time
import datetime
import re
try:
    import snscrape.modules.twitter as sntwitter
except:
    os.system('pip3 install -r requirements')
    import snscrape.modules.twitter as sntwitter


#def FormatTime(dma, hms):
def FormatTime(dma):
    now = datetime.datetime.now()
    formated = ""

    if dma == "":
        formated.append(str(now.year) + "-" + str(now.month) + "-" + str(now.day))
    else:
        dmaV = dma.split("/")
        if len(dmaV) == 0:
            dmaV = []
            dmaV.append(str(now.day))
        if len(dmaV) == 1:
            dmaV.append(str(now.month))
        if len(dmaV) == 2:
            dmaV.append(str(now.year))

        '''hmsV = hms.split(":")
        if len(hmsV) == 2:
            hmsV.append("00")'''

        formated = dmaV[2] + "-" + dmaV[1] + "-" + dmaV[0]
        
    #print(formated)
    return formated

def ExtractData(lim, date, user, hashtag):
    tweetlist = []

    since = date[0]
    if(len(date) == 1):
        now = datetime.datetime.now()
        until = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    else:
        until = date[1]

    if not (user == ""):
        user += " "
    if not (hashtag == ""):
        hashtag += " "


    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(user + hashtag + 'since:' + since + 'until:' + until).get_items()):
        if (i>lim) and (lim != -1):
            break
        tweetlist.append([tweet.date, tweet.content, tweet.user.username])

    return tweetlist
