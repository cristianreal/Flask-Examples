import requests, urllib, json
from flask import Flask, render_template, request, Response, jsonify, make_response
app = Flask(__name__)

class MicroservicioArchivosTraducidos():
	def __init__(self, Nombre):
		self.Nombre = Nombre

@app.route('/')
def hello_world():
    titulo = "Sistemas Operativos"
    usuario = {'nombre': 'Christian'}
    return render_template('index.html', titulo=titulo, usuario=usuario)


@app.route('/prueba', methods=['GET', 'POST'])
def Prueba():
	if request.method == 'POST':
		url = "https://opensource.adobe.com/Spry/data/json/donuts.js"
		json_url = urlopen(url)
		data = json.loads(json_url.read())
		print(data)
		#headers = {'Content-type': 'application/json'}
		return "Hola hermoso"
	return render_template('Button.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')