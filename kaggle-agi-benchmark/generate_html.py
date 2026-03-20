import subprocess
import json

output = subprocess.check_output(['python', 'metacognition_task.py'], stderr=subprocess.STDOUT, text=True)
js_text = json.dumps('> python metacognition_task.py\n' + output)

html = f"""<!DOCTYPE html>
<html>
<head>
<style>
  body {{ background-color: #1e1e1e; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; font-size: 16px; margin: 0; }}
  pre {{ margin: 0; white-space: pre-wrap; line-height: 1.5; }}
  .cursor {{ display: inline-block; width: 10px; height: 16px; background-color: #00ff00; animation: blink 1s step-end infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
</head>
<body>
<pre id="terminal"></pre>
<script>
const text = {js_text};
let i = 0;
const el = document.getElementById('terminal');
function typeWriter() {{
  if (i < text.length) {{
    let chars = text.substring(i, i + 5); 
    el.innerHTML += chars;
    i += 5;
    window.scrollTo(0, document.body.scrollHeight);
    setTimeout(typeWriter, 10);
  }} else {{
    el.innerHTML += '<span class="cursor"></span>';
  }}
}}
window.onload = typeWriter;
</script>
</body>
</html>"""

with open('terminal.html', 'w', encoding='utf-8') as f:
    f.write(html)
