import mysql.connector
from database.DB_connect import DBConnect
from model.studente import Studente
class StudenteDao:
    @staticmethod
    def get_studenti_corso(corso):
        cnx = DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.*
                FROM studente s, iscrizione i 
                WHERE i.codins = %s AND s.matricola = i.matricola"""
            cursor.execute(query, (corso,))
            if cursor.with_rows:
                for row in cursor:
                    result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
            cursor.close()
            cnx.close()
            return result

