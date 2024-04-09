# We used the telepot library to send messages via Telegram bot
import datetime
import telepot

bot = telepot.Bot("5463450324:AAGUK8NX9f8R2315eXEMaGi8czdhxTXO5ts")


# Function to send images
def send_image(image, person):
    bot.sendPhoto(
        -292128344,
        photo=open(image, "rb"),
        caption=datetime.datetime.now().strftime("%H:%M:%S")
        + "\n"
        + person
        + " is on the front door.",
    )


# Function to send message
def send_message(msg):
    bot.sendMessage(-292128344, msg)


# Function to send message with some text
def send_emotion_and_person_on_door(person_name, emotion):
    msg = "An unknown person is on the front door."
    if person_name != "Unknown":
        msg = person_name + " is on the front door " + emotion + "."
    send_message(msg)


# send_message("hello")
