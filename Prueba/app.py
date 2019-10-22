import os
#import magic
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/CReal/Downloads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#-----------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#-----------------------------------------------------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'softwareavanzado'
#-----------------------------------------------------------------------
mysql = MySQL(app)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO uploads VALUES (%s, ?)", (filename, [file]))
			mysql.connection.commit()
			cur.close()
			#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

if __name__ == "__main__":
    app.run()