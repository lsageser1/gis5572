import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route('/polygon')
def polygon():
    connection = psycopg2.connect(
        host="",
        database="",
        user="",
        password=''
    )

    cursor = connection.cursor()
    query = "SELECT JSON_BUILD_OBJECT('type', 'FeatureCollection', 'features', JSON_AGG(ST_AsGeoJSON(polygon.*)::json)) FROM polygon;"

    cursor.execute(query)
    data = cursor.fetchone()[0]

    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
