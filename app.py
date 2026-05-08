from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Alice', 'grade': 'A'},
    {'id': 2, 'name': 'Bob', 'grade': 'B'},
    {'id': 3, 'name': 'Charlie', 'grade': 'C'}
]

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student)

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name field'}), 400
    
    new_id = len(students) + 1
    new_student = {
        'id': new_id, 
        'name': data['name'], 
        'grade': data.get('grade', 'N/A')
    }
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
