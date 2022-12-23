from flask import Flask, render_template, redirect, session,request
app=Flask(__name__)
app.template_folder = "template"
app.static_folder="static"
app.config.from_object('myApp.config')
from .model import bdd as bdd
import pandas
from openpyxl import Workbook
import datetime




@app.route('/')
def membres():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    session['Clio']=bdd.compte(1,last_month.strftime("%Y-%m"))
    session['208']=bdd.compte(2,last_month.strftime("%Y-%m"))
    session['C3']=bdd.compte(3,last_month.strftime("%Y-%m"))
    session['calc_m']=last_month.strftime("%Y-%m")
    return render_template("membres.html",listeMembres=bdd.get_trajets())


@app.route("/suppMembre/<idUser>")
def suppMembre(idUser=""):
    bdd.SuppTrajets(idUser)
    return redirect('/')

@app.route('/addMembre', methods=['POST'])
def addMembre():
    idvoiture = request.form['Voiture']
    today = datetime.date.today()
    bdd.add_membreData(idvoiture,today.strftime("%Y-%m-%d"))
    return redirect('/')

