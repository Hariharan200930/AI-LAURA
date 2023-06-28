import pyttsx3 as pyt

# VOICE ID:
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_CatherineM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_SayakaM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_HarukaM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_taIN_ValluvarM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_AyumiM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM



def speak_EN(Text):

    engine = pyt.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_CatherineM')
    engine.setProperty('rate', 200)

    print("    ")
    print(f"A.I : {Text}")
    engine.say(Text)
    print("    ")

    engine.runAndWait()

def speak_JP(Text):

    engine = pyt.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_HarukaM')
    engine.setProperty('rate', 200)

    print("    ")
    print(f"A.I : {Text}")
    engine.say(Text)
    print("    ")

    engine.runAndWait()

def speak_TM(Text):

    engine = pyt.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_taIN_ValluvarM')
    engine.setProperty('rate', 200)

    print("    ")
    print(f"A.I : {Text}")
    engine.say(Text)
    print("    ")

    engine.runAndWait()

def speak_HN(Text):

    engine = pyt.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM')
    engine.setProperty('rate', 200)

    print("    ")
    print(f"A.I : {Text}")
    engine.say(Text)
    print("    ")

    engine.runAndWait()
# --------------------------------------------------------

# speak_EN("hello sir")
# speak_JP("こんにちは sir")
speak_JP("もしもし")
# speak_TM("வணக்கம்")
# speak_HN("नमस्ते sir")