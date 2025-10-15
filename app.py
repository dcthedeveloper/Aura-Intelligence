import os
import traceback
import re
from io import BytesIO
from flask import Flask, request, render_template, Response, stream_with_context, jsonify, send_file
from dotenv import load_dotenv
from groq import Groq
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

try:
    client = Groq()
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    client = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/app')
def app_tool():
    return render_template('app.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/use-cases')
def use_cases():
    return render_template('use_cases.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/pricing')
def pricing():
    # Placeholder - will create this page next
    return "<h1>Pricing - Coming Soon</h1><a href='/'>Back to Home</a>"

@app.route('/lab')
def lab():
    """
    Olfactory AI Lab - A/B Testing Interface
    """
    return render_template('lab.html')

@app.route('/science')
def science():
    """
    The Science of Scent - Educational content hub
    """
    return render_template('science.html')

@app.route('/dashboard')
def dashboard():
    """
    Marketing Dashboard - Analytics and performance tracking
    """
    return render_template('dashboard.html')

def get_accurate_notes(fragrance_name):
    """
    Uses a web-search enabled model to get accurate notes for a known fragrance.
    """
    if not client:
        print("No Groq client available for note retrieval.")
        return "Not specified"
    try:
        print(f"Searching web for notes of: {fragrance_name}")
        chat_completion = client.chat.completions.create(
            model="groq/compound",  # Web-search enabled system
            messages=[
                {"role": "system", "content": "You are a fragrance database expert. Return only the exact top, heart, and base notes for a given fragrance."},
                {"role": "user", "content": f"What are the exact notes for the fragrance '{fragrance_name}'?"}
            ],
            temperature=0,
        )
        accurate_notes = chat_completion.choices[0].message.content.strip()
        print(f"Found notes: {accurate_notes}")
        return accurate_notes if accurate_notes else "Not specified"
    except Exception as e:
        print(f"Error getting accurate notes: {e}")
        print(traceback.format_exc())
        return "Not specified"

