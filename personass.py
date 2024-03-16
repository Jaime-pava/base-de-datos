from flask import Flask,request,jsonify

app = Flask(_name_)

@app.route('/personas', methods=['GET'])
def get_personas():
    
    lista_personas = [
        {'nombre': 'Claudia'},
        {'nombre': 'Carlos'},
        {'nombre': 'Stiven'},
        {'nombre': 'Tatiana'},
        {'nombre': 'Darcy'},
    ]
 
    return jsonify(lista_personas)

if _name_ == '_main_':
    app.run(debug=True)
