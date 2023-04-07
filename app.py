from flask import Flask
from flask_cors import CORS
from main.controllers import blueprints_ctrl
from main.services.setting import Setting

app = Flask(
    __name__,
    template_folder='main/templates'
)
CORS(
    app,
    resources={
        r'/cam/*': {'origins': Setting.get('EXTERNAL_IP')}
    }
)

for bp in blueprints_ctrl:
    app.register_blueprint(bp)