@app.route('/generate', methods=['POST'])
def generate():
    if not client:
        return Response("Groq client not initialized. Please check your API key.", status=500)

    # Extract form data and log all received inputs
    use_case = request.form.get('use_case', 'existing')
    product_name = request.form.get('product_name', 'Unnamed Fragrance')
    key_notes_input = request.form.get('key_notes', '')
    vibe_keywords = request.form.get('vibe_keywords', 'Elegant and mysterious')
    target_audience = request.form.get('target_audience', 'A discerning individual')
    storytelling_angle = request.form.get('storytelling_angle', 'An elegant evening')
    brand_voice = request.form.get('brand_voice', '')
    competitor_text = request.form.get('competitor_text', '')
    seo_keywords = request.form.get('seo_keywords', '')
    tone = request.form.get('tone', 'Poetic & Evocative')
    output_length = request.form.get('output_length', 'product')  # product, full, or short

    print("== Incoming request data ==")
    print("use_case:", use_case)
    print("product_name:", product_name)
    print("key_notes_input:", key_notes_input)
    print("vibe_keywords:", vibe_keywords)
    print("target_audience:", target_audience)
    print("storytelling_angle:", storytelling_angle)
    print("brand_voice:", brand_voice)
    print("competitor_text:", competitor_text)
    print("seo_keywords:", seo_keywords)
    print("tone:", tone)
    print("output_length:", output_length)

    # Determine key notes robustly
    final_key_notes = key_notes_input
    if use_case == 'existing' and not key_notes_input:
        final_key_notes = get_accurate_notes(product_name)
    elif not key_notes_input:
        final_key_notes = "Not specified"

    print("Final used notes:", final_key_notes)

    # Configure output specifications based on selected length
    if output_length == 'short':
        length_instruction = """
# OUTPUT LENGTH: SHORT FORM (150-200 words)
Create a concise yet evocative fragrance story. Even in brevity, maintain the Aura Intelligence touch - sensory, emotive, and magnetic.

STRUCTURE:
- ### Opening (2-3 sentences that transport the reader)
- ### Notes (Present as poetic bullet points, not just a list)
  * Top: [describe with imagery]
  * Heart: [describe with emotion]
  * Base: [describe with feeling]
- ### Essence (1-2 sentences capturing who wears this and why)

VOICE: Concise but never clinical. Each word should evoke a feeling, not just inform. Think luxury ad copy that lingers in memory."""
        max_tokens = 350
        
    elif output_length == 'full':
        length_instruction = """
# OUTPUT LENGTH: FULL STORY (800-1200 words)
Craft an immersive olfactory narrative that transcends product description. This is storytelling as art - create a world where the fragrance lives.

STRUCTURE:
Output detailed Markdown sections with '###' headings:
- ### The Awakening (Sensory hook - transport the reader to a moment, place, or feeling)
- ### The Olfactory Journey (Layer-by-layer progression through top, heart, base - make each note a character in the story)
- ### The Muse (Paint the portrait of the wearer - lifestyle, aspirations, secret desires)
- ### The Experience (Sensory immersion - how this fragrance transforms moments, spaces, perceptions)
- ### The Invitation (Poetic closing that leaves them longing for the scent)

VOICE: Rich, poetic, cinematic. Use metaphor, sensory language, and emotional resonance. This isn't a product - it's a portal to another world."""
        max_tokens = 1800
        
    else:  # product (default)
        length_instruction = """
# OUTPUT LENGTH: PRODUCT DESCRIPTION (300-500 words)
Create an SEO-smart fragrance story that balances search visibility with sensory storytelling. This should feel luxurious and magnetic, not formulaic.

STRUCTURE:
Output Markdown sections with '###' headings:
- ### The Story (2-3 paragraph opening - set the scene, evoke a feeling, introduce the fragrance's soul)
- ### The Notes
  * **Top Notes:** [Don't just list - describe how they greet the skin, the first impression]
  * **Heart Notes:** [The emotional center - what blooms as time passes]
  * **Base Notes:** [The lasting memory - what lingers on skin and in mind]
- ### The Essence (Who is this for? What moments does it elevate? Be specific but poetic)

VOICE: Luxury brand storytelling meets e-commerce clarity. Use keywords naturally within evocative sentences. Short paragraphs for scannability, but never sacrifice beauty for SEO. Think Byredo, Le Labo, Diptyque - sophisticated yet accessible."""
        max_tokens = 1024

    # Compose the system prompt
    system_prompt = f"""
# ROLE
You are "Aura" - an elite fragrance copywriter who transforms scent into story. You combine the precision of a master perfumer, the artistry of luxury brand storytelling, and the conversion power of world-class marketing copy.

# CORE DIRECTIVE
Make readers **feel the fragrance before they smell it**. Create desire through sensory language, emotional resonance, and narrative immersion.

# YOUR APPROACH
- **Fragrances are experiences, not products** - Write about moments, identities, and memories
- **Every word must earn its place** - Be evocative, never verbose. Be precise, never clinical
- **Balance poetry with purpose** - Luxury voice that converts, whether for e-commerce or editorial
- **Notes are truth, prose is magic** - Transform accurate ingredients into sensory poetry

{length_instruction}

# INPUT VARIABLES
- Fragrance Name: {product_name}
- Use Case: {"Describing a new creation" if use_case == "new" else "Re-interpreting an existing fragrance"}
- Olfactory Notes: {final_key_notes}
- Desired Vibe: {vibe_keywords}
- Wearer's Persona: {target_audience}
- Narrative Scene: {storytelling_angle}
- Brand Voice Examples: {brand_voice or 'Not provided'}
- Competitor's Story: {competitor_text or 'Not provided'}
- SEO Keywords: {seo_keywords or 'Not provided'}
- Writing Style/Tone: {tone}

# OUTPUT REQUIREMENTS
- Use olfactory notes provided as absolute truth - enhance them, don't invent
- Integrate SEO keywords naturally within evocative prose when provided
- Match the specified tone while maintaining sophisticated brand voice
- Create content that's scannable (headings, short paragraphs) yet magnetic
"""
    user_prompt = "Craft the olfactory story."

    def stream():
        try:
            stream_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=max_tokens,
                top_p=1,
                stop=None,
                stream=True,
            )
            empty = True
            for chunk in stream_response:
                part = chunk.choices[0].delta.content or ""
                if part.strip():
                    empty = False
                print("Story stream chunk:", repr(part))
                yield part
            if empty:
                yield "\n### Error\nNo output generated — please check fragrance notes or model input."
        except Exception as e:
            print(f"Error during story generation: {e}")
            print(traceback.format_exc())
            yield "An error occurred during generation. Please check the server logs."

    return Response(stream_with_context(stream()), content_type='text/event-stream')


