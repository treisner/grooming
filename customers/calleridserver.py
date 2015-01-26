import serial
import re
import psycopg2
import time
import os
import sys


def main():
    while True:
        fromid = callid()
        message = {}
        cust=get_customer(fromid['phone'],fromid['NAME'])
        message['callernumber']=fromid['phone']
        message['callername']=fromid['NAME']
        message['calledat']=fromid['time']
        message['NMBR']=fromid['NMBR']
        message['customer'] = cust['name']
        message['pk']=cust['pk']
        message['url']=cust['url']
        message['custtype']=cust['custtype']
        publish('callerid','caller',message)
        print("published...",message)

        crs.execute("insert into customers_call "
                    "values (default, '{}','{}','{}',{}) "
                    .format(fromid['phone'],fromid['NAME'],fromid['time'], cust["pk"]))
        crs.execute("commit")

def callid():
    while True:
        callerid={}
        while len(callerid)<4:
            reply = modem.readline().decode(encoding='ascii')
            if reply:
                replydata=re.match(r'([A-Z]{4})=(.+)\r\n',reply)
                if replydata:
                    callerid[replydata.group(1)]=replydata.group(2)
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        p = callerid['NMBR']
        pn = p[0:3]+"-"+p[3:6]+"-"+p[6:10]
        callerid['phone']=pn
        callerid['time']=t
        callerid['NAME']=callerid['NAME'].replace(r"&","and")
        return callerid

def get_customer(phone,caller):
    count=1
    name=None
    calling=None
    cust={}
    try:
        calling=Customer.objects.get(home_phone=phone)
    except:
        try:
            count = Customer.objects.filter(work_phone=phone).count()
            callers=Customer.objects.filter(work_phone=phone)
            calling=callers.first()
        except:
            name = ' The caller is not a grooming customer.'
    if calling is None:
        cust['custtype']="New"
        cust['pk']=-1
        cust['url']='/customer/create/?phone={}&name={}'.format(phone,encoding.filepath_to_uri(caller))
    else:
        cust['custtype']="Existing"
        if count>1:
            cust['pk']=calling.pk
            name = "{} grooming customers use this number.  The first is {} ".format(count,calling.name)
        else:
            cust['pk']=calling.id
            name = calling.name+" is the grooming customer name."
        cust['url']='/customer/{}'.format(cust['pk'])
    cust['name']=name
    return cust


if __name__=='__main__':
    cnx = psycopg2.connect(user='treisner', password='Fred0fred', database='grooming')
    crs = cnx.cursor()
    modem = serial.Serial(2)
    modem.setTimeout(10)
    modem.write(b'ats0=0\r\n')
    modem.write(b'at+vcid=1\r\n')
    sys.path.append('C:\\www\\grooming')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'grooming.settings'
    import django
    django.setup()
    from omnibus.api import publish
    from customers.models import Customer
    from django.utils import encoding
    main()

