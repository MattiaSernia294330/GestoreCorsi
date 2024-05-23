import mysql.connector
from database.DB_connect import DBConnect
from model.Corso import Corso


class Corso_DAO:
    @staticmethod
    def get_corsi_periodo(pd):
        cnx =DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor=cnx.cursor(dictionary=True)
            query="""SELECT c.*
                FROM corso c
                WHERE c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso( row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result
    @staticmethod
    def get_studenti_periodo(pd):
        cnx =DBConnect.get_connection()
        result=0
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor=cnx.cursor(dictionary=True)
            query="""SELECT COUNT(DISTINCT i.matricola)
                    FROM corso c, iscrizione i
                    where c.pd=%s and c.codins =i.codins"""
            cursor.execute(query, (pd,))
            if cursor.with_rows:
                result=cursor.fetchone().get('COUNT(DISTINCT i.matricola)')
            cursor.close()
            cnx.close()
            return result