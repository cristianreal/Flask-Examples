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
		data = {
		"items":{
			"item":[
				{
				"id": "0001",
				"type": "donut",
				"name": "Cake",
				"ppu": 0.55,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
						]
						},
					"topping":[
						{ "id": "5001", "type": "None" },
						{ "id": "5002", "type": "Glazed" },
						{ "id": "5005", "type": "Sugar" },
						{ "id": "5007", "type": "Powdered Sugar" },
						{ "id": "5006", "type": "Chocolate with Sprinkles" },
						{ "id": "5003", "type": "Chocolate" },
						{ "id": "5004", "type": "Maple" }
						]
				},
				{
				"id": "0002",
				"type": "donut",
				"name": "Raised",
				"ppu": 0.55,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" }
						]
						},
					"topping":[
						{ "id": "5001", "type": "None" },
						{ "id": "5002", "type": "Glazed" },
						{ "id": "5005", "type": "Sugar" },
						{ "id": "5003", "type": "Chocolate" },
						{ "id": "5004", "type": "Maple" }
						]
				},
				{
				"id": "0003",
				"type": "donut",
				"name": "Old Fashioned",
				"ppu": 0.55,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
						]
						},
					"topping":[
						{ "id": "5001", "type": "None" },
						{ "id": "5002", "type": "Glazed" },
						{ "id": "5003", "type": "Chocolate" },
						{ "id": "5004", "type": "Maple" }
						]
				},
				{
				"id": "0004",
				"type": "bar",
				"name": "Bar",
				"ppu": 0.75,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" },
						]
						},
					"topping":[
						{ "id": "5003", "type": "Chocolate" },
						{ "id": "5004", "type": "Maple" }
						],
					"fillings":{
						"filling":[
							{ "id": "7001", "name": "None", "addcost": 0 },
							{ "id": "7002", "name": "Custard", "addcost": 0.25 },
							{ "id": "7003", "name": "Whipped Cream", "addcost": 0.25 }
							]
							}
				},
				{
				"id": "0005",
				"type": "twist",
				"name": "Twist",
				"ppu": 0.65,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" },
						]
						},
					"topping":[
						{ "id": "5002", "type": "Glazed" },
						{ "id": "5005", "type": "Sugar" },
						]
				},
				{
				"id": "0006",
				"type": "filled",
				"name": "Filled",
				"ppu": 0.75,
				"batters":{
					"batter":[
						{ "id": "1001", "type": "Regular" },
						]
						},
					"topping":[
						{ "id": "5002", "type": "Glazed" },
						{ "id": "5007", "type": "Powdered Sugar" },
						{ "id": "5003", "type": "Chocolate" },
						{ "id": "5004", "type": "Maple" }
						],
					"fillings":{
						"filling":[
							{ "id": "7002", "name": "Custard", "addcost": 0 },
							{ "id": "7003", "name": "Whipped Cream", "addcost": 0 },
							{ "id": "7004", "name": "Strawberry Jelly", "addcost": 0 },
							{ "id": "7005", "name": "Rasberry Jelly", "addcost": 0 }
							]
							}
					}
					]
					}
					}
		print(data)
		#headers = {'Content-type': 'application/json'}
		return "Hola hermoso"
	return render_template('Button.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')