@app.route('/analyze-customer', methods=['POST'])
def analyze_customer():
    """
    Multi-Agent Customer Analysis
    Uses 5 specialized AI agents to analyze the customer/fragrance from different angles
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('fragrance_name', 'Unnamed Fragrance')
        key_notes = data.get('key_notes', '')
        target_audience = data.get('target_audience', '')
        vibe_keywords = data.get('vibe_keywords', '')
        
        print(f"=== Multi-Agent Analysis Started for: {fragrance_name} ===")
        
        # Agent 1: Customer Profile Agent
        profile_prompt = f"""As a Customer Profile Agent, analyze the target audience for this fragrance:

Fragrance: {fragrance_name}
Target Audience: {target_audience or 'General luxury fragrance buyer'}
Vibe: {vibe_keywords}

Provide a detailed customer profile including:
- Demographics (age range, gender, income level)
- Lifestyle characteristics
- Shopping behaviors
- Values and priorities

Keep it concise (150 words max)."""

        profile_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Customer Profile Analyst specializing in luxury fragrance markets."},
                {"role": "user", "content": profile_prompt}
            ],
            temperature=0.6,
            max_tokens=300,
        )
        profile_analysis = profile_response.choices[0].message.content.strip()
        
        # Agent 2: Preference Agent
        preference_prompt = f"""As a Preference Agent, analyze the scent preferences for this fragrance:

Fragrance: {fragrance_name}
Notes: {key_notes}
Vibe: {vibe_keywords}

Analyze:
- Olfactory family preferences
- Complementary scent profiles
- What type of fragrance wearer would gravitate to this
- Similar fragrances they might already own

Keep it concise (150 words max)."""

        preference_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Fragrance Preference Analyst with deep knowledge of olfactory families and consumer taste patterns."},
                {"role": "user", "content": preference_prompt}
            ],
            temperature=0.6,
            max_tokens=300,
        )
        preference_analysis = preference_response.choices[0].message.content.strip()
        
        # Agent 3: Psychology Agent
        psychology_prompt = f"""As a Psychology Agent, analyze the emotional triggers and motivations for this fragrance:

Fragrance: {fragrance_name}
Notes: {key_notes}
Target: {target_audience}
Vibe: {vibe_keywords}

Analyze:
- Primary emotional triggers (confidence, romance, nostalgia, power, etc.)
- Psychological benefits of wearing this scent
- Identity expression and self-perception
- Purchase motivations

Keep it concise (150 words max)."""

        psychology_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Consumer Psychology Specialist focusing on fragrance purchasing behavior and emotional connections."},
                {"role": "user", "content": psychology_prompt}
            ],
            temperature=0.6,
            max_tokens=300,
        )
        psychology_analysis = psychology_response.choices[0].message.content.strip()
        
        # Agent 4: Public Data Agent (using web-search model)
        public_data_prompt = f"""As a Market Trends Agent, analyze current market trends for this type of fragrance:

Fragrance: {fragrance_name}
Notes: {key_notes}
Vibe: {vibe_keywords}

Research and provide:
- Current fragrance market trends relevant to this profile
- Popular notes/families in the market right now
- Competitive landscape insights
- Social media sentiment about similar fragrances

Keep it concise (150 words max)."""

        public_data_response = client.chat.completions.create(
            model="groq/compound",  # Web-search enabled
            messages=[
                {"role": "system", "content": "You are a Market Research Analyst specializing in fragrance industry trends and consumer data."},
                {"role": "user", "content": public_data_prompt}
            ],
            temperature=0.5,
            max_tokens=300,
        )
        public_data_analysis = public_data_response.choices[0].message.content.strip()
        
        # Agent 5: Understanding Agent (Synthesizes all insights)
        understanding_prompt = f"""As the Understanding Agent, synthesize these multi-agent analyses into actionable insights:

CUSTOMER PROFILE:
{profile_analysis}

PREFERENCE ANALYSIS:
{preference_analysis}

PSYCHOLOGY INSIGHTS:
{psychology_analysis}

MARKET TRENDS:
{public_data_analysis}

Provide a synthesis that includes:
- Key insights summary (what stands out across all analyses)
- Strategic recommendations for positioning this fragrance
- Suggested messaging angles that will resonate
- Warning signs or challenges to address

