import bcrypt
from functools import wraps
from flask import Flask, g, redirect, url_for, json, render_template, request, session, url_for

import sqlite3

from contextlib import closing
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

valid_email = 'person@napier.ac.uk'
valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())
db_location = 'var/sqlite3.db'

def check_auth(email, password):
  if (email == valid_email and valid_pwhash == bcrypt.hashpw(password.encode('utf-8'), valid_pwhash)):
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
  return redirect(url_for('.logindef'))

@app.route('/user/')
@requires_login
def secret():
  return render_template('loggedin.html')

@app.route('/login/', methods=['GET', 'POST'])
def logindef():
  if request.method == 'POST':
    user = request.form['email']
    pw = request.form['password']

    if check_auth(request.form['email'], request.form['password']):
      session['logged_in'] = True
      return redirect(url_for('.secret'))
  return render_template('login2.html')



def get_db():
  db = getattr(g, 'db', None)
  if db is None:
    db = sqlite3.connect(db_location)
    g.db = db
  return db

@app.teardown_appcontext
def close_db_connection(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()


@app.route('/')
def main():
  return render_template('pillar.html')


@app.route('/registration/')
def registration():
  return render_template('registration.html')


@app.route('/signUp/', methods=['POST'])
def signUp():

  username = request.form['inputUsername']
  password = request.form['inputPassword']

  #if _username and _password:
    #return json.dumps({'html':'<span>All fields good !!</span'})
 # else:
   # return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/something/')
def something():
  db = get_db()
  db.cursor().execute('INSERT INTO members values("Helen", "Sharp")')
  db.commit()

  page = []
  page.append('<html><ul>')
  sql = "SELECT rowid, * FROM members"
  for row in db.cursor().execute(sql):
    page.append('<li>')
    page.append(str(row))
    page.append('</li>')

  page.append('</ul><html>')
  return ''.join(page)




if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

