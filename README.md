# 🌸 Aura Intelligence  
### The Olfactory Storyteller & Curator  

Aura Intelligence is a sophisticated, AI-powered web application designed for the niche fragrance market.  
It provides two powerful modes: a **Storyteller** for crafting deep, narrative-driven product descriptions, and a **Curator** chatbot for fragrance discovery using live web data.

Built with **Python/Flask** and the **Groq API**, it serves as a strategic tool for brand owners, e-commerce managers, and content creators to translate olfactory notes into compelling narratives that drive sales.

---

## ✨ Core Features  

### 🖋️ Storyteller Mode  
A guided, 4-step experience for crafting sophisticated fragrance descriptions.

- **Dynamic Creative Brief:** Adapts prompts based on whether you're describing a new creation or existing fragrance.  
- **Strategic Inputs:** Define wearer persona, narrative scene, brand voice, tone, and competitor differentiation.  
- **Accurate Note Recall:** Uses a two-step "Researcher-Writer" process to ensure factual accuracy for known fragrances.  
- **Elegant Output:** Presents the final story in beautifully formatted, individual cards.  

---

### 🔍 Curator Mode (Chatbot)  
A conversational AI expert for fragrance discovery and curation.

- **Live Web Search:** Real-time access to fragrance data, pricing, and reviews via Groq's compound model.  
- **Expert Capabilities:** Compare fragrances, build curated collections, and discover seasonal recommendations.  
- **Conversational Interface:** Intuitive chat with suggestion chips for quick queries.  
- **Streaming Responses:** See answers generate in real time.  

---

## 🛠️ Tech Stack  

| Component | Technology |
|------------|-------------|
| **Backend** | Python 3.7+ with Flask |
| **AI Engine** | Groq API |
| **Storyteller Model** | llama-3.3-70b-versatile |
| **Curator Model** | groq/compound (with web search) |
| **Frontend** | HTML5, TailwindCSS, Vanilla JavaScript |
| **Markdown Rendering** | Marked.js |
| **Environment** | python-dotenv |

---

## 🚀 Setup and Installation  

### Prerequisites  
- Python 3.7+ installed  
- A free **Groq API key** from [console.groq.com](https://console.groq.com)

### Installation Steps  

**1. Clone the repository:**  
```bash
git clone https://github.com/yourusername/aura-intelligence.git
cd aura-intelligence
2. Create and activate a virtual environment:

On macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
On Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
3. Install dependencies:

bash
Copy code
pip install -r requirements.txt
4. Set up your environment variables:
Create a file named .env in the root of your project folder and add your API key:

ini
Copy code
GROQ_API_KEY="your_actual_groq_api_key_here"
5. Run the application:

bash
Copy code
python app.py
6. Open in your browser:
http://127.0.0.1:5001

📁 Project Structure
bash
Copy code
aura-intelligence/
├── app.py              # Flask backend with all logic
├── requirements.txt    # Python dependencies
├── .env                # Your secret API key (create this file)
├── templates/
│   └── index.html      # The single-page frontend application
└── README.md
🎯 Usage
Storyteller Mode
Select "Storyteller" from the mode toggle.

Choose between "Existing Fragrance" or "New Creation."

Complete the 4-step form:

The Fragrance: Name and key notes

The Aura: Vibe and target audience

The Narrative: Storytelling angle and tone

The Edge: Competitor text and SEO keywords

Click "Craft Story" to generate your marketing copy.

Use the "Copy" button to export results instantly.

Curator Mode
Select "Curator" from the mode toggle.

Ask natural language questions such as:

“What are the best summer fragrances for 2025?”

“Compare Creed Aventus and Dior Sauvage.”

“Create a 5-piece luxury collection under $500.”

Use suggestion chips for quick exploration.

View real-time answers sourced from live web data.

🎨 Key Design Principles
Luxury Aesthetic: Cream backgrounds, Playfair Display typography, and gold accents.

Progressive Disclosure: A clean 4-step form ensures a smooth, guided experience.

Micro-Interactions: Smooth animations, fading transitions, and card reveals.

Mobile Responsive: Fully optimized for all screen sizes.

Zero Learning Curve: Intuitive, single-page layout with smart placeholders and hints.

🔑 Environment Variables
Variable	Description	Required
GROQ_API_KEY	Your Groq API key for AI model access	Yes

🚦 API Endpoints
POST /generate
Generates fragrance descriptions using Storyteller Mode.

Parameters (form data):

product_name: Fragrance name

key_notes: Olfactory notes

vibe_keywords: Desired vibe

target_audience: Wearer persona

storytelling_angle: Narrative scene

tone: Writing style

brand_voice: Brand tone examples (optional)

competitor_text: Competitor description (optional)

seo_keywords: SEO keywords (optional)

Returns:
Server-Sent Events (SSE) stream of generated text.

POST /chat
Handles Curator chatbot queries with web search.

Parameters (JSON):

message: User’s question or request

Returns:
Server-Sent Events (SSE) stream of AI response.

🌟 Features Roadmap
 User authentication and saved projects

 Export to PDF/DOCX

 Multi-language support

 Fragrance note autocomplete

 A/B testing multiple descriptions

 Analytics dashboard

 Shopify/WooCommerce integration

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Steps to contribute:

Fork the repository

Create your feature branch

bash
Copy code
git checkout -b feature/AmazingFeature
Commit your changes

bash
Copy code
git commit -m 'Add some AmazingFeature'
Push to the branch

bash
Copy code
git push origin feature/AmazingFeature
Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

🙏 Acknowledgments
Built with Groq for ultra-fast AI inference

UI design inspired by luxury niche fragrance houses (Byredo, Le Labo, Diptyque)

Powered by Meta’s Llama 3.3 models

Project Link: https://github.com/dcthedeveloper/Aura-Intelligence

Crafted with ❤️ for the olfactory world.