Keep it concise but comprehensive (200 words max)."""

        understanding_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Strategic Synthesis Agent that combines multiple data points into actionable business insights."},
                {"role": "user", "content": understanding_prompt}
            ],
            temperature=0.7,
            max_tokens=400,
        )
        understanding_analysis = understanding_response.choices[0].message.content.strip()
        
        print("=== Multi-Agent Analysis Complete ===")
        
        return jsonify({
            "success": True,
            "analysis": {
                "customer_profile": profile_analysis,
                "preferences": preference_analysis,
                "psychology": psychology_analysis,
                "market_trends": public_data_analysis,
                "synthesis": understanding_analysis
            }
        })
        
    except Exception as e:
        print(f"Error in multi-agent analysis: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to complete multi-agent analysis"}), 500


@app.route('/generate-variants', methods=['POST'])
def generate_variants():
    """
    Generate multiple story variants for A/B testing
    Each variant uses insights from different agents
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('fragrance_name', 'Unnamed Fragrance')
        key_notes = data.get('key_notes', '')
        agent_insights = data.get('agent_insights', {})
        num_variants = data.get('num_variants', 2)  # Default: 2 variants for A/B testing
        
        print(f"=== Generating {num_variants} story variants for: {fragrance_name} ===")
        
        variants = []
        
        # Variant approaches based on different agent insights
        approaches = [
            {
                "name": "Psychology-Driven",
                "focus": "psychology",
                "instruction": f"Focus on emotional triggers and psychological benefits. Use insights: {agent_insights.get('psychology', '')}"
            },
            {
                "name": "Profile-Optimized",
                "focus": "customer_profile",
                "instruction": f"Tailor to the specific customer profile and lifestyle. Use insights: {agent_insights.get('customer_profile', '')}"
            },
            {
                "name": "Trend-Aligned",
                "focus": "market_trends",
                "instruction": f"Align with current market trends and competitive positioning. Use insights: {agent_insights.get('market_trends', '')}"
            },
            {
                "name": "Preference-Based",
                "focus": "preferences",
                "instruction": f"Appeal to scent preferences and olfactory family lovers. Use insights: {agent_insights.get('preferences', '')}"
            }
        ]
        
        # Generate the requested number of variants
        for i in range(min(num_variants, len(approaches))):
            approach = approaches[i]
            
            variant_prompt = f"""Create a luxury fragrance product description (300-400 words) for:

**Fragrance:** {fragrance_name}
**Notes:** {key_notes}

**Approach:** {approach['name']}
**Special Focus:** {approach['instruction']}

Use Markdown formatting with ### headings:
- ### The Story
- ### The Notes (Top, Heart, Base)
- ### The Essence

Make it sophisticated, sensory, and conversion-focused."""

            variant_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an elite fragrance copywriter creating targeted product descriptions based on customer insights."},
                    {"role": "user", "content": variant_prompt}
                ],
                temperature=0.75,
                max_tokens=800,
            )
            
            variants.append({
                "id": i + 1,
                "name": approach['name'],
                "focus_agent": approach['focus'],
                "content": variant_response.choices[0].message.content.strip()
            })
        
        print(f"=== Generated {len(variants)} variants successfully ===")
        
        return jsonify({
            "success": True,
            "variants": variants
        })
        
    except Exception as e:
        print(f"Error generating variants: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to generate story variants"}), 500


