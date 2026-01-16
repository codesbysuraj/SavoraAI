# Google Cloud Setup for SavoraAI

Your project has been successfully migrated to use **Google Generative AI (Gemini)** instead of OpenRouter.

## Setup Instructions

### 1. Get a Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Set Up Environment Variables

Create a `.env` file in the `backend/` directory with:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your actual Google API key.

### 3. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the Backend

```bash
# From the SavoraAI root directory:
cd backend
python app.py
```

The backend will start on `http://localhost:5000`

## Changes Made

### Backend Updates

- ✅ Replaced OpenRouter API with Google Gemini 1.5 Flash
- ✅ Updated `requirements.txt` to use `google-generativeai` package
- ✅ Modified all API calls to use Google's Generative AI client
- ✅ Updated environment variable from `OPENROUTER_API_KEY` to `GOOGLE_API_KEY`

### API Model

- **Model**: `gemini-1.5-flash` - Fast, efficient, and cost-effective for recipe generation
- **Provider**: Google Cloud's Generative AI service
- **Capabilities**: Text generation, JSON responses, recipe creation, cooking advice

## Benefits of Using Google Gemini

✨ **Advantages**:

- No rate limiting issues (unlike free OpenRouter models)
- High quality responses for recipe generation
- Integrated with Google's ecosystem
- Better JSON response handling
- Consistent API reliability

## Testing the API

Once the backend is running, you can test it with:

```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "ingredients": ["chicken", "rice", "garlic"],
    "cuisine": "Asian",
    "mealType": "dinner"
  }'
```

## Environment Variables Reference

| Variable         | Description            | Source                                                     |
| ---------------- | ---------------------- | ---------------------------------------------------------- |
| `GOOGLE_API_KEY` | Your Google AI API key | [Google AI Studio](https://aistudio.google.com/app/apikey) |

## Troubleshooting

**Error: "GOOGLE_API_KEY not found"**

- Make sure `.env` file exists in the `backend/` directory
- Verify the API key is correctly copied
- Restart the backend after updating `.env`

**Error: "API quota exceeded"**

- Check your Google API quota in [Google Cloud Console](https://console.cloud.google.com)
- Note: Free tier has generous limits for Gemini

**Error: "Invalid API key"**

- Verify your key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Make sure there are no extra spaces in the `.env` file

## Full Google Tech Stack

Your SavoraAI project now uses:

- 🔵 **Database/Auth**: Firebase (Google)
- 🤖 **AI/ML**: Google Gemini 1.5 Flash
- ☁️ **Backend API**: Flask (can be deployed to Google Cloud Run/App Engine)
- ⚡ **Frontend**: React with Vite

---

**Note**: All previous OpenRouter references have been removed and replaced with Google Generative AI service.
