from flask import Flask
from config import config

app = Flask(__name__,template_folder='templates')
app.config.from_object(config)

import routes
if __name__ == "__main__": 
    app.run(debug=True) 
