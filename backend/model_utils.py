import os
from PIL import Image, ImageDraw
import uuid

def generate_image_from_sketch(sketch_path: str, prompt: str) -> str:
    # TEMP — placeholder: copy sketch to simulate output
    img = Image.open(sketch_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), f"Prompt: {prompt}", fill="red")
    output_path = f"/tmp/{uuid.uuid4()}.png"
    img.save(output_path)
    return output_path

def vectorize_sketch(sketch_path: str) -> str:
    # TEMP — placeholder SVG
    svg_path = f"/tmp/{uuid.uuid4()}.svg"
    with open(svg_path, "w") as f:
        f.write(f"<svg width='500' height='500'><text x='10' y='20'>Vector from {os.path.basename(sketch_path)}</text></svg>")
    return svg_path

def answer_question(question: str) -> str:
    # TEMP — placeholder answer
    return f"You asked: '{question}'. This is a placeholder answer."
