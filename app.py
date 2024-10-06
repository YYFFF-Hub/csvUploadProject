from flask import Flask, render_template
from flask_cors import CORS
from blueprints.ReadCSV import csv_blueprint
import config
from extensions import db

# 初始化Flask应用
app = Flask(__name__)
CORS(app)

# register blueprints
app.register_blueprint(csv_blueprint)

# bind config
app.config.from_object(config)

# 初始化数据库
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def upload_file():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)