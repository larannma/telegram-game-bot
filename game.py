import telebot

# Set up your bot token
bot_token = '6645362489:AAHgrHACXpsCpqcBHVRc2Oxv0LU6vrNQCaA'

# Create an instance of the bot
bot = telebot.TeleBot(bot_token)

# Set up the game short name
game_short_name = 'MilkyCow'

# Handler for when the user sends the "start" command
@bot.message_handler(commands=['start'])
def send_game(message):
    # Extract the user ID from the incoming message
    user_id = message.chat.id
    
    # Build the game URL
    game_url = f'https://larannma.github.io/telegram-game-bot/'
    
    # Send the game to the user
    bot.send_game(user_id, game_short_name, reply_markup=None, disable_notification=True, timeout=None)

# Handler for game queries
@bot.callback_query_handler(func=lambda query: query.game_short_name == game_short_name)
def handle_game_query(query):
    # Handle game-related queries if necessary
    # For example, you can handle different game actions or events here
    
    # Send a message to acknowledge the query
    bot.answer_callback_query(query.id, url='https://larannma.github.io/telegram-game-bot/')

# Start the bot
bot.polling()