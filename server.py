from flask_app import app

#Importando Controlador
from flask_app.controllers import product_controller, user_controller

if __name__=="__main__":
    app.run(debug=True) 

    #Pasos a seguir:
#pipenv install flask pymysql  ...... pipenv install flask pymysql flask-bcrypt
#pipenv shell
#python server.py -> python3, py o python

#pipenv install werkzeug     ----> para añadir imagenes