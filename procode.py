from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
import PIL.Image
import math, random 
import smtplib
import shutil
import os
import requests
import pandas
from bs4 import BeautifulSoup
import webbrowser
import socket
import random
import re


hostname="localhost"
dbuser="root"
dbpass=""
dbname="firstdatabase"
connection=pymysql.connect(host="localhost", user="root", password="", database="firstdatabase")

window=Tk()
window.title("Movie Finder")
window.geometry("1280x640")
f=('Lucida Fax', 15)
A=('Georgia', 50 )
B=('Lucida Fax', 10)
c=('Lucida Fax',25)

canvas=Canvas(window, width=1280, height=640)
canvas.pack()
img=Image.open("0mm.jpg")
canvas.image=ImageTk.PhotoImage(img)
canvas.create_image(0,0, image= canvas.image, anchor='nw')



def registration():
	signup=Tk()
	signup.geometry('1280x640')
	signup.title("registration")
	canvas=Canvas(signup, width=1280, height=640)
	canvas.pack()
	canvas4=Canvas(signup, width=1280, height=640)
	canvas4.pack()
	img4=Image.open("4mm.jpg")
	canvas4.image=ImageTk.PhotoImage(img4)
	canvas.create_image(0,0, image= canvas4.image, anchor='nw')

	name2=StringVar()
	global username1
	lbl2=Label(signup,text="Enter your username:", font=f,bg="#161616",fg='white' )
	lbl2.place(x=250,y=150)
	username1=Entry(signup,font=f,textvariable=name2)
	username1.place(x=540,y=152)


	name3=StringVar()
	global email1	
	lbl4=Label(signup,text="Enter your Email Address:", font=f,bg="#161616",fg="white")
	lbl4.place(x=250,y=210)
	email1=Entry(signup,font=f,textvariable=name3)
	email1.place(x=540,y=210)


	name4=StringVar()
	global password1 
	lbl6=Label(signup,text="Enter password again:",font=f,bg="#161616",fg="white")
	lbl6.place(x=250,y=350)
	password1=Entry(signup,font=f,textvariable=name4,show="*")
	password1.place(x=540,y=280)
	
	name5=StringVar()
	global repassword1
	lbl4=Label(signup,font=f,text="Enter your password:",bg="#161616",fg="white")
	lbl4.place(x=250,y=280)
	repassword1=Entry(signup,font=f,textvariable=name5)
	repassword1.place(x=540,y=350)
	
	
	

	def signin():
		global username11
		global email11
		global password11
		global repassword11

		username11=username1.get()
		email11=email1.get()
		password11=password1.get()
		repassword11=repassword1.get()		
		if re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",email11)  and password11==repassword11:
			str="insert into user(USERNAME,EMAILID,PASSWORD,REPASSWORD) values('"+username11+"','"+email11+"','"+password11+"','"+repassword11+"')"	
			cursor=connection.cursor()
			res=cursor.execute(str)
			connection.commit()
			print(res)
			connection.close()
			messagebox.showwarning("signup","WELCOME !!!")

			

		else:
			messagebox.showwarning("email","Invalid Email Address or password do not match")

			
		



	btn3=Button(signup,text="SUBMIT", font=f,bg="#161616",fg="white",command=signin)
	btn3.place(x=350,y=400,width=330,height=30)


btn2=Button(window, text="Sign Up",bg='black', font=f,fg='white' ,command=registration)
btn2.place(x=320,y=570, width=200, height=45)

	


canvas3=Canvas(window, width=100, height=100)
canvas3.pack()
img3=Image.open("14.png")
canvas3.image=ImageTk.PhotoImage(img3)
canvas.create_image(280,250, image= canvas3.image, anchor='nw')

def frontpage (event):
	name0.set("")
	name1.set("")

name0=StringVar()
name1=StringVar()

name0.set("Enter Username: ")
name1.set("Enter Password: ")

usernameinput=Entry(window, textvariable=name0, font=f)
passwordinput=Entry(window, textvariable=name1, font=f)

usernameinput.bind("<FocusIn>", frontpage)

usernameinput.place(x=150,y=370,width=350,height=35)
passwordinput.place(x=150,y=450,width=350,height=35)
lbl2=Label(window, fg='#ebe6e6')
lbl3=Label(window)

lbl2.pack()
lbl3.pack()
def loginpage():


	cursor=connection.cursor()
	cursor.execute("select *from user")
	row=cursor.fetchall()

	validusername=False
	for x in row:
		username=x[1]
		password=x[3]	
		if username==usernameinput.get():
			if password==passwordinput.get():
				window.destroy()
				newwindow()
				validusername=True
				break
			else:
				print("invalid password")
				break
		else:
			continue			
	
	if validusername==False:
		messagebox.showwarning("login", "Invalid userid, password")
			

