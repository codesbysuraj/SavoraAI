from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json
from groq import Groq

# Load environment variables
load_dotenv(override=True)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configure Groq API
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    print("WARNING: GROQ_API_KEY not found in environment variables!")
else:
    print(f"GROQ_API_KEY loaded successfully (starts with: {api_key[:10]}...)")

# Initialize Groq client
client = Groq(api_key=api_key)
MODEL = "llama-3.1-8b-instant"  # Fast and free model

def generate_completion(prompt, temperature=0.7, max_tokens=2000):
    """Helper function to generate completion from Groq API"""
    try:
        if not api_key:
            raise Exception("GROQ_API_KEY is not set in .env file. Please add your Groq API key.")
        
        print(f"\n=== Groq Request ===")
        print(f"Model: {MODEL}")
        print(f"Temperature: {temperature}")
        print(f"Max tokens: {max_tokens}")
        
        # Generate content using Groq
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        response_text = response.choices[0].message.content
        if not response_text:
            raise Exception("Groq API returned empty response")
        
        print(f"\n=== Groq Response ===")
        print(f"Status: Success")
        print(f"Response: {response_text[:500]}...")
        
        return response_text
    except Exception as e:
        print(f"Groq API error details: {str(e)}")
        import traceback
        traceback.print_exc()
        raise Exception(f"Groq API error: {str(e)}")

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to SAVORA AI Backend API - Powered by Groq',
        'status': 'running',
        'model': MODEL,
        'api_provider': 'Groq',
        'api_provider': 'Google Generative AI',
        'endpoints': {
            '/generate': 'POST - Generate recipe from ingredients',
            '/chat': 'POST - Chat with recipe assistant',
            '/rescue': 'POST - Get help fixing cooking problems',
            '/nutrition': 'POST - Get nutrition information',
            '/meal-plan': 'POST - Generate weekly meal plan',
            '/health': 'GET - Health check'
        }
    })

