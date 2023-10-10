import whisper
import os
import openai

# Load the model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("fileToText.mp3", fp16=False)
text = result["text"]

# Add a newline character every 100 characters
formatted_text = ''
for i in range(0, len(text), 200):
    formatted_text += text[i:i+200] + '\n'

# Write the transcribed text to a file
with open("speechToText.txt", "w", encoding='utf-8') as file:
    file.write(formatted_text)