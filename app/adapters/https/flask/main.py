from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    dashboard_data = {"data": "dashboard"}
    return jsonify(dashboard_data)

@app.route('/rocket', methods=['GET'])
def get_rocket():
    rocket_result = {"data": "rocket launched"}
    return jsonify({'result': rocket_result})

@app.route('/satellite', methods=['GET'])
def get_satellite():
    satellite_result = {"data": "satellite launched"}
    return jsonify({'result': satellite_result})

