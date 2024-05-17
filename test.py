from gtts import gTTS


proxies = {"http": "http://192.168.18.66:3128", "https": "http://192.168.18.66:3128"}
text_block = "Hola Hernán Varillas, esta es una prueba de texto a audio"


tts = gTTS(text_block, lang="es", proxies=proxies)
tts.save("audio.mp3")
