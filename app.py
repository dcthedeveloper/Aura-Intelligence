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

@app.route('/generate', methods=['POST'])
def generate():
    if not client:
        return Response("Groq client not initialized. Please check your API key.", status=500)

    # Extract form data
    use_case = request.form.get('use_case', 'existing')
    product_name = request.form.get('product_name', 'Unnamed Fragrance')
    key_notes = request.form.get('key_notes', 'Not specified')
    vibe_keywords = request.form.get('vibe_keywords', 'Elegant and mysterious')
    target_audience = request.form.get('target_audience', 'A discerning individual')
    storytelling_angle = request.form.get('storytelling_angle', 'An elegant evening')
    brand_voice = request.form.get('brand_voice', '')
    competitor_text = request.form.get('competitor_text', '')
    seo_keywords = request.form.get('seo_keywords', '')
    tone = request.form.get('tone', 'Poetic & Evocative')

    system_prompt = f"""
# ROLE & EXPERTISE
You are "Aura," an elite AI-powered Niche Fragrance Copywriter and Olfactory Storyteller. Your expertise combines the art of a master perfumer, the science of sensory psychology, and the skill of a direct-response copywriter. You don't just list notes; you translate scents into identities, memories, and aspirations. If the user provides a name of a real fragrance, you MUST use your internal knowledge to recall its actual notes if they are not provided.

# CORE OBJECTIVE
Generate a psychologically resonant, emotionally evocative, and commercially effective multi-part story for a niche fragrance based on the provided inputs.

# INPUT VARIABLES
- Fragrance Name: {product_name}
- Use Case: {"Describing a new creation" if use_case == "new" else "Re-interpreting an existing fragrance"}
- Olfactory Notes: {key_notes}
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
            # MODEL UPGRADED FOR ACCURACY
            stream_response = client.chat.completions.create(
                model="llama3-70b-8192", # Using the larger, more knowledgeable model
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
            # Using compound model for web search
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
