from flask import Flask,render_template,request,flash
from flask import  session
#from flask.ext.session import Session
from flask_uploads import UploadSet,configure_uploads,IMAGES
from models import login as dbl
from models import lo as db
import datetime
import os

app=Flask(__name__,template_folder='templates')

photos=UploadSet('photos',IMAGES)
im='static/img/'
app.config['UPLOADED_PHOTOS_DEST']='static/img'
configure_uploads(app,photos)

@app.route('/form')
def form():
  return render_template('admin/form.html',clges=dbl.get_clg())
@app.route('/admins')
def admin():
 return request.base_url
@app.route('/dept',methods=['GET','POST'])
def dept():
  if request.method=='POST' and 'create' in request.form:
    clge=request.form.get('clge')
    mail=request.form.get('mail')
    pas=request.form.get('pass')
    message=dbl.create_clge(clge,mail,pas)
    return render_template('admin/chart.html',message=message)
  return "no result"
@app.route('/auth',methods=['GET','POST'])
def check():
   if request.method=='POST' and 'log' in request.form: 
       mail=request.form.get('email')
       pas=request.form.get('pass')
       flag=dbl.verify(mail,pas)
       if flag!=False:
         session['username'] = mail;
         session['type']=flag
         if flag=='student':
          return(render_template('student/home.html',data=dbl.get_stud_data(session['username'])))
         elif flag=='admin':
          return(render_template('admin/home.html'))
         else:
          return(render_template('clge/home.html'))
       else:
         return(render_template('login.html',message='Invalid Mail id or Password'));
   else:
      return 'not'
@app.route('/create_course',methods=['GET','POST'])
def create_course():
  if request.method=='POST' and 'create' in request.form: 
    data=request.form
    clge=(session['username'])
    message=dbl.crt_course(data,clge)
    #return message
    return(render_template('clge/new.html',message=message))
  else:
    return (render_template('clge/new.html'))

@app.route('/clge')
def home():
  return(render_template('home.html'))
def profile():
  #return str(db.clg_details(session['username']))
  return(render_template('clge/profile.html',message="",data=db.clg_details(session['username'])))
def new():
  return(render_template('new.html'))
@app.route('/clge1')
def clge1():
  #return str(db.clg_details(session['username']))
  return(render_template('clge/profile.html',message="",data=db.clg_details(session['username'])))
@app.route('/course')
def course():
  #return str(db.avl_courses(session['username'])) 
  return(render_template('clge/view.html',clges=db.avl_courses(session['username'])))

@app.route('/depart',methods=['GET','POST'])
def depart():
  if request.method=='POST' and 'view' in request.form: 
     data=request.form.get('view')
     return (render_template('clge/edit.html',data=db.get_data(data)))
  if request.method=='POST' and 'del' in request.form: 
     data=request.form.get('del')
     res=db.del_course(data)
     return(render_template('clge/view.html',clges=db.avl_courses(session['username']),data=res))



@app.route('/edit',methods=['GET','POST'])
def edit():
  if request.method=='POST' and 'update' in request.form: 
     data=request.form
     std=session['username']
     message=dbl.update_std(data,std)
     return (render_template('/student/home.html',message=message,data=dbl.get_stud_data(session['username'])))
  else:
    return (render_template('/student/home.html',data=dbl.get_stud_data(session['username'])))
@app.route('/search',methods=['GET','POST'])
def search():
  if request.method=='POST' and 'search' in request.form: 
     course=request.form.get('course')
     std=session['username']
     res1,flag,gen=db.get_course(course,session['username'])
     #return str(db.get_course(course,session['username']))
     if(flag==True):
      res=list(res1)
      y=db.get_min(session['username'])
      subj=list(db.get_pp(session['username']))
      for x in res1:
       if int(x[4])>int(y) and x[5] not in subj:
        res.remove(x)
      if(len(res)!=0):
        if(gen=='1'):
         return (render_template('/student/result.html',search=res,course=course,female=gen))
        else:
          return (render_template('/student/result.html',search=res,course=course))
      else:
        return (render_template('/student/result.html',result="No data found",course=course))
     else:
      return (render_template('/student/result.html',result=res1,course=course))

     #data=dbl.get_course(course,session['username'])
     #return str(data)
  else:
    return'no'
@app.route('/fb')
def fb():
  data=db.get_cmt()
  return render_template('admin/fb.html',data1=data)
@app.route('/del_cmt',methods=['GET','POST'])
def del_cmt():
  if request.method=='POST' and 'view' in request.form:
    name=request.form.get('view')
    data=db.del_cm(name)
    return(render_template('admin/fb.html',data1=db.get_cmt(),data=data))


@app.route('/feed',methods=['GET','POST'])
def feed():
  if request.method=='POST' and 'fb' in request.form:
    data1=request.form.get('mail')
    data2=request.form.get('fb')
    db.comment(data1,data2)
    return render_template('home.html')


