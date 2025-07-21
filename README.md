# Memory Game

A personal memory game built with Flask featuring special moments and dates.

## Features
- Interactive quiz format
- Personal questions with multiple choice answers
- Kitten-themed responses
- Responsive design

## Local Development
```bash
pip install -r requirements.txt
python app.py
```

## Deployment
This app is configured for deployment on Render.com:
1. Connect your GitHub repository to Render
2. Set the start command to: `python3 app.py`
3. The app will automatically install dependencies from requirements.txt

## Files
- `app.py` - Main Flask application
- `templates/game.html` - Game interface
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version for deployment
