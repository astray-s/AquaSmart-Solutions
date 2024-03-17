# Import necessary libraries
from flask import Flask, render_template, request, redirect
import openai
import os
import time
# from main import usage

# Set the OpenAI API key
openai.api_key = "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"

# Define the name of the bot
name = 'Emma'

# Define the role of the bot
role = 'Water sustainability specialist'

def role(usage, total_usage, shower_usage, flush_usage, cycle_usage, average_zip_usage):
    zipcode = usage[0]
    ppl = usage[1]
    shower = usage[2]
    flush = usage[3]
    cycles = usage[4]
# Define the impersonated role with instructions
    global impersonated_role
    impersonated_role = f"""
        From now on, you are going to act as {name}. Your role is {role}.
        Only speak about ways to improve water sustainability, and if you do not know the answer to a question by the user, reply by saying that that is not within your field of knowledge. Tell them to ask a different question related to water sustainability. Provide the website where you got this information. 
        
        Remember the following:
        The user lives in {zipcode} with a household of {ppl} people. The following information is the information done by the whole household:
        The total shower duration per day is {shower} minutes, the total flush duration per day is {flush} minutes, and the total number of cycles per day is {cycles}. The average water usage in the zipcode is {average_zip_usage} gallons per day. The household's total usage is {total_usage} gallons per day. The household's shower usage is {shower_usage} gallons per day. The household's flush usage is {flush_usage} gallons per day. The household's cycle usage is {cycle_usage} gallons per day. Use this information to provide accurate responses tailored to them.
    """

# Initialize variables for chat history
explicit_input = ""
chatgpt_output = 'Chat log: /n'
cwd = os.getcwd()
i = 1

# Find an available chat history file
while os.path.exists(os.path.join(cwd, f'chat_history{i}.txt')):
    i += 1

history_file = os.path.join(cwd, f'chat_history{i}.txt')

# Create a new chat history file
with open(history_file, 'w') as f:
    f.write('\n')

# Initialize chat history
chat_history = ''

    # Create a Flask web application
    # app = Flask(__name__)

    # Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, impersonated_role, explicit_input, chat_history):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Conversation history: {chat_history}"},
            {"role": "user", "content": f"{user_input}. {explicit_input}"},
        ]
    )

    for item in output['choices']:
        chatgpt_output = item['message']['content']

    return chatgpt_output

    # Function to handle user chat input
def chat(user_input):
    global chat_history, name, chatgpt_output
    current_day = time.strftime("%d/%m", time.localtime())
    current_time = time.strftime("%H:%M:%S", time.localtime())
    chat_history += f'\nUser: {user_input}\n'
    chatgpt_raw_output = chatcompletion(user_input, impersonated_role, explicit_input, chat_history).replace(f'{name}:', '')
    chatgpt_output = f'{name}: {chatgpt_raw_output}'
    chat_history += chatgpt_output + '\n'
    with open(history_file, 'a') as f:
        f.write('\n'+ current_day+ ' '+ current_time+ ' User: ' +user_input +' \n' + current_day+ ' ' + current_time+  ' ' +  chatgpt_output + '\n')
        f.close()
    return chatgpt_raw_output

    # Function to get a response from the chatbot
def get_response(userText):
    return chat(userText)

# Define app routes
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/get")
# # Function for the bot response
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(get_response(userText))

# @app.route('/refresh')
# def refresh():
#     time.sleep(600) # Wait for 10 minutes
#     return redirect('/refresh')

# Run the Flask app
# if __name__ == "__main__":
#     app.run()
