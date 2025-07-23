from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import requests
import json

app = Flask(__name__)
CORS(app)

# Pre-defined acronyms that could plausibly be either health insurance or RL
ACRONYMS = [
    "SAC", "HMO", "EPO", "POS", "DDPG", "TRPO",
    "IPA", "MCO", "ACO", "HSA", "FSA", "MSA", "PPG", "MCTS", "UCB", "MAB",
    "QRL", "IRL", "GAE", "VPG", "NPG", "CEM", "PSO", "RND", "ICM", "NGU",
    "DQN", "A2C", "A3C", "TD3", "PPD", "CPO", "IMPALA", "APEX", "RBF", "SIL",
    "PER", "HER", "CURL", "MAML", "PEARL", "REPTILE", "FOML", "META", "RAIN",
    "DOC", "PAX", "MVP", "OPT", "SLA", "EOB", "CPT", "ICD", "DRG", "CMI",
    "LOS", "ALOS", "SNF", "IRF", "LTCH", "IPF", "CAH", "MDH", "RHC", "FQHC",
    "HRSA", "CMS", "OIG", "CDC", "FDA", "NIH", "WHO", "AMA", "AHA", "AAMC",
    "HIMSS", "HITECH", "HIPAA", "PHI", "EMR", "EHR", "HIE", "HIT", "CPOE",
    "CDSS", "CDS", "PACS", "RIS", "LIS", "BCMA", "MAR", "EMAR", "CPRS", "VistA"
]

# Track game state
game_counter = 0

@app.route('/')
def index():
    global game_counter
    game_counter = 0
    # First acronym is always PPO
    return render_template('index.html', acronym="PPO")

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
        'explanation': f"Wrong! {acronym} actually stands for '{expansion}' in {'relation to health insurance' if correct_category == 'health' else 'reinforcement learning'}."
    }
    
    return jsonify(result)

@app.route('/new_game', methods=['POST'])
def new_game():
    global game_counter
    game_counter += 1
    
    if game_counter == 1:
        # Second acronym is always MDP
        acronym = "MDP"
    else:
        # After that, random from the list
        acronym = random.choice(ACRONYMS)
    
    return jsonify({'acronym': acronym})

