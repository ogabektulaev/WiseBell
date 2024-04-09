import telepot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
bot_token = "5463450324:AAGUK8NX9f8R2315eXEMaGi8czdhxTXO5ts"

# Replace 'CHAT_ID' with the ID of the chat you want to send the message to
chat_id = "-2004754809"

# Message text
message_text = "Hello, this is a test message!"

bot = telepot.Bot(bot_token)

# Send the message
bot.sendMessage(-2004754809, message_text)
