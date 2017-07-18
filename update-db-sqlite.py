#	-*- coding: utf-8 -*-

import psycopg2
import sqlite3

#   conexão com o banco MYSQL
postgres = psycopg2.connect(host="187.17.184.44", user="postgres", password="", database="noticias")
cursorPostgres = postgres.cursor()
cursorPostgres.execute("SELECT * FROM noticias")

#	Conexao com o banco SQLite3
sqlite = sqlite3.connect("noticias.db")
cursorSqlite = sqlite.cursor()
deleteTable = "DROP TABLE IF EXISTS NOTICIAS"
createTable = "CREATE TABLE IF NOT EXISTS noticias (id INT, tagBox TEXT, imgBox TEXT, titulo VARCHAR(40) PRIMARY KEY, fontBox TEXT, descricao TEXT, mainBox TEXT)"
cursorSqlite.execute(deleteTable)
cursorSqlite.execute(createTable)
cursorSqlite.execute("SELECT * FROM noticias")

#	Recupera do banco de dados MYSQL o resultado apenas das Tuplas que não estão presentes no SQLite
insert = "INSERT INTO noticias(id,tagBox, imgBox, titulo, fontBox, descricao, mainBox) VALUES(?,?,?,?,?,?,?)"
for linePostgres in cursorPostgres.fetchall():
	for lineSqlite in cursorSqlite.fetchall():
		if(linePostgres == lineSqlite):
			pass
	cursorSqlite.execute(insert,(linePostgres[0], linePostgres[1], linePostgres[2], linePostgres[3], linePostgres[4], linePostgres[5], linePostgres[6]))

sqlite.commit()

#cursorSqlite.execute("SELECT * FROM NOTICIAS;")
#for line in cursorSqlite.fetchall():
#	print(line)

#	Fechando conexões
cursorPostgres.close()
cursorSqlite.close()

print("Banco de dados atualizado com sucesso!")