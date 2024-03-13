from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify, json

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploadet_files'

@app.route('/upload')
def upload_file():
    return render_template(template_name_or_list='upload.html')


@app.route('/data')
def data():
  return jsonify({'key': 'value'})

@app.route('/get_data')
def show_data():
    with open('uploadet_files/sh.json') as file:
        return str(json.load(file))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)
