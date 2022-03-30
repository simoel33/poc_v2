from static import swagger_ui_bluerint_perso
from werkzeug.utils import send_from_directory


@swagger_ui_bluerint_perso.route('/static/path:path')
def send_static(path):
    return send_from_directory('static', path)