import telebot
from telebot import types
import json

# Basic data
BOT_PASSWORD = 'poolooshk'
BOT_TOKEN = '5072829364:AAEUipc1q03LzshPw2_dTQ0Wlnp6TvN5Rps'
MAX_CLINENT = 15

# Xray class
class XRayConfiguration:
    def __init__(self) -> None:
        self.config_path = ''
        self.clients = {}
    
    def user_list(self) -> list:
        return [i for i in range(16)]

    def add_user(self, name) -> bool:
        pass

    def remove_user(self, name) -> bool:
        pass


# Define the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Function to check if the user is authorized
def is_authorized(id):
    with open('authorized.json', 'r') as f:
        data = json.load(f)
        if str(id) in list(data.keys()):
            return True
        return False
    

# Function to handle the "/start" command
@bot.message_handler(commands=['start'])
def start(message):
    # Check if the user is authorized
    with open('authorized.json', 'r') as f:
        data = json.load(f)
        if str(message.chat.id) in data.keys():
            bot.reply_to(message, 'Welcome to the bot!')
            return
    try:
        if (message.text).split(' ')[1] == BOT_PASSWORD:
            data[message.chat.id] = message.from_user.id
            with open('authorized.json', 'w') as f:
                json.dump(data, f)
            bot.reply_to(message, 'Welcome to the bot!')
            return
        bot.reply_to(message, 'You are not authorized to use this bot.')
    except IndexError:
        bot.reply_to(message, 'Please Enter password with /strat')

# Function to handle the "Add User" option
@bot.message_handler(commands=['add_user'])
def add_user(message):
    # Check if the user is authorized
    if not is_authorized(message.chat.id):
        bot.reply_to(message, 'You are not authorized to use this bot.')
        return
    # Max user check
    cl = XRayConfiguration()
    if len(cl.user_list()) > MAX_CLINENT:
        bot.reply_to(message, 'The capacity of this server has been completed!')
        return
    # Ask the user for the name of the new user
    bot.reply_to(message, 'Please enter the name of the new user:')
    # Wait for the user to enter the name of the new user
    @bot.message_handler(func=lambda message: True)
    def get_name(message):
        # Ask the user to confirm the name of the new user
        keyboard = types.InlineKeyboardMarkup()
        confirm_button = types.InlineKeyboardButton('Yes', callback_data=f'add_user_{message.text}')
        cancel_button = types.InlineKeyboardButton('No', callback_data='cancel')
        keyboard.add(confirm_button, cancel_button)
        bot.reply_to(message, f'Are you sure you want to add {message.text}?', reply_markup=keyboard)

        # Handle the button clicks
        @bot.callback_query_handler(func=lambda call: call.data.startswith('add_user_') or call.data == 'cancel')
        def handle_confirm_callback(call):
            if call.data.startswith('add_user_'):
                # Get the name of the new user from the callback data
                name = call.data.split('_')[2]
                if name == message.text:
                    # Call the X1 function with the name of the new user
                    cl.add_user(name)
                    bot.answer_callback_query(call.id, f'{name} has been added successfully.')
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{name} has been added successfully.', reply_markup=None)
                else:
                    bot.answer_callback_query(call.id, 'Operation cancelled.')
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Operation cancelled.', reply_markup=None)
            elif call.data == 'cancel':
                bot.answer_callback_query(call.id, 'Operation cancelled.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Operation cancelled.', reply_markup=None)


# Function to handle the "Delete User" option
@bot.message_handler(commands=['delete_user'])
def delete_user(message):
    # Check if the user is authorized
    if not is_authorized(message.chat.id):
        bot.reply_to(message, 'You are not authorized to use this bot.')
        return
    # Call the X1 function to get the list of users
    cl = XRayConfiguration()
    users = cl.user_list()
    # Check if there are any users
    if not users or len(users) == 0:
        bot.reply_to(message, 'There are no users to delete.')
        return
    # Create a keyboard with the list of users
    keyboard = telebot.types.InlineKeyboardMarkup()
    for user in users:
        delete_button = telebot.types.InlineKeyboardButton(user, callback_data=f'delete_user_{user}')
        keyboard.add(delete_button)
    # Ask the user to select a user to delete
    bot.reply_to(message, 'Please select a user to delete:', reply_markup=keyboard)

    # Handle the button clicks
    @bot.callback_query_handler(func=lambda call: call.data.startswith('delete_user_'))
    def handle_delete_user_callback(call):
        # Get the name of the user to delete from the callback data
        name = call.data.split('_')[2]

        # Ask the user to confirm the delete action
        confirm_keyboard = telebot.types.InlineKeyboardMarkup()
        confirm_button_yes = telebot.types.InlineKeyboardButton('Yes', callback_data=f'confirm_delete_user_{name}_yes')
        confirm_button_no = telebot.types.InlineKeyboardButton('No', callback_data=f'confirm_delete_user_{name}_no')
        confirm_keyboard.row(confirm_button_yes, confirm_button_no)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Are you sure you want to delete {name}?', reply_markup=confirm_keyboard)

        # Handle the confirmation button clicks
        @bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_delete_user_'))
        def handle_confirm_delete_user_callback(call):
            # Get the name and confirmation status from the callback data
            data = call.data.split('_')
            name = data[2]
            confirmed = True if data[-1] == 'yes' else False

            if confirmed:
                # Call the X2 function with the name of the user to delete
                cl.remove_user(name)
                bot.answer_callback_query(call.id, f'{name} has been deleted successfully.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{name} has been deleted successfully.', reply_markup=None)
            else:
                bot.answer_callback_query(call.id, 'Delete operation cancelled.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Delete operation cancelled.', reply_markup=None)


# Function to handle the "Display Users" option
@bot.message_handler(commands=['display_users'])
def display_users(message):
    # Check if the user is authorized
    if not is_authorized(message.chat.id):
        bot.reply_to(message, 'You are not authorized to use this bot.')
        return
    # Call the X3 function to get the list of users
    cl = XRayConfiguration()
    users = cl.user_list()
    # Check if there are any users
    if not users:
        bot.reply_to(message, 'There are no users to display. 😔')
        return
    # Create a formatted message with the list of users
    user_list = '\n'.join([f'• {user}' for user in users])
    message_text = f'Here is the list of users: \n👥 Max user: {MAX_CLINENT} \n\n{user_list}'
    bot.reply_to(message, message_text)




bot.polling()