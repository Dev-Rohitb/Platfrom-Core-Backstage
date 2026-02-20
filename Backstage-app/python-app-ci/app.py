from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <html>
      <head><title>Python App</title></head>
      <body style="font-family: Arial; padding: 24px;">
        <h1>✅ Python App is running</h1>
        <p>Repo scaffolded via Backstage, built with Docker, pushed by GitHub Actions.</p>
        <p><a href="/health">Health check</a></p>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Local run
    app.run(host="0.0.0.0", port=8080)