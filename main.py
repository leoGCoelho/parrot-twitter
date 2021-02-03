#export FLASK_APP=main.py   --- macos and linux
#set FLASK_APP=main.py   --- windows
#flask run

from flask import Flask, request, jsonify

app = Flask(__name__)


pedidos = []

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)

    '''contexts = data['queryResult']['outputContexts']
    for context in contexts:
        parametros = context['parameters']
        user = parametros['username']
        hash = parametros['hashtag']
        quantidade = parametros['number-integer']
        periodo = parametros['time-period']
        pedidos.append({ 'nome': nome, 'sabor': sabor })
    print(username)
    print(hashtag)
    print(number-integer)
    print(time-period)
    data['fulfillmentText'] = 'O tweet é: ...'
    '''

    print(data)

    return jsonify(data)

# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()