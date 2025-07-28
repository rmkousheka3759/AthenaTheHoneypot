import requests
import time

def simulate_attack():
    url = 'http://127.0.0.1:5000/log_attack'
    data = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'ip_address': '192.168.1.1',
        'attack_type': 'SQL Injection'
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('Attack simulated successfully')
        else:
            print(f'Failed to simulate attack. Status Code: {response.status_code}')
    except Exception as e:
        print(f'Exception occurred: {str(e)}')

if __name__ == '__main__':
    while True:
        simulate_attack()
        time.sleep(5)
