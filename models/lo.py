import mysql.connector
from mysql.connector import Error

def get_course(val1,val2):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select place,caste,gender from student where mail="'+val2+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		place=row[0][0]
		caste=row[0][1]
		gender=row[0][2]
		gen='0'
		if gender=='female':
			st=',female'
			fst=',ffemale'
			gen='1'
		else:
			st=fst=''
		if place!=None:
		 query='select clge,fees,des,link,min,paper,'+str(caste) +',f'+str(caste)+',open,fopen,des1,course,id'+st+fst+' from courses where locate("'+val1+'",course) or locate("'+val1+'",des);"'
		 cursor.execute(query,multi=True)
		 row=cursor.fetchall()
		 #return row[0][12];
		 cursor.close()
		 connection.close();
		 if(len(row)!=0):
		 	return row,True,gen;
		 else:
		 	return 'No colleges Found for you,...',False,gen

def get_course1(val1,val2):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select place,caste,gender from student where mail="'+val2+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		place=row[0][0]
		caste=row[0][1]
		gender=row[0][2]
		gen='0'
		if gender=='female':
			st=',female'
			fst=',ffemale'
			gen='1'
		else:
			st=fst=''
		if place!=None:
		 query='select clge,fees,des,link,min,paper,'+str(caste) +',f'+str(caste)+',open,fopen,des1,course'+st+fst+' from courses where (locate("'+val1+'",course) or locate("'+val1+'",des)) and (place="'+place+'");'
		 #return query,False,0
		 cursor.execute(query,multi=True)
		 row=cursor.fetchall()
		 cursor.close()
		 connection.close();
		 if(len(row)!=0):
		  return row,True,gen;
		 else:
		 	return 'No colleges Found for you,...',False,gen
		return 'No Colleges found',False,0;

def get_min(val1):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select marks from student where mail="'+val1+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row[0][0]
def get_pp(val1):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select s1,s2,s3,s4 from student where mail="'+val1+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row[0][0]

def get_clge_details(val1):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name place,city from clge where name="'+val1+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row[0][0]
	return'nothing'

def get_course_details(val1):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select marks from student where mail="'+val1+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row[0][0]
def update_clge(data,std):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='update clge set name="'+data['name']+'",link1="'+data['page']+'",link2="'+data['dis']+'",place="'+data['loc']+'",city="'+data['dist']+'" where mail="'+std+'";'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "updated Successfully"
	else:
		return "No connection"
def clg_details(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name,link2,link1,place,city from clge where mail="'+mail+'"'
		cursor.execute(query)
		rows=cursor.fetchall()
		cursor.close()
		return rows[0]
	return 'nothing'

def clg_details(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='select name,link2,link1,place,city from clge where mail="'+mail+'"'
		cursor.execute(query)
		rows=cursor.fetchall()
		cursor.close()
		return rows[0]
def del_clge(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='delete from clge where mail="'+mail+'"'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "Deleted Successfully"
def avl_courses(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	#cursor1=connection.cursor()
	if connection.is_connected():
		query='select course,id from courses where mail="'+mail+'"'
		cursor.execute(query)
		row=cursor.fetchall()
		return row
		#return get(row[0][0])
	return 'val'
def get(val):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	#cursor=connection.cursor()
	cursor1=connection.cursor()
	if connection.is_connected():
		v=val
		v="RKS College"
		if v==val:
			return 'true'
		else:
		    return '"'+str(v)+'" =>   "'+str(val)+'"'

		query='select * from courses,id where clge="'+v+'";'
		#return query;
		cursor1.execute(query)
		row1=cursor1.fetchall()
		return row1;
		cursor1.close()
def increment(val1,val2):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	#cursor=connection.cursor()
	cursor1=connection.cursor()
	if connection.is_connected():
		query='select caste,gender from student where mail="'+val2+'"'
		cursor1.execute(query)
		row1=cursor1.fetchall()
		caste=row1[0][0]
		gender=row1[0][1]
		query='select '+caste+',f'+caste+' from courses where id="'+val1+'"'
		cursor1.execute(query)
		row1=cursor1.fetchall()
		if int(row1[0][0])<int(row1[0][1]):
			caste='open'
		#return caste;
		if gender=='male':
		 query='update courses set f'+caste+'=f'+caste+'+1  where id ="'+val1+'"'
		else:
			query='update courses set f'+caste+'=f'+caste+'+1 ffemale=ffemale+1  where id ="'+val1+'"'
		cursor1.execute(query)
		connection.commit()
		cursor1.close()
def comment(val1,val2):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	#cursor=connection.cursor()
	cursor1=connection.cursor()
	if connection.is_connected():
		query='insert into feedback (mail,cnt) values ("'+val1+'","'+val2+'");'
		cursor1.execute(query)
		connection.commit()
		cursor1.close()
def get_cmt():
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	#cursor=connection.cursor()
	cursor1=connection.cursor()
	if connection.is_connected():
		query='select * from feedback;'
		cursor1.execute(query)
		row=cursor1.fetchall()
		return row
def del_cm(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='delete from feedback where id="'+mail+'"'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "Deleted Successfully"
def del_course(mail):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='delete from courses where id="'+mail+'"'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "Deleted Successfully"
def get_data(id):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	#cursor=connection.cursor()
	cursor1=connection.cursor()
	if connection.is_connected():
		query='select course,des,paper,min,open,bc,mbc,sc,oc,female,fees,duration,link,fbc,fmbc,fsc,foc,ffemale,id,fopen from courses where id="'+id+'";'
		cursor1.execute(query)
		row=cursor1.fetchall()
		if(len(row)!=0):
		 return row[0]
		else:
		 return 'no'

def update_crse(data,id):
	connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='user',
                             password='admin')
	cursor=connection.cursor()
	if connection.is_connected():
		query='update courses set course="'+data['name']+'",des="'+data['desc']+'",paper="'+data['must']+'",min="'+data['text-input']+'",open="'+data['open']+'",bc="'+data['bc']+'",mbc="'+data['mbc']+'",sc="'+data['sc']+'",oc="'+data['oc']+'",female="'+data['female']+'",duration="'+data['duration']+'",link="'+data['link']+'",fees="'+data['fee']+'",ffemale="'+data['ffemale']+'",fbc="'+data['sbc']+'",fmbc="'+data['fmbc']+'",fsc="'+data['fsc']+'",foc="'+data['foc']+'" where id="'+id+'";'
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return "updated Successfully"
	else:
		return "No connection"