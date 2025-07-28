from flask import render_template, redirect, url_for, jsonify, request
from datetime import datetime
from app import app, db
from models.attack_log import AttackLog

def calculate_analytics():
    analytics_data = {
        'Total Attacks': AttackLog.query.count(),
        'Successful Logins': 500,
        'Failed Logins': 50,
    }
    return analytics_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    logs = AttackLog.query.all()
    return render_template('logs.html', logs=logs)

@app.route('/analytics')
def analytics():
    analytics_data = calculate_analytics()
    return render_template('analytics.html', analytics_data=analytics_data)

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/simulate_log', methods=['POST'])
def simulate_log():
    data = request.get_json()
    timestamp = data.get('timestamp')
    ip_address = data.get('ip_address')
    attack_type = data.get('attack_type')
    details = data.get('details')

    new_log = AttackLog(timestamp=timestamp, ip_address=ip_address, attack_type=attack_type, details=details)
    db.session.add(new_log)
    db.session.commit()

    emit_log_to_clients(new_log)

    return jsonify({'message': 'Log simulated successfully'})

def emit_log_to_clients(log):
    """
    socketio.emit('log_update', {
        'timestamp': log.timestamp,
        'ip_address': log.ip_address,
        'attack_type': log.attack_type,
        'details': log.details
    })
    """
@app.route('/geolocate_ip', methods=['POST'])
def geolocate_ip():
    ip_address = request.form.get('ip_address')

    geolocation_data = {
        'country': 'United States',
        'region': 'California',
        'city': 'San Francisco',
        'zip': '94105',
        'lat': '37.7749',
        'lon': '-122.4194',
        'timezone': 'America/Los_Angeles',
        'isp': 'Sample ISP',
        'org': 'Sample Organization',
        'as': 'AS12345 Sample AS'
    }
    return jsonify(geolocation_data)

if __name__ == '__main__':
    app.run(debug=True)
