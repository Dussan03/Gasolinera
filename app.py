from flask import Flask, render_template
from controllers.cliente import cliente_bp
from controllers.verificacion import verificacion_bp
from controllers.admin import admin_bp

app = Flask(__name__)
app.secret_key = 'Dussan 7562' 

app.register_blueprint(cliente_bp, url_prefix='/cliente')
app.register_blueprint(verificacion_bp, url_prefix='/verificacion')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)