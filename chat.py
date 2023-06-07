
import openai

# Imposta l'API key di OpenAI
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    if response['choices'][0]['text']:
        return response['choices'][0]['text'].strip()
    else:
        return "Mi dispiace, non ho una risposta per te in questo momento."

# Loop principale della chat
while True:
    user_input = input("Utente: ")
    
    # Termina la chat se l'utente digita 'bye'
    if user_input.lower() == 'bye':
        print("Chatbot: Arrivederci!")
        break
    
    # Genera una risposta utilizzando ChatGPT
    response = chat_with_gpt(user_input)
    print("Chatbot:", response)

