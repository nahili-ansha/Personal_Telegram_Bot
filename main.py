from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final= '' # use the API TOKEN provided by BotFather
BOT_USERNAME: Final = '' # use the user_name you choosed

# Commands
# start_command: \start
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am Nahili!')

# help_command: \help give users information on how the bot works
async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Nahili! Please type something so I can respond!')

# something else
async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Responses
def handle_response(text: str) -> str:
    text = text.lower().strip()

    responses = {
        'hello': 'Greetings! How can I help you today?',
        'how are you': 'I am functioning optimally, thank you! How about yourself?',
        'what is your name': 'I am Nahili Bot.',
        'who are you': 'I am the dedicated Telegram bot of Nahili Ansha, here to assist you with your inquiries.',
        'who is nahili': ('Nahili Ansha is a passionate sophomore in Computer Science at Minnesota State University, Mankato.'),
        'tell me about nahili': ('Nahili Ansha is a detail-oriented and successful student pursuing a degree in Computer Science. '
                                 'She is a powerful and friendly individual, actively contributing as an RSO Coordinator, Teaching Assistant,Event Organizer and peer mentor. '
                                 'Her leadership and dedication are evident in her various roles and her commitment to helping others.'),
        'how old is she': 'Nahili is 19 years old.',
        'what is her github': 'You can explore Nahili\'s work on GitHub under the username: nahili-ansha.',
        'what projects has nahili worked on': ('Nahili has an impressive portfolio including projects like a Telegram Bot, Tkinter ChatGPT API app, '
                                               'a Book Recommendation System, a School Registration System, and a Calculator Application.'),
        'what are her interests': ('Nahili is enthusiastic about various activities such as Photography, Baking, Coding, Competitive Gaming, '
                                         'Trying Ethnic Foods, and Mentoring/Volunteering.'),
        'how can i contact her': 'You can reach Nahili through her GitHub profile or connect with her on LinkedIn.'
    }

    for key, response in responses.items():
        if key in text:
            return response

    return 'I\'m sorry, I didn\'t quite catch that. Could you please rephrase your question?'


# whether they are in a group or private chat
async def handle_message(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text:str = update.message.text
    print(f'User {update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response: str  =handle_response(new_text)
    else:
        response:str = handle_response(text)
    await update.message.reply_text(response)

# logging errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting the bot...")
    app = Application.builder().token(TOKEN).build()
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # MessageS
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Checks for updates every x seconds
    print("Polling...")
    app.run_polling(poll_interval=3)
