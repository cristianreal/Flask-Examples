import requests, urllib, json
from flask import Flask, render_template, request, Response, jsonify, make_response
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'softwareavanzado'

mysql = MySQL(app)

class MicroservicioArchivosTraducidos():
	def __init__(self, Nombre):
		self.Nombre = Nombre

@app.route('/')
def hello_world():
    titulo = "Software Avanzado"
    usuario = {'nombre': 'Christian'}
    return render_template('index.html', titulo=titulo, usuario=usuario)

@app.route('/po', methods=['GET', 'POST'])
def Creacion_Archivo_PO():
	if request.method == 'POST':
		cur = mysql.connection.cursor()
		cur.execute("SELECT original, traducida FROM contacts")
		data = cur.fetchall()
		cur.close()
		return render_template('Button.html', data=data)
	return render_template('Button.html')

@app.route('/prueba', methods=['GET', 'POST'])
def Prueba():
	if request.method == 'POST':
		data = usuario = [
			{'id': '12340', 'name': 'Alejandro', 'path': 'es_gt', 'languaje':'es', 'state':'completo',  'user': 'Happy1'},
			{'id': '12345', 'name': 'Miguel',    'path': 'en_eu', 'languaje':'en', 'state':'incompleto','user': 'Happy2'},
			{'id': '12346', 'name': 'Mario',     'path': 'en_uk', 'languaje':'uk', 'state':'completo',  'user': 'Happy3'},
			{'id': '12347', 'name': 'Osmary',    'path': 'es_ar', 'languaje':'ar', 'state':'incompleto','user': 'Happy4'},
			{'id': '12348', 'name': 'Dachi',     'path': 'es_es', 'languaje':'es', 'state':'completo',  'user': 'Happy5'},
			{'id': '12349', 'name': 'Luis',      'path': 'fr_fr', 'languaje':'fr', 'state':'incompleto','user': 'Happy6'},
			{'id': '12341', 'name': 'Aldo',      'path': 'es_it', 'languaje':'it', 'state':'completo',  'user': 'Happy7'}
		]
		#headers = {'Content-type': 'application/json'}
		return render_template('index.html', data=data)
	return render_template('Button.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')