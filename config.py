# set the database
HOSTNAME = '192.168.0.54'      # 数据库地址
PORT = 3306
USERNAME = 'root'  # 数据库用户名
PASSWORD = 'root'  # 数据库密码
DATABASE = 'team_management'   # 数据库名称
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# set the folder for upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}