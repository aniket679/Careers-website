from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'Pune, India',
    'salary': 'Rs. 3,00,000'
}, {
    'id': 2,
    'title': 'Java Developer',
    'location': 'Delhi, India',
    'salary': 'Rs. 4,00,000'
}, {
    'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Remote',
}, {
    'id': 4,
    'title': 'BackEnd Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]


@app.route("/")
def index():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if (__name__) == "__main__":
  app.run(debug=True)