@app.route('/generate', methods=['POST'])
def generate_recipe():
    """
    Generate recipe based on user inputs
    Expected JSON: {ingredients, cuisine, taste, mealType, portion, dietary, spiceLevel, cookingTime}
    """
    try:
        data = request.json
        ingredients = data.get('ingredients', [])
        cuisine = data.get('cuisine', 'Any')
        taste = data.get('taste', 'Any')
        meal_type = data.get('mealType', 'Any')
        portion = data.get('portion', '2-3 people')
        dietary = data.get('dietary', 'None')
        spice_level = data.get('spiceLevel', 'Medium')
        cooking_time = data.get('cookingTime', 'Any')
        
        # Build comprehensive prompt
        prompt = f"""
You are a professional chef AI assistant. Create a detailed recipe based on these requirements:

INGREDIENTS AVAILABLE: {', '.join(ingredients) if isinstance(ingredients, list) else ingredients}
CUISINE TYPE: {cuisine}
TASTE PREFERENCE: {taste}
MEAL TYPE: {meal_type}
PORTION SIZE: {portion}
DIETARY RESTRICTIONS: {dietary}
SPICE LEVEL: {spice_level}
COOKING TIME: {cooking_time}

Please provide a recipe in this EXACT JSON format (respond with ONLY valid JSON, no markdown):
{{
    "title": "Creative dish name",
    "description": "Brief enticing description of the dish",
    "prepTime": "15 mins",
    "cookTime": "30 mins",
    "totalTime": "45 mins",
    "difficulty": "Easy/Medium/Hard",
    "servings": "{portion}",
    "cuisine": "{cuisine}",
    "ingredients": [
        "Ingredient 1 with measurement",
        "Ingredient 2 with measurement"
    ],
    "instructions": [
        "Step 1 instruction",
        "Step 2 instruction"
    ],
    "tips": [
        "Helpful tip 1",
        "Helpful tip 2"
    ],
    "nutrition": {{
        "calories": "approximate per serving",
        "protein": "approximate",
        "carbs": "approximate",
        "fat": "approximate"
    }},
    "alternatives": [
        "Alternative ingredient suggestion 1",
        "Alternative ingredient suggestion 2"
    ]
}}

Make the recipe creative, practical, and delicious! Ensure it matches the {spice_level} spice level and can be prepared within {cooking_time}. Return ONLY the JSON object, no additional text.
"""
        
        # Generate response from OpenRouter
        recipe_text = generate_completion(prompt, temperature=0.7, max_tokens=2000)
        recipe_text = recipe_text.strip()
        
        # Try to parse as JSON
        try:
            # Remove markdown code blocks if present
            if recipe_text.startswith('```'):
                recipe_text = recipe_text.split('```')[1]
                if recipe_text.startswith('json'):
                    recipe_text = recipe_text[4:]
                recipe_text = recipe_text.strip()
            recipe_json = json.loads(recipe_text)
            
            return jsonify({
                'success': True,
                'recipe': recipe_json,
                'format': 'json'
            })
        except json.JSONDecodeError:
            # Return as text if JSON parsing fails
            return jsonify({
                'success': True,
                'recipe': recipe_text,
                'format': 'text'
            })
    
    except Exception as e:
        print(f"Error in generate_recipe: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chatbot follow-up questions about cooking
    Expected JSON: {question, recipeContext}
    """
    try:
        data = request.json
        question = data.get('question', '')
        recipe_context = data.get('recipeContext', '')
        
        # Build chatbot prompt with recipe context
        prompt = f"""
You are a friendly and helpful cooking assistant named Chef Savora. The user is cooking this recipe:

{json.dumps(recipe_context) if isinstance(recipe_context, dict) else recipe_context}

User's question: {question}

Provide a clear, helpful, and friendly answer to their cooking question. Be concise and practical.
Use emojis occasionally to be more engaging. If you don't know something, be honest about it.
"""
        
        answer = generate_completion(prompt, temperature=0.7, max_tokens=500)
        
        return jsonify({
            'success': True,
            'answer': answer
        })
    
    except Exception as e:
        print(f"Error in chat: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/rescue', methods=['POST'])
def rescue_recipe():
    """
    Rescue My Recipe mode - help fix cooking disasters
    Expected JSON: {problem, dishType}
    """
    try:
        data = request.json
        problem = data.get('problem', '')
        dish_type = data.get('dishType', '')
        
        prompt = f"""
You are an expert chef helping someone fix a cooking problem. Be calm, reassuring, and practical.

DISH TYPE: {dish_type}
PROBLEM: {problem}

Provide immediate, practical solutions to rescue this dish. Be specific and actionable.
Format your response as:

🚨 QUICK FIXES (what to do RIGHT NOW):
[Immediate actions]

🔧 ADJUSTMENTS NEEDED:
[Specific adjustments]

💡 PRO TIP:
[How to prevent this next time]

Be encouraging - most cooking mistakes can be fixed!
"""
        
        solution = generate_completion(prompt, temperature=0.7, max_tokens=800)
        
        return jsonify({
            'success': True,
            'solution': solution
        })
    
    except Exception as e:
        print(f"Error in rescue_recipe: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/nutrition', methods=['POST'])
def get_nutrition():
    """
    Get nutrition information for a recipe or ingredient
    Expected JSON: {recipe or ingredients}
    """
    try:
        data = request.json
        recipe = data.get('recipe', '')
        ingredients = data.get('ingredients', '')
        
        content = recipe if recipe else ingredients
        
        # Extract just the ingredients for faster analysis
        if isinstance(content, dict) and 'ingredients' in content:
            ingredients_list = content.get('ingredients', [])
            servings = content.get('servings', '2-3 people')
        else:
            ingredients_list = content
            servings = '2-3 people'
        
        prompt = f"""Analyze nutrition for these ingredients (serves {servings}):
{ingredients_list}

Return ONLY this JSON:
{{"perServing":{{"calories":250,"protein":"15g","carbs":"30g","fat":"8g","fiber":"4g","sugar":"5g","sodium":"400mg"}},"healthScore":7,"benefits":["benefit1","benefit2"],"tips":"one tip"}}"""
        
        result = generate_completion(prompt, temperature=0.3, max_tokens=400)
        result = result.strip()
        
        try:
            # Clean up response
            if '```' in result:
                result = result.split('```')[1] if '```' in result else result
                if result.startswith('json'):
                    result = result[4:]
                result = result.strip()
            
            # Find JSON in response
            start = result.find('{')
            end = result.rfind('}') + 1
            if start != -1 and end > start:
                result = result[start:end]
            
            nutrition_json = json.loads(result)
            return jsonify({
                'success': True,
                'nutrition': nutrition_json
            })
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}, raw result: {result}")
            # Return a default structure
            return jsonify({
                'success': True,
                'nutrition': {
                    'perServing': {
                        'calories': '~300',
                        'protein': '~20g',
                        'carbs': '~35g',
                        'fat': '~12g'
                    },
                    'healthScore': 7,
                    'benefits': ['Balanced macros'],
                    'tips': 'Add more vegetables for extra fiber'
                }
            })
    
    except Exception as e:
        print(f"Error in get_nutrition: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/meal-plan', methods=['POST'])
def generate_meal_plan():
    """
    Generate a weekly meal plan
    Expected JSON: {preferences, dietary, peopleCount}
    """
    try:
        data = request.json
        preferences = data.get('preferences', 'balanced')
        dietary = data.get('dietary', 'none')
        people_count = data.get('peopleCount', 2)
        
        prompt = f"""
Create a 7-day meal plan with the following requirements:

PREFERENCES: {preferences}
DIETARY RESTRICTIONS: {dietary}
SERVINGS: {people_count} people

Provide a meal plan in this JSON format:
{{
    "weekPlan": [
        {{
            "day": "Monday",
            "breakfast": {{"name": "dish name", "quickDescription": "brief description"}},
            "lunch": {{"name": "dish name", "quickDescription": "brief description"}},
            "dinner": {{"name": "dish name", "quickDescription": "brief description"}},
            "snack": {{"name": "snack name", "quickDescription": "brief description"}}
        }}
    ],
    "shoppingList": ["ingredient 1", "ingredient 2"],
    "tips": ["meal prep tip 1", "meal prep tip 2"]
}}

Make it varied, nutritious, and practical. Return ONLY valid JSON.
"""
        
        result = generate_completion(prompt, temperature=0.7, max_tokens=3000)
        result = result.strip()
        
        try:
            if result.startswith('```'):
                result = result.split('```')[1]
                if result.startswith('json'):
                    result = result[4:]
                result = result.strip()
            meal_plan_json = json.loads(result)
            return jsonify({
                'success': True,
                'mealPlan': meal_plan_json
            })
        except json.JSONDecodeError:
            return jsonify({
                'success': True,
                'mealPlan': result
            })
    
    except Exception as e:
        print(f"Error in generate_meal_plan: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/suggest-ingredients', methods=['POST'])
def suggest_ingredients():
    """
    Suggest complementary ingredients based on what user has
    """
    try:
        data = request.json
        current_ingredients = data.get('ingredients', [])
        
        prompt = f"""
The user has these ingredients: {', '.join(current_ingredients) if isinstance(current_ingredients, list) else current_ingredients}

Suggest 5-8 complementary ingredients that would pair well to make delicious dishes.
Return as a JSON array of objects:
[
    {{"ingredient": "name", "reason": "why it pairs well", "dishes": ["possible dish 1", "possible dish 2"]}}
]

Return ONLY valid JSON.
"""
        
        result = generate_completion(prompt, temperature=0.7, max_tokens=1000)
        result = result.strip()
        
        try:
            if result.startswith('```'):
                result = result.split('```')[1]
                if result.startswith('json'):
                    result = result[4:]
                result = result.strip()
            suggestions = json.loads(result)
            return jsonify({
                'success': True,
                'suggestions': suggestions
            })
        except json.JSONDecodeError:
            return jsonify({
                'success': True,
                'suggestions': result
            })
    
    except Exception as e:
        print(f"Error in suggest_ingredients: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'api_configured': api_key is not None,
        'model': MODEL,
        'api_provider': 'Google Generative AI'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
