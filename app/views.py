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
		cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = ?", tagBox)
	else:
		cursor.execute("SELECT * FROM NOTICIAS")
	noticia = choice(cursor.fetchall())
	conn.close()
	return noticia

@app.route('/', methods=['GET','POST'])
def index():
	return "<h1>Você não escolheu uma tag!</h1>"

@app.route('/nutricao')
def nutricao():
	noticia = query("nutricao")
	return render_template('index.html', tagBox=noticia[1], imgBox=noticia[2], titulo=noticia[3],
	 fontBox=noticia[4], descricao=noticia[5], mainBox=noticia[6])

@app.route('/saude')
def saude():
	conn = sqlite3.connect("noticias.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = 'saude'")
	noticia = choice(cursor.fetchall())
	tag = noticia[1]
	img = noticia[2]
	title = noticia[3]
	font = noticia[4]
	description = noticia[5]
	text = noticia[6]
	conn.close()
	return render_template('index.html', tagBox=tag, imgBox=img, titulo=title, fontBox=font,descricao=description, mainBox=text)

@app.route('/dieta')
def dieta():
	conn = sqlite3.connect("noticias.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = 'dieta'")
	noticia = choice(cursor.fetchall())
	tag = noticia[1]
	img = noticia[2]
	title = noticia[3]
	font = noticia[4]
	description = noticia[5]
	text = noticia[6]
	conn.close()
	return render_template('index.html', tagBox=tag, imgBox=img, titulo=title, fontBox=font,descricao=description, mainBox=text)

@app.route('/energiaesaude')
def energiaesaude():
	conn = sqlite3.connect("noticias.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = 'academia'")
	noticia = choice(cursor.fetchall())
	img = noticia[2]
	title = noticia[3]
	font = noticia[4]
	description = noticia[5]
	text = noticia[6]
	conn.close()
	return render_template('energiaesaude.html', imgBox=img, titulo=title, fontBox=font, descricao=description, mainBox=text)

@app.route('/belezamasculina')
def belezamasculina():
	conn = sqlite3.connect("noticias.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM NOTICIAS WHERE TAGBOX = 'beleza'")
	noticia = choice(cursor.fetchall())
	img = noticia[2]
	title = noticia[3]
	font = noticia[4]
	text = noticia[6]
	conn.close()
	return render_template('belezamasculina.html', imgBox=img, titulo=title, fontBox=font, mainBox=text)
