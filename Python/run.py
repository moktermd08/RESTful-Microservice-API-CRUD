from flask import Flask
from app.routes import configure_routes  # Updated import statement

app = Flask(__name__)
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)