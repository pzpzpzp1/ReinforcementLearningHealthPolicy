# Abbreviation Game

A fun web game where you guess whether abbreviations come from <span style="color: #4ecdc4">**Reinforcement Learning**</span> or <span style="color: #ff6b6b">**Health Insurance**</span>. 

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

## Optional: LLM Integration

For enhanced backronym generation, you can set up LLM locally:

1. **Install LLM:**
```
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf
```

2. **Remove the and False in app.py**
