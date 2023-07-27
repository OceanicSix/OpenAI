import openai
import json
openai.api_key = "xxx"
file_name="xxx.mp3"
audio_file = open(file_name, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text=json.loads(str(transcript))["text"]

save_file=open(f"{file_name}.txt","w")
save_file.write(text)
save_file.close()
