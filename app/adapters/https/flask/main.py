from app.adapters.repositories.elasticsearch.satellite_repository import SatelliteStore
from app.adapters.repositories.elasticsearch.telemetry_repository import TelemetryStore
from flask import Flask, jsonify
from app.usescase.dashboard import Dashboard
app = Flask(__name__)


usecase = Dashboard(
    satellite_store=SatelliteStore("http://elasticsearch", "9200"),
    telemetry_store=TelemetryStore("http://elasticsearch", "9200")
)

@app.errorhandler(Exception)
def handle_all_errors(error):
    status_code = getattr(error, 'code', 500)
    print(error)
    error_str, description = str(error).split(': ', 1)
    return jsonify({
        "error": error_str,
        "description": description,
        "status": status_code
    }), status_code

@app.route('/dashboard')
def dashboard():
    dashboard_data = usecase.get_dashboard() 
    return jsonify(dashboard_data)

@app.route('/rocket', methods=['GET'])
def get_rocket():
    rocket_result = {"data": "rocket launched"}
    return jsonify({'result': rocket_result})

@app.route('/satellite', methods=['GET'])
def get_satellite():
    satellite_result = {"data": "satellite launched"}
    return jsonify({'result': satellite_result})

