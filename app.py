import os
import traceback
from flask import Flask, request, render_template, Response, stream_with_context, jsonify
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

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

    # Determine key notes robustly
    final_key_notes = key_notes_input
    if use_case == 'existing' and not key_notes_input:
        final_key_notes = get_accurate_notes(product_name)
    elif not key_notes_input:
        final_key_notes = "Not specified"

    print("Final used notes:", final_key_notes)

    # Compose the system prompt
    system_prompt = f"""
# ROLE & EXPERTISE
You are "Aura," an elite AI-powered Niche Fragrance Copywriter. Your expertise combines the art of a master perfumer with the skill of a direct-response copywriter.

# Note Accuracy
You have been provided with the definitive olfactory notes. Use these as the source of truth.

# CORE OBJECTIVE
Generate a multi-part story for a niche fragrance. Use the provided info.

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

# OUTPUT STRUCTURE
Output Markdown sections starting with '###' (e.g., '### The Hook', '### The Olfactory Journey').
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
                max_tokens=1024,
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


@app.route('/chat', methods=['POST'])
def chat():
    """
    Curator mode: conversational fragrance recommendations
    """
    if not client:
        return jsonify({"error": "Groq client not initialized. Please check your API key."}), 500

    try:
        data = request.get_json()
        user_message = data.get('message', '')
        chat_history = data.get('history', [])

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Build conversation history
        messages = [
            {
                "role": "system",
                "content": """You are "Aura," a knowledgeable fragrance curator and expert. 
You help users discover fragrances based on their preferences, occasions, and tastes.
Provide personalized recommendations, explain fragrance families, suggest similar scents, 
and share insights about perfumery. Be conversational, enthusiastic, and helpful.
Keep responses concise but informative."""
            }
        ]
        
        # Add chat history
        for msg in chat_history:
            messages.append({"role": msg.get("role"), "content": msg.get("content")})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Get AI response using groq/compound for web-search capabilities
        chat_completion = client.chat.completions.create(
            model="groq/compound",
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )

        ai_response = chat_completion.choices[0].message.content.strip()
        
        return jsonify({
            "response": ai_response,
            "success": True
        })

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        print(traceback.format_exc())
        return jsonify({"error": "An error occurred during chat. Please try again."}), 500


if __name__ == '__main__':
    app.run(debug=True)
