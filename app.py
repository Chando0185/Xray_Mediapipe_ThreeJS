"""X-Ray Mirror - tiny Flask server.
All tracking + rendering happens in the browser; the server only serves static files.
Run:  python app.py   ->  open http://localhost:5000
"""
import mimetypes
from flask import Flask, send_from_directory

mimetypes.add_type("application/javascript", ".mjs")
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("application/octet-stream", ".task")

app = Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.after_request
def no_cache_html(resp):
    if resp.mimetype == "text/html":
        resp.headers["Cache-Control"] = "no-store"
    return resp


if __name__ == "__main__":
    # Camera access is allowed on http://localhost. For other machines on the LAN use HTTPS
    # e.g. app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")  (needs: pip install pyopenssl)
    app.run(host="127.0.0.1", port=5000, debug=False)
