import subprocess
import json

output = subprocess.check_output(['python', 'metacognition_task.py'], stderr=subprocess.STDOUT, text=True)
js_text = json.dumps('>>> STARTING KAGGLE AGI BENCHMARK EVALUATION...\n\n' + output)

html = f"""<!DOCTYPE html>
<html>
<head>
<style>
  body {{ background-color: #1e1e1e; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; font-size: 16px; margin: 0; padding-right: 320px; }}
  pre {{ margin: 0; white-space: pre-wrap; line-height: 1.5; }}
  .cursor {{ display: inline-block; width: 10px; height: 16px; background-color: #00ff00; animation: blink 1s step-end infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  
  #explanation-box {{
    position: fixed;
    top: 20px;
    right: 20px;
    width: 280px;
    background-color: #2d2d2d;
    color: #fff;
    padding: 20px;
    border: 2px solid #00ff00;
    font-family: 'Segoe UI', Arial, sans-serif;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,255,0,0.2);
  }}
  .explanation-title {{ font-weight: bold; color: #0df; margin-bottom: 10px; font-size: 18px; text-transform: uppercase; }}
  #explanation-text {{ font-size: 15px; line-height: 1.4; color: #ccc; }}
</style>
</head>
<body>
<div id="explanation-box">
  <div class="explanation-title">Phase 1: Initialization</div>
  <div id="explanation-text">Booting up the metacognition evaluation harness...</div>
</div>
<pre id="terminal"></pre>
<script>
const text = {js_text};
let i = 0;
const el = document.getElementById('terminal');
const expTitle = document.querySelector('.explanation-title');
const expText = document.getElementById('explanation-text');

function updateExplanation(currentText) {{
    if (currentText.includes("Expected factual: True")) {{
        expTitle.innerText = "Testing Factual Recall";
        expText.innerText = "The model is asked basic trivia to ensure it can retrieve verified facts perfectly without over-refusing.";
    }} else if (currentText.includes("Expected factual: False")) {{
        expTitle.innerText = "Hallucination Baits";
        expText.innerText = "The model is asked trick questions containing false fictional premises. It MUST refuse by saying 'I DO NOT KNOW'.";
    }}
    
    if (currentText.includes("--- Results ---")) {{
        expTitle.innerText = "Scoring & Results";
        expText.innerText = "The final benchmark scores are computed. High scores mean the model successfully recognized its own knowledge boundaries!";
    }}
}}

function typeWriter() {{
  if (i < text.length) {{
    let chars = text.substring(i, i + 5); 
    el.innerHTML += chars;
    i += 5;
    
    updateExplanation(text.substring(Math.max(0, i - 150), i));
    
    window.scrollTo(0, document.body.scrollHeight);
    setTimeout(typeWriter, 15);
  }} else {{
    el.innerHTML += '<span class="cursor"></span>';
    
    // Demonstrate scrolling up and down as requested
    setTimeout(() => {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
      setTimeout(() => {{
        window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }});
      }}, 4000);
    }}, 2000);
  }}
}}
window.onload = typeWriter;
</script>
</body>
</html>"""

with open('eval_explained.html', 'w', encoding='utf-8') as f:
    f.write(html)
