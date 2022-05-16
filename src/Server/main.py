from flask import Flask, render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

counts =[]

class CurrentCount(Resource):
    print(counts)
    def get(self):
        return {'count': counts}
    def put(self):
        counts.append(request.form['data'])
        return {'count': counts}

api.add_resource(CurrentCount, '/count')

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)