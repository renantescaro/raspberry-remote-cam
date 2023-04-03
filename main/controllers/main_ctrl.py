from flask import render_template, Blueprint

bp = Blueprint(
    'main',
    __name__,
    template_folder='templates'
)

class MainCtrl:
    @bp.route('/', methods=['GET'])
    def main_route():
        return render_template(
            template_name_or_list='cam.html',
            title='Controle da camera'
        )
