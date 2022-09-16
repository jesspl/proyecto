from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Product:

    def __init__(self, data):
        self.id = data['id']
        self.product = data['product']
        self.ready_at = data['ready_at']  
        self.lost_at = data['lost_at']  
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.image=data['image']

        self.first_name = data['first_name']
        self.email= data['email']

    @staticmethod
    def valida_product(formulario):
        es_valido = True
        print("$$$$$$$$$$$$###########xd"+str(formulario))

        if len(formulario['product']) < 2:
            flash("el nombre del producto debe tener almenos 2 caracteres", "cita")
            es_valido = False

        if len(formulario['description']) < 2:
            flash("la descripcion del producto debe tener al menos 2 caracteres", "cita")
            es_valido = False

        if formulario['ready_at'] == "":
            flash("Ingrese una fecha de cuando se espera el producto listo", "cita")
            es_valido = False
        
        if formulario['lost_at'] == "":
            flash("Ingrese una fecha de vencimiento o disponibilidad del producto", "cita")
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO products (product, description, ready_at, lost_at, image, user_id) VALUES (%(product)s, %(description)s, %(ready_at)s, %(lost_at)s,%(image)s, %(user_id)s )"
        nuevoId = connectToMySQL('proyecto').query_db(query, formulario)
        return nuevoId

    @classmethod
    def get_all(cls, formulario):
        query = "SELECT products.*, first_name, email FROM products LEFT JOIN users ON users.id =products.user_id" # where user_id=%(id)s cuando quiero ver solo la informacion que levanto el usuario
        results = connectToMySQL('proyecto').query_db(query, formulario) #Lista de diccionarios
        shows = []
        for show in results:
            shows.append(cls(show)) #cls(show) -> Instancia de Date, Agregamos la instancia a mi lista de apointments
        #print(citas)
        return shows     #acabo de cambiar cls(tv)

    @classmethod
    def update(cls, formulario): #Recibir el formulario. OJO con todo y el ID de las citas
        query = "UPDATE products SET product= %(product)s, description= %(description)s, ready_at= %(ready_at)s, lost_at= %(lost_at)s WHERE id = %(id)s" 
        result = connectToMySQL('proyecto').query_db(query, formulario)
        return result
#products SET title (product, description, ready_at, lost_at) VALUES (%(product)s, %(description)s, %(ready_at)s, %(lost_at)s)"

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de cita a borrar
        query = "DELETE FROM products WHERE id = %(id)s"
        result = connectToMySQL('proyecto').query_db(query, formulario)
        return result

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT products.*, first_name, email FROM products LEFT JOIN users ON users.id = products.user_id WHERE products.id= %(id)s" # CAMBIO user_id= %(id)s  #where user_id=%(id)s
        result = connectToMySQL('proyecto').query_db(query, formulario) # se recibe unaLista de diccionarios
        show = cls(result[0])
        return show

    # @classmethod
    # def update(cls, formulario): #Recibir el formulario. OJO con todo y el ID de la receta
    #     query = "UPDATE recipes SET name = %(name)s, under30 = %(under30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE id = %(id)s"
    #     result = connectToMySQL('recetas_g1').query_db(query, formulario)
    #     return result

