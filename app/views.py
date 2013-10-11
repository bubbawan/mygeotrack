from flask import jsonify, request, redirect, render_template
from app import app

result = dict()
result['type'] = 'FeatureCollection'
collection = []
result['features'] = collection

@app.route('/')
def index():
    return render_template('index.html', message = 'WELCOME')

@app.route('/adddata', methods=['POST'])
def addData():
    pname = request.form['pname']
    clon =  request.form['clon']
    clat =  request.form['clat']
    collection.append(create_feature(pname, 'true', [clon, clat] ))
    return redirect('/dataform')

@app.route('/dataform')
def addDataForm():
    return render_template('dataform.html')

@app.route('/map')
def showMap():
    return render_template('map.html')
            
@app.route('/geodata')
def geoData():
    return jsonify(result)

def create_feature(pname, pshow, coordinates, gtype='Point'):
    feature = dict()
    feature['type'] = 'Feature'
    feature['properties'] = dict()
    feature['properties']['name'] = pname
    feature['properties']['popupContent'] = 'What`s up????'
    feature['geometry'] = dict()
    feature['geometry']['type'] = gtype
    feature['geometry']['coordinates'] = coordinates
    return feature