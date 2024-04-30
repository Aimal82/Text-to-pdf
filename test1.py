import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import io

def latex_to_png(latex_str):
    fig, ax = plt.subplots()

    ax.axis("off")
    ax.text(0.5, 0.5, f"${latex_str}$", size=50, ha="center", va="center")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0.4)
    buffer.seek(0)

    return buffer

latex_formula = "\\theta = a_2 + b_4 + c^3"
png_buffer = latex_to_png(latex_formula)

image = Image.open(png_buffer)
image.show()
