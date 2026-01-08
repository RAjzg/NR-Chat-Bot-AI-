from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = "আমি NR Chat Bot AI"
    if request.method == "POST":
        user = request.form.get("message")
        if user:
            if user.lower() == "hi":
                reply = "হ্যালো 😊"
            elif user == "তোমার নাম কি":
                reply = "আমি NR Chatbot AI"
            elif user.lower() == "bye":
                reply = "আল্লাহ হাফেজ 👋"
            else:
                reply = "আমি শিখছি, পরে উত্তর দেব 😅"
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
