from flask import Flask
from index import views

app = Flask(__name__)

#linking to index.py
app.register_blueprint(views, url_prefix="/views")



if __name__ == '__main__':
    app.run(debug=True, port=1000)