import mysql.connector
from mysql.connector import Error
cursor=''
connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')

#cursor=connection.cursor()
def verify(mail,pas):
    cursor=connection.cursor()
    if connection.is_connected():
        query='select type from login where mail="'+str(mail)+'" and pass="'+str(pas)+'"'
        cursor.execute(query)
        row=cursor.fetchall()
        if(len(row)!=1):
           cursor.close()
           return False
        else:
           cursor.close()
           return row[0][0]
def sign(name,mail,pas,mobile):
    cursor=connection.cursor()
    if connection.is_connected():
    	query='select type from login where mail="'+str(mail)+'"'
    	cursor.execute(query)
    	row=cursor.fetchall()
    	if(len(row)==0):
    		query='insert into student(name,mail,mobile,password) values("'+str(name)+'","'+str(mail)+'","'+str(mobile)+'","'+str(pas)+'");'
    		flag=cursor.execute(query)
    		query='insert into login values("'+str(mail)+'","'+str(pas)+'","student");'
    		cursor.execute(query)
    		connection.commit()
    		cursor.close()
    		return True,"Account Created"
    	else:
    		cursor.close()
    		return False,"Already the mail id is registerd with a "+str(row[0][0])+" Account"
    	cursor.close()
    	return False,"No connection"
def get_clg():
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name,mail,place from clge '
		cursor.execute(query)
		row=cursor.fetchall()
		return row

def create_clge(name,mail,pas):
	cursor=connection.cursor()
	if connection.is_connected():
		query='select type from login where mail="'+str(mail)+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		if(len(row)==0):
			query='insert into clge(name,mail,password) values("'+str(name)+'","'+str(mail)+'","'+str(pas)+'");'
			flag=cursor.execute(query)
			query='insert into login values("'+str(mail)+'","'+str(pas)+'","student");'
			cursor.execute(query)
			connection.commit()
			cursor.close()
			return "Account Created"
		else:
			cursor.close()
			return "Already the mail id is registerd with a "+str(row[0][0])+" Account"
		cursor.close()
		return "No connection"
def crt_course(data,clge):
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name,link2 from clge where mail="'+clge+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		clge1=row[0][0]
		place=row[0][1]
		query='insert into courses(mail,clge,course,des,level,paper,min,open,bc,mbc,sc,oc,male,female,fees,duration,link,place,fbc,fmbc,fsc,foc,ffemale,fopen) values("'+clge+'","'+clge1+'","'+data['name']+'","'+data['desc']+'","'+data['level']+'","'+data['must']+'","'+data['text-input']+'","'+data['open']+'","'+data['bc']+'","'+data['mbc']+'","'+data['sc']+'","'+data['oc']+'","'+data['male']+'","'+data['female']+'","'+data['fee']+'","'+data['duration']+'","'+data['link']+'","'+place+'","'+data['sbc']+'","'+data['fmbc']+'","'+data['fsc']+'","'+data['foc']+'","'+data['ffemale']+'","'+data['fopen']+'");'

		#return query
		flag=cursor.execute(query)
		connection.commit()
		cursor.close()
		return "Course Added"
	else:
		return "No connection"

def get_stud_data(var):
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name,qualification,dob,age,place,caste,marks,s1,s2,s3,s4,gender from student where mail="'+var+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row[0]
	return'no data'

def update_std(data,std):
	cursor=connection.cursor()
	if connection.is_connected():
		query='update student set qualification="'+data['qual']+'",dob="'+data['dob']+'",age="'+data['age']+'",place="'+data['dist']+'",caste="'+data['caste']+'",marks="'+data['mark']+'",s1="'+data['s1']+'",s2="'+data['s2']+'",s3="'+data['s3']+'",s4="'+data['s4']+'",gender="'+data['gender']+'" where mail="'+std+'";'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "updated Successfully"
	else:
		return "No connection"





