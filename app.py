from flask import Flask

app =Flask(__name__)

@app.route("/")
def start():
    return"primeiro codigo em flask"

    @app.route('/produtos')
    def produto():
        return "produtos"
    @app.route('/login')
    def login():
        return'login'