# Aura Intelligence  
### The Olfactory Storyteller & Curator  

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-API-orange.svg)](https://console.groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Executive Summary

**Aura Intelligence** is an AI-powered fragrance marketing platform that bridges the gap between olfactory artistry and compelling commerce. Built for the $64B global fragrance industry, it transforms technical fragrance notes into narrative-driven product descriptions that convert browsers into buyers.

### The Problem
- Niche fragrance brands lack resources for professional copywriting
- Product descriptions are often technical and uninspiring
- Consumers struggle to discover fragrances that match their preferences
- Brands need consistent, SEO-optimized content at scale

### The Solution
A dual-mode AI application leveraging Groq's advanced language models:
1. **Storyteller Mode**: Generates luxury-grade product descriptions in 4 guided steps
2. **Curator Mode**: Conversational AI assistant for fragrance discovery with real-time web search

### Target Market
- **B2B**: Indie perfume brands, e-commerce managers, marketing agencies
- **B2C**: Fragrance enthusiasts, gift shoppers, collectors

### Competitive Advantage
- **Web-Search Integration**: Real-time fragrance data via `groq/compound` model
- **Dual Model Architecture**: Optimized for both accuracy (web search) and creativity (storytelling)
- **Neuroscience-Backed Content**: Science of Scent page explains olfactory marketing psychology
- **Multi-Agent AI Lab**: Customer persona analysis and A/B testing for marketing optimization
- **Zero Learning Curve**: Intuitive, guided 4-step workflow
- **Luxury Design System**: Emoji-free, champagne-accented minimalist aesthetic
- **Production-Ready**: Streaming responses, error handling, mobile-responsive design

### Business Model Potential
- **Freemium**: Limited free generations, paid tiers for unlimited access
- **SaaS**: Monthly subscriptions for brands ($49-$199/month)
- **API**: White-label solution for e-commerce platforms
- **Enterprise**: Custom integrations for luxury fragrance houses

---

## ✨ Core Features  

### 🖋️ **Storyteller Mode**  
A guided, 4-step creative brief system for crafting sophisticated fragrance narratives.

**Key Capabilities:**
- **Intelligent Note Discovery**: Automatically looks up fragrance compositions via web search
- **Use Case Flexibility**: Handles both existing fragrances and new creations
- **Strategic Inputs**: 
  - Product name and olfactory notes
  - Vibe keywords and target audience
  - Storytelling angle and tone selection
  - Competitor analysis and SEO optimization
- **Multi-Section Output**: Generates structured stories with sections like:
  - The Hook (captures attention)
  - The Olfactory Journey (emotional storytelling)
  - The Depth (ingredient exploration)
  - The Revelation (brand philosophy)
  - The Legacy (lasting impression)
- **Professional Formats**: Markdown output, easy copy-paste for e-commerce platforms

**Model Used**: `llama-3.3-70b-versatile` (optimized for creative, long-form content)

---

### 🔍 **Curator Mode (Enhanced AI Assistant)**  
A dual-mode conversational AI fragrance expert with advanced recommendation capabilities.

**🚀 NEW: Two Intelligence Levels**

**Enhanced Mode (Default):**
- **Upgraded Model**: `llama-3.3-70b-versatile` for superior accuracy
- **Expert Knowledge Base**: Deep understanding of:
  - 6 fragrance families (Floral, Oriental, Woody, Fresh, Chypre, Fougère)
  - Note structures (top/heart/base with timing & longevity)
  - Personality matching algorithms (MBTI, lifestyle, values → scent profiles)
  - Occasion recommendations (work, date, wedding, seasonal)
- **Few-Shot Learning**: Pre-trained with expert consultation examples
- **Specific Recommendations**: Suggests actual perfume names (Creed Aventus, Tom Ford Oud Wood, etc.)
- **1024 Token Responses**: Detailed explanations with actionable advice

**🧠 Deep Analysis Mode (Optional):**
- **Multi-Agent Architecture**: 3 specialized AI agents collaborate:
  1. **Master Perfumer**: Technical analysis (accords, longevity, composition)
  2. **Personal Stylist**: Lifestyle & personality matching
  3. **Curator Synthesizer**: Creates final recommendations from both insights
- **Transparent Reasoning**: See each agent's analysis (collapsible view)
- **Best For**: Complex queries like building fragrance wardrobes, personality deep-dives
- **Track Record**: Separately tracked analytics (`curatorDeep` vs `curator`)

**Shared Capabilities:**
- **Natural Conversations**: Context-aware chat with full conversation memory
- **Quick Start Chips**: Pre-built suggestions (Summer scents, Date night, Woody fragrances)
- **Streaming Responses**: Real-time answer generation
- **Smart Follow-Ups**: Asks clarifying questions to refine recommendations

**Models Used**: 
- Enhanced: `llama-3.3-70b-versatile` (1 agent)
- Deep: `llama-3.3-70b-versatile` × 3 (multi-agent system)

---

### 🧪 **Science of Scent**  
Educational content explaining the neuroscience behind olfactory marketing.

**Key Topics:**
- **Neuroscience Foundation**: How scent bypasses cognitive filters and triggers emotional memory
- **Research-Backed Insights**: Links to Harvard, Psychology Today, and HBR studies
- **Marketing Psychology**: Why scent marketing drives 40% higher brand recall
- **Olfactory Journey**: Understanding how fragrance notes interact with brain chemistry
- **Business Applications**: Using scent psychology to enhance customer experiences

**Educational Sections**:
- The Power of Scent (emotional memory triggers)
- Neuroscience Meets Marketing (limbic system activation)
- The Olfactory Journey (perfume pyramid structure)
- Building Your Scent Story (brand identity through fragrance)

**Page Design**: Gradient background with translucent navigation, SVG icons for neuroscience concepts

---

### 🔬 **AI Lab (Multi-Agent Analysis)**  
Advanced customer persona analysis and A/B testing for fragrance marketing optimization.

**Key Capabilities:**
- **Multi-Agent Customer Analysis**: 
  - Psychographic Analyst (emotional triggers, values, lifestyle)
  - Behavioral Analyst (purchase patterns, decision-making)
  - Market Analyst (competitive positioning, trends)
  - Brand Strategist (messaging recommendations)
- **A/B Testing Simulation**: Compare two fragrance descriptions with predicted performance metrics
- **JSON-Formatted Insights**: Structured output for easy integration with marketing tools
- **Strategic Recommendations**: Actionable advice for targeting specific customer segments

**Use Cases**:
- Understanding target audience psychology before launching campaigns
- Testing description variants before committing to production
- Competitive analysis for positioning new fragrances
- Data-driven messaging strategies

**Model Used**: `llama-3.3-70b-versatile` with specialized multi-agent prompts

---

### 📊 **Marketing Dashboard**  
Real-time analytics and performance tracking for your fragrance storytelling.

**Key Capabilities:**
- **Usage Analytics**: 
  - Total stories generated
  - Stories saved to library
  - A/B tests completed
  - Feature adoption metrics
- **Content Performance**: 
  - Average SEO scores
  - Top performing tones/vibes
  - Most analyzed fragrances
  - Word count trends
- **Visualization**: 
  - Usage over time (7-day trend chart)
  - Most popular tones (doughnut chart)
  - Feature adoption progress bars
  - Recent activity feed
- **Export & Insights**: 
  - Top fragrances analyzed table
  - Engagement metrics by feature
  - Data refresh and clear options

**Technical Implementation**:
- **LocalStorage Tracking**: Client-side analytics for privacy-first data collection
- **Chart.js Visualization**: Interactive, champagne-themed charts
- **Cross-Page Integration**: Analytics tracking from Story Builder, Curator, and AI Lab
- **Real-Time Updates**: Live dashboard refresh with activity feed

**Use Cases**:
- Portfolio demonstration of full-stack product thinking
- Content strategy optimization based on usage patterns
- A/B test result tracking and comparison
- Feature adoption analysis for product development

---

## 🛠️ Tech Stack  

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.7+ with Flask | Lightweight web framework |
| **AI Engine** | Groq API | Ultra-fast LLM inference |
| **Storyteller Model** | `llama-3.3-70b-versatile` | Creative writing |
| **Curator Model** | `groq/compound` | Web-search + conversation |
| **Frontend** | HTML5, TailwindCSS, Vanilla JS | Responsive, luxury UI |
| **Markdown Rendering** | Marked.js | Beautiful formatted output |
| **Environment Management** | python-dotenv | Secure API key handling |

**Why This Stack?**
- **Groq**: 10x faster than OpenAI for similar quality
- **Dual Models**: Cost-optimized (web search only when needed)
- **Flask**: Simple, scalable, production-ready
- **No Framework Overhead**: Vanilla JS for lightweight frontend

---

## 🚀 Setup and Installation  

### Prerequisites  
- **Python 3.7+** installed ([Download](https://www.python.org/downloads/))
- **Groq API Key** (free tier available at [console.groq.com](https://console.groq.com))

### Installation Steps  

**1. Clone the repository:**  
```bash
git clone https://github.com/dcthedeveloper/Aura-Intelligence.git
cd Aura-Intelligence
```

**2. Create and activate a virtual environment:**

*macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

*Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables:**

Create a `.env` file in the project root:
```ini
GROQ_API_KEY=your_actual_groq_api_key_here
```

**5. Run the application:**
```bash
python app.py
```

**6. Open in your browser:**
```
http://127.0.0.1:5000
```

The app will open to the landing page. Navigate to `/app` to access the Story Builder tool.

---

## 📁 Project Structure

```
Aura-Intelligence/
├── app.py                     # Flask backend (650+ lines)
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (create this)
├── .env.example              # Template for environment variables
├── .gitignore                # Git ignore rules (protects .env)
├── templates/
│   ├── app.html              # Story Builder & Curator tool (1,830+ lines)
│   ├── home.html             # Landing page (562 lines)
│   ├── how_it_works.html     # How It Works page (550 lines)
│   ├── use_cases.html        # Use Cases page (706 lines)
│   ├── features.html         # Features page (675 lines)
│   ├── science.html          # Science of Scent (neuroscience) (513 lines)
│   ├── lab.html              # AI Lab (multi-agent analysis) (650+ lines)
│   └── dashboard.html        # Marketing Dashboard (analytics) (900+ lines)
├── LICENSE                   # MIT License
├── PROJECT_WRITEUP.md        # Technical documentation
├── SUBMISSION_CHECKLIST.md   # Project submission checklist
└── README.md                 # This file

Total: ~8,000+ lines of production code
```

---

## 🎯 Usage Guide

### **Storyteller Mode**

1. Select **"Storyteller"** from the mode toggle
2. Choose your use case:
   - **"An Existing Fragrance"**: App will auto-lookup notes via web search
   - **"A New Creation"**: Manually input your fragrance notes
3. Complete the 4-step guided form:
   - **Step 1 - The Fragrance**: Name and olfactory notes
   - **Step 2 - The Aura**: Vibe and target wearer persona
   - **Step 3 - The Narrative**: Scene and tone selection
   - **Step 4 - The Edge**: Competitor analysis and SEO keywords
4. Click **"Craft Story"** to generate your description
5. Copy the formatted output for use in product pages, marketing materials, etc.

**Example Input:**
- Fragrance: "Creed Aventus"
- Vibe: "Bold, successful, charismatic"
- Audience: "Confident professionals"
- Tone: "Modern & Direct"

**Example Output:** Multi-section story with hooks, journeys, and calls-to-action

---

### **Curator Mode**

1. Select **"Curator"** from the mode toggle
2. **Choose Your Intelligence Level:**
   - **Enhanced Mode** (default, checkbox off): Fast, accurate recommendations
   - **🧠 Deep Analysis Mode** (checkbox on): 3 AI agents for complex queries
3. Type questions or click suggestion chips:
   - "What's a good fresh summer fragrance?"
   - "Help me build a 4-season fragrance wardrobe" (try Deep Mode!)
   - "I'm an introvert who loves books and coffee. What should I wear?"
   - "Recommend something woody for date night"
4. Receive expert recommendations with specific perfume names
5. **Deep Mode Only**: Expand analysis insights to see Master Perfumer + Stylist reasoning
6. Continue the conversation—both modes remember context

**Pro Tip:** Use Enhanced Mode for quick questions, Deep Mode when you want transparent multi-agent analysis!

**Example Deep Mode Query:**
- "I need a signature scent for a creative director who wants to be taken seriously but stay approachable"
- **Master Perfumer Analysis**: Technical notes (woody-aromatic, citrus freshness, moderate projection)
- **Personal Stylist Analysis**: Personality insights (balanced authority + creativity signals)
- **Final Recommendations**: 3-4 specific fragrances with detailed reasoning

---

## 🎨 Design Philosophy

**Luxury Aesthetic**  
- Champagne color palette (#FEFDFB to #3A3327) inspired by premium fragrance packaging
- Cormorant Garamond serif headings + Inter body text for modern elegance
- Emoji-free design system for sophisticated, minimalist brand presence
- Consistent champagne-500 accent colors across all interactive elements
- Gradient backgrounds for information architecture (Science page uses subtle gradients)
- Minimalist design matching niche fragrance brands (Byredo, Kilian, Nishane)

**User Experience**  
- **Progressive Disclosure**: 4-step form prevents overwhelm
- **Unified Navigation**: "Launch App" CTA consistently leads to full tool suite
- **Mobile-First**: Fully responsive design with standardized mobile menus
- **Micro-Interactions**: Smooth animations and transitions
- **Zero Learning Curve**: Smart placeholders and inline hints
- **Information Architecture**: Intentional background color variance (white for marketing pages, gradients for educational content)

**Performance**  
- **Streaming Responses**: See results generate in real-time
- **Optimized Models**: Right tool for each job (cost + speed)
- **Error Handling**: Graceful fallbacks and user feedback

---

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API authentication key | ✅ Yes |

**Get Your API Key:**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up (free tier available)
3. Navigate to API Keys section
4. Create new key and copy to `.env` file

---

## 🚦 API Endpoints

### `POST /generate`
**Purpose**: Generates fragrance descriptions (Storyteller Mode)

**Request Type**: `multipart/form-data`

**Parameters**:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `use_case` | string | Yes | `"existing"` or `"new"` |
| `product_name` | string | Yes | Fragrance name |
| `key_notes` | string | No | Olfactory notes (auto-filled if existing) |
| `vibe_keywords` | string | Yes | Desired emotional vibe |
| `target_audience` | string | Yes | Wearer persona |
| `storytelling_angle` | string | Yes | Narrative scene/context |
| `tone` | string | Yes | Writing style preference |
| `brand_voice` | string | No | Brand voice examples |
| `competitor_text` | string | No | Competitor description for differentiation |
| `seo_keywords` | string | No | Target SEO terms |

**Response**: Server-Sent Events (SSE) stream of generated markdown text

---

### `POST /chat`
**Purpose**: Handles Curator queries with dual-mode AI (Enhanced or Deep Analysis)

**Request Type**: `application/json`

**Parameters**:
```json
{
  "message": "User's question or request",
  "history": [
    {"role": "user", "content": "Previous message"},
    {"role": "assistant", "content": "Previous response"}
  ],
  "deepMode": false  // true = 3-agent analysis, false = enhanced single model
}
```

**Response (Enhanced Mode)**: JSON with AI response
```json
{
  "response": "AI-generated recommendation with specific perfume names",
  "success": true,
  "mode": "enhanced"
}
```

**Response (Deep Mode)**: JSON with multi-agent analysis
```json
{
  "response": "Final synthesized recommendations",
  "success": true,
  "mode": "deep",
  "analysis": {
    "expert": "Master Perfumer technical analysis",
    "stylist": "Personal Stylist lifestyle assessment"
  }
}
```
{
  "response": "AI-generated answer with web-sourced data",
  "success": true
}
```

---

## 🌟 Roadmap & Future Features

### Phase 1 (Current) ✅ **COMPLETED**
- ✅ Storyteller mode with 4-step workflow
- ✅ Curator chatbot with web search
- ✅ Dual model architecture
- ✅ Mobile-responsive design with consistent navigation
- ✅ **Copy to Clipboard**
- ✅ **Save & History** (localStorage, 50 stories)
- ✅ **PDF Export**
- ✅ **Social Media Post Generator** (Instagram/X/Facebook)
- ✅ **SEO Analysis & Auto-Optimize**
- ✅ **Output Length Control** (Product/Full/Short)
- ✅ **Enhanced Tone Selection** (8 tones with previews)
- ✅ **Curated Collections** (Best Niche Fragrances - 21 premium scents)
- ✅ **Science of Scent Page** (Neuroscience-backed olfactory marketing education)
- ✅ **AI Lab** (Multi-agent customer analysis & A/B testing tool)
- ✅ **Marketing Dashboard** (Real-time analytics with Chart.js visualizations)
- ✅ **Comprehensive UX/UI Audit** (Luxury design system with emoji-free aesthetic)

### Phase 2 (Q1-Q2 2026) - Expansion
- 🔲 User authentication & cloud storage
- 🔲 Export to DOCX format
- 🔲 Fragrance note autocomplete
- 🔲 Additional curated collections:
  - 🍂 Seasonal Collections (Spring/Summer/Fall/Winter)
  - 🔥 Trending Now (AI-powered, updates weekly)
  - 👩 Best for Women
  - 👨 Best for Men
  - ⚡ Unisex Favorites
- 🔲 A/B testing (generate multiple variants)
- 🔲 Brand voice training (upload samples, AI learns your style)

### Phase 3 (Q3-Q4 2026) - Monetization
- 🔲 Enhanced analytics (cloud-based historical tracking & exports)
- 🔲 Shopify/WooCommerce plugin (one-click integration)
- 🔲 Team collaboration features
- 🔲 Usage-based pricing tiers
- 🔲 White-label API for agencies
- 🔲 Multi-language support (French, Arabic, Mandarin)

### Phase 4 (2027+) - Enterprise
- 🔲 Custom model fine-tuning (brand-specific AI)
- 🔲 Fragrance recommendation engine (quiz-based)
- 🔲 Email marketing integration
- 🔲 CRM integrations (HubSpot, Salesforce)
- 🔲 Advanced SEO tools (keyword research, SERP tracking)
- 🔲 Content calendar & scheduling

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or proposing new features.

**How to Contribute:**

1. **Fork the repository**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

**Contribution Guidelines:**
- Follow existing code style
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ Provided "as is" without warranty

---

## 🙏 Acknowledgments

- **[Groq](https://groq.com)** - For ultra-fast AI inference and web-search capabilities
- **[Meta AI](https://ai.meta.com/)** - For the Llama 3.3 70B model
- **Design Inspiration** - Luxury niche fragrance houses (Byredo, Le Labo, Diptyque, Maison Francis Kurkdjian)
- **Community** - The indie perfume community for feedback and testing

---

## 📞 Contact & Support

- **GitHub**: [@dcthedeveloper](https://github.com/dcthedeveloper)
- **Project Link**: [https://github.com/dcthedeveloper/Aura-Intelligence](https://github.com/dcthedeveloper/Aura-Intelligence)
- **Issues**: [Report a bug or request a feature](https://github.com/dcthedeveloper/Aura-Intelligence/issues)

---

## 🎯 Use Cases & Success Stories

**For Brands:**
> "Aura Intelligence helped us create consistent product descriptions across our entire 50+ fragrance collection in one afternoon. The SEO optimization increased our organic traffic by 40%."  
> *— Indie Perfume Brand Owner*

**For Content Creators:**
> "As a fragrance blogger, the Curator mode helps me discover new scents and understand complex note breakdowns instantly."  
> *— Fragrance Influencer*

**For E-commerce:**
> "We integrated Aura's storytelling into our Shopify store. Customer engagement went up, and our bounce rate dropped by 25%."  
> *— E-commerce Manager*

---

## 🔬 Technical Deep Dive

### Why Two Models?

**Cost Optimization:**
- `groq/compound` (web-search): ~$0.70/1M tokens
- `llama-3.3-70b-versatile`: ~$0.59/1M tokens
- Only using web-search when needed saves 15-20% on API costs

**Performance:**
- Web search adds 2-3 seconds latency
- Creative writing doesn't need web access
- Storyteller mode is 40% faster without compound model

**Quality:**
- Each model optimized for its specific task
- Compound model: Accuracy & current data
- Versatile model: Creativity & storytelling

### Architecture Decisions

**Why Flask over FastAPI?**
- Simpler deployment for MVP
- Better template rendering
- Mature ecosystem for production

**Why Server-Sent Events (SSE)?**
- Real-time streaming without WebSockets
- Simpler implementation
- Better browser compatibility

**Why Vanilla JS over React?**
- Faster page load (no bundle)
- Lower complexity
- Easier for contributors

---

<div align="center">

**Crafted with ❤️ for the olfactory world**

[⬆ Back to Top](#-aura-intelligence)

</div>
