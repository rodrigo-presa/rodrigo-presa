"""Genera roar-standalone.html: el mismo index.html con las imágenes embebidas en base64.
Uso: python3 build-standalone.py"""
import base64, mimetypes, pathlib, re

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")

def inline(match):
    path = root / match.group(1)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode())

out = re.sub(r"(assets/[\w.-]+\.(?:jpg|png))", inline, html)
(root / "roar-standalone.html").write_text(out, encoding="utf-8")
print("roar-standalone.html: %.1f MB" % (len(out) / 1e6))
