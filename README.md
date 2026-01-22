<div align="center">

# 🍳 SAVORA AI

### Transform Your Kitchen Ingredients Into Delicious Recipes

*An intelligent recipe generator powered by AI that creates personalized meals based on what you already have at home*

[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-v10-FFCA28?style=for-the-badge&logo=firebase&logoColor=white)](https://firebase.google.com/)
[![Google Gemma](https://img.shields.io/badge/Google_Gemma-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Tech Stack](#tech-stack)

</div>

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🤖 **AI-Powered Generation**
Generate custom recipes using Google Gemma's advanced AI model through OpenRouter API.

### 🎤 **Voice Recognition**
Speak your ingredients - our voice input feature converts speech to text seamlessly.

### 💾 **Smart Storage**
Save favorite recipes and access your complete recipe history anytime.

</td>
<td width="50%">

### 💬 **Interactive Assistant**
Get instant cooking help, substitution suggestions, and tips from our AI chatbot.

### 🔐 **Secure Authentication**
Firebase-powered authentication with Google Sign-In for seamless access.

### 🎛️ **Advanced Filters**
Customize by cuisine type, dietary restrictions, spice levels, portion sizes, and more.

</td>
</tr>
</table>

---

## 🎬 Demo

> **Note:** This project is for educational and portfolio purposes. 

**What makes SAVORA AI special:**
- Real-time recipe generation based on available ingredients
- Multi-cuisine support (Indian, Chinese, Italian, Mexican, Thai, and more)
- Dietary restriction awareness (Vegetarian, Vegan, Gluten-Free, etc.)
- Smart spice level customization
- Cooking time estimation
- Nutritional information and meal planning

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 16+** - [Download](https://nodejs.org/)
- **Firebase Account** - [Sign up](https://firebase.google.com/)
- **OpenRouter API Key** - [Get yours](https://openrouter.ai/)

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
│  🛠️ Tech Stack

<table>
<tr>
<td align="center" width="50%">

**Frontend**
- ⚛️ React 18
- ⚡ Vite
- 🔥 Firebase (Auth & Firestore)
- 🎤 Web Speech API
- 🎨 Custom CSS

</td>
<td align="center" width="50%">

**Backend**
- 🐍 Flask
- 🌐 Flask-CORS
- 🤖 OpenRouter API
- 🧠 Google Gemma 2 9B IT
- 🔐 Python dotenv

</td>
</tr>
</table>
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

## 👥 Contributors

This project was collaboratively developed by:

<table>
<tr>
<td align="center">
<a href="https://github.com/codesbysuraj">
<img src="https://github.com/codesbysuraj.png" width="100px" alt="Suraj"/><br />
<b>Suraj</b>
</a>
</td>
<td align="center">
<a href="https://github.com/YashicaThanekar">
<img src="https://github.com/YashicaThanekar.png" width="100px" alt="Yashica Thanekar"/><br />
<b>Yashica Thanekar</b>
</a>
</td>
</tr>
</table>

## 🤝 Contributing

We appreciate feedback and suggestions! If you find any bugs or have ideas for improvements:

1. Open an issue describing the bug or feature request
2. Feel free to fork and experiment
3. Share your feedback

## 📜 License & Usage

**© 2026 Suraj & Yashica Thanekar. All Rights Reserved.**

This project is provided for **educational and demonstration purposes only**. 

⚠️ **Usage Restrictions:**
- You may **view and study** the code for learning purposes
- You may **not redistribute, modify, or use** this code for commercial purposes
- You may **not claim** this work as your own
- **Contact us** for permission if you wish to use any part of this project

For collaboration or licensing inquiries, please open an issue or reach out directly.

---

<div align="center">

**Made with ❤️ by [Suraj](https://github.com/codesbysuraj) & [Yashica Thanekar](https://github.com/YashicaThanekar)**

If you found this project interesting, give it a ⭐!

[Report Bug](https://github.com/codesbysuraj/SavoraAI/issues) • [Request Feature](https://github.com/codesbysuraj/SavoraAI/issues)

</div>oints:

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
