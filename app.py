from flask import Flask, render_template, request, redirect,flash, url_for
##from data import Articles
##from werkzeug import secure_filename
from flask_uploads import UploadSet
import csv
import pandas as pd

import blast


UPLOAD_FOLDER = '/img'
app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##Articles = Articles()
##
##@app.route('/')
##def index():
##    return render_template('index.html')
##
##@app.route('/about')
##def about():
##    return render_template('about.html')
##
##@app.route('/articles')
##def articles():
##    return render_template('articles.html', articles = Articles)
##
##@app.route('/article/<string:id>/')
##def article(id):
##    return render_template('article.html', id=id)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route('/submitReport.html')
def reports():
    return render_template('form.html')

@app.route('/map')
def maps():
    return render_template('my.html')

@app.route('/', methods=['POST'])
def value():
    longitude = request.form["longitude"]
    depth = request.form["depth"]
    latitude = request.form["latitude"]
    width = request.form["width"]
    lane = request.form["lane"]
    fixed = request.form["fixed"]
    columns=['image','latitude','longitude','depth','width','location','fixed']
    df=pd.read_csv("./templates/potholes.csv.html",index_col=0, )
    list=[["image",latitude,longitude,depth,width,lane,fixed]]
    df=df.append(pd.DataFrame(list,columns=columns))
    df.to_csv("./templates/potholes.csv.html")

    blast
    
    return render_template('my.html')

@app.route('/potholes.csv')
def readcsv():
    return render_template('potholes.csv.html')



##photos = UploadSet('photos', IMAGES)



##@app.route('/upload', methods=['GET', 'POST'])
##def upload():
  ##  if request.method == 'POST' and 'photo' in request.files:
    ##    filename = photos.save(request.files['photo'])
      ##  rec = Photo(filename=filename, user=g.user.id)
     ##   rec.store()
     ##   flash("Photo saved.")
     ##   return redirect(url_for('show', id=rec.id))
  ##  return render_template('upload.html')

##@app.route('/photo/<id>')
##def show(id):
##    photo = Photo.load(id)
 ##   if photo is None:
  ##      abort(404)
 ##   url = photos.url(photo.filename)
##    return render_template('show.html', url=url, photo=photo)

if __name__=='__main__':
    app.run(debug=True)