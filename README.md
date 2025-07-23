# Abbreviation Game

A fun web game where you guess whether abbreviations come from <span style="color: #4ecdc4">**Reinforcement Learning**</span> or <span style="color: #ff6b6b">**Health Insurance**</span>. 

No matter what you choose, you're always wrong! The game then generates a plausible expansion for the category you didn't pick.

## Features

- **Always Wrong**: No matter your choice, the game shows you're incorrect
- **Dynamic Backronyms**: Uses LLaMA to generate plausible expansions (with comprehensive fallbacks)
- **Continuous Gameplay**: Results appear on the left, next challenge on the right
- **Two-Panel Interface**: Clean side-by-side layout for seamless play

## Quick Start

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser to:**
   ```
   http://localhost:5000
   ```

## Optional: LLaMA Integration

For enhanced backronym generation, you can set up LLaMA locally:

1. **Install Ollama:**
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull LLaMA model:**
   ```bash
   ollama pull llama2
   ```

3. **Start Ollama service:**
   ```bash
   ollama serve
   ```

The app will automatically use LLaMA if available, otherwise it falls back to pre-defined expansions.

## Game Rules

1. You're presented with an abbreviation (PPO, SAC, HMO, etc.)
2. Choose whether it's from Reinforcement Learning or Health Insurance
3. You're always wrong!
4. See the "correct" expansion for the category you didn't choose
5. Next abbreviation appears automatically

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI**: LLaMA integration (optional)
- **Styling**: CSS with glass morphism effects