import smtplib
import speech_recognition as sr
import pyttsx3 as tts3
listener =sr.Recognizer()
engine = tts3.init()
def talk(text):
   engine.say(text)
   engine.runAndWait()
def get_info():
   try:
      with sr.Microphone() as source:
         print("listening--")
         voice = listener.listen(source)
         info = listener.recognize_google(voice)
         print(info)
   except:
      pass
def send_email():
   sender = 'sravyakommisetti@gmail.com'
   receivers = ['deepikakommisetti@gmail.com']

   message = """This is a test e-mail message."""

   try:
      smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
      smtpObj.starttls()
      smtpObj.login('sravyakommisetti@gmail.com', '9704624444')
      smtpObj.sendmail(sender, receivers, message)
      print("Successfully sent email")
   except (Exception):
      print("Error: unable to send email")
def starting():
   talk("to whom you want to send the gmail")
starting()
