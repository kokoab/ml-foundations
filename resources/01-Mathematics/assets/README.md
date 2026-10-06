# Mathematics teaching figures

The `visuals/` PNG files are embedded in chapters 03–07 with relative Markdown
image links. They display in VS Code's built-in Markdown preview without an
extension, network connection, or running Python. Captions and image alternative
text explain the figures; new labels use plain notation.

Figures illustrate public explanations and worked examples, or use separate
demonstration data. They do not expose hidden solutions or draw the norm shapes
requested in Linear Algebra exercise 3.5. Simulations use fixed random seeds.

To regenerate the images, run from `resources/01-Mathematics` in a Python
environment with NumPy and Matplotlib installed:

```sh
python assets/generate_visuals.py
```

The script writes the PNG files and prints placement metadata as JSON. It does
not edit the chapter text. No Python dependencies are needed to view the images.
