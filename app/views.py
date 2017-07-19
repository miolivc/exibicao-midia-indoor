#	-*- coding: utf-8 -*-
#	usr/bin/python3

from app import app
from flask import render_template
from random import choice
import sqlite3

def query(tagBox):
	conn = sqlite3.connect("noticias.db")
	cursor = conn.cursor()
	if tagBox != None:
		cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = ?", [tagBox])
	else:
		cursor.execute("SELECT * FROM NOTICIAS")
	noticia = choice(cursor.fetchall())
	conn.close()
	return noticia

@app.route('/', methods=['GET'])
def index():
	return "<h1>Você não escolheu uma tag!</h1>"

@app.route('/nutricao')
def nutricao():
	noticia = query("nutricao")
	return render_template('index.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3], fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])

@app.route('/saude')
def saude():
	noticia = query("saude")
	return render_template('index.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3], fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])

@app.route('/dieta')
def dieta():
	noticia = query("dieta")
	return render_template('index.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3], fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])

@app.route('/energiaesaude')
def energiaesaude():
	noticia = query("energiaesaude")
	return render_template('energiaesaude.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3], fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])

@app.route('/belezamasculina')
def belezamasculina():
	noticia = query("belezamasculina")
	return render_template('belezamasculina.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3], fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])
