from website import app  # Import Flask app
from website.route import *  # Import routes van route.py

if __name__ == '__main__':
    app.run(debug=True)
