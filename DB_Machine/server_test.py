from flask import Blueprint, request
from werkzeug.utils import secure_filename

bp = Blueprint('image', __name__, url_prefix = '/image')

@bp.route('/', methods = ['POST'])
def savec_image():
  f = request.files['file']
  f.save('./savce_image/' + secure_filename(f.filename))
  return 'done!'
