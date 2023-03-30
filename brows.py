import flask as f

app = f.Flask(__name__)

@app.route("/imgs/<img>")
def get_img(img):
    return f.send_from_directory("./imgs", img)

if __name__ == '__main__':
    app.run()
