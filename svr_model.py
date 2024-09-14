from flask import Flask, request, render_template
from text2img_model import create_pipeline, text2img

app =  Flask(__name__)

# Définition des paramètres
IMAGE_PATH  = "static/output.jpg"

# Initialiser le pipeline
pipeline = create_pipeline()

@app.route("/", methods = ['GET', 'POST'])
def index():
    # Vérifier si l'utilisateur consulte le site Web
    if request.method == "GET":
        # Renvoie l'interface de la page Web
        return render_template("index.html")
    else:
        # Gérer l'invite de soumission de l'utilisateur -> générer une image -> retourner
        user_input = request.form["prompt"]

        print("Start gen....")
        im = text2img(user_input, pipeline)
        print("Finish gen....")
        im.save(IMAGE_PATH)

        return render_template("index.html", image_url = IMAGE_PATH)

if __name__ =='__main__':
    app.run(debug=False, host='0.0.0.0', port=8888, use_reloader=False)