@app.route('/incr',methods=['GET','POST'])
def incr():
  if request.method=='POST' and 'in' in request.form:
     data=request.form.get('in')
     course=request.form.get('course')
     std=session['username']
     #return str(course)
     (db.increment(data,session['username']))
     res1,flag,gen=db.get_course(course,session['username'])
     #return str(db.get_course(course,session['username']))
     if(flag==True):
      res=list(res1)
      y=db.get_min(session['username'])
      subj=list(db.get_pp(session['username']))
      for x in res1:
       if int(x[4])>int(y)and (x[5] not in subj or x[5]!='None'):
        res.remove(x)
      if(len(res)!=0):
        if(gen=='1'):
         return (render_template('/student/result.html',search=res,course=course,female=gen))
        else:
          return (render_template('/student/result.html',search=res,course=course))
      else:
        return (render_template('/student/result.html',result="No data found",course=course))
     else:
      return (render_template('/student/result.html',result=res1,course=course))

     #data=dbl.get_course(course,session['username'])
     #return str(data)
  else:
    return'no'
    
@app.route('/update_course',methods=['GET','POST'])
def update_course():
  if request.method=='POST' and 'update' in request.form: 
    data=request.form;
    id=request.form.get('id')
    message=db.update_crse(data,id)
    data=db.get_data(id)
    if data!='no':
     return(render_template('clge/edit.html',message=message,data=data))
    else:
      return id;



@app.route('/clge_update',methods=['GET','POST'])
def clge_update():
  if request.method=='POST' and 'update' in request.form: 
    data=request.form;
    message=db.update_clge(data,session['username'])
    return(render_template('clge/profile.html',message=message,data=db.clg_details(session['username'])))
  else:
    return(render_template('clge/profile.html',data=db.clg_details(session['username'])))
@app.route('/search1',methods=['GET','POST'])
def search1():
  if request.method=='POST' and 'pro' in request.form: 
     course=request.form.get('course')
     i=request.form.get('pro')
     std=session['username']
     if(i=='1'):
      res1,flag,gen=db.get_course(course,session['username'])
     else:
      res1,flag,gen=db.get_course1(course,session['username'])
     if(flag==True):
      
      res=list(res1)
      y=db.get_min(session['username'])
      subj=list(db.get_pp(session['username']))
      for x in res1:
       if int(x[4])>int(y) and x[5] not in subj:
        res.remove(x)
      if(len(res)!=0):
        if(gen=='1'):
         return (render_template('/student/result.html',search=res,course=course,female=gen,dist=i))
        else:
          return (render_template('/student/result.html',search=res,course=course,dist=i))
      else:
        return (render_template('/student/result.html',result="No data found",course=course,dist=i))
     else:
      return (render_template('/student/result.html',result=res1,course=course,dist=i))


     #data=dbl.get_course(course,session['username'])
     #return str(data)
     
  else:
    return'no'

@app.route('/student')
def shome():
  if 'username' in session:
   res=dbl.get_stud_data(session['username'])
   return(render_template('/student/home.html',data=res))
  else:
    return (render_template('login.html'))

@app.route('/logout')
def tes():
  session.clear();
  return render_template('home.html')
 
@app.route('/signup',methods=['GET','POST'])
def sign():
  if request.method=='POST' and 'name' in request.form:
    name=request.form.get('name')
    mail=request.form.get('email')
    pas=request.form.get('pass')
    mobile=request.form.get('mobile')
    flag=dbl.sign(name,mail,pas,mobile)
    message=flag[1]
    return (render_template('home.html',message=message))
  else:
    return'noy'
@app.route('/')
def index():
     return render_template('home.html')
@app.route('/view_clge',methods=['GET',"POST"])
def view_clge():
  if request.method=='POST' and 'view' in request.form:
    name=request.form.get('view')
    data=db.del_clge(name)
    return(render_template('admin/form.html',clges=dbl.get_clg(),data=data))



@app.route('/<string:folder_name>/<string:page_name>')
def load(folder_name,page_name):
  if(folder_name in ('admin','clge','student')):
   if('type' in session):
    if(folder_name=='admin'):
     if(session['type']=='admin'):
      if(page_name.endswith(".html")):
        return render_template(folder_name+"/"+page_name)
      else:
        return render_template(folder_name+"/"+page_name+".html")
     else:
      return(render_template('login.html'))
    elif(folder_name=='student'):
      if(session['type']=='student'):
       if(page_name.endswith(".html")):
        return render_template(folder_name+"/"+page_name)
       else:
        return render_template(folder_name+"/"+page_name+".html")
      else:
       return(render_template('login.html'))
    elif(folder_name=='clge'):
      if(session['type']=='clge'):
       if(page_name.endswith(".html")):
        return render_template(folder_name+"/"+page_name)
       else:
        return render_template(folder_name+"/"+page_name+".html")
      else:
        return(render_template('login.html'))
   else:
    return(render_template('login.html'))
  else:
      if(page_name.endswith(".html")):
        return render_template(folder_name+"/"+page_name)
      else:
        return render_template(folder_name+"/"+page_name+".html")
@app.route('/details',methods=['GET','POST'])
def details():
  if request.method=='POST' and 'get' in request.form:
    clge=request.form.get('get')
    course=request.form.get('course')
    r1=db.get_clge_details(clge)
    r2=db.get_course_details(course)
    return render_template('student/details',r1=r1,r2=r2)
@app.route('/<string:page_name>/')
def render_static(page_name):
  if(page_name.endswith(".html")):
    return render_template(page_name)
  else:
    return render_template("%s.html" %page_name)


if __name__=='__main__':
    app.secret_key='many random bytes'
    app.run(debug=True)
