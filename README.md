# AquaSmart Solutions: AI-Powered Water Sustainability
This website uses several features to promote water sustainability. It first obtains necessary information from the user about their water usage, such as their shower duration, toilet flushes, and their dishwasher cycles. It will then calculate the average usage for each of these functions and then multiply it by the user’s inputs to get their average water usage. The website will then take the user’s water usage and then compare it to the average usage in their zip code. The website will also have an AI that will provide guidance to the user on how to change their water usage habits and promote a sustainable environment. 

![Python Version](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue)
![Flask Version](https://img.shields.io/badge/Flask-2.0.1-green)
![OpenAI GPT Version](https://img.shields.io/badge/OpenAI%20GPT-3.5%20Turbo-yellow)


## Features

- Calculates your daily water usage with specific user inputs
- Compares your daily water usage to the average in your zip code
- Utilizes OpenAI's GPT 3.5 Turbo for intelligent and practical response
- User-friendly interface built with HTML, CSS, and Flask
- Stores each chat history in separate text files

## Getting Started

### Prerequisites

- Python 3.7+ installed on your system.
- Flask 2.0.1 and OpenAI Python SDK installed.
- Set up your OpenAI API key.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/astray-s/AquaSmart-Solutions.git
    ```

2.  Navigate to the project directory: https://github.com/astray-s/AquaSmart-Solutions
   
      ```bash
      cd AquaSmart-Solutions
      ```

3. Pin your installation to openai==0.28
   
   ```bash
   pip3 install openai==0.28
   ```

4. Configure your OpenAI API key.
   
   In order to use OpenAI's GPT-3.5 Turbo for intelligent responses in your chatbot, you'll need to configure your OpenAI API key in the chat.py file. Follow these steps:

   a. Open chat.py in a text editor or code editor of your choice.

   
   b. Locate the following line in chat.py:
         ```python
         openai.api_key = "OPEN_AI_API_KEY"
         ```
   
   c. Replace "OPEN_AI_API_KEY" with your actual OpenAI API key. It should look something like this:
         ```python
         openai.api_key = "sk-zqn9OVmS71IvKsg10nFiTsgRykFJxlMij3WPjdaxegvhzPB2p"
         ```
   
   d. Save the changes to the chat.py file and exit the text editor.
   With these steps completed, your chatbot application is now set up to use OpenAI's GPT-3.5 Turbo and is ready to be launched.
   

6. Usage

Now that you've completed the setup, you can use your very own AquaSmart Solutions: AI-Powered Water Sustainability App!

![Screenshot 2024-03-17 150249](https://raw.githubusercontent.com/astray-s/water_usage_calculator/main/static/images/Screenshot%202024-03-17%20150249.png)

   a. Start the Flask app:
      ```
      python main.py
      ```
       
   b. Open your web browser and go to http://localhost:5000 to interact with your Water Usage Calculator.

   c. Enter your average daily usages to calculate your water consumption and click the submit button

   d. Once you submit, you will get your water usage report and be compared to your zipcode average, where you will be see whether you are maintaining healthy water habits or not.

![Screenshot 2024-03-17 152042](https://raw.githubusercontent.com/astray-s/water_usage_calculator/main/static/images/Screenshot%202024-03-17%20152042.png)


   e. Click the link at the bottom of the Water Usage Report to chat with an customized AI bot that will provide guidance to help you save water
   
   f. You can ask questions or advice to the AI such as "based on my usage, what actions can I do to save water?"

![Screenshot 2024-03-17 152507](https://raw.githubusercontent.com/astray-s/water_usage_calculator/main/static/images/Screenshot%202024-03-17%20152507.png)
