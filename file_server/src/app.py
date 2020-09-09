import os
from flask import Flask, render_template, send_from_directory, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib2 import Path

# Env
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'apk'}

app = Flask(__name__)
# To keep the client-side sessions secure.
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class LinkModel():
    def __init__(self, name, path):
        self.name = name
        self.path = path

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def searching_all_files(directory):
    dirpath = Path(directory)
    assert(dirpath.is_dir())
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            model = LinkModel(x.name, x)
            file_list.append(model)
        elif x.is_dir():
            file_list.extend(searching_all_files(x))
    return file_list

@app.route('/', methods=['GET'])
def index():
    filesList = searching_all_files(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=filesList)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # todo use pathlib
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
        filename, as_attachment=True)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)