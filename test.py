
app = Flask('vulpy')
app.config['SECRET_KEY'] = 'aaaaaaa'
app.config['SECRET_KEY'] = '123aa8a93bdde342c871564a62282af857bda14b3359fde95d0c5e4b321610c1'
app.register_blueprint(mod_hello, url_prefix='/hello')
