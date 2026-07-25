from flask import Flask, jsonify

app = Flask(__name__)

courses = {
    1: {"id": 1, "name": "Python"},
    2: {"id": 2, "name": "Machine Learning"}
}

@app.route("/")
def home():
    return "Course Service Running"

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = courses.get(course_id)

    if course:
        return jsonify(course)

    return jsonify({"message": "Course not found"}), 404

if __name__ == "__main__":
    app.run(port=5001, debug=True)