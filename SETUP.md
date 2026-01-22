# 🔧 Setup Instructions for SAVORA AI

Follow these steps after cloning the repository:

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- Firebase account
- OpenRouter account (for Google Gemma API access)

---

## 🔐 Step 1: Configure Backend Environment Variables

1. Navigate to the `backend/` folder
2. Copy `.env.example` to create `.env`:
   ```bash
   cd backend
   cp .env.example .env
   ```
3. Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

**Get your OpenRouter API key:**
- Visit https://openrouter.ai/
- Sign up or log in
- Go to Keys section
- Generate a new API key
- Paste it in the `.env` file

---

## 🔥 Step 2: Configure Frontend Environment Variables

1. Navigate to the `frontend/` folder
2. Copy `.env.example` to create `.env`:
   ```bash
   cd frontend
   cp .env.example .env
   ```
3. Edit `.env` and add your Firebase configuration:
   ```
   VITE_FIREBASE_API_KEY=your_api_key
   VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your_project_id
   VITE_FIREBASE_STORAGE_BUCKET=your_project.firebasestorage.app
   VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
   VITE_FIREBASE_APP_ID=your_app_id
   VITE_FIREBASE_MEASUREMENT_ID=your_measurement_id
   ```

**Get your Firebase credentials:**
1. Go to https://console.firebase.google.com/
2. Create a new project (or use existing)
3. Go to Project Settings → General
4. Scroll down to "Your apps" section
5. Click "Add app" → Web (</>) icon
6. Register your app
7. Copy the config values to your `.env` file

---

## 🔓 Step 3: Configure Firebase Services

### Enable Authentication:
1. In Firebase Console, go to **Authentication**
2. Click "Get started"
3. Enable **Email/Password** sign-in method
4. Enable **Google** sign-in method

### Enable Firestore Database:
1. In Firebase Console, go to **Firestore Database**
2. Click "Create database"
3. Choose "Start in test mode" (for development)
4. Select your preferred region
5. Click "Enable"

### Update Firestore Rules:
1. Go to **Firestore Database** → **Rules** tab
2. Copy the content from `firestore.rules` in the project root
3. Paste it in the Firebase rules editor
4. Click "Publish"

---

## 🚀 Step 4: Install Dependencies and Run

### Backend Setup:
```bash
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

# Run the server
python app.py
```

Backend will run on: http://localhost:5000

### Frontend Setup:
```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run on: http://localhost:5173

---

## ✅ Verification

1. Open http://localhost:5173 in your browser
2. Try signing up with email/password
3. Try signing in with Google
4. Enter some ingredients and generate a recipe
5. Check if the recipe is saved in your history

---

## 🐛 Common Issues

### "OPENROUTER_API_KEY not found"
- Make sure you created the `.env` file in the `backend/` folder
- Check that the API key is properly formatted (no quotes needed)
- Restart the Flask server after adding the key

### "Firebase configuration error"
- Verify all Firebase environment variables in `frontend/.env`
- Make sure variable names start with `VITE_`
- Restart the Vite dev server after adding variables

### "Module not found" errors
- Delete `node_modules` and run `npm install` again
- Make sure you're in the correct directory
- Check Node.js version (should be 16+)

### CORS errors
- Ensure backend is running on port 5000
- Check that Flask-CORS is installed
- Verify frontend is making requests to http://localhost:5000

---

## 📚 Additional Resources

- [Firebase Documentation](https://firebase.google.com/docs)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [React Documentation](https://react.dev)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Happy Cooking with SAVORA AI! 🍳**
