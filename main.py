## in tab 1
#export FLASK_APP=main.py   --- macos and linux
#set FLASK_APP=main.py   --- windows
#flask run

## in tab 2
# ./ ngrok http PORT_VALUE
#copy the https url

## in dialogflow dashboard > fulfilment
#enable webhook
#paste the https url and save

import os
import re
import defaultfunc as func
try:
    from flask import Flask, request, jsonify
    import snscrape.modules.twitter as sntwitter
except:
    os.system('pip3 install -r requirements')
    from flask import Flask, request, jsonify
    import snscrape.modules.twitter as sntwitter




app = Flask(__name__)
pedidos = []

@app.route('/', methods=['POST'])
def main():
    lim = ""
    date = []
    data = request.get_json(silent=True)

    contexts = data['queryResult']['outputContexts']
    for context in contexts:
        parametros = context['parameters']
        users = parametros['username']
        hashtags = parametros['hashtag']
        quantidade = parametros['number-integer']
        periodo = parametros['datetime_exp']
        dma = parametros['datetime_dma']
        hms = parametros['datetime-hms']

    #users[0] = re.sub(r'@', r'', users[0])
    print(users)
    print(hashtags)
    print(quantidade)
    print(periodo)
    print(dma)
    print(hms)

    if len(quantidade) == 0:
        lim = 1
    for quant in quantidade:
        lim = int(quant)

    print(lim)

    for dmaV in dma:
        date.append(func.FormatTime(dmaV))
    if len(dmaV) == 0:
        date = [func.FormatTime("03/02/2021"), func.FormatTime("03/02/2021")]
    elif len(dmaV) == 1:
        date.append(func.FormatTime("03/02/2021"))
    txt = ""

    '''if len(hashtags) == 0:
        if len(users) == 0:
            extrated = func.ExtractData(lim, date, "", "")
            txt += "O tweet de" + extrated[2] + ' é:\n\n' + extracted[1] + '\n\nPosted in ' + extracted[0] + "\n\n"
        else:
            for user in users:
                extrated = func.ExtractData(lim, date, user, "")
                    txt += "O tweet de" + extrated[2] + ' é:\n\n' + extracted[1] + '\n\nPosted in ' + extracted[0] + "\n\n"
    else:
        for hashtag in hashtags:
            if len(users) == 0:
                extrated = func.ExtractData(lim, date, "", hashtag)
                txt += "O tweet de" + extrated[2] + ' é:\n\n' + extracted[1] + '\n\nPosted in ' + extracted[0] + "\n\n"
            else:
                for user in users:
                    extrated = func.ExtractData(lim, date, user, hashtags)
                    txt += "O tweet de" + extrated[2] + ' é:\n\n' + extracted[1] + '\n\nPosted in ' + extracted[0] + "\n\n"'''

    extracted = func.ExtractData(lim, date, "", hashtags[0])
    
    for extr in extracted:
        txt += "O tweet de" + ' é:\n\n' + str(extr[1]) + '\n\nPostado em ' + str(extr[0]) + "\n\n"
        #txt = str(extrated)

    data['fulfillmentText'] = txt

    #print(data)

    return jsonify(data)

# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()