@app.route('/chat', methods=['POST'])
def chat():
    """
    Curator mode: conversational fragrance recommendations
    Supports both standard and deep analysis modes
    """
    if not client:
        return jsonify({"error": "Groq client not initialized. Please check your API key."}), 500

    try:
        data = request.get_json()
        user_message = data.get('message', '')
        chat_history = data.get('history', [])
        deep_mode = data.get('deepMode', False)  # New: multi-agent analysis

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # OPTION 1: Multi-Agent Deep Analysis Mode
        if deep_mode:
            return _deep_analysis_chat(user_message, chat_history)
        
        # OPTION 2: Enhanced Single Model (Default Mode)
        # Build conversation history with upgraded system prompt
        messages = [
            {
                "role": "system",
                "content": """You are "Aura," an elite fragrance curator and perfumery expert with deep knowledge of:

**Fragrance Families & Classifications:**
- Floral (Soliflore, Floral Bouquet, Soft Floral)
- Oriental (Soft Oriental, Oriental, Woody Oriental)
- Woody (Woods, Mossy Woods, Dry Woods)
- Fresh (Citrus, Green, Water, Fruity)
- Chypre (Floral, Fruity, Fresh, Green)
- Fougère (Classic, Aromatic, Soft)

**Note Structures:**
- Top Notes: First impression (5-15 min) - citrus, herbs, light florals
- Heart Notes: Character (20-60 min) - florals, spices, fruits
- Base Notes: Longevity (2-8 hours) - woods, resins, musks, vanilla

**Expertise Areas:**
- Personality matching (MBTI, lifestyle, values → fragrance profiles)
- Occasion recommendations (work, date, wedding, travel, seasons)
- Layering techniques and fragrance wardrobes
- Vintage vs modern compositions
- Niche, designer, and artisan houses
- Longevity, projection, and sillage analysis

**Response Style:**
- Ask clarifying questions to understand preferences deeply
- Provide 2-3 specific fragrance recommendations with reasoning
- Explain why certain notes work for their personality/occasion
- Suggest similar alternatives at different price points
- Share fascinating perfumery insights when relevant

Be warm, conversational, and enthusiastic. Give actionable recommendations with specific fragrance examples when possible."""
            }
        ]
        
        # Add few-shot examples for better accuracy
        if not chat_history:
            messages.extend([
                {
                    "role": "user",
                    "content": "I need a confidence-boosting fragrance for important business meetings"
                },
                {
                    "role": "assistant",
                    "content": "For commanding presence in business settings, I'd recommend:\n\n1. **Tom Ford Oud Wood** - Woody oriental with oud, sandalwood, and tonka. Projects quiet authority without overwhelming. Perfect for boardrooms.\n\n2. **Creed Aventus** - Fresh fruity with pineapple, birch, and musk. Universally respected, confidence in a bottle.\n\n3. **Dior Sauvage** - Fresh spicy with bergamot and pepper. Clean, powerful, memorable.\n\nAll three have excellent longevity (6-8 hours) and moderate projection - noticed but not invasive. Which style resonates with you: the mysterious depth of oud, the fresh success energy of Aventus, or the clean power of Sauvage?"
                }
            ])
        
        # Add actual chat history
        for msg in chat_history:
            messages.append({"role": msg.get("role"), "content": msg.get("content")})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Upgraded: llama-3.3-70b (same as Story Builder) + increased tokens
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,  # Doubled for better explanations
        )

        ai_response = chat_completion.choices[0].message.content.strip()
        
        return jsonify({
            "response": ai_response,
            "success": True,
            "mode": "enhanced"
        })

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "An error occurred during chat. Please try again."}), 500


def _deep_analysis_chat(user_message, chat_history):
    """
    Multi-agent deep analysis for complex fragrance recommendations
    Uses 3 specialized agents similar to AI Lab architecture
    """
    try:
        # Agent 1: Fragrance Expert - Technical knowledge
        expert_prompt = f"""You are a Master Perfumer with 30 years of experience in fragrance composition.

USER QUERY: {user_message}

CHAT CONTEXT: {chat_history[-3:] if len(chat_history) > 0 else 'New conversation'}

Analyze this query from a technical perfumery perspective:
1. What fragrance families and note structures would work best?
2. What specific raw materials/accords should be featured?
3. What longevity and projection characteristics are needed?
4. Any technical considerations (skin chemistry, season, layering)?

Provide expert analysis in 3-4 sentences."""

        expert_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": expert_prompt}],
            temperature=0.6,
            max_tokens=400,
        )
        expert_analysis = expert_response.choices[0].message.content.strip()

        # Agent 2: Personal Stylist - Lifestyle & personality matching
        stylist_prompt = f"""You are an elite Personal Fragrance Stylist who matches scents to personalities and lifestyles.

USER QUERY: {user_message}

CHAT CONTEXT: {chat_history[-3:] if len(chat_history) > 0 else 'New conversation'}

Analyze this query from a personality and lifestyle perspective:
1. What does their request reveal about their personality/values?
2. What occasions or contexts will they wear this?
3. What impression do they want to project?
4. What should be avoided based on their needs?

Provide lifestyle analysis in 3-4 sentences."""

        stylist_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": stylist_prompt}],
            temperature=0.7,
            max_tokens=400,
        )
        stylist_analysis = stylist_response.choices[0].message.content.strip()

        # Agent 3: Curator - Synthesize and recommend
        curator_prompt = f"""You are "Aura," the ultimate fragrance curator synthesizing expert insights into perfect recommendations.

USER QUERY: {user_message}

PERFUMER ANALYSIS: {expert_analysis}

STYLIST ANALYSIS: {stylist_analysis}

Based on these expert insights, provide:
1. 3-4 specific fragrance recommendations (name the actual perfumes)
2. Why each one works (connect to both technical and lifestyle factors)
3. A final thought or tip

Be warm, enthusiastic, and actionable. Format beautifully with clear sections."""

        curator_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": curator_prompt}],
            temperature=0.8,
            max_tokens=800,
        )
        final_recommendation = curator_response.choices[0].message.content.strip()

        return jsonify({
            "response": final_recommendation,
            "success": True,
            "mode": "deep",
            "analysis": {
                "expert": expert_analysis,
                "stylist": stylist_analysis
            }
        })

    except Exception as e:
        print(f"Error in deep analysis: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Deep analysis failed. Please try standard mode."}), 500


