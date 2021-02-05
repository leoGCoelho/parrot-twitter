import time
import datetime
import re
try:
    import snscrape.modules.twitter as sntwitter
except:
    os.system('pip3 install -r requirements')
    import snscrape.modules.twitter as sntwitter


def ExtractData(lim, date, usern, hashtag):
    tweetlist = []

    since = date[0]
    if(len(date) == 1):
        now = datetime.datetime.now()
        until = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    else:
        until = date[1]

    if not (usern == ""):
        usern += " "
    if not (hashtag == ""):
        hashtag += " "


    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(usern + hashtag + 'since:' + since + 'until:' + until).get_items()):
        if (i>lim-1) and (lim != -1):
            break

        print(i, ": ", tweet.content)
        tweetlist.append([tweet.date, tweet.content])

    return tweetlist


def GetCurrDate():
    now = datetime.datetime.now()
    return (str(now.year) + "-" + str(now.month) + "-" + str(now.day))


def GetNPassDate(days):
    passday = datetime.datetime.now() - datetime.timedelta(days)
    return (str(passday.year) + "-" + str(passday.month) + "-" + str(passday.day))


def GetDatetime(date):
    if (date == 'Agora') or (date == 'agora') or (date == 'AGORA'):
        return GetCurrDate()
    elif (date == 'Hoje') or (date == 'hoje') or (date == 'HOJE') or (date == 'hj') or (date == 'HJ'):
        return GetCurrDate()
    elif (date == 'nesse momento') or (date == 'Nesse momento') or (date == 'NESSE momento') or (date == 'nesse Momento') or (date == 'nesse MOMENTO') or (date == 'NESSE momento') or (date == 'Nesse Momento') or (date == 'NESSE MOMENTO'):
        return GetCurrDate()
    elif (date == 'neste momento') or (date == 'Neste momento') or (date == 'NESTE momento') or (date == 'neste Momento') or (date == 'neste MOMENTO') or (date == 'NESTE momento') or (date == 'Neste Momento') or (date == 'NESTE MOMENTO'):
        return GetCurrDate()

    elif (date == 'Ontem') or (date == 'ontem') or (date == 'ONTEM'):
        return GetNPassDate(1)
    elif (date == '1 dia') or (date == 'um dia') or (date == '1 Dia') or (date == 'Um Dia') or  (date == '1 DIA') or (date == 'UM DIA'):
        return GetNPassDate(1) 


    elif (date == 'Anteontem') or (date == 'anteontem') or (date == 'ANTEONTEM'):
        return GetNPassDate(2)
    elif (date == '2 dias') or (date == 'dois dias') or (date == '2 Dias') or (date == 'Dois Dias') or  (date == '2 DIAS') or (date == 'DOIS DIAS'):
        return GetNPassDate(2)

    else:
        return FormatTime(date)

    return ""


#def FormatTime(dma, hms):
def FormatTime(dma):
    now = datetime.datetime.now()
    formated = ""

    if dma == "":
        formated.append( GetCurrDate() )
    else:
        dmaV = str(dma).split("/")
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


def SetDatetime(dma):
    data = []
    #print(dma)

    if dma == []:
        data = [GetCurrDate(), GetCurrDate()]
    else:
        for date in dma:
            data.append( GetDatetime(date) )

        if len(dma) == 1:
            data.append( GetCurrDate() )

    return data

            
