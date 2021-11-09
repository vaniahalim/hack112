# signSpeak: hack112 (CMU hackathon) project
Our project aims to translate American Sign Language (ASL) to text and speech. There are estimated to be more than 200,000 users of ASL, and as far as we know, there are no technologies they can use that allows for easy translation and communication with those who don't know ASL.
There are currently other projects out there that have translated letters in ASL to words, but as far as we know, we are the only ones to attempt to do so with full words.

Modules required to run:
playsound 1.2.2\
gTTS\
ffmpeg\
numpy\
tensorflow 1.13.2\
object_detection API\
LabelImg\
OpenCV\
Keras\

How to use:
Upon running the program, the user's camera will turn on so that it can be used to detect handsigns. Upon performing the signs for the words, the word being signed will be read and converted to text, and speech.

Words: There are currently 18 words in the database
