import pyttsx3
import wikipedia
import datetime
import webbrowser
import subprocess
import mysql.connector
import time
from selenium import webdriver
def getsimilar(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def aloud(x):
  engine.say(x)
  engine.runAndWait() 

def aloudp(x):
  print(x)
  engine.say(x)
  engine.runAndWait() 

cont= "yes"


# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 
engine.say('Hello Ayush. How may I help you?')
# run and wait method, it processes the voice commands.  
engine.runAndWait() 

def assistant():
 Query = input("Enter Command:") 
 print(Query)
 Query.lower()
 if 'wiki' in Query:
   engine.say("Type your search")
   engine.runAndWait() 
   sQuery = input("Enter Search:") 
   print(sQuery)
   try:
     result = wikipedia.summary(sQuery, sentences=2) 
     print(result)
     engine.say("According to wikipedia," + result)
     engine.runAndWait() 
   except:
     print("Sorry, I ran into an error.")
     engine.say("I'm sorry but I ran into an error.")
     engine.runAndWait()
 elif 'time'==Query:
   strTime = datetime.datetime.now().strftime("%H:%M")    
   engine.say("The time is " + strTime)
   print(strTime)
   engine.runAndWait()
 elif 'web' in Query:
   engine.say("Type the website's URL")
   engine.runAndWait() 
   wQuery = input("Enter full URL:") 
   print(wQuery)
   engine.say("Opening " + wQuery) 
   webbrowser.open(wQuery)
 elif 'youtube' in Query:
   engine.say("Type the search term")
   engine.runAndWait() 
   yQuery = input("Type the search term") 
   print(yQuery)
   engine.say("Searching " + yQuery) 
   webbrowser.open("https://www.youtube.com/results?search_query=" + yQuery) 
 elif Query=='remember':
   engine.say("Yes, what should I remember for you?")
   engine.runAndWait() 
   rQuery = input("Type what you want me to remember:") 
   print(rQuery)
   mydb = mysql.connector.connect(host="localhost", user="root", password="", database="assistantdb")
   mycursor = mydb.cursor()
   sql = "INSERT INTO remembers (text) VALUES (%s)"
   val = (rQuery,)
   mycursor.execute(sql, val)
   mydb.commit()
   engine.say("Ok. I will remember this.")
   engine.runAndWait()
 elif 'what did i ask' in Query and 'remember' in Query:
   mydb = mysql.connector.connect(host="localhost", user="root", password="", database="assistantdb")
   engine.say("Here's everything that you asked me to remember:-")
   engine.runAndWait()
   mycursor = mydb.cursor()
   mycursor.execute("SELECT text FROM remembers")
   myresult = mycursor.fetchall()
   for row in myresult:
     print(row[0] + "\n")
   if (mydb.is_connected()):
     mydb.close()
     mycursor.close()
 elif Query=="hi":
   print("Hi. How may I help you?")
   engine.say('Hi. How may I help you?')  
   engine.runAndWait()
 
 elif 'weather' in Query:
   driver= webdriver.Chrome(r'C:\Users\YOUR USERNAME\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\site-packages\selenium\chromedriver.exe')  # Optional argument, if not specified will search path.
   driver.get("https://www.google.com/search?q=weather") # add your computer's username above
   time.sleep(1)
   element = driver.find_element_by_id("wob_tm")
   weather= element.text
   print(weather)
   engine.say('It is ' + weather + 'degree Celsius now.') 
   engine.runAndWait()
   time.sleep(2) # Let the user actually see something!
   driver.quit()

 elif "time table" in Query:
   print("Checking your class time table.")
   x = datetime.datetime.now()
   day= x.strftime("%A")
   hour= x.hour
   def timetabler(classes, times):
       c= len(times)
       for i in range(c):
         if hour < times[i]:
           if 12 <= times[i]: # formats to a.m. and p.m.
             print("Next class is " + classes[i] + " at " + str(times[i] - 12) + " p.m.")
             aloud("Next class is " + classes[i] + " at " + str(times[i] - 12) + " p.m.")
             break
           elif hour < 12:
             print("Next class is " + classes[i] + " at " + str(times[i]) + " a.m.")
             aloud("Next class is " + classes[i] + " at " + str(times[i]) + " a.m.")
             break
            
         elif times[c - 1] < hour:
           print("No more classes today.")
           aloud("No more classes today")
           break
   
   if day=='Monday':
     classes= ["MT", "Maths", "English", "Chemistry"]
     times= [8, 10, 11, 15]
     timetabler(classes,times)
   elif day=='Tuesday':
     classes= ["CT period", "Geography", "Physics", "Hindi"]
     times= [8.45, 9, 10, 15]
     timetabler(classes, times)
   elif day=='Wednesday':
     classes= ["PT", "CT period", "Biology", "History", "Chemistry", "Computer"]
     times= [8, 8.45, 10, 11, 12, 15]
     timetabler(classes, times)
   elif day=='Thursday':
     classes= [" a Monday Test", "Maths", "History", "Computer"]
     times= [8, 10, 11, 15]
     timetabler(classes, times)
   elif day=='Friday':
     classes= ["CT period", "Geography", "Physics", "Hindi", "Biology"]
     times= [8.45, 9, 10, 11, 13]
     timetabler(classes, times)
   elif day=='Saturday' or day=='Sunday':
     print("Today is a holiday")
     aloud("Today is a holiday.")
 elif Query=='what can u do' or Query=='what can you do':
  aloudp("I can open wikipedia, tell you your time table, tell weather, remember things, search YouTube and open a website.")
 elif Query=='what is your name' or Query=='what is ur name' or Query=='who are u' or Query=='who are you':
  aloudp("I am Spark. I am always glad to asist you.")
 elif Query=='who created you' or Query=='who created u' or Query=='who made u' or Query=='who made you':
   aloudp("I was created By Ayush. I live in a computer currently.")
 elif 'exit'==Query:
   print("exited")
   global cont
   cont= "no"


#make a teach mode where you teach assistant questions and answers
# create a column unique_token_words which contains the token words from question
# the assistant searches for keywords in the question and then answers
#what are my events for today?
# today time table - make it tell like "u hv a class in 10 mins"
# show weather, news using selenium

while cont=="yes":
  if cont=="yes":
   assistant()
