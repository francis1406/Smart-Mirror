from datetime import datetime
import Classes.sensor
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
    resposta = requests.get(url)

    while True:
        hora = datetime.fromisoformat(resposta.json()["datetime"]).strftime("%H:%M:%S")
        data = datetime.fromisoformat(resposta.json()["datetime"]).strftime("%d/%m/%Y")
        return render_template('index.html', hora=hora, data=data)

    return render_template('index.html', hora=hora, data=data, my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run()
