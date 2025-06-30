from flask import Flask, render_template
from controllers.cliente import cliente_bp

app = Flask(__name__)
app.register_blueprint(cliente_bp, url_prefix='/cliente')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)