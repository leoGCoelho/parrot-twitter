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
try:
    from flask import Flask, request, jsonify
except:
    os.system('pip3 install -r requirements')
    from flask import Flask, request, jsonify

app = Flask(__name__)


pedidos = []

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)

    contexts = data['queryResult']['outputContexts']
    for context in contexts:
        parametros = context['parameters']
        user = parametros['username']
        hashtag = parametros['hashtag']
        quantidade = parametros['number-integer']
        periodo = parametros['datetime_exp']
        dma = parametros['datetime_dma']
        hms = parametros['datetime-hms']
    print(user)
    print(hashtag)
    print(quantidade)
    print(periodo)
    print(dma)
    print(hms)
    data['fulfillmentText'] = 'O tweet é: ...'
    

    #print(data)

    return jsonify(data)

# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()