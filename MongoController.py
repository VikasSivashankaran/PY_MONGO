from flask import Flask, request, jsonify

from StudentService import student_service
from Student import Student

app = Flask(__name__)

service = student_service()

@app.route('/mongo', methods = ['POST'])
def create_user():
    data = request.get_json()
    service.insert_mongo(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5002')