btn=Button(window, text="SUBMIT", bg='black', font=f,fg='white' ,command=loginpage)
btn.place(x=190,y=520, width=250, height=45)

def forgetp ():
	window.destroy()
	forgetp=Tk()
	forgetp.geometry('1280x640')
	canvas=Canvas(forgetp, width=1280, height=640)
	canvas.pack()
	canvas5=Canvas(forgetp, width=1280, height=640)
	canvas5.pack()
	img5=Image.open("4mm.jpg")
	canvas5.image=ImageTk.PhotoImage(img5)
	canvas.create_image(0,0, image= canvas5.image, anchor='nw')

	lbl=Label(forgetp,text='Enter your Email Address :-', font=c,bg='#161616',fg='white')
	lbl.place(x=310,y=200)
	name8=StringVar()
	global mailid	
	mailid=Entry(forgetp,textvariable=name8, font=f)
	mailid.place(x=360,y=250, width=330, height=35)


	lbl7=Label(forgetp,text="Enter OTP here: ",font=c,bg="#161616",fg="white")
	lbl7.place(x=310,y=400)




	def maingame():
		cursor=connection.cursor()
		cursor.execute("select *from user")
		row=cursor.fetchall()
		validusername=False
		for x in row:
			email=x[2]
			
			if email==mailid.get():
				mailtosend=str(mailid.get())

				validusername=True
				def generateOTP():

		
					print("Here")    
					def otpgeneration():			
						digits ="0123456789"
						OTP = ""
						for i in range(4) : 
							OTP+=digits[math.floor(random.random() * 10)]
						return OTP
					
					print("otp is")
					smtp=smtplib.SMTP('smtp.gmail.com',587)
					smtp.ehlo()
					smtp.starttls() 
					smtp.ehlo()
					smtp.login("kunaldsn@gmail.com","Kunal7507")
					subject="OTP le khush rhe"
					global body
					body=(otpgeneration())    	
					msg='subject:'+subject+'\n\n'+body
					smtp.sendmail("kunaldsn@gmail.com", mailtosend ,msg)
				generateOTP()
				break	
			else:
				continue			
	
		if validusername==False:
			messagebox.showwarning("password","you need to signin first!!!!")

	btn5=Button(forgetp,text='Get OTP', bg='#161616',fg='white', font=f, command=maingame)
	btn5.place(x=360,y=300,width=200,height=45)		

	name10=StringVar()
	global otpenter	
	otpenter=Entry(forgetp,textvariable=name10, font=f)
	otpenter.place(x=360,y=450, width=330, height=35)
	
	def newotp():
		global otpenter			
		global body
		otpcheck=False
		if body==otpenter.get():
			otpcheck=True
			print("sahi chal rha hai")
			change()

		else:
			print("Enter correct OTP")	

	btn6=Button(forgetp,text="SUBMIT",bg="#161616",fg='white',font=f,command=newotp)
	btn6.place(x=360,y=500,width=200,height=45)		
   
btn4=Button(window, text="Forget password", font=f, bg='#000000', fg='white',command=forgetp)
btn4.place(x=110,y=570, width=200, height=45)


			
		
def change():
	update=Tk()
	update.title("update")
	update.geometry("1280x640")
	canvas=Canvas(update, width=1280, height=640)
	canvas.pack()
	canvas7=Canvas(update, width=1280, height=640)
	canvas7.pack()
	img7=Image.open("4mm.jpg")
	canvas7.image=ImageTk.PhotoImage(img7)
	canvas.create_image(0,0, image= canvas7.image, anchor='nw')

























