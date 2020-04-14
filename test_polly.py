#using AWS SDK to make call to Polly service
#text-to-speech translation

import boto3

sp_obj=boto3.client('polly')

response=sp_obj.synthesize_speech(OutputFormat='mp3',
Text='polly test voice Ramakrishna Siva Sai Kolli',
VoiceId='Joey'
)
#print(response['AudioStream'])

audio = response['AudioStream'].read()

#open file in byte mode
file=open("new_clip.mp3", "wb")

#writing stream data
file.write(audio)

#closing the file
file.close()


