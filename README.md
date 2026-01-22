# 🥗 AI Fridge Chef

An AI-powered web application that analyzes your fridge contents from a photo and suggests quick, easy recipes you can make with available ingredients.

## 🌟 Features

- 📸 **Image Analysis**: Upload a photo of your fridge and AI extracts visible ingredients
- 🤖 **OpenAI Vision**: Uses GPT-4o-mini for accurate ingredient detection
- 👨‍🍳 **Smart Recipe Generation**: Get 3-5 quick recipes (≤30 minutes) based on available ingredients
- ⚡ **Quick Filters**: Automatically filters recipes by cooking time
- 🎯 **Ingredient Normalization**: Intelligently normalizes ingredient names

## 🏗️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **OpenAI API** - GPT-4o for vision and recipe generation
- **Python 3.14** - Latest Python features
- **Uvicorn** - ASGI server

### Frontend
- **React** - UI library
- **JavaScript** - Frontend logic
- **Create React App** - Build tooling

## 📋 Prerequisites

- Python 3.14+
- Node.js 14+
- OpenAI API key

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-fridge-chef.git
cd ai-fridge-chef
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install fastapi uvicorn openai python-dotenv python-multipart pillow

# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the backend server
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000`

## 🔧 Configuration

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 📁 Project Structure

```
ai-fridge-chef/
├── backend/
│   ├── app/
│   │   ├── config.py              # Configuration and environment variables
│   │   ├── main.py                # FastAPI application entry point
│   │   ├── routes/
│   │   │   └── fridge.py          # API endpoints
│   │   └── services/
│   │       ├── ai_service.py      # OpenAI API integration
│   │       ├── ingredient_normalizer.py  # Ingredient processing
│   │       └── time_filter.py     # Recipe filtering logic
│   └── venv/                      # Python virtual environment
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js                 # Main React component
│   │   ├── App.css                # Styling
│   │   └── index.js               # React entry point
│   └── package.json
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

### `POST /api/analyze-fridge`

Analyzes a fridge image and returns ingredients with recipe suggestions.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `image` (file)

**Response:**
```json
{
  "ingredients": ["eggs", "milk", "cheese", "tomatoes"],
  "recipes": [
    {
      "dish": "Cheese Omelette",
      "time_minutes": 15,
      "difficulty": "easy",
      "uses": ["eggs", "cheese"],
      "missing_optional": ["butter"],
      "quick_steps": [
        "Beat eggs in a bowl",
        "Heat pan with butter",
        "Pour eggs and add cheese",
        "Fold and serve"
      ]
    }
  ]
}
```

## 🎯 Usage

1. Open the app at `http://localhost:3000`
2. Click "Choose File" or use camera on mobile
3. Take/select a photo of your fridge
4. Click "Analyze Fridge"
5. View detected ingredients and recipe suggestions
6. Follow the quick steps to cook!

## 🛠️ Development

### Backend Development
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

### Frontend Development
```bash
cd frontend
npm start
```

## 🚢 Deployment

### Backend
- Deploy to services like Render, Railway, or AWS Lambda
- Set environment variables in your hosting platform
- Use `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend
```bash
cd frontend
npm run build
```
Deploy the `build/` folder to Vercel, Netlify, or any static hosting service.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- OpenAI for GPT-4o API
- FastAPI for the excellent Python web framework
- React team for the frontend library

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/YOUR_USERNAME/ai-fridge-chef](https://github.com/YOUR_USERNAME/ai-fridge-chef)
