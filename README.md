# SAVORA AI 🍳

A smart recipe generator that helps you create meals from whatever ingredients you have at home. Built with React, Flask, and Google Gemma AI.

## What it does

This app generates personalized recipes based on what you have in your kitchen. Just enter your ingredients, set your preferences (cuisine type, spice level, dietary restrictions), and get AI-generated recipes with step-by-step instructions.

**Key features:**
- AI recipe generation using Google Gemma
- Voice input for ingredients
- Save your favorite recipes
- Recipe history tracking
- Interactive cooking chatbot
- Firebase authentication with Google Sign-In
- Filters for cuisine, meal type, portion size, and dietary needs

## Getting Started

**You'll need:**
- Python 3.8 or higher
- Node.js 16 or higher
- A Firebase account
- An OpenRouter API key

### Backend Setup

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
# Copy .env.example to .env
cp .env.example .env

# Edit .env and add your OpenRouter API key
# OPENROUTER_API_KEY=your_api_key_here

# Run the Flask server
python app.py
```

Backend runs on `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Setup environment variables
# Copy .env.example to .env
cp .env.example .env

# Edit .env and add your Firebase credentials
# VITE_FIREBASE_API_KEY=your_firebase_api_key
# VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
# etc...

# Run the development server
npm run dev
```

Frontend runs on `http://localhost:5173`

## API Keys Setup

**OpenRouter API Key:**
1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Go to the Keys section and generate a new key
3. Add it to `backend/.env` file

**Firebase Setup:**
1. Create a project in [Firebase Console](https://console.firebase.google.com/)
2. Enable Authentication (Email/Password and Google Sign-In)
3. Create a Firestore Database
4. Go to Project Settings and add a web app
5. Copy the config values to `frontend/.env`

## Project Structure

```
SavoraAI/
├── backend/
│   ├── app.py              # Flask API server
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Example environment file
│   └── firestore.rules     # Firestore security rules
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main app component
│   │   ├── firebase.js     # Firebase configuration
│   │   ├── pages/          # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── History.jsx
│   │   │   └── Favorites.jsx
│   │   └── components/     # Reusable components
│   │       ├── Navbar.jsx
│   │       ├── RecipeCard.jsx
│   │       ├── Filters.jsx
│   │       ├── VoiceInput.jsx
│   │       └── Chatbot.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── .env.example
│
└── README.md
```

## Tech Stack

**Frontend:** React 18, Vite, Firebase (Auth & Firestore), Web Speech API

**Backend:** Flask, Flask-CORS, OpenRouter API, Google Gemma 2 9B IT, Python dotenv

## Security ⚠️

Don't commit sensitive data to Git. All API keys and credentials should be in `.env` files, which are already ignored by git.

## API Endpoints

The backend API runs on `http://localhost:5000` with these endpoints:

- `GET /` - Health check
- `POST /generate` - Generate recipe from ingredients
- `POST /chat` - Chat with AI assistant
- `POST /rescue` - Get help with cooking problems
- `POST /nutrition` - Get nutrition info
- `POST /meal-plan` - Generate meal plans

## Deployment

**Backend:** Deploy to Heroku, Railway, or Render. Make sure to set your `OPENROUTER_API_KEY` environment variable.

**Frontend:** Deploy to Vercel or Netlify. Build with `npm run build` and deploy the `dist` folder. Don't forget to add all your Firebase environment variables.

## Contributing

Pull requests are welcome. Feel free to open an issue if you find bugs or have suggestions.

## License

MIT License - feel free to use this project however you'd like.
