from flask import Flask

import mysql.connector 


# db = list()
db = mysql.connector.connect( 
    host ='informatica.iesquevedo.es',
    port = 3333,
    user ='root',
    password ='1asir', 
    database='JonatanAnes'
) 



def create_app():
    app = Flask(__name__, template_folder='template')
    app.debug = True
    

    

    from .routes import routes
    
    app.register_blueprint(routes.rutas_mitienda)

    return app