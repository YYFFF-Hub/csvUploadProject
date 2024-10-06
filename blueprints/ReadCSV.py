import os
import pandas as pd
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename
from extensions import db
from models import UserModel
from flask import Blueprint

# create an object for blueprints
csv_blueprint = Blueprint("ReadCSV", __name__, url_prefix = "/")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@csv_blueprint.route('/upload', methods=['POST'])
def upload():

    # get config
    UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER']

    # 检查上传文件夹是否存在，不存在则创建
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if 'file' not in request.files:
        return '没有文件'
    file = request.files['file']
    if file.filename == '':
        return '未选择文件'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # 读取 CSV 文件
        data = pd.read_csv(file_path)

        # 遍历 CSV 数据并插入到数据库中
        for index, row in data.iterrows():
            # 创建一个 UserModel 实例
            user = UserModel(name=row['name'], team=row['team'], mentor=row['mentor'])
            # 添加到数据库会话
            db.session.add(user)

        # 提交所有的更改
        db.session.commit()

        # 将上传的 CSV 数据返回给前端，作为 JSON
        return jsonify({
            'message': '文件上传成功，数据已保存到数据库！',
            'csv_data': data.to_dict(orient="records")  # 返回 CSV 数据作为 JSON
        })
    return jsonify({'error': '不允许的文件类型'})