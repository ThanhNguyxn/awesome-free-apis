"""
OpenAI API Example - Text Generation with GPT
Documentation: https://platform.openai.com/docs/api-reference
Note: Requires API key (sign up for free trial credits)
"""
import requests
import os

# ⚠️ IMPORTANT: Set your API key as environment variable
# export OPENAI_API_KEY='your-api-key-here'
API_KEY = os.getenv('OPENAI_API_KEY')

def chat_completion(prompt, model='gpt-3.5-turbo', max_tokens=150):
    """
    Generate text completion using OpenAI's chat models
    
    Args:
        prompt: Your question or instruction
        model: Model to use ('gpt-3.5-turbo' or 'gpt-4')
        max_tokens: Maximum length of response
    
    Returns:
        str: Generated text response
    """
    if not API_KEY:
        print("❌ Error: OPENAI_API_KEY environment variable not set!")
        print("Set it with: export OPENAI_API_KEY='your-key'")
        return None
    
    try:
        url = 'https://api.openai.com/v1/chat/completions'
        
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': max_tokens,
            'temperature': 0.7  # Creativity level (0-2)
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        
        # Extract the generated text
        message = result['choices'][0]['message']['content']
        usage = result['usage']
        
        return {
            'response': message,
            'tokens_used': usage['total_tokens'],
            'model': result['model']
        }
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("❌ Authentication failed! Check your API key.")
        elif e.response.status_code == 429:
            print("❌ Rate limit exceeded or quota exhausted!")
        else:
            print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# Example usage
if __name__ == '__main__':
    print("🤖 OpenAI GPT Chat Example")
    print("="*50)
    
    # Example 1: Simple question
    prompt1 = "Explain what an API is in one sentence."
    print(f"\n💬 Prompt: {prompt1}")
    
    result = chat_completion(prompt1)
    if result:
        print(f"\n🤖 Response: {result['response']}")
        print(f"📊 Tokens used: {result['tokens_used']}")
        print(f"🏷️  Model: {result['model']}")
    
    # Example 2: Code generation
    print("\n" + "="*50)
    prompt2 = "Write a Python function to reverse a string."
    print(f"\n💬 Prompt: {prompt2}")
    
    result2 = chat_completion(prompt2, max_tokens=200)
    if result2:
        print(f"\n🤖 Response:\n{result2['response']}")
    
    # Example 3: Creative writing
    print("\n" + "="*50)
    prompt3 = "Write a haiku about programming."
    print(f"\n💬 Prompt: {prompt3}")
    
    result3 = chat_completion(prompt3, max_tokens=50)
    if result3:
        print(f"\n🤖 Response:\n{result3['response']}")

"""
💡 Tips:
- Get free trial credits at: https://platform.openai.com/signup
- Keep your API key secret! Never commit it to GitHub
- Monitor usage at: https://platform.openai.com/usage
- gpt-3.5-turbo is cheaper and faster than gpt-4
"""
