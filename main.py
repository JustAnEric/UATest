import sqlite3, random
from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = str(random.randint(14, 49755))

# blueprints
from blueprints.delete import bp as delb
from blueprints.read import bp as readb
from blueprints.write import bp as writeb
from blueprints.create import bp as createb
from blueprints.root import bp as root

app.register_blueprint(delb)
app.register_blueprint(readb)
app.register_blueprint(writeb)
app.register_blueprint(createb)
app.register_blueprint(root)

# run
app.run(
    host="0.0.0.0",
    port=9090
)