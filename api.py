from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import print_api

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)

app.debug = True


@app.route("/")
def index():
    return "Hello World!"


# Create a directory in a known location to save files to.
uploads_dir = os.path.join(".", "uploads")


# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     print("Req Recived")
#     if request.method == "POST":

#         print(request)

#         # save each "charts" file
#         file = list(request.files.keys())
#         print("FGILE", file)
#         # file.save(os.path.join(uploads_dir, file.name))

#         return "uploaded"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":

        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ext = filename.split(".")[-1]

            filepath = os.path.join(UPLOAD_FOLDER, str("to_print") + "." + ext)
            file.save(filepath)
            print_api.send_to_os(filepath)

    return """
    printed
    """


if __name__ == "__main__":
    app.run()
