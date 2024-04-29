import os
import subprocess

# Load environment variables
NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN', '23baKlcVFtF3OkJtNrD6xExrYlI_7ZVM8X8z3bG6s3Zvt3Jgc')

# Start the FastChat services
subprocess.Popen(['python3', '-m', 'fastchat.serve.controller', '--host', '0.0.0.0'])
subprocess.Popen(['python3', '-m', 'fastchat.serve.model_worker', '--model-path', './chatglm2-6b', '--host', '0.0.0.0'])
subprocess.Popen(['python3', '-m', 'fastchat.serve.openai_api_server', '--host', '0.0.0.0', '--port', '8888'])
# subprocess.Popen(['python3', '-m', 'fastchat.serve.gradio_web_server', '--host', '0.0.0.0'])

# Start ngrok
ngrok_process = subprocess.Popen(['ngrok', 'http', '8888', '--auth', NGROK_AUTH_TOKEN], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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