import os

from flask import Flask, render_template, request
import random
import time

app = Flask(__name__, static_url_path='/static')

# Arapça harf listesi ve doğru cevaplar
arabic_letters = ["ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف",
                  "ق", "ك", "ل", "م", "ن", "ه", "و", "ى"]
dogrucevap = ["elif", "be", "te", "se", "cim", "ha", "hı", "dal", "zel", "ra", "ze", "sin", "şın", "sad", "sad", "tı",
              "zı", "ayın", "gayın", "fe", "kaf", "kef", "lam", "mim", "nun", "he", "vav", "ye"]
file_extension = ".png"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Rastgele bir Arapça harf seçin
        selected_letter = random.choice(arabic_letters)

        # Seçilen harfe göre dosya adını oluşturun
        image_file = selected_letter + file_extension

        return render_template('index.html', filename=image_file, arabic_letter=selected_letter, message="")
    elif request.method == 'POST':
        # Kullanıcının gönderdiği cevabı alın
        user_answer = request.form['answer']

        # Doğru cevabı al
        # Doğru cevabı al
        correct_answer_index = arabic_letters.index(request.form['arabic_letter'])
        correct_answer = dogrucevap[correct_answer_index]

        # Doğru cevap kontrolü
        if user_answer.strip().lower() == correct_answer:
            message = "Cevabınız doğru!"
        else:
            message = "Cevabınız yanlış! " + "Doğru Cevap: " + correct_answer

        # 1 saniye bekleyerek mesajın ekranda bir süre gösterilmesini sağlayalım
        time.sleep(1)

        # Eğer cevap doğruysa veya yanlışsa, tekrar rastgele bir harf seç ve bunu kullanıcıya göster
        selected_letter = random.choice(arabic_letters)
        image_file = selected_letter + file_extension
        return render_template('index.html', filename=image_file, arabic_letter=selected_letter, message=message)

if __name__ == "__main__":
    app.run(debug=True)
