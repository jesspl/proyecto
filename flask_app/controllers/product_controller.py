from fileinput import filename
from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app

#Importar el modelo de User
from flask_app.models.users import User

#Importar el modelo de dates
from flask_app.models.product import Product

#Subir imagenes
from werkzeug.utils import secure_filename
import os

@app.route('/new/appoinment')
def new_show():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario)
    
    return render_template('new_date.html', user=user)

@app.route('/create/appoinment', methods=['POST'])
def create_show():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #Tengo que validar mi asignacion
    if not Product.valida_product(request.form): #(ENVIA FORMULARIO). SI NO ES VALIDO
        return redirect('/new/appoinment')

    if 'image' not in request.files:
        flash ('Imagen no encontrada', 'cita')
        return redirect("/new/appoinment")

    image = request.files['image']

    if image.filename == '':
        flash('Nombre de imagen vacio', 'cita')
        return redirect("/new/appoinment")

    nombre_imagen = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))

    #crear nuevo formulario que sea igual a todos los campos del formualrio

    formulario = {
        "product" : request.form['product'],
        "description" : request.form['description'],
        "ready_at" : request.form['ready_at'],
        "lost_at" : request.form['lost_at'],
        "user_id" : request.form['user_id'],
        "image" : nombre_imagen
    }

    Product.save(formulario)
    return redirect('/dashboard')

    
@app.route('/edit/show/<int:id>') #Recibo el identificador de las citas que quiero editar
def edit_show(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_show = { "id": id }
    #llamar a una función y debo de recibir la appoinment
    show = Product.get_by_id(formulario_show)

    return render_template('edit_date.html', user=user, show=show)

@app.route('/update/appoinment', methods=['POST'])
def update_show():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Product.valida_product(request.form):
        return redirect('/edit/show/'+request.form['id'])   #/edit/show/1

    Product.update(request.form)

    return redirect('/dashboard')



@app.route('/delete/show/<int:id>')
def delete_show(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Product.delete(formulario)

    return redirect('/dashboard')

#--------------------------------------

@app.route('/show/show/<int:id>') #A través de la URL recibimos el ID de la receta
def show(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_show = { "id": id }
    #llamar a una función y debo de recibir la informacion
    show = Product.get_by_id(formulario_show)

    return render_template('show.html', user=user, show=show)

