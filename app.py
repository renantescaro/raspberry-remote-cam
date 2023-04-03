from flask import Flask
from main.controllers import blueprints_ctrl

app = Flask(
    __name__,
    template_folder='main/templates'
)

for bp in blueprints_ctrl:
    app.register_blueprint(bp)
