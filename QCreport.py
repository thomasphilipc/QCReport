# -*- coding: utf-8 -*-
import io
import random



class QCDeivce:
    imei  = 'not init'
    type = 'CFV'
    events = []
    hour = []
    min = []
    sec = []
    index = []


    def __init__(self,imei,type,hour,min):
        self.imei=imei
        self.type
        if type == 'CFV':
            self.events= ['TAG IN', 'IGNITION ON' , 'IGNITION OFF' , 'TAG OUT' , 'POLL RESPONSE']
            list_length =  5
            self.hour = hour
            if min>54:
                min=55
            self.min = random.sample(range(6),list_length)
            self.min[:] = [i + min for i in self.min]
            self.min = sorted(self.min)
            self.sec = random.sample(range(10,59),list_length)
            self.index = range(list_length)
        elif type == 'GEN':
            self.events = ['IGNITION ON', 'IGNITION OFF', 'POLL RESPONSE']
            list_length = 3
            self.hour = hour
            if min>54:
                min=55
            self.min = random.sample(range(4),list_length)
            self.min[:] = [i + min for i in self.min]
            self.min = sorted(self.min)
            self.sec = random.sample(range(10,59),list_length)
            self.index = range(list_length)


from jinja2 import Environment, FileSystemLoader , select_autoescape
import webbrowser


QCDeivceList = []

QCDeivceList.append(QCDeivce('359006059546816','CFV',10,42))
QCDeivceList.append(QCDeivce('359006059546758','CFV',12,33))
QCDeivceList.append(QCDeivce('359006059541973','CFV',12,10))
QCDeivceList.append(QCDeivce('356363056947262','CFV',12,46))
QCDeivceList.append(QCDeivce('359006059546816','CFV',11,14))
QCDeivceList.append(QCDeivce('359006059546741','CFV',11,20))
QCDeivceList.append(QCDeivce('359006059549448','CFV',11,11))
QCDeivceList.append(QCDeivce('359006059546550','CFV',11,48))
QCDeivceList.append(QCDeivce('359006059544522','CFV',13,17))
QCDeivceList.append(QCDeivce('359006059541577','CFV',13,22))
QCDeivceList.append(QCDeivce('356363056943592','CFV',13,27))
QCDeivceList.append(QCDeivce('359006059541528','CFV',13,41))
QCDeivceList.append(QCDeivce('356363056944988','CFV',14,12))
QCDeivceList.append(QCDeivce('359006059537039','CFV',14,20))
QCDeivceList.append(QCDeivce('359006059541650','CFV',14,29))
QCDeivceList.append(QCDeivce('359006059544852','CFV',14,46))
QCDeivceList.append(QCDeivce('356363056944194','CFV',15,18))
QCDeivceList.append(QCDeivce('356363056947429','CFV',15,23))
QCDeivceList.append(QCDeivce('356363056943535','CFV',15,28))
QCDeivceList.append(QCDeivce('356363056943758','CFV',15,36))
QCDeivceList.append(QCDeivce('359006059537682','CFV',16,43))
QCDeivceList.append(QCDeivce('353705061251200','CFV',16,49))
QCDeivceList.append(QCDeivce('359006059544829','CFV',16,53))


ENV = Environment(loader=FileSystemLoader('./template'),autoescape=select_autoescape(['html', 'xml']))

template = ENV.get_template('QCReportTemplate.html')

html = template.render( _QCDeivceList_ = QCDeivceList ,  _DATE_ = '08/30/2017')

print (html.encode('utf-8-sig'))
stringhtml= (str(html))

file_name = 'QCReportTemplate.html'


with io.open(file_name, "w", encoding="utf-8") as out_file:
    out_file.write(html)

    webbrowser.open(file_name);

