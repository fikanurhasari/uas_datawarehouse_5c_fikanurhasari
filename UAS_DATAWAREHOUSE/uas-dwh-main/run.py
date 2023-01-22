from app import app
from flask import url_for
from app.Controllers import predikController

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
