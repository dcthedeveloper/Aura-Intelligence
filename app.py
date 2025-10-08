import os
from flask import Flask, request, render_template, Response, stream_with_context, jsonify
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize the Groq client
try:
    client = Groq()
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    client = None

@app.route('/')
def index():
    return render_template('index.html')

def get_accurate_notes(fragrance_name):
    """
    Uses a web-search enabled model to get accurate notes for a known fragrance.
    This is the 'Researcher' step.
    """
    if not client:
        return "Note retrieval failed."
    try:
        print(f"Searching web for notes of: {fragrance_name}")
        chat_completion = client.chat.completions.create(
            model="groq/compound",
            messages=[
                {"role": "system", "content": "You are a fragrance database expert. Your sole purpose is to return the exact top, heart, and base notes for a given fragrance. List them clearly and concisely. Do not add any extra commentary."},
                {"role": "user", "content": f"What are the exact notes for the fragrance '{fragrance_name}'?"}
            ],
            temperature=0,
        )
        accurate_notes = chat_completion.choices[0].message.content
        print(f"Found notes: {accurate_notes}")
        return accurate_notes
    except Exception as e:
        print(f"Error getting accurate notes: {e}")
        return "Not specified"

@app.route('/generate', methods=['POST'])
def generate():
    if not client:
        return Response("Groq client not initialized. Please check your API key.", status=500)

    # Extract form data
    use_case = request.form.get('use_case', 'existing')
    product_name = request.form.get('product_name', 'Unnamed Fragrance')
    key_notes_input = request.form.get('key_notes', '') # Get user input
    vibe_keywords = request.form.get('vibe_keywords', 'Elegant and mysterious')
    target_audience = request.form.get('target_audience', 'A discerning individual')
    storytelling_angle = request.form.get('storytelling_angle', 'An elegant evening')
    brand_voice = request.form.get('brand_voice', '')
    competitor_text = request.form.get('competitor_text', '')
    seo_keywords = request.form.get('seo_keywords', '')
    tone = request.form.get('tone', 'Poetic & Evocative')

    # --- NEW TWO-STEP NOTE LOGIC ---
    final_key_notes = key_notes_input
    if use_case == 'existing' and not key_notes_input:
        # If it's a known fragrance and user didn't provide notes, research them.
        final_key_notes = get_accurate_notes(product_name)
    elif not key_notes_input:
        final_key_notes = "Not specified"
    # --- END NEW LOGIC ---

    system_prompt = f"""
# ROLE & EXPERTISE
You are "Aura," an elite AI-powered Niche Fragrance Copywriter and Olfactory Storyteller. You are an expert in translating scents into identities.

# CRITICAL INSTRUCTION
You have been provided with the definitive olfactory notes for this fragrance. You MUST use these notes as the single source of truth for the olfactory journey. Your credibility depends on accurately describing these specific notes.

# CORE OBJECTIVE
Generate a psychologically resonant, emotionally evocative, and commercially effective multi-part story for a niche fragrance based on the provided inputs.

# INPUT VARIABLES
- Fragrance Name: {product_name}
- Use Case: {"Describing a new creation" if use_case == "new" else "Re-interpreting an existing fragrance"}
- Olfactory Notes: {final_key_notes}
- Desired Vibe: {vibe_keywords}
- Wearer's Persona: {target_audience}
- Narrative Scene: {storytelling_angle}
- Brand Voice Examples: {'"'+brand_voice+'"' if brand_voice else 'Not provided'}
- Competitor's Story (to differentiate from): {'"'+competitor_text+'"' if competitor_text else 'Not provided'}
- Target SEO Keywords: {seo_keywords if seo_keywords else 'Not provided'}
- WRITING STYLE / TONE: {tone}

# MANDATORY OUTPUT STRUCTURE
You MUST generate the output in clean Markdown. The response must be broken into several distinct sections, with each section starting with '###' followed by a title. Adhere strictly to this format. Example sections include: '### The Hook', '### The Olfactory Journey', '### Who You Become', '### Wear It When'. DO NOT use bolding or asterisks on the '###' titles.
"""
    user_prompt = "Craft the olfactory story."
    
    def stream():
        try:
            # This is the 'Writer' step, now using the correct model
            stream_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=True,
            )
            for chunk in stream_response:
                yield chunk.choices[0].delta.content or ""
        except Exception as e:
            print(f"Error during stream generation: {e}")
            yield "An error occurred during generation. Please check the server logs."

    return Response(stream_with_context(stream()), content_type='text/event-stream')


# CHATBOT ENDPOINT
@app.route('/chat', methods=['POST'])
def chat():
    if not client:
        return jsonify({"error": "Groq client not initialized."}), 500

    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "No message provided."}), 400

    chat_system_prompt = """
You are "Aura Curator," a sophisticated fragrance expert and curator with deep knowledge of niche perfumery. Your capabilities include searching the web for current fragrance information, discovering scents, creating curated collections, and comparing fragrance profiles. Always provide specific names, houses, and key notes, and explain your reasoning. Your tone is refined, knowledgeable, and conversational.
"""
    
    def stream():
        try:
            stream_response = client.chat.completions.create(
                model="groq/compound",
                messages=[
                    {"role": "system", "content": chat_system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.6,
                max_tokens=2048,
                top_p=1,
                stop=None,
                stream=True,
            )
            for chunk in stream_response:
                yield chunk.choices[0].delta.content or ""
        except Exception as e:
            print(f"Error during chat stream: {e}")
            yield "My apologies, I'm having trouble connecting. Please try again."

    return Response(stream_with_context(stream()), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
