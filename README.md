Aura Intelligence: The Olfactory Storyteller & Curator

Executive Summary

Aura Intelligence is a sophisticated, AI-powered web application designed for the niche fragrance market. It solves the problem of generic, time-consuming product descriptions by providing two distinct, powerful modes: a Storyteller for crafting deep, narrative-driven content for a specific fragrance, and a Curator chatbot for broader discovery, comparison, and market research using live web data. Built with Python/Flask and the Groq API, it serves as a strategic tool for brand owners, e-commerce managers, and content creators to translate olfactory notes into compelling narratives that drive sales.

Core Features
Aura Intelligence operates in two distinct, powerful modes:

1. Storyteller Mode
A guided, multi-step experience for crafting a deep, narrative-driven description for a single fragrance.

Dynamic Creative Brief: The intelligent form adapts its language and prompts based on whether you are describing a new creation or re-interpreting an existing fragrance.

Strategic Inputs: Go beyond simple keywords. Define the wearer's persona, the narrative scene, the brand's voice, and even provide competitor text for strategic differentiation.

Elegant Output: The final story is presented in beautifully formatted, individual cards, creating a sophisticated, editorial-style reading experience.

2. Curator Mode (Chatbot)
A conversational AI expert for broader fragrance discovery, comparison, and strategy.

Live Web Search: Powered by a specialized model, the Curator can access up-to-date information on fragrances, prices, and reviews from across the internet.

Expert Capabilities: Ask it to compare two well-known fragrances, build a curated collection for your shop, or discover hidden gems for a specific season or mood.

Conversational Interface: An intuitive chat interface with suggestion chips to guide your discovery process.

Tech Stack
Backend: Python with the Flask web framework.

AI Engine: Connected to the high-speed Groq API.

Storyteller: llama-3.1-8b-instant for creative text generation.

Curator: groq/compound for conversational AI with built-in web search.

Frontend: HTML5 with TailwindCSS for a responsive, luxury-inspired design.

Core Libraries: python-dotenv for environment management, groq for API communication.

Setup and Installation
Follow these steps to get Aura Intelligence running on your local machine.

1. Prerequisites
Python 3.7+ installed on your system.

A Groq API key. You can get a free key from console.groq.com.

2. Clone or Download the Repository
Get the project files onto your computer. This includes app.py, requirements.txt, and the templates folder containing index.html.

3. Navigate to the Project Directory
Open your terminal or command prompt and use the cd command to go into the project folder.

cd path/to/your/Aura-Intelligence-App

4. Create and Activate a Virtual Environment
It's best practice to create an isolated environment for the project.

# Create the environment
python3 -m venv venv

# Activate the environment (macOS/Linux)
source venv/bin/activate

# Or on Windows
# venv\Scripts\activate

5. Install Dependencies
Install all the required Python libraries using pip.

pip install -r requirements.txt

6. Set Up Your API Key
Create a file named .env in the root of your project folder. Add your Groq API key to this file.

GROQ_API_KEY="your_actual_groq_api_key_goes_here"

7. Run the Application
Start the Flask development server.

python app.py

The application will be running at http://12.0.0.1:5001. You can now open this address in your web browser.

Future Enhancements
This project serves as a powerful foundation. Future iterations could include:

Interactive Sensory Profile: Allow users to click on generated notes to see where they appear in the story.

Visual Generation: Incorporate AI-powered image generation to create mood boards or visual representations of the fragrance's "evoked color palette."

Saved Collections: A user account system to save and manage generated stories and curated collections.
