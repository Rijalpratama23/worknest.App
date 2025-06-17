from flask import Flask, request, render_template
import google.generativeai as genai
import os
import markdown 
# Masukkan API Key Gemini
genai.configure(api_key="AIzaSyDGB6iYKQT9PemfdbabtHH_4m68pGp99X0")

app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        nama = request.form.get("nama","");
        jenis_kelamin = request.form.get("jenis_kelamin", "")
        pendidikan = request.form["pendidikan"]
        keahlian = request.form["keahlian"]
        pengalaman = request.form["pengalaman"]

        prompt = (
            f"Saya bernama {nama}, seorang {jenis_kelamin} dengan pendidikan terakhir {pendidikan}. "
            f"Saya memiliki keahlian di bidang {keahlian}. "
            f"Pengalaman kerja saya: {pengalaman}. "
            f"Berdasarkan data tersebut, tolong rekomendasikan pekerjaan yang cocok untuk saya beserta alasannya."
            f"Berikan saya Link sumber/platform yang dapat memberikan  rekomendasi pekerjaan yang akurat"
        )

        response = model.generate_content(prompt)
        reply_raw = response.text
        reply = markdown.markdown(reply_raw)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
