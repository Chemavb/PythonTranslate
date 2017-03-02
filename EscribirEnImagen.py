from PIL import Image, ImageDraw, ImageFont
from textblob import TextBlob
import time
import os

listaIdiomas = ("af", "de-DE", "am", "ar", "hy-AM", "az-AZ", "bn-BD", "be", "my-MM", "bg", "kn-IN", "ca", "cs-CZ",
                    "zh-CN", "zh-TW", "si-LK", "ko-KR", "hr", "da-DK", "sk", "sl", "et", "eu-ES", "fil", "fr-FR",
                    "fr-CA", "gl-ES", "ka-GE", "el-GR", "iw-IL", "hi-IN", "hu-HU", "id", "is-IS", "it-IT", "ja-JP",
                    "km-KH", "ky-KG", "lo-LA", "lv", "lt", "mk-MK", "ml-IN", "ms", "mr-IN", "mn-MN", "nl-NL", "ne-NP",
                    "no-NO", "fa", "pl-PL", "pt-BR", "pt-PT", "rm", "ro", "ru-RU", "sr", "sw", "sv-SE", "th", "ta-IN",
                    "te-IN", "tr-TR", "uk", "vi", "zu", "en-US", "es-ES", "es-US", "es-419", "en-AU", "en-IN", "en-GB")

path = "E:/Users/chema/PycharmProjects/untitled/"

Y_COORDENADA = 200
FONT_SIZE = 120

s1 = "COMPITE CON TU SELECCIÓN"
s2 = "VENCE A DIFERENTES RIVALES"
s3 = "RIVALES CADA VEZ MÁS DUROS"
s4 = "GANA LA COMPETICIÓN"

for idioma in listaIdiomas:
    #input("Press Enter for the next translation in " + idioma)

    if idioma == "am":
        font = ImageFont.truetype("ebrima.ttf", FONT_SIZE)
    elif idioma in ("bn-BD", "kn-IN", "si-LK", "hi-IN", "ml-IN", "mr-IN", "ne-NP", "ta-IN", "te-IN"):
        font = ImageFont.truetype("Nirmala.ttf", FONT_SIZE)
    elif idioma == "my-MM":
        font = ImageFont.truetype("mmrtext.ttf", FONT_SIZE)
    elif idioma == "zh-CN":
        font = ImageFont.truetype("msjh.ttc", FONT_SIZE)
    elif idioma == "zh-TW":
        font = ImageFont.truetype("msgothic.ttc", FONT_SIZE)
    elif idioma in ("ko-KR", "ja-JP"):
        font = ImageFont.truetype("calibri.ttf", FONT_SIZE)
    elif idioma == "ka-GE":
        font = ImageFont.truetype("sylfaen.ttf", FONT_SIZE)
    elif idioma in ("km-KH", "lo-LA"):
        font = ImageFont.truetype("LeelawUI.ttf", FONT_SIZE)
    elif idioma == "tahoma":
        font = ImageFont.truetype("tahoma.ttf", FONT_SIZE)
    else:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)

    base1 = Image.open("Base1.jpg")
    base2 = Image.open("Base2.jpg")
    base3 = Image.open("Base3.jpg")
    base4 = Image.open("Base4.jpg")
    W, H = base1.size
    time.sleep(2) #Duerme dos segundos para no congestionar la API

    try:
        print("Idioma " + idioma + "\n")
        s1_blob = TextBlob(s1)
        s2_blob = TextBlob(s2)
        s3_blob = TextBlob(s3)
        s4_blob = TextBlob(s4)

        s1Translated = str(s1_blob.translate(to=idioma))
        s2Translated = str(s2_blob.translate(to=idioma))
        s3Translated = str(s3_blob.translate(to=idioma))
        s4Translated = str(s4_blob.translate(to=idioma))

        #Debug Purpose
        print(s1Translated)
        print(s2Translated)
        print(s3Translated)
        print(s4Translated)
        #
        draw1 = ImageDraw.Draw(base1)
        draw2 = ImageDraw.Draw(base2)
        draw3 = ImageDraw.Draw(base3)
        draw4 = ImageDraw.Draw(base4)

        w1, h1 = draw1.textsize(s1Translated, font=font)
        w2, h2 = draw2.textsize(s2Translated, font=font)
        w3, h3 = draw3.textsize(s3Translated, font=font)
        w4, h4 = draw4.textsize(s4Translated, font=font)

        draw1.text(((W-w1)/2, Y_COORDENADA), s1Translated, font=font, fill="white")
        draw2.text(((W-w2)/2, Y_COORDENADA), s2Translated, font=font, fill="white")
        draw3.text(((W-w3)/2, Y_COORDENADA), s3Translated, font=font, fill="white")
        draw4.text(((W-w4)/2, Y_COORDENADA), s4Translated, font=font, fill="white")

        carpeta = path + idioma
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        name1 = "./" + idioma + "/" + "Final_" + "1.jpg"
        name2 = "./" + idioma + "/" + "Final_" + "2.jpg"
        name3 = "./" + idioma + "/" + "Final_" + "3.jpg"
        name4 = "./" + idioma + "/" + "Final_" + "4.jpg"

        base1.save(name1)
        base2.save(name2)
        base3.save(name3)
        base4.save(name4)
        print(" - - - - - - I M A G E N - C R E A D A  - - - - - -  ")
    except:
        print("No traduccion disponible en " + idioma)
