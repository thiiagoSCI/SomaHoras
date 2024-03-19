from flask import Flask, request, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

def soma_horas(*horas):
    total_segundos = 0

    for hora in horas:
        if len(hora) == 4:
            hora = hora[:2] + ':' + hora[2:] + ':00'
        
        h, m, s = map(int, hora.split(':'))
        total_segundos += h * 3600 + m * 60 + s

    horas_totais = total_segundos // 3600
    minutos_totais = (total_segundos % 3600) // 60
    segundos_totais = total_segundos % 60

    return '{:02d}:{:02d}:{:02d}'.format(horas_totais, minutos_totais, segundos_totais)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/somar_horas', methods=['POST'])
def somar_horas():
    horas = request.form.getlist('hora')
    resultado = soma_horas(*horas)
    return render_template_string(open('resultado.html').read(), resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
