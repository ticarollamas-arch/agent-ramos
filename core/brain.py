import requests

OLLAMA_URL = 'http://127.0.0.1:11434/api/generate'
MODEL = 'gemma2:2b'

def ask_llm(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={'model': MODEL, 'prompt': prompt, 'stream': False}, timeout=120)
        response.raise_for_status()
        return response.json().get('response', 'Sem resposta')
    except Exception as e:
        return f'Erro: {str(e)}'