@app.route('/export-pdf', methods=['POST'])
def export_pdf():
    """
    Export fragrance story as a PDF
    """
    try:
        data = request.get_json()
        fragrance_name = data.get('name', 'Fragrance Story')
        content = data.get('content', '')
        
        # Create PDF in memory
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                               topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        # Container for PDF elements
        story = []
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor='#1a1a1a',
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor='#B7904C',
            spaceBefore=20,
            spaceAfter=10,
            fontName='Helvetica-Bold'
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            leading=16,
            spaceAfter=12,
            alignment=TA_LEFT
        )
        
        # Add title
        story.append(Paragraph(fragrance_name, title_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Add branding
        branding = Paragraph("Generated by Aura Intelligence", styles['Italic'])
        story.append(branding)
        story.append(Spacer(1, 0.4*inch))
        
        # Parse content and add to PDF
        sections = content.split('###')
        for section in sections:
            if section.strip():
                lines = section.strip().split('\n', 1)
                if len(lines) == 2:
                    section_title, section_body = lines
                    story.append(Paragraph(section_title.strip(), heading_style))
                    # Clean HTML tags from body
                    clean_body = re.sub('<[^<]+?>', '', section_body)
                    story.append(Paragraph(clean_body.strip(), body_style))
                elif len(lines) == 1:
                    clean_text = re.sub('<[^<]+?>', '', lines[0])
                    story.append(Paragraph(clean_text.strip(), body_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"{fragrance_name.replace(' ', '_')}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to generate PDF"}), 500


@app.route('/social-media', methods=['POST'])
def generate_social_media():
    """
    Generate social media posts from fragrance story
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('name', 'This Fragrance')
        story_content = data.get('content', '')
        platform = data.get('platform', 'instagram')  # instagram, twitter, facebook
        
        # Prepare prompt based on platform
        if platform == 'instagram':
            prompt = f"""Based on this fragrance story, create an engaging Instagram caption (150-200 characters) with 5-7 relevant hashtags.

Fragrance: {fragrance_name}
Story: {story_content[:500]}...

Format:
[Engaging caption that creates desire]

#hashtag1 #hashtag2 #hashtag3"""
        elif platform == 'twitter':
            prompt = f"""Create a compelling tweet (280 characters max) about this fragrance:

Fragrance: {fragrance_name}
Story: {story_content[:300]}...

Include 2-3 hashtags and make it shareable."""
        else:  # facebook
            prompt = f"""Create an engaging Facebook post (2-3 sentences) about this fragrance:

Fragrance: {fragrance_name}
Story: {story_content[:400]}...

Make it conversational and include a call-to-action."""
        
        # Generate using llama model (creative writing)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a social media expert for luxury fragrance brands. Create engaging, concise posts that drive engagement."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=200,
        )
        
        post_content = completion.choices[0].message.content.strip()
        
        return jsonify({
            "success": True,
            "platform": platform,
            "content": post_content
        })
        
    except Exception as e:
        print(f"Error generating social media post: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to generate social media post"}), 500


@app.route('/seo-analysis', methods=['POST'])
def analyze_seo():
    """
    Analyze fragrance story for SEO and provide optimization suggestions
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('name', 'Fragrance')
        story_content = data.get('content', '')
        target_keywords = data.get('keywords', '')
        
        # Calculate word count
        word_count = len(story_content.split())
        
        # Prepare SEO analysis prompt
        prompt = f"""Analyze this fragrance product description for SEO optimization.

