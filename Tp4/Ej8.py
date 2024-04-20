

import datetime


class Fecha:
    dia:int
    mes:int
    ano:int

    def __validateDia__(self):
        dia=self.dia
        if dia<1 or dia>31:
            dia=1
        elif self.mes==2:
            if self.esBisiesto():
                if dia>29:
                    dia=1
            else:
                if dia>28:
                    dia=1
        elif self.mes==4 or self.mes==6 or self.mes==9 or self.mes==11:
            if dia>30:
                dia=1
        return dia
    
    def __validateMes__(self):
        mes=self.mes
        if mes < 1 or mes > 12:
            mes=1
        return mes
    
    def __validateAno__(self):
        ano=self.ano
        if ano < 1900 or ano > 2050:
            ano= 1900
        return ano
    
    def __validate__(self):
        ano=self.__validateAno__()
        mes=self.__validateMes__()
        dia=self.__validateDia__()
        self.dia=dia
        self.mes=mes
        self.ano=ano

    def __init__(self, dia=1, mes=1, ano=1900):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.__validate__()

    def esBisiesto(self):
        if self.ano % 4 == 0 and self.ano % 100 != 0 or self.ano % 400 == 0:
            return True
        else:
            return False
    def getDia(self):
        return self.dia

    def getMes(self):
        return self.mes

    def getAno(self):
        return self.ano
    def setDia(self, dia):
        self.dia = dia
        self.__validate__()

    def setMes(self, mes):
        self.mes = mes
        self.__validate__()

    def setAno(self, ano):
        self.ano = ano
        self.__validate__()

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    def hoy():
        hoy = datetime.now()
        return Fecha(hoy.day, hoy.month, hoy.year)
    def corta(self):
        return f"{self.dia} - {self.mes} - {self.ano}"