from flask import Flask, render_template
import datetime


app = Flask(__name__)

empresa = "Mexican Lapse"
contador_visitas = 0

@app.route('/')
def index():
    global contador_visitas
    fecha_hora_actual = datetime.datetime.now()
    contador_visitas += 1
    return render_template('index.html', empresa=empresa,
                           fecha_hora_actual=fecha_hora_actual,
                           contador_visitas=contador_visitas)

if __name__ == '__main__':
    app.run(debug=True)