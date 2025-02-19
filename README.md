
# demo video link - milestone 1
https://www.loom.com/share/b9d1139fd6dc4964b36a7098eb1253ae?sid=831c25a6-3882-4edb-8596-5e58fd9e0203
# demo video link - milestone 2
https://www.loom.com/share/8e79bd6625a847fd850bd54b9ae9547b?sid=83ba174c-962c-48bb-889b-38a912d26228

In Milestone 2, I implemented a chat completions endpoint for my application. This involved defining database models for providers and responses, creating a view function to handle POST requests and validate inputs, configuring URL patterns, and populating the database with predefined static responses. I also integrated this functionality with a frontend interface, allowing users to select a provider and model, enter a prompt, and receive responses. This setup ensured that requests are routed correctly, validated, and responded to with predefined data, laying a solid foundation for a scalable and modular chat application.
# demo video link - milestone 3
https://www.loom.com/share/37e8836a1a4c4592b803a63f0bea79c0?sid=2cc6ddff-26ca-4021-b4d9-345d99997a38

- **Implemented Regex-Based Routing**: Added functionality to check user prompts against stored regex patterns and reroute requests based on matches.
- **Updated Database Models**: Introduced a new model to store regex rules and their associated routing policies in the database.
- **Modified View Logic**: Enhanced the `chat_completions` view to validate inputs, apply regex-based routing, and return appropriate responses.
- **Added Management Command**: Created a command to populate the database with predefined regex policies for routing.
- **Tested and Verified**: Ensured that prompts matching specific patterns (e.g., "credit card") were rerouted to the correct model and provided the expected responses. 🚀
# demo video link - milestone 4
https://www.loom.com/share/f9f3216a200f475ca4958f3873bd03ab?sid=a7017ac0-9578-4d26-a2a6-4c7cf9785454
In Milestone 4, I built a minimal web-based chat UI that allows users to interact with the chat application. The UI fetches and lists available models via the /models endpoint, provides dropdown menus for users to select a provider and model, accepts user prompts, sends requests to the POST /v1/chat/completions endpoint, and displays the response. Additionally, I enhanced the UI with animations, transitions, and hover effects to make it visually appealing and engaging.
# demo video link - milestone 5
https://www.loom.com/share/209a34494bfb476eb9b7e8fe3a199720?sid=bd359e91-1e1b-41a6-b795-29c658f2978d

In Milestone 5, I created an admin portal for managing regex policies. This included developing a web interface to add, edit, and delete regex rules, associating them with specific redirect and original models. This enhances my chat application's flexibility by dynamically rerouting models based on user prompts.
# demo video link - milestone 6
https://www.loom.com/share/a53f589bb76340a59b337a0ad6df2006?sid=8d932ab5-eba5-4be2-a15c-5f86994ca9e4
I added the FileUpload model to store file information in the database.


# Unbound Chat App

Unbound Chat App is a Django-based web application that provides a chat interface with AI models from various providers. It includes an admin portal for managing regex rules for routing prompts to different models.

## Features

- Chat interface with AI models
- Admin portal for managing regex rules
- File upload support
- Predefined responses for providers

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/unbound_chat_app.git
   cd unbound_chat_app
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the chat interface.
## Design Choices and Architecture
Models
ModelProvider: Represents a provider of AI models.
RegexPolicy: Defines regex patterns for routing prompts to different models.
ProviderResponse: Stores responses from providers.
Provider: Contains provider details including API keys.
FileUpload: Manages file uploads.
Views
Chat Interface: Allows users to interact with AI models.
Admin Portal: Enables management of regex rules and viewing of responses.
Templates
Admin Page: Custom admin interface for managing regex rules.
Index Page: Main chat interface.
Static Files
CSS: Custom styles for the admin and chat interfaces.

## Usage

Chat Interface
Select a provider and model.
Enter your prompt and optionally upload a file.
Click "Send" to get a response from the selected model.
Admin Portal
Go to http://127.0.0.1:8000/custom-admin/ to access the admin portal.
Add new regex rules for routing prompts to different models.
View, edit, and delete existing regex rules.
Management Commands
add_model_data: Adds sample model data to the database.
add_regex_policies: Adds regex policies for routing.
add_predefined_responses: Adds predefined responses for providers.



