from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Données simulées (à remplacer par un import depuis une base ou un autre script)
horaires = [
    {"coach": "03-Nicolas Roy", "date": "2025-05-21", "name": "N1 - Introduction boxe", "time": "06:00 - 07:00"},
    {"coach": "Estefanio Abreu", "date": "2025-05-21", "name": "N2 - Régulier boxe", "time": "07:00 - 08:00"},
    {"coach": "David Azor", "date": "2025-05-24", "name": "N1 - Introduction boxe", "time": "10:30 - 11:30"},
    {"coach": "Ralia Guassemi", "date": "2025-05-25", "name": "N3 - Intermédiaire boxe", "time": "11:30 - 13:00"}
]

@app.route('/horaires', methods=['GET'])
def get_horaires():
    return jsonify(horaires)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

