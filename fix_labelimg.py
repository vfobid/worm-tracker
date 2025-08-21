import os
import re

# Path to the canvas.py in your virtual environment
canvas_path = r"C:\Users\vfobi\OneDrive - Northeastern University\Undergrad\CS\GitHub\worm-tracker\.venv310\Lib\site-packages\libs\canvas.py"

if not os.path.exists(canvas_path):
    print(f"❌ File not found: {canvas_path}")
    exit(1)

with open(canvas_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix drawLine(x1, y1, x2, y2) calls
drawline_pattern = re.compile(
    r"p\.drawLine\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\)]+)\)"
)
content = drawline_pattern.sub(
    r"p.drawLine(int(\1), int(\2), int(\3), int(\4))", content
)

# Fix drawRect(x, y, w, h) calls
drawrect_pattern = re.compile(
    r"p\.drawRect\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\)]+)\)"
)
content = drawrect_pattern.sub(
    r"p.drawRect(int(\1), int(\2), int(\3), int(\4))", content
)

with open(canvas_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Finished patching LabelImg drawLine and drawRect calls.")