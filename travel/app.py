

import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]

from flask import Flask, request, jsonify, render_template

app = Flask(__name__) 




from flask import Flask, render_template, request, jsonify
import datetime
from translate import Translator
import speech_recognition as sr
# ------------------------------------ FLASK APP -------------------------------------------------
import random
import string
#app = Flask(__name__)
# Global user context to maintain state across requests
user_context = {}

# Sample data for the chatbot 
data = {
    "Bengaluru": {
        "places": [
            {"name": "Bangalore Palace", "details": "Historical palace built in 1878."},
            {"name": "Lalbagh Botanical Garden", "details": "A 240-acre garden with diverse plant species."}
        ],
        "events": [
            {"name": "Tech Expo", "date": (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d'), "location": "Whitefield, Bengaluru"},
            {"name": "Music Fest", "date": (datetime.date.today() + datetime.timedelta(days=6)).strftime('%Y-%m-%d'), "location": "MG Road, Bengaluru"}
        ],
        "hotels": [
            {"name": "Hotel Paradise", "rent_per_day": 3000, "rating": 4.5, "location": "Koramangala, Bengaluru"},
            {"name": "Luxury Stay", "rent_per_day": 5000, "rating": 4.8, "location": "Indiranagar, Bengaluru"}
        ]
    },
    "bengaluru": {
        "places": [
            {"name": "Bangalore Palace", "details": "Historical palace built in 1878."},
            {"name": "Lalbagh Botanical Garden", "details": "A 240-acre garden with diverse plant species."}
        ],
        "events": [
            {"name": "Tech Expo", "date": (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d'), "location": "Whitefield, Bengaluru"},
            {"name": "Music Fest", "date": (datetime.date.today() + datetime.timedelta(days=6)).strftime('%Y-%m-%d'), "location": "MG Road, Bengaluru"}
        ],
        "hotels": [
            {"name": "Hotel Paradise", "rent_per_day": 3000, "rating": 4.5, "location": "Koramangala, Bengaluru"},
            {"name": "Luxury Stay", "rent_per_day": 5000, "rating": 4.8, "location": "Indiranagar, Bengaluru"}
        ]
    },
    "Mangalore": {
        "places": [
            {"name": "Panambur Beach", "details": "Popular beach with scenic views."},
            {"name": "St. Aloysius Chapel", "details": "Famous for its beautiful frescoes."}
        ],
        "events": [
            {"name": "Beach Carnival", "date": (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d'), "location": "Panambur Beach, Mangalore"},
            {"name": "Cultural Fest", "date": (datetime.date.today() + datetime.timedelta(days=8)).strftime('%Y-%m-%d'), "location": "Kadri Park, Mangalore"}
        ],
        "hotels": [
            {"name": "Coastal Comfort", "rent_per_day": 2500, "rating": 4.2, "location": "City Center, Mangalore"},
            {"name": "Sea View Resort", "rent_per_day": 4000, "rating": 4.6, "location": "Tannirbhavi, Mangalore"}
        ]
    },
     "mangalore": {
        "places": [
            {"name": "Panambur Beach", "details": "Popular beach with scenic views."},
            {"name": "St. Aloysius Chapel", "details": "Famous for its beautiful frescoes."}
        ],
        "events": [
            {"name": "Beach Carnival", "date": (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d'), "location": "Panambur Beach, Mangalore"},
            {"name": "Cultural Fest", "date": (datetime.date.today() + datetime.timedelta(days=8)).strftime('%Y-%m-%d'), "location": "Kadri Park, Mangalore"}
        ],
        "hotels": [
            {"name": "Coastal Comfort", "rent_per_day": 2500, "rating": 4.2, "location": "City Center, Mangalore"},
            {"name": "Sea View Resort", "rent_per_day": 4000, "rating": 4.6, "location": "Tannirbhavi, Mangalore"}
        ]
    },
    "Mysore": {
        "places": [
            {"name": "Mysore Palace", "details": "A historical palace and royal residence."},
            {"name": "Brindavan Gardens", "details": "Famous for its symmetric design and fountains."}
        ],
        "events": [
            {"name": "Art Fair", "date": (datetime.date.today() + datetime.timedelta(days=9)).strftime('%Y-%m-%d'), "location": "Mysore Palace, Mysore"},
            {"name": "Yoga Retreat", "date": (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d'), "location": "KRS, Mysore"}
        ],
        "hotels": [
            {"name": "Royal Heritage", "rent_per_day": 3500, "rating": 4.7, "location": "Chamundi Hill Road, Mysore"},
            {"name": "Green Valley Resort", "rent_per_day": 4500, "rating": 4.8, "location": "Nanjangud Road, Mysore"}
        ]
    },
    "mysore": {
        "places": [
            {"name": "Mysore Palace", "details": "A historical palace and royal residence."},
            {"name": "Brindavan Gardens", "details": "Famous for its symmetric design and fountains."}
        ],
        "events": [
            {"name": "Art Fair", "date": (datetime.date.today() + datetime.timedelta(days=9)).strftime('%Y-%m-%d'), "location": "Mysore Palace, Mysore"},
            {"name": "Yoga Retreat", "date": (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d'), "location": "KRS, Mysore"}
        ],
        "hotels": [
            {"name": "Royal Heritage", "rent_per_day": 3500, "rating": 4.7, "location": "Chamundi Hill Road, Mysore"},
            {"name": "Green Valley Resort", "rent_per_day": 4500, "rating": 4.8, "location": "Nanjangud Road, Mysore"}
        ]
    }
}

# Function to translate text into different languages
def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    return translator.translate(text)

@app.route('/')
def home():
    return render_template('login44.html') 
@app.route('/chatbot2')
def chatbot2():
    return render_template('index.html')


@app.route('/bengaluru')
def bengaluru():
    return render_template('bengaluru.html') 



@app.route('/bengaluru_places')
def bengaluru_places():
    return render_template('bengaluru_places.html') 



@app.route('/mysuru')
def mysuru():
    return render_template('mysuru.html') 



@app.route('/mysuru_places')
def mysuru_places():
    return render_template('mysuru_places.html') 



@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    # Save the text to a pickle file
    text = str(int_features3[0])
    with open('smartai_text.pkl', 'wb') as file:
        pickle.dump(text, file)


    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
  #  print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    #print(password_list)
    #print(gmail_list.index(logu))
    #print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index44.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                               

        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')
@app.route('/chat', methods=['POST'])
def chat():
    global user_context  # Ensure we're using the global user_context

    user_message =request.json.get("message").strip().lower()
    print("The user message is:", user_message)
    
    response = ""
    user_id = request.remote_addr  # Using user's IP as a unique identifier for simplicity

    # Initialize user context if not already present
    if user_id not in user_context:
        user_context[user_id] = {"city": None}

    context = user_context[user_id]

    print("Current context:", context)
    
    if "reset" in user_message or "other cities" in user_message or "restart" in user_message:
        context["city"] = None
        response = "Let's start over! Please select a city: Bengaluru, Mangalore, Mysore."
    elif context["city"] is None:
        for city in data.keys():
            if city.lower() in user_message:
                context["city"] = city
                response = f"You selected {city}. What would you like to know? (Places, Events, Hotels)"
                break
        else:
            response = "I'm here to help! Please select a city: Bengaluru, Mangalore, Mysore."
    else:
        city = context["city"]
        if "places" in user_message:
            places = data[city]["places"]
            response = "Here are some places to visit:\n" + "\n".join([f"{p['name']}: {p['details']}" for p in places])
        elif "events" in user_message:
            events = data[city]["events"]
            response = "Upcoming events:\n" + "\n".join([f"{e['name']} on {e['date']} at {e['location']}" for e in events])
        elif "hotels" in user_message:
            hotels = data[city]["hotels"]
            response = "Here are some hotels:\n" + "\n".join([f"{h['name']}: ₹{h['rent_per_day']}/day, Rating: {h['rating']}, Location: {h['location']}" for h in hotels])
        else:
            response = f"What would you like to know about {city}? (Places, Events, Hotels)"

    # Translate the response to different languages
    kannada_translation = translate_text(response, "kn")
    hindi_translation = translate_text(response, "hi")
    tamil_translation = translate_text(response, "ta")
    malayalam_translation = translate_text(response, "ml")
    from gtts import gTTS
    from pydub import AudioSegment
    import pygame
    import os

    text = str(response)
    language = 'en'

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio in a file
        tts.save("output.mp3")
        print("Audio file saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Play the saved audio file using pygame
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value as needed

        # Close the mixer
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error playing audio: {e}")

    return jsonify({
        'response': response,
        'kannada_translation': kannada_translation,
        'hindi_translation': hindi_translation,
        'tamil_translation': tamil_translation,
        'malayalam_translation': malayalam_translation
    })                     

def speech_to_text_for_5_seconds():
        # Initialize recognizer
        recognizer = sr.Recognizer()
        
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
            
            print("Listening for 5 seconds. Please speak...")
            try:
                # Listen to the microphone for 5 seconds
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognize speech using Google Web Speech API
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"Recognized Text: {text}")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand the audio.")
                except sr.RequestError as e:
                    print(f"Request error from Google Speech Recognition: {e}")
            
            except sr.WaitTimeoutError:
                print("No speech detected within the timeout period.")

        return     text  

p="None"    
@app.route('/chat2',methods=['POST','GET'])

@app.route('/chat2', methods=['POST'])
def chat2():
    global user_context  # Ensure we're using the global user_context

    user_message = str(speech_to_text_for_5_seconds()).strip().lower()
    print("The user message is:", user_message)
    
    response = ""
    user_id = request.remote_addr  # Using user's IP as a unique identifier for simplicity

    # Initialize user context if not already present
    if user_id not in user_context:
        user_context[user_id] = {"city": None}

    context = user_context[user_id]

    print("Current context:", context)
    
    if "reset" in user_message or "other cities" in user_message or "restart" in user_message:
        context["city"] = None
        response = "Let's start over! Please select a city: Bengaluru, Mangalore, Mysore."
    elif context["city"] is None:
        for city in data.keys():
            if city.lower() in user_message:
                context["city"] = city
                response = f"You selected {city}. What would you like to know? (Places, Events, Hotels)"
                break
        else:
            response = "I'm here to help! Please select a city: Bengaluru, Mangalore, Mysore."
    else:
        city = context["city"]
        if "places" in user_message:
            places = data[city]["places"]
            response = "Here are some places to visit:\n" + "\n".join([f"{p['name']}: {p['details']}" for p in places])
        elif "events" in user_message:
            events = data[city]["events"]
            response = "Upcoming events:\n" + "\n".join([f"{e['name']} on {e['date']} at {e['location']}" for e in events])
        elif "hotels" in user_message:
            hotels = data[city]["hotels"]
            response = "Here are some hotels:\n" + "\n".join([f"{h['name']}: ₹{h['rent_per_day']}/day, Rating: {h['rating']}, Location: {h['location']}" for h in hotels])
        else:
            response = f"What would you like to know about {city}? (Places, Events, Hotels)"

    # Translate the response to different languages
    kannada_translation = translate_text(response, "kn")
    hindi_translation = translate_text(response, "hi")
    tamil_translation = translate_text(response, "ta")
    malayalam_translation = translate_text(response, "ml")
    from gtts import gTTS
    from pydub import AudioSegment
    import pygame
    import os

    text = str(response)
    language = 'en'

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio in a file
        tts.save("output.mp3")
        print("Audio file saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Play the saved audio file using pygame
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value as needed

        # Close the mixer
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error playing audio: {e}")

    return jsonify({
        'response': response,
        'kannada_translation': kannada_translation,
        'hindi_translation': hindi_translation,
        'tamil_translation': tamil_translation,
        'malayalam_translation': malayalam_translation
    })                     


if __name__ == "__main__":
    app.run(debug=True)