def newwindow():
	window2=Tk()
	window2.geometry("1920x1080")
	title=[]
	imdb=[]
	poster=[]
	actors=[]
	votes=[]
	year=[]
	rate=[]

	newlist=[]
	newrate=[]
	newvote=[]

	info=''
	api_address0='http://www.omdbapi.com/?apikey=1ce5655c&type=movie&t='

	def poster_show():
		global img
		a=PIL.Image.open('local_image1.jpg')  
		img=ImageTk.PhotoImage(a)  
		canvas.create_image(20, 20, anchor=NW,image=img)







	def d(event):
		sv=StringVar()
		print(event)


		url1=api_address0+event
		json_data0=requests.get(url1).json()
		print(json_data0)

		o=json_data0['Title']
		oo=json_data0['Year']
		ooo=json_data0['Plot']
		image_url=json_data0['Poster']

		q1=ooo[0:80]
		q2=ooo[80:160]
		q3=ooo[160:-1]

		print(q1)
		print(q2)
		print(q3)

		O=q1+"\n"+q2+"\n"+q3
		print(O)


	
		image_url=json_data0['Poster']
		ib3.grid(column=0,row=0)
		ib2.grid(column=0,row=0)
		ib.grid(column=0,row=0)
		ib1.grid(column=0,row=0)
		ib.config(text=o)
		ib1.config(text=oo)
		ib3.config(text=O)


	

	
		resp = requests.get(image_url, stream=True)
		
		local_file = open('local_image1.jpg', 'wb')

		resp.raw.decode_content = True
		
		shutil.copyfileobj(resp.raw, local_file)
		poster_show()


	def e(event):
		print(event)
		



		url0=api_address0+event
		json_data0=requests.get(url0).json()
		print(json_data0)


		url1=api_address0+event
		json_data0=requests.get(url1).json()
		print(json_data0)

		o=json_data0['Title']
		oo=json_data0['Year']
		ooo=json_data0['Plot']

		print(ooo)

		q1=ooo[0:80]
		q2=ooo[80:160]
		q3=ooo[160:-1]

		print(q1)
		print(q2)
		print(q3)

		O=q1+"\n"+q2+"\n"+q3
		print(O)


		
		image_url=json_data0['Poster']
		ib3.grid(column=0,row=0)
		ib2.grid(column=0,row=0)
		ib.grid(column=0,row=0)
		ib1.grid(column=0,row=0)
		ib.config(text=o)
		ib1.config(text=oo)
		ib3.config(text=O)


		

		
		resp = requests.get(image_url, stream=True)
		
		local_file = open('local_image1.jpg', 'wb')

		resp.raw.decode_content = True
		
		shutil.copyfileobj(resp.raw, local_file)
		poster_show()


	def ww():
		sv2=StringVar()
		sv2.set("SORTED BY RATING")
		drop2=OptionMenu(labelframe3,sv2,*sort_1,command=d)
		drop2.config(width=90,bg="#161616",fg="white",font=B)

		drop2.place(x=280,y=165)




	def w():
		






		sv2=StringVar()
		sv2.set("SORTED BY YEAR")
		drop2=OptionMenu(labelframe3,sv2,*sort,command=d)
		drop2.config(width=90,bg="#161616",fg="white",font=B)

		drop2.place(x=280,y=165)

	def www():

		sv2=StringVar()
		sv2.set("SORTED BY VOTES")
		drop2=OptionMenu(labelframe3,sv2,*sort_3,command=d)
		drop2.config(width=90,bg="#161616",fg="white",font=B)

		drop2.place(x=280,y=165)


	def selection(event):
		print(event)

		if event=="by year":
			w()
		if event=="by rating":
			ww()
		if event=="by votes":
			www()		






	def c():

		global sort
		global sort_1
		global sort_3

		sv=StringVar()
		sv.set(title[0])
		drop=OptionMenu(labelframe3,sv,*title,command=d)
		drop.config(width=90,bg="#161616",fg="white",font=B)

		drop.place(x=280,y=165)

		
		sv=StringVar()

		#sv.set(title[0])
		#drop=OptionMenu(labelframe3,sv,*title,command=d)
		#drop.config(width=90)

		#drop.place(x=280,y=165)
		opts=["by year","by rating"]


		
		
		api_address1='http://www.omdbapi.com/?apikey=1ce5655c&type=movie&i='
		for u in imdb:
			url1=api_address1+u
			json_data1=requests.get(url1).json()
			#print(json_data1)
			print("")
			#actors.append(json_data1["Actors"])
			votes.append(json_data1["imdbVotes"])
			year.append(json_data1["Year"])
			rate.append(json_data1["imdbRating"])
			#poster.append(json_data1['Poster'])

			
			if float(json_data1["imdbRating"])>float(8):
				newlist.append(json_data1["Title"])
				newvote.append(json_data1["imdbVotes"])
				newrate.append(json_data1["imdbRating"])


			if u not in imdb:
				continue
		print(newlist)
		print(newrate)
		print(newvote)	

				


				

		info=pandas.DataFrame({'TITLE':title,'ID':imdb,'YEAR':year,'VOTES':votes,
			'RATING':rate})
		print(info)
		print("")	

		
		print("")		
		#print(actors)
		print("")
		#print(year)


		info_2 = info.sort_values(by='YEAR')
		print(info_2)


		sort=info_2['TITLE'].values.tolist()
		print(sort)

		info_3=info.sort_values(by='RATING',ascending=False)
		print(info_3)

		sort_1=info_3['TITLE'].values.tolist()
		print(sort_1)


		if len(newlist)!=0:
			opts.append("by votes")
			info_4=pandas.DataFrame({"TITLE":newlist,"RATING":newrate,"VOTES":newvote})
			info_5=info_4.sort_values(by='VOTES',ascending=False)
			print(info_5)
			sort_3=info_5['TITLE'].values.tolist()

		
	 	


		sv9=StringVar()
		sv9.set("SORT BY")
		drop9=OptionMenu(labelframe3,sv9,*opts,command=selection)
		drop9.config(width=20,bg="#161616",fg="white")

		drop9.place(x=120,y=57)






				

	def s():
		
		title.clear()
		imdb.clear()
		poster.clear()
		actors.clear()
		votes.clear()
		year.clear()
		rate.clear()
		newlist.clear()
		newrate.clear()
		newvote.clear()
		
		



		print(name.get())
		api_address='http://www.omdbapi.com/?apikey=1ce5655c&type=movie&plot=long&s='
		url=api_address+name.get()
		json_data=requests.get(url).json()
		print(json_data)
		#print(json_data)
		a=json_data['Search']


		




		for i in a:
			aa=i['Title']
			#print(aa)
			title.append(i['Title'])
			imdb.append(i['imdbID'])
			poster.append(i['Poster'])

			if i not in a:
				break
		#print(title)
		#print(poster)
		#info={'movie':title,'ids':imdb}
		#df=pandas.DataFrame(info)
		#print(df)

		c()	
		
		




	  

	#window = Tk()
	#window.title("MOVIE FINDER")
	#window.geometry('1980x1080')

	# Create a panedwindow
	pane = PanedWindow(window2, orient=HORIZONTAL)
	pane.pack()

	# Add label widgets on panedwindow
	labelframe1 = LabelFrame(pane,width=300,height=1080)  
	pane.add(labelframe1)


	labelframe2 = LabelFrame(pane,width=1680,height=1080,bg='black')  
	pane.add(labelframe2) 

	labelframe3=LabelFrame(labelframe2,width=1680,height=200,bg='#b3050f')
	labelframe3.place(x=0,y=0)


	#######
	#labelframe4=LabelFrame(labelframe2,height=400,width=400,bd=5).place(x=0,y=300)


		  
	canvas = Canvas(labelframe2, width = 400, height = 500,bg='black')  
	canvas.place(x=50,y=300)


	####################################labels
	##title
	labelframe5=LabelFrame(labelframe2,height=50,width=300,bd=10,text='title',bg='black')
	labelframe5.place(x=650,y=300)

	rr="star war"

	ib=Label(labelframe5,bg='black',font=B,fg="white")





	###year
	labelframe6=LabelFrame(labelframe2,height=50,width=150,bd=10,bg='black')
	labelframe6.place(x=650,y=400)

	ib1=Label(labelframe6,bg='black',font=B,fg="white")
	ib1.grid(column=0,row=0)

	######rate
	labelframe7=LabelFrame(labelframe2,height=50,width=100,bd=10,bg='black')
	labelframe7.place(x=850,y=400)


	ib2=Label(labelframe7,bg='black',font=B,fg="white")


	######plot
	labelframe8=LabelFrame(labelframe2,height=200,width=500,bd=10,bg='black')
	labelframe8.place(x=550,y=500)


	ib3=Label(labelframe8,bg='black',font=B,fg="white")


	###SEarch
	name=StringVar()
	name.set("")
	inp=Entry(labelframe3,textvariable=name,font=f)
	inp.config(width=45)
	inp.place(x=300,y=60)

	b1=Button(labelframe3,text="Search",height=2,width=6,command=s,relief='flat', bg="#161616",fg="white")
	b1.place(x=920,y=60,width=80,height=30)

	###new release###

	url0="https://www.imdb.com/chart/boxoffice/"
	r=requests.get(url0)
	soup=BeautifulSoup(r.content,'html5lib')

	#print(soup.prettify())

	table=soup.findAll('td',attrs={'class':'posterColumn'})

	#print(table)

	img=[]
	poster=[]

	for row in table:
		img.append(row.img["alt"])
		#poster.append(row.img["src"])
		if row not in table:
			break


	#print(img)
	sv1=StringVar()
	sv1.set("NEW RELEASE")
	drop1=OptionMenu(labelframe1,sv1,*img,command=e)
	drop1.config(width=30,bg="#161616",fg="white",font=B)

	drop1.place(x=50,y=500)

	########################
	#global img00
	#canvas00 = Canvas(labelframe1, width = 300, height = 300,bg='black')  
	#canvas00.place(x=0,y=0)

	#a00=PIL.Image.open('logo.png')  
	#img00=ImageTk.PhotoImage(a00)  
	#canvas00.create_image(0, 0, anchor=NW,image=img00)





	 

window.mainloop()



	




































































































































