def generate_expansion(acronym, category):

    if acronym not in ["MDP", "PPO"] and False:
        """Generate plausible expansion using LLaMA backend"""
        try:
            acronym_p = ".".join([c for c in acronym])
            if category == 'health':
                prompt = f"Generate a plausible health insurance related expansion for the acronym '{acronym_p}'. Only return the expansion, nothing else."
            else:
                prompt = f"Generate a plausible reinforcement learning related expansion for the acronym '{acronym_p}'. Only return the expansion, nothing else."
            
            # Call LLaMA API (you'll need to set up your LLaMA endpoint)
            response = call_llama_api(prompt)
            return response.strip()
            
        except Exception as e:
            pass
    
    # Fallback expansions if LLaMA is unavailable or returns generic response
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
            'NGU': 'Network Group Utilization',
            'MDP': 'Medical Decision Protocol',
            'DQN': 'Diagnosis Quality Network',
            'A2C': 'Advanced Care Coordination',
            'A3C': 'Ambulatory Care Control Center',
            'TD3': 'Treatment Decision Documentation',
            'PPD': 'Preventive Primary Diagnosis',
            'CPO': 'Clinical Practice Organization',
            'IMPALA': 'Integrated Medical Practice and Laboratory Assessment',
            'APEX': 'Advanced Patient Experience',
            'RBF': 'Risk-Based Financing',
            'SIL': 'Specialized Insurance Liaison',
            'PER': 'Patient Experience Review',
            'HER': 'Health Expense Report',
            'CURL': 'Care Utilization Review Liaison',
            'MAML': 'Medical Administrative Management Link',
            'PEARL': 'Patient Experience and Risk Limitation',
            'REPTILE': 'Regional Provider Technology Integration and Learning Exchange',
            'FOML': 'Family Oriented Medical Liaison',
            'META': 'Medical Emergency Treatment Authorization',
            'RAIN': 'Risk Assessment Information Network',
            'DOC': 'Designated Outpatient Care',
            'PAX': 'Patient Access Exchange',
            'MVP': 'Medical Value Program',
            'OPT': 'Outpatient Treatment',
            'SLA': 'Service Level Agreement',
            'EOB': 'Explanation of Benefits',
            'CPT': 'Current Procedural Terminology',
            'ICD': 'International Classification of Diseases',
            'DRG': 'Diagnosis Related Group',
            'CMI': 'Case Mix Index',
            'LOS': 'Length of Stay',
            'ALOS': 'Average Length of Stay',
            'SNF': 'Skilled Nursing Facility',
            'IRF': 'Inpatient Rehabilitation Facility',
            'LTCH': 'Long-Term Care Hospital',
            'IPF': 'Inpatient Psychiatric Facility',
            'CAH': 'Critical Access Hospital',
            'MDH': 'Medical Data Hub',
            'RHC': 'Rural Health Clinic',
            'FQHC': 'Federally Qualified Health Center',
            'HRSA': 'Health Resources and Services Administration',
            'CMS': 'Centers for Medicare and Medicaid Services',
            'OIG': 'Office of Inspector General',
            'CDC': 'Centers for Disease Control and Prevention',
            'FDA': 'Food and Drug Administration',
            'NIH': 'National Institutes of Health',
            'WHO': 'World Health Organization',
            'AMA': 'American Medical Association',
            'AHA': 'American Hospital Association',
            'AAMC': 'Association of American Medical Colleges',
            'HIMSS': 'Healthcare Information and Management Systems Society',
            'HITECH': 'Health Information Technology for Economic and Clinical Health',
            'HIPAA': 'Health Insurance Portability and Accountability Act',
            'PHI': 'Protected Health Information',
            'EMR': 'Electronic Medical Record',
            'EHR': 'Electronic Health Record',
            'HIE': 'Health Information Exchange',
            'HIT': 'Health Information Technology',
            'CPOE': 'Computerized Provider Order Entry',
            'CDSS': 'Clinical Decision Support System',
            'CDS': 'Clinical Decision Support',
            'PACS': 'Picture Archiving and Communication System',
            'RIS': 'Radiology Information System',
            'LIS': 'Laboratory Information System',
            'BCMA': 'Bar Code Medication Administration',
            'MAR': 'Medication Administration Record',
            'EMAR': 'Electronic Medication Administration Record',
            'CPRS': 'Computerized Patient Record System',
            'VistA': 'Veterans Health Information Systems and Technology Architecture'
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
            'NGU': 'Never Give Up',
            'MDP': 'Markov Decision Process',
            'DQN': 'Deep Q-Network',
            'A2C': 'Advantage Actor-Critic',
            'A3C': 'Asynchronous Advantage Actor-Critic',
            'TD3': 'Twin Delayed Deep Deterministic Policy Gradient',
            'PPD': 'Persistent Policy Distillation',
            'CPO': 'Constrained Policy Optimization',
            'IMPALA': 'Importance Weighted Actor-Learner Architecture',
            'APEX': 'Asynchronous Prioritized Experience',
            'RBF': 'Radial Basis Function',
            'SIL': 'Self-Imitation Learning',
            'PER': 'Prioritized Experience Replay',
            'HER': 'Hindsight Experience Replay',
            'CURL': 'Contrastive Unsupervised Representations for Reinforcement Learning',
            'MAML': 'Model-Agnostic Meta-Learning',
            'PEARL': 'Probabilistic Embeddings for Actor-critic RL',
            'REPTILE': 'Rapid Episodic Policy Transfer in Learning',
            'FOML': 'First-Order Model-Agnostic Learning',
            'META': 'Model-Agnostic Episodic Training Algorithm',
            'RAIN': 'Recurrent Attention in Networks',
            'DOC': 'Differentiable Optimal Control',
            'PAX': 'Policy Attention eXtension',
            'MVP': 'Model-based Value Planning',
            'OPT': 'Optimistic Policy Transfer',
            'SLA': 'State-Level Abstraction',
            'EOB': 'End-of-Episode Baseline',
            'CPT': 'Curiosity-driven Policy Transfer',
            'ICD': 'Intrinsic Curiosity Drive',
            'DRG': 'Deep Reinforcement Gradient',
            'CMI': 'Counterfactual Multi-agent Imitation',
            'LOS': 'Latent Option Space',
            'ALOS': 'Adaptive Latent Option Selection',
            'SNF': 'Stochastic Neural Function',
            'IRF': 'Implicit Reward Function',
            'LTCH': 'Long-Term Credit Horizon',
            'IPF': 'Intrinsic Policy Function',
            'CAH': 'Curiosity-driven Action Hierarchy',
            'MDH': 'Multi-Domain Hierarchy',
            'RHC': 'Receding Horizon Control',
            'FQHC': 'Finite Q-function Hierarchical Control',
            'HRSA': 'Hierarchical Reward State Abstraction',
            'CMS': 'Curiosity-driven Multi-Scale',
            'OIG': 'Online Imitation Gradient',
            'CDC': 'Continuous Domain Control',
            'FDA': 'Functional Domain Adaptation',
            'NIH': 'Neural Information Hierarchy',
            'WHO': 'Weighted Hierarchical Optimization',
            'AMA': 'Adaptive Multi-Agent',
            'AHA': 'Attention-based Hierarchical Architecture',
            'AAMC': 'Adaptive Actor-critic Multi-Critic',
            'HIMSS': 'Hierarchical Imitation Multi-Scale System',
            'HITECH': 'Hierarchical Information Technology Enhanced Control Hierarchy',
            'HIPAA': 'Hierarchical Information Processing and Action Architecture',
            'PHI': 'Policy Hierarchy Interface',
            'EMR': 'Episodic Memory Replay',
            'EHR': 'Experience Hierarchy Representation',
            'HIE': 'Hierarchical Information Exchange',
            'HIT': 'Hierarchical Information Transfer',
            'CPOE': 'Continuous Policy Optimization Engine',
            'CDSS': 'Curiosity-Driven State Space',
            'CDS': 'Curiosity-Driven Search',
            'PACS': 'Policy and Critic System',
            'RIS': 'Reinforcement Information System',
            'LIS': 'Learning Information System',
            'BCMA': 'Bayesian Curiosity Multi-Agent',
            'MAR': 'Multi-Agent Reinforcement',
            'EMAR': 'Episodic Multi-Agent Reinforcement',
            'CPRS': 'Continuous Policy Representation System',
            'VistA': 'Value-based Information and State Transfer Architecture'
        }
    
    return fallbacks.get(acronym, f"Advanced {acronym} Protocol")

def call_llama_api(prompt):
    """Call LLaMA API - you'll need to configure this for your setup"""
    # This is a placeholder - replace with your actual LLaMA endpoint
    from llama_cpp import Llama
    llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_0.gguf")
    response = llm(f"{prompt}", max_tokens=32)
    result = response["choices"][0]["text"].strip()
    return result
    

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
