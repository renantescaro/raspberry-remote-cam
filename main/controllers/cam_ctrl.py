from flask import Blueprint
from main.services.cam import Camera

bp = Blueprint(
    'can',
    __name__,
    template_folder='templates'
)

class MainCtrl:
    @bp.route('/cam/up', methods=['GET'])
    def up_route():
        Camera().mover_vertical(10)
        return ''

    @bp.route('/cam/down', methods=['GET'])
    def down_route():
        Camera().mover_vertical(-10)
        return ''

    @bp.route('/cam/left', methods=['GET'])
    def left_route():
        Camera().mover_horizontal(10)
        return ''

    @bp.route('/cam/right', methods=['GET'])
    def right_route():
        Camera().mover_horizontal(-10)
        return ''
