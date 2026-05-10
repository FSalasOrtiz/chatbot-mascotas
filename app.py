from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Cargar el conocimiento
with open("conocimiento.txt", "r", encoding="utf-8") as f:
    CONOCIMIENTO = f.read()

def preguntar_al_chatbot(pregunta, historial):
    # Prompt engineering: le decimos al modelo quién es y qué sabe
    system_prompt = f"""Eres un asistente experto en cuidado de mascotas. 
Responde SOLO preguntas relacionadas con mascotas, usando el siguiente conocimiento:

{CONOCIMIENTO}

Si la pregunta no es sobre mascotas, responde amablemente que solo puedes ayudar con temas de mascotas.
Responde siempre en español, de forma clara y amigable.
"""
    # Construir mensajes con historial
    messages = [{"role": "system", "content": system_prompt}]
    for msg in historial:
        messages.append(msg)
    messages.append({"role": "user", "content": pregunta})

    # Llamar a Ollama
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": messages,
            "stream": False
        }
    )
    data = response.json()
    return data["message"]["content"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pregunta = data.get("pregunta", "")
    historial = data.get("historial", [])
    respuesta = preguntar_al_chatbot(pregunta, historial)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
