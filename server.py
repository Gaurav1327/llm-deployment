import os
import subprocess
import openai

# Load environment variables
NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN', 'your-ngrok-auth-token')

# Start the FastChat services
subprocess.Popen(['python', '-m', 'fastchat.serve.controller', '--host', '0.0.0.0'])
subprocess.Popen(['python', '-m', 'fastchat.serve.model_worker', '--model-path', '/Llama-2-7b-chat-hf', '--host', '0.0.0.0'])
subprocess.Popen(['python', '-m', 'fastchat.serve.openai_api_server', '--host', '0.0.0.0'])
subprocess.Popen(['python', '-m', 'fastchat.serve.gradio_web_server', '--host', '0.0.0.0'])

# Start ngrok
ngrok_process = subprocess.Popen(['ngrok', 'http', '8002', '--auth', NGROK_AUTH_TOKEN], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read the ngrok public URL
for line in ngrok_process.stdout:
    line = line.decode('utf-8')
    if 'URL' in line:
        public_url = line.split('URL:')[1].strip()
        break

# Register the API with the central server (replace with your code)
print(f'Public URL: {public_url}')

# Wait for the processes to complete
ngrok_process.wait()