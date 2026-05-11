# Chatbot Cuidado de Mascotas 🐾

Chatbot especializado en cuidado de mascotas desarrollado con Llama 3, Flask y prompt engineering.

## Estructura del proyecto
chatbot-mascotas/
├── app.py              <- Backend del chatbot
├── preguntas.txt       <- Pregunta de prueba
├── conocimiento.txt    <- Base de conocimiento sobre mascotas
├── README.md           <- Esta guía
└── templates/
    └── index.html      <- Interfaz web

---

## Instalación desde cero

### Linux (Fedora)
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
sudo dnf install git -y
git clone https://github.com/FSalasOrtiz/chatbot-mascotas.git
cd chatbot-mascotas
pip install flask requests

### Windows
1. Instalar Ollama desde https://ollama.com/download
2. Instalar Python desde https://www.python.org/downloads/
   (marcar "Add Python to PATH")
3. Instalar Git desde https://git-scm.com/download/win
4. Abrir CMD y ejecutar:
   ollama pull llama3.2:3b
   git clone https://github.com/FSalasOrtiz/chatbot-mascotas.git
   cd chatbot-mascotas
   pip install flask requests

---

## Instrucciones de uso

### Linux (Fedora)

Iniciar:
   sudo systemctl start ollama
   cd chatbot-mascotas
   python app.py

Abrir en navegador: http://localhost:5000

Detener:
   Ctrl+C
   sudo systemctl stop ollama

### Windows

Iniciar:
   CMD 1: ollama serve
   CMD 2: cd chatbot-mascotas && python app.py

Abrir en navegador: http://localhost:5000

Detener:
   Ctrl+C en ambas ventanas de CMD

---

## Preguntas de evaluación
1. ¿Qué vacunas necesita un perro?
2. ¿Cada cuánto debo bañar a mi gato?
3. ¿Qué alimentos son tóxicos para los perros?
4. ¿Cada cuánto debo desparasitar a mi mascota?
5. ¿Qué es el parvovirus y cómo se previene?
6. ¿A qué edad debo esterilizar a mi perro?
7. ¿Cómo sé si mi gato está estresado?
8. ¿Qué hago si mi perro tiene una convulsión?
9. ¿Qué diferencia hay entre comida para cachorro y adulto?
10. ¿Qué es la toxoplasmosis y debo preocuparme?
