from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
### Importing libraries to run different functions of the app. ###

@app.route('/privatearea/')
def privatearea():
  return redirect(url_for('sorry'))
### Automatically redirects to /sorry/ route. ###

@app.route('/sorry/')
def sorry():
  return "<h3 style='color: #545b5d; font-family: Arial'>I'm sorry. Access denied.</h3>"
### Deadend. CSS applied. - CSS applied ###

@app.errorhandler(404)
def page_not_found(error):
  return "<h3 style='color: #545b5d; font-family: Arial'>Jesus Christ, you gave me a number 404 heart attack</h3>", 404
### Giving a bad URL results error 404. (It hurts the app.) - CSS applied ###

@app.route('/')
def treespecies():
  return render_template('pillar.html')
### Front page. ###

@app.route('/alders/')
def firsttype():
  names = ['Alder']
  return render_template('firsttype.html', names=names)
### Directs to /alders/ route, shows dictionary of types, ###
### and displays its html page. ###

@app.route('/alders/alder/')
def firsttypea():
  return render_template('alder.html')
### Shows html page. ###

@app.route('/alders/alder/alder_extra/')
def alder_extra():
  return render_template('alder_extra_content.html')
### Adds extra content to alders html page. ###

@app.route('/alders/alder/alder_image/')
def static_alder_img():
  start = '<p><img src="'
  url = url_for('static', filename='aldertree.jpg')
  end = '"></p>'
  link = '<a style="color: #41494b; font-family: Arial;" href="/">Back to the front page.</a>'
  return start+url+end+link, 200
### Displays an image of alder tree and gives the option to go back to ###
### the front page. CSS tags are also applied on this option.###

@app.route('/apples/')
def secondtype():
  names = ['Crab Apple']
  return render_template('secondtype.html', names=names)
### Directs to /apples/ route, shows dictionary of types, ###
### and displays its html page. ###

@app.route('/apples/crabapple/')
def secondtypea():
  return render_template('crabapple.html')
### Shows html page. ###

@app.route('/apples/crabapple/crabapple_extra/')
def crabapple_extra():
  return render_template('apple_extra_content.html')
### Adds extra content to apples html page. ###

@app.route('/apples/crabapple/crabapple_image/')
def static_crabapple_img():
  start = '<p><img src="'
  url = url_for('static', filename='crabappletree.jpg')
  end = '"></p>'
  link = '<a style="color: #41494b; font-family: Arial;" href="/">Back to the front page</a>'
  return start+url+end+link, 200
### Displays an image of apple tree and gives the option to go back to ###
### the front page. CSS tags are also applied on this option. ###

@app.route('/ashes/')
def thirdtype():
  names = ['Common Ash']
  return render_template('thirdtype.html', names=names)
### Directs to /ashes/ route, shows dictionary of types, ###
### and displays its html page. ###

@app.route('/ashes/commonash/')
def thirdtypea():
  return render_template('commonash.html')
### Shows html page. ###

@app.route('/ashes/commonash/commonash_extra/')
def commonash_extra():
  return render_template('ash_extra_content.html')
### Adds extra content to ashes html page. ###

@app.route('/ashes/commonash/commonash_image/')
def static_commonash_img():
  start = '<p><img src="'
  url = url_for('static', filename='commonash.jpg')
  end = '"></p>'
  link = '<a style="color: #41494b; font-family: Arial;" href="/">Back to the front page</a>'
  return start+url+end+link, 200
### Displays an image of ashes tree and gives the option to go back to ###
### the front page. CSS tags are also applied on this option. ###

@app.route('/birches/')
def fourthtype():
  names = ['Silver Birch', 'Downy Birch']
  return render_template('fourthtype.html', names=names)
### Directs to /birches/ route, shows dictionary of types, ###
### and displays its html page. ###

@app.route('/birches/silverbirch/')
def fourthtypea():
  return render_template('silverbirch.html')
### Shows html page. ###

@app.route('/birches/silverbirch/silverbirch_extra/')
def silverbirch_extra():
  return render_template('silver_extra_content.html')
### Adds extra content to silver birch html page. ###

@app.route('/birches/silverbirch/silverbirch_image/')
def static_silverbirch_img():
  start = '<p><img src="'
  url = url_for('static', filename='silverbirch.jpg')
  end = '"></p>'
  link = '<a style="color: #41494b; font-family: Arial;" href="/">Back to the front page</a>'
  return start+url+end+link, 200
### Displays an image of silver birch tree and gives the option to go ###
### back to the front page. CSS tags are also applied on this option. ###

@app.route('/birches/downybirch/')
def fourthtypeb():
  return render_template('downybirch.html')
### Shows html page. ###

@app.route('/birches/downybirch/downybirch_extra/')
def downy_extra():
  return render_template('downy_extra_content.html')
### Adds extra content to downy birch html page. ###

@app.route('/birches/downybirch/downybirch_image/')
def static_downybirch_img():
  start = '<p><img src="'
  url = url_for('static', filename='downybirch.jpg')
  end = '"></p>'
  link = '<a style="color: #41494b; font-family: Arial;" href="/">Back to the front page</a>'
  return start+url+end+link, 200
### Displays an image of downy birch tree and gives the option to go ###
### back to the front page. CSS tags are also applied on this option. ###

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

