from main import main
import keep_alive
import asyncio
from flask import Flask

app = Flask('')
@app.route('/')
def home():
  asyncio.run(main())
  return "ok"