from database.corso_dao import Corso_DAO
from database.studente_Dao import StudenteDao



class Model:
    def __init__(self):
        pass

    def get_corsi_periodo(self,pd):
        return Corso_DAO().get_corsi_periodo(pd)
    def get_studenti_periodo(self,pd):
        return Corso_DAO().get_studenti_periodo(pd)
    def get_studenti_corso(self,corso):
        return StudenteDao.get_studenti_corso(corso)
