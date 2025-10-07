🌸 Aura Intelligence
The Olfactory Storyteller & Curator

Aura Intelligence is a sophisticated, AI-powered web application designed for the niche fragrance market. It provides two powerful modes: a Storyteller for crafting deep, narrative-driven product descriptions, and a Curator chatbot for fragrance discovery using live web data.

Built with Python/Flask and the Groq API, it serves as a strategic tool for brand owners, e-commerce managers, and content creators to translate olfactory notes into compelling narratives that drive sales.
✨ Core Features
🖋️ Storyteller Mode
A guided, 4-step experience for crafting sophisticated fragrance descriptions.

Dynamic Creative Brief: Adapts prompts based on whether you're describing a new creation or existing fragrance

Strategic Inputs: Define wearer persona, narrative scene, brand voice, tone, and competitor differentiation

5 Tone Options: Poetic, Modern, Minimalist, Mysterious, Playful

Elegant Output: Beautifully formatted cards with smooth animations

One-Click Copy: Export descriptions instantly

🔍 Curator Mode (Chatbot)
A conversational AI expert for fragrance discovery and curation.

Live Web Search: Real-time access to fragrance data, pricing, and reviews via Groq's compound model

Expert Capabilities: Compare fragrances, build curated collections, discover seasonal recommendations

Conversational Interface: Intuitive chat with suggestion chips

Streaming Responses: See answers generate in real-time

🛠️ Tech Stack
| Component | Technology | |-----------|------------| | Backend | Python 3.7+ with Flask | | AI Engine | Groq API | | Storyteller Model | llama-3.1-8b-instant | | Curator Model | groq/compound (with web search) | | Frontend | HTML5, TailwindCSS, Vanilla JavaScript | | Markdown Rendering | Marked.js | | Environment | python-dotenv |
🚀 Setup and Installation
Prerequisites
Python 3.7+ installed

Groq API key (get free at console.groq.com)

Installation Steps
Clone the repository

git clone [https://github.com/yourusername/aura-intelligence.git](https://github.com/yourusername/aura-intelligence.git)
cd aura-intelligence

Create virtual environment

python3 -m venv venv

Activate (macOS/Linux)

source venv/bin/activate

Activate (Windows)

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Set up environment variables
Create a .env file in the root directory:

GROQ_API_KEY=your_actual_groq_api_key_here

Run the application

python app.py

Open in browser
Navigate to http://127.0.0.1:5001

📁 Project Structure
aura-intelligence/
├── app.py             # Flask backend with Groq integration
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (create this)
├── templates/
│   └── index.html   # Frontend application
└── README.md

🎯 Usage
Storyteller Mode
Select "Storyteller" from the mode toggle

Choose between "Existing Fragrance" or "New Creation"

Fill in the 4-step form:

The Fragrance: Name and notes

The Aura: Vibe and target audience

The Narrative: Storytelling angle and tone

The Edge: Competitor text and SEO keywords

Click "Craft Story" to generate sophisticated marketing copy

Use "Copy" to export the results

Curator Mode
Select "Curator" from the mode toggle

Ask questions like:

"What are the best summer fragrances for 2025?"

"Compare Creed Aventus and Dior Sauvage"

"Create a 5-piece luxury collection under $500"

Use suggestion chips for quick queries

Get real-time responses with web-sourced data

🎨 Key Design Principles
Luxury Aesthetic: Cream backgrounds, Playfair Display typography, gold accents

Progressive Disclosure: Clean 4-step form prevents overwhelming users

Micro-interactions: Smooth animations and transitions throughout

Mobile Responsive: Optimized for all screen sizes

Zero Learning Curve: Intuitive interface with helpful placeholders

🔑 Environment Variables
| Variable | Description | Required | |----------|-------------|----------| | GROQ_API_KEY | Your Groq API key for AI model access | Yes |
🚦 API Endpoints
POST /generate
Generates fragrance descriptions using Storyteller mode.

Parameters (form data):

product_name: Fragrance name

key_notes: Olfactory notes

vibe_keywords: Desired vibe

target_audience: Wearer persona

storytelling_angle: Narrative scene

tone: Writing style

brand_voice: Brand voice examples (optional)

competitor_text: Competitor description (optional)

seo_keywords: SEO keywords (optional)

Returns: Server-Sent Events stream of generated text

POST /chat
Handles Curator chatbot queries with web search.

Parameters (JSON):

message: User's question or request

Returns: Server-Sent Events stream of AI response
🌟 Features Roadmap
[ ] User authentication and saved projects

[ ] Export to PDF/DOCX

[ ] Multi-language support

[ ] Fragrance note autocomplete

[ ] A/B testing multiple descriptions

[ ] Analytics dashboard

[ ] Shopify/WooCommerce integration

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments
Built with Groq for ultra-fast AI inference

UI design inspired by luxury niche fragrance houses (Byredo, Le Labo, Diptyque)

Powered by Meta's Llama 3.1 models


Project Link: https://https://github.com/dcthedeveloper/Aura-Intelligence
<div align="center">
<strong>Crafted with ❤️ for the olfactory world</strong>
</div>
