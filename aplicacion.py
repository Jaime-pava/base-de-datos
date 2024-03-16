from flask import Flask, jsonify
from database.personas import personas

app = Flask(_name_)


@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({"personas":personas})

if _name_ == "main":
    app.run(debug=True,port=5000)
