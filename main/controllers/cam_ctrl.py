from flask import Blueprint
from main.services.cam import Camera

bp = Blueprint(
    'can',
    __name__,
    template_folder='templates'
)

class MainCtrl:
    @staticmethod
    @bp.route('/cam/vertical/<angle>', methods=['GET'])
    def up_route(angle):
        Camera().mover_vertical(float(angle))
        return ''

    @staticmethod
    @bp.route('/cam/horizontal/<angle>', methods=['GET'])
    def left_route(angle):
        Camera().mover_horizontal(float(angle))
        return ''