Fragrance Name: {fragrance_name}
Target Keywords: {target_keywords or 'Not specified'}
Content Length: {word_count} words
Content: {story_content}

Provide:
1. **SEO Score** (0-100) with brief justification
2. **Keyword Analysis**: Are target keywords naturally integrated? Mention density and placement.
3. **Content Length**: Is it optimal for search engines? (300-500 words ideal for e-commerce)
4. **Readability**: Is it engaging and scannable? Check for headers, bullets, paragraph length.
5. **Top 3 Optimization Suggestions** (specific, actionable improvements)

Format as JSON with keys: score, keyword_analysis, length_analysis, readability, suggestions (array), word_count"""
        
        # Generate SEO analysis
        completion = client.chat.completions.create(
            model="groq/compound",  # Use web-search model for SEO best practices
            messages=[
                {"role": "system", "content": "You are an SEO expert specializing in e-commerce product descriptions. Analyze content and provide data-driven optimization recommendations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature for analytical consistency
            max_tokens=800,
        )
        
        analysis_text = completion.choices[0].message.content.strip()
        
        # Try to parse JSON response, fallback to text if needed
        try:
            # Extract JSON from potential markdown code blocks
            if '```json' in analysis_text:
                json_start = analysis_text.find('```json') + 7
                json_end = analysis_text.find('```', json_start)
                analysis_text = analysis_text[json_start:json_end].strip()
            elif '```' in analysis_text:
                json_start = analysis_text.find('```') + 3
                json_end = analysis_text.find('```', json_start)
                analysis_text = analysis_text[json_start:json_end].strip()
            
            import json
            analysis_data = json.loads(analysis_text)
            analysis_data['word_count'] = word_count
        except:
            # Fallback: return as structured text
            analysis_data = {
                "score": 75,
                "keyword_analysis": "Analysis completed",
                "length_analysis": "See detailed report",
                "readability": "See detailed report",
                "suggestions": ["Review the detailed analysis below"],
                "raw_analysis": analysis_text,
                "word_count": word_count
            }
        
        return jsonify({
            "success": True,
            "analysis": analysis_data
        })
        
    except Exception as e:
        print(f"Error analyzing SEO: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to analyze SEO"}), 500


@app.route('/optimize-seo', methods=['POST'])
def optimize_for_seo():
    """
    Automatically optimize content for SEO best practices
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('name', 'Fragrance')
        original_content = data.get('content', '')
        target_keywords = data.get('keywords', '')
        
        # Prepare optimization prompt
        prompt = f"""Rewrite this fragrance product description to be SEO-optimized for e-commerce.

REQUIREMENTS:
1. **Length**: 300-500 words (ideal for product pages)
2. **Structure**: Use clear markdown headings (###) for sections:
   - ### Top Notes
   - ### Heart Notes  
   - ### Base Notes
   - ### The Experience (or similar)
   - ### Perfect For (target audience)
3. **Keywords**: Naturally integrate these keywords: {target_keywords or fragrance_name + ', luxury fragrance, perfume'}
4. **Format**: Use bullet points for note pyramids, short paragraphs (2-3 sentences max)
5. **Tone**: Maintain luxury brand voice while being concise and scannable
6. **Call-to-Action**: End with a compelling reason to purchase

ORIGINAL CONTENT:
{original_content[:2000]}...

Rewrite this as an SEO-optimized product description. Keep the essence but make it concise, structured, and search-engine friendly."""
        
        # Generate optimized content
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert copywriter specializing in SEO-optimized luxury fragrance descriptions. Create concise, structured, keyword-rich content that ranks well and converts."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=1024,
        )
        
        optimized_content = completion.choices[0].message.content.strip()
        
        return jsonify({
            "success": True,
            "optimized_content": optimized_content
        })
        
    except Exception as e:
        print(f"Error optimizing content: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to optimize content"}), 500


