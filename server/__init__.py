from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from server.db_tools import build_db_connection_uri_string

import os

app = Flask(__name__, static_folder="../static/build/static", template_folder="../static/build")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    build_db_connection_uri_string(use_env_vars=True,
                                   use_defaults=True)

print('URI: ' + (app.config['SQLALCHEMY_DATABASE_URI'] or 'NONE'))
print('EV OPTS: ' + (os.environ.get('SWE_IDB_PGDB_OPTS') or 'NONE'))
print('EV ADDR: ' + (os.environ.get('SWE_IDB_PGDB_ADDR') or 'NONE'))
print('EV PW: ' + (os.environ.get('SWE_IDB_PGDB_PW') or 'NONE'))

db = SQLAlchemy(app)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()