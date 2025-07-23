from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import requests
import json

app = Flask(__name__)
CORS(app)

# Pre-defined acronyms that could plausibly be either health insurance or RL
ACRONYMS = [
    "PPO", "SAC", "HMO", "EPO", "POS", "DDPG", "TRPO",
    "IPA", "MCO", "ACO", "HSA", "FSA", "MSA", "PPG", "MCTS", "UCB", "MAB",
    "QRL", "IRL", "GAE", "VPG", "NPG", "CEM", "PSO", "RND", "ICM", "NGU"
]

@app.route('/')
def index():
    # Generate a random acronym for the game
    acronym = random.choice(ACRONYMS)
    return render_template('index.html', acronym=acronym)

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    user_choice = data.get('choice')  # 'health' or 'rl'
    acronym = data.get('acronym')
    
    if not acronym or not user_choice:
        return jsonify({'error': 'Missing data'}), 400
    
    # User is always wrong - generate expansion for the opposite choice
    correct_category = 'rl' if user_choice == 'health' else 'health'
    
    # Generate plausible expansion using LLaMA
    expansion = generate_expansion(acronym, correct_category)
    
    result = {
        'wrong': True,
        'user_choice': user_choice,
        'correct_category': correct_category,
        'acronym': acronym,
        'expansion': expansion,
        'explanation': f"Wrong! {acronym} actually stands for '{expansion}' in {'health insurance' if correct_category == 'health' else 'reinforcement learning'}."
    }
    
    return jsonify(result)

@app.route('/new_game', methods=['POST'])
def new_game():
    acronym = random.choice(ACRONYMS)
    return jsonify({'acronym': acronym})

def generate_expansion(acronym, category):
    """Generate plausible expansion using LLaMA backend"""
    # Use fallbacks directly since LLaMA is likely not set up
    # try:
    #     if category == 'health':
    #         prompt = f"Generate a plausible health insurance related expansion for the acronym '{acronym}'. Only return the expansion, nothing else."
    #     else:
    #         prompt = f"Generate a plausible reinforcement learning related expansion for the acronym '{acronym}'. Only return the expansion, nothing else."
    #     
    #     # Call LLaMA API (you'll need to set up your LLaMA endpoint)
    #     response = call_llama_api(prompt)
    #     return response.strip()
    #     
    # except Exception as e:
    # Fallback expansions
    if category == 'health':
        fallbacks = {
            'PPO': 'Preferred Provider Organization',
            'SAC': 'Specialized Acute Care',
            'HMO': 'Health Maintenance Organization',
            'EPO': 'Exclusive Provider Organization',
            'POS': 'Point of Service',
            'DDPG': 'Direct Drug Prescription Guidelines',
            'TRPO': 'Treatment Response Planning Organization',
            'IPA': 'Independent Practice Association',
            'MCO': 'Managed Care Organization',
            'ACO': 'Accountable Care Organization',
            'HSA': 'Health Savings Account',
            'FSA': 'Flexible Spending Account',
            'MSA': 'Medical Savings Account',
            'PPG': 'Physician Practice Group',
            'MCTS': 'Medical Care Treatment Standards',
            'UCB': 'Utilization Control Board',
            'MAB': 'Medical Advisory Board',
            'QRL': 'Quality Review Liaison',
            'IRL': 'Insurance Risk Limitation',
            'GAE': 'General Administrative Expenses',
            'VPG': 'Vendor Practice Guidelines',
            'NPG': 'Network Provider Group',
            'CEM': 'Clinical Excellence Management',
            'PSO': 'Patient Safety Organization',
            'RND': 'Risk and Notification Department',
            'ICM': 'Integrated Care Management',
            'NGU': 'Network Group Utilization'
        }
    else:
        fallbacks = {
            'PPO': 'Proximal Policy Optimization',
            'SAC': 'Soft Actor-Critic',
            'HMO': 'Hierarchical Memory Optimization',
            'EPO': 'Evolutionary Policy Optimization',
            'POS': 'Policy Optimization System',
            'DDPG': 'Deep Deterministic Policy Gradient',
            'TRPO': 'Trust Region Policy Optimization',
            'IPA': 'Inverse Planning Algorithm',
            'MCO': 'Monte Carlo Optimization',
            'ACO': 'Actor-Critic Optimization',
            'HSA': 'Hierarchical State Abstraction',
            'FSA': 'Finite State Automaton',
            'MSA': 'Multi-Step Approximation',
            'PPG': 'Phasic Policy Gradient',
            'MCTS': 'Monte Carlo Tree Search',
            'UCB': 'Upper Confidence Bound',
            'MAB': 'Multi-Armed Bandit',
            'QRL': 'Quantum Reinforcement Learning',
            'IRL': 'Inverse Reinforcement Learning',
            'GAE': 'Generalized Advantage Estimation',
            'VPG': 'Vanilla Policy Gradient',
            'NPG': 'Natural Policy Gradient',
            'CEM': 'Cross-Entropy Method',
            'PSO': 'Particle Swarm Optimization',
            'RND': 'Random Network Distillation',
            'ICM': 'Intrinsic Curiosity Module',
            'NGU': 'Never Give Up'
        }
    
    return fallbacks.get(acronym, f"Advanced {acronym} Protocol")

def call_llama_api(prompt):
    """Call LLaMA API - you'll need to configure this for your setup"""
    # This is a placeholder - replace with your actual LLaMA endpoint
    try:
        # Example using ollama local setup
        response = requests.post('http://localhost:11434/api/generate', 
                               json={
                                   'model': 'llama2',
                                   'prompt': prompt,
                                   'stream': False
                               })
        if response.status_code == 200:
            return response.json()['response']
    except:
        pass
    
    # If LLaMA is not available, return a generic response
    return "Advanced Professional Protocol"

if __name__ == '__main__':
    app.run(debug=True)