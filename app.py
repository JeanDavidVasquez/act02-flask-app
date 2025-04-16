from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt
    response = requests.get(url)
    contenido = response.text.strip().splitlines()

    encabezados = contenido[0].split("|")
    filas = []
    for linea in contenido[1:]:
        columnas = linea.split("|")
        if columnas[0][0] in ['3', '4', '5', '7']:
            filas.append(columnas)

    tabla_html = "<table border='1'>"
    tabla_html += "<tr>" + "".join(f"<th>{col}</th>" for col in encabezados) + "</tr>"
    for fila in filas:
        tabla_html += "<tr>" + "".join(f"<td>{col}</td>" for col in fila) + "</tr>"
    tabla_html += "</table>"

    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    return f'¡Hola, Loja!<br><b>{fecha_formateada}</b><br><br>{tabla_html}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)