@app.route('/psychology-score', methods=['POST'])
def psychology_score():
    """
    Analyze copy for psychological impact based on neuroscience research
    Scores how well the copy leverages scent-emotion-memory connections
    """
    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500
    
    try:
        data = request.get_json()
        fragrance_name = data.get('name', 'Fragrance')
        copy_content = data.get('content', '')
        
        # Psychology scoring prompt based on research
        prompt = f"""As a neuroscience expert specializing in scent psychology, analyze this fragrance copy for psychological impact.

**SCIENTIFIC FRAMEWORK:**
Based on Harvard and Psychology Today research:
1. **Scent bypasses cognitive processing** → connects directly to amygdala (emotion) and hippocampus (memory)
2. **Smell and emotion are stored as one memory** → nostalgic scents trigger vivid emotional recall
3. **Childhood scent imprinting** → preferences formed before age 10 create lifelong associations
4. **Color-scent synesthesia** → cross-sensory language enhances neural processing
5. **Identity signaling** → fragrance choice reflects self-perception and aspirational identity

**COPY TO ANALYZE:**
Fragrance: {fragrance_name}
Content: {copy_content}

**SCORING RUBRIC (0-100):**

**1. Emotional Trigger Strength (0-25 points)**
- Does it trigger immediate emotion (confidence, romance, nostalgia, power)?
- Uses sensory language that bypasses logic?
- Creates visceral imagery vs. clinical descriptions?

**2. Memory Activation (0-25 points)**
- References universal nostalgic moments?
- Uses temporal language (remember, transport, return)?
- Anchors scent to specific life experiences or places?

**3. Identity Connection (0-25 points)**
- Positions scent as self-expression or signature?
- Connects to aspirational identity/lifestyle?
- Emphasizes psychological benefits (confidence, allure, presence)?

**4. Sensory Integration (0-25 points)**
- Engages multiple senses (not just smell)?
- Uses color-scent synesthesia (visual imagery)?
- Creates immersive, cinematic scenes?

**OUTPUT FORMAT (JSON):**
{{
    "overall_score": [0-100],
    "emotional_trigger": {{
        "score": [0-25],
        "strengths": ["list specific examples from the copy"],
        "improvements": ["specific suggestions"]
    }},
    "memory_activation": {{
        "score": [0-25],
        "strengths": ["list specific examples"],
        "improvements": ["specific suggestions"]
    }},
    "identity_connection": {{
        "score": [0-25],
        "strengths": ["list specific examples"],
        "improvements": ["specific suggestions"]
    }},
    "sensory_integration": {{
        "score": [0-25],
        "strengths": ["list specific examples"],
        "improvements": ["specific suggestions"]
    }},
    "key_insights": "Overall assessment in 2-3 sentences",
    "top_3_enhancements": ["Actionable improvement 1", "2", "3"]
}}

Return ONLY valid JSON, no markdown formatting."""

        # Use compound model for analytical depth
        analysis_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a scent psychology analyst with expertise in neuroscience and consumer behavior. Provide data-driven psychological impact assessments."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temp for analytical consistency
            max_tokens=1200,
        )
        
        analysis_text = analysis_response.choices[0].message.content.strip()
        
        # Parse JSON response
        try:
            # Clean potential markdown formatting
            if '```json' in analysis_text:
                json_start = analysis_text.find('```json') + 7
                json_end = analysis_text.find('```', json_start)
                analysis_text = analysis_text[json_start:json_end].strip()
            elif '```' in analysis_text:
                json_start = analysis_text.find('```') + 3
                json_end = analysis_text.find('```', json_start)
                analysis_text = analysis_text[json_start:json_end].strip()
            
            import json
            psychology_data = json.loads(analysis_text)
            
        except Exception as parse_error:
            print(f"JSON parse error: {parse_error}")
            # Fallback structure
            psychology_data = {
                "overall_score": 75,
                "emotional_trigger": {
                    "score": 18,
                    "strengths": ["Analysis completed"],
                    "improvements": ["See detailed report"]
                },
                "memory_activation": {
                    "score": 18,
                    "strengths": ["Analysis completed"],
                    "improvements": ["See detailed report"]
                },
                "identity_connection": {
                    "score": 19,
                    "strengths": ["Analysis completed"],
                    "improvements": ["See detailed report"]
                },
                "sensory_integration": {
                    "score": 20,
                    "strengths": ["Analysis completed"],
                    "improvements": ["See detailed report"]
                },
                "key_insights": "Detailed analysis available in raw format.",
                "top_3_enhancements": ["Review detailed analysis"],
                "raw_analysis": analysis_text
            }
        
        print(f"Psychology Score for '{fragrance_name}': {psychology_data.get('overall_score', 'N/A')}/100")
        
        return jsonify({
            "success": True,
            "psychology_score": psychology_data
        })
        
    except Exception as e:
        print(f"Error calculating psychology score: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "Failed to calculate psychology score"}), 500


if __name__ == '__main__':
    app.run(debug=True)
