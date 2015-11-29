import bcrypt
import os
from functools import wraps
from flask import Flask, flash, redirect, url_for,  render_template, request, session, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

valid_username = '40181252'
valid_pwhash = bcrypt.hashpw('pw', bcrypt.gensalt())

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.errorhandler(404)
def error404(error):
  start = '<img src="'
  url = url_for('static', filename='img/error.jpg')
  end = '" width="1300" height="550">'
  link = '<br /><a href="/" style="font-family: Arial;">This link will take you back to the home page.</a>'
  return start+url+end+link, 200

def check_auth(username, password):
  if (username == valid_username and valid_pwhash == bcrypt.hashpw(password.encode('utf-8'), valid_pwhash)):
    return True
  return False


def requires_login(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    status = session.get('logged_in', False)
    if not status:
      return redirect(url_for('.logindef'))
    return f(*args, **kwargs)
  return decorated

@app.route('/logout/')
def logout():
  session['logged_in'] = False
  flash('You were logged out successfully.')
  return redirect(url_for('.logindef'))

@app.route('/user/')
@requires_login
def secret():
  return render_template('loggedin.html')

@app.route('/login/', methods=['GET', 'POST'])
def logindef():
  if request.method == 'POST':
    user = request.form['username']
    pw = request.form['password']

    if check_auth(request.form['username'], request.form['password']):
      session['logged_in'] = True
      flash('You were logged in successfully.')
      return redirect(url_for('.secret'))
  return render_template('login.html')



@app.route('/')
def root():
  return render_template('pillar.html'), 200


@app.route('/user/motocross/')
@requires_login
def motocross():
  return render_template('motocross.html')

@app.route('/user/motocross/motoquote/')
@requires_login
def motoquote():
  return render_template('motoquote.html')

@app.route('/user/sportbike/')
@requires_login
def sportbike():
  return render_template('sportbike.html')

@app.route('/user/sportbike/sportquote/')
@requires_login
def sportquote():
  return render_template('sportquote.html')

@app.route('/user/cruiser/')
@requires_login
def cruiser():
  return render_template('cruiser.html')

@app.route('/user/cruiser/cruiserquote/')
@requires_login
def cruiserquote():
  return render_template('cruiserquote.html')


@app.route('/user/uploadfiles/')
@requires_login
def uploadfiles():
  return render_template('uploadfiles.html')

@app.route('/user/uploadfiles/upload', methods=['POST'])
@requires_login
def upload():
  file = request.files['file']

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    message = "<div class='container uploadcomplete'>File has been uploaded</div>"
    return render_template('uploadfiles.html') + message



if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

