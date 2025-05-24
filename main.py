from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/api/horaires', methods=['GET'])
def get_horaires():
    url = "https://academiefrontenac.fliipapp.com/horaire/1ff8a7b5dc7a7d1f0ed65aaa29c04b1e/DefaultRoom"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    classes = []

    for div in soup.select('.table-chk.eg-double-classbox'):
        course_id = div.get('data-id')
        date = div.get('data-date')
        
        class_name_tag = div.select_one('.class_name')
        class_time_tag = div.select_one('.class_time')
        
        name = class_name_tag.get_text(strip=True) if class_name_tag else ""
        time = class_time_tag.get_text(strip=True) if class_time_tag else ""
        
        coach = ""
        original_title = div.find('p').get('data-original-title')
        if original_title:
            soup_title = BeautifulSoup(original_title, 'html.parser')
            coach_tag = soup_title.find('span', string=lambda text: "Instructeur" in text if text else False)
            if coach_tag:
                coach = coach_tag.get_text(strip=True).replace("Instructeur :", "").strip()

        classes.append({
            "id": course_id,
            "date": date,
            "time": time,
            "name": name,
            "coach": coach
        })

    return jsonify(classes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
