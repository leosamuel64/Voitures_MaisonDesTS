from flask import Flask, render_template, redirect, session,request
app=Flask(__name__)
app.template_folder = "template"
app.static_folder="static"
app.config.from_object('myApp.config')
from .model import bdd as bdd
import pandas
from openpyxl import Workbook
import datetime

COUT_GPL=0.7
COUT_ESSENCE=1.35
COUT_DIESEL=0.96


@app.route('/')
def membres():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    session['Clio']=bdd.compte(1,last_month.strftime("%Y-%m"))
    session['208']=bdd.compte(2,last_month.strftime("%Y-%m"))
    session['C3']=bdd.compte(3,last_month.strftime("%Y-%m"))
    session['Fabia']=bdd.compte(4,last_month.strftime("%Y-%m"))
    
    session['ct_Clio']=round(session['Clio']*COUT_GPL*2,2)
    session['ct_208']=round(session['208']*COUT_DIESEL*2,2)
    session['ct_C3']=round(session['C3']*COUT_DIESEL*2,2)
    session['ct_Fabia']=round(session['Fabia']*COUT_ESSENCE*2,2)
    
    session['Clio_c']=bdd.compte(1,today.strftime("%Y-%m"))
    session['208_c']=bdd.compte(2,today.strftime("%Y-%m"))
    session['C3_c']=bdd.compte(3,today.strftime("%Y-%m"))
    session['Fabia_c']=bdd.compte(3,today.strftime("%Y-%m"))
    
    session['ct_Clio_c']=round(session['Clio_c']*COUT_GPL*2,2)
    session['ct_208_c']=round(session['208_c']*COUT_DIESEL*2,2)
    session['ct_C3_c']=round(session['C3_c']*COUT_DIESEL*2,2)
    session['ct_Fabia_c']=round(session['C3_c']*COUT_ESSENCE*2,2)
    
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

