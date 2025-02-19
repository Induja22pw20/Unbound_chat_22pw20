
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
