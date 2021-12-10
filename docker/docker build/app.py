import os
from flask import Flask
from api import fl_app

if __name__ == "__main__":
    flask_app = Flask(__name__)
    flask_app.register_blueprint(fl_app)
    flask_app.run(debug=True,host=os.environ.get('FLASK_HOST'),port=os.environ.get('FLASK_PORT'))
