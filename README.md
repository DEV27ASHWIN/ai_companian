AI Companion Chat Interface
Project Overview
The AI Companion Chat Interface is a web-based chat application designed to provide a user-friendly and interactive platform for conversing with an AI model. This project aims to mimic the functionalities of popular AI chat platforms, such as ChatGPT, providing features like dynamic message generation, message regeneration, dark mode, and responsive design.

Features
Dynamic Message Generation: Allows users to send messages and receive dynamic responses from the AI model.
Message Regeneration: Provides the ability to regenerate responses based on the initial prompt.
Dark Mode: Offers a dark mode option for better user experience during nighttime usage.
Responsive Design: Ensures the chat interface is flexible and adapts to different screen sizes.
Fixed Chat Input: Keeps the chat input box fixed at the bottom of the screen for easy access.
Scroll Indicator: Indicates when new messages are available at the bottom of the chat window.
Keyboard Shortcuts: Supports sending messages with Enter and adding new lines with Shift+Enter.
Technologies Used
HTML
CSS
JavaScript
Django (Backend framework)
FontAwesome (For icons)
Project Structure
arduino
Copy code
.
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── user.png
│   │   ├── bot.png
│   │   └── loading.gif
│   └── js
│       └── main.js
├── templates
│   └── index.html
├── views.py
└── README.md
Setup Instructions
Prerequisites
Python 3.x
Django
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/ai-companion.git
cd ai-companion
Install Dependencies:

bash
Copy code
pip install django
Run the Django Server:

bash
Copy code
python manage.py runserver
Access the Application:

Open your web browser and navigate to http://127.0.0.1:8000/.

File Details
index.html: Contains the HTML structure of the chat interface.
style.css: Contains the CSS styles for the chat interface, including dark mode styles.
main.js: Contains the JavaScript functions for handling message sending, regenerating responses, and scroll indicators.
views.py: Contains the Django views for handling requests and responses.
Usage
Send a Message: Type your message in the input box and press Enter or click the "Send" button.
Regenerate a Response: Click the regenerate icon to generate a new response based on the initial prompt.
Toggle Dark Mode: Use the switch in the top right corner to toggle dark mode.
Copy a Message: Click the copy icon to copy the message text to your clipboard.
Contributing
Fork the Repository: Click on the "Fork" button at the top right of the repository page.

Clone the Forked Repository:

bash
Copy code
git clone https://github.com/your-username/ai-companion.git
Create a New Branch:

bash
Copy code
git checkout -b feature-name
Make Your Changes: Implement your feature or bug fix.

Commit Your Changes:

bash
Copy code
git add .
git commit -m "Description of your changes"
Push to Your Branch:

bash
Copy code
git push origin feature-name
Create a Pull Request: Go to the original repository and create a pull request.

License
This project is licensed under the apache.org License. See the LICENSE file for more information.
