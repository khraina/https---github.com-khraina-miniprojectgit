from flask import Flask,render_template,request,session,redirect,url_for,g,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField,FormField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SECRET_KEY'] = 'thisisasecretkey'

class UploadFileForm(FlaskForm):
  file = FileField("File");
  submit = SubmitField("Upload file");
  




@app.route("/")
def home():
  return render_template('home.html')



      
@app.route("/login", methods=['GET', 'POST'])
def login():
  return render_template('login.html')
  
@app.route("/profile" , methods=['GET', 'POST'])
def profile():
  form = UploadFileForm()
  if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        flash('File has been uploaded.','success')
  return render_template('profile.html',form=form)


@app.route("/about_us")
def aboutus():
  return render_template('about.html')

@app.route("/view")
def views():
  return render_template('view.html')

@app.route("/logins",methods=['GET','POST'])
def logins():
  email = None
  return render_template('logins.html',boolean=True)

      
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)