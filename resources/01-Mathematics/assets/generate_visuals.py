"""Regenerate the teaching figures: python assets/generate_visuals.py.

Requires NumPy and Matplotlib. Prints figure placement metadata as JSON.
All numerical examples are explanations or separate demonstrations, not
exercise solutions. Fixed random seeds make simulated figures repeatable.
"""

import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle


OUT = Path(__file__).resolve().parent / "visuals"
OUT.mkdir(exist_ok=True)
BLUE, ORANGE, GREEN, GRAY = "#2463a6", "#c46a24", "#267665", "#64748b"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold", "axes.labelsize": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#94a3b8", "text.color": "#25334a",
    "axes.labelcolor": "#25334a", "xtick.color": GRAY, "ytick.color": GRAY,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "lines.linewidth": 2.2,
})
FIGURES = []


def panels(n=1, height=3.8):
    fig, axes = plt.subplots(1, n, figsize=(9.6, height), layout="constrained", squeeze=False)
    return fig, axes[0]


def plane(ax, bounds=(-1, 5, -1, 5)):
    ax.set(xlim=bounds[:2], ylim=bounds[2:], xlabel="x", ylabel="y")
    ax.set_aspect("equal")
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.axvline(0, color=GRAY, lw=0.8)
    ax.grid(alpha=0.16)


def arrow(ax, start, end, color=BLUE, label=None, offset=(7, 7), lw=2.5):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "color": color, "lw": lw})
    if label:
        ax.annotate(label, end, xytext=offset, textcoords="offset points", color=color, fontsize=10)


def finish(fig, name, section, heading, caption):
    assert chr(36) not in caption and chr(36) not in name
    fig.savefig(OUT / (name + ".png"), dpi=160, bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)
    FIGURES.append(dict(name=name, section=section, heading=heading, caption=caption))


def normal(x, mean=0, sd=1):
    return np.exp(-0.5 * ((x - mean) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))


def flow(ax, labels, top="", bottom=""):
    ax.axis("off")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    width = 0.8 / len(labels)
    centers = np.linspace(0.11, 0.89, len(labels))
    for i, (x, label) in enumerate(zip(centers, labels)):
        ax.text(x, 0.5, label, ha="center", va="center", fontsize=11,
                bbox=dict(boxstyle="round,pad=0.65", fc="#eef4fa", ec=BLUE))
        if i:
            arrow(ax, (centers[i-1] + width / 2, 0.5), (x - width / 2, 0.5), GRAY)
    ax.text(0.5, 0.84, top, ha="center", fontsize=13, weight="bold")
    ax.text(0.5, 0.12, bottom, ha="center", fontsize=11, color=GREEN)


# 03 — Linear algebra
fig, (ax,) = panels()
plane(ax, (-0.5, 4.8, -0.5, 3.8))
arrow(ax, (0, 0), (3, 1), BLUE, "a = [3, 1]", (0, -22))
arrow(ax, (3, 1), (4, 3), ORANGE, "b = [1, 2]", (-100, 5))
arrow(ax, (0, 0), (4, 3), GREEN, "a + b = [4, 3]", (0, 15))
ax.set_title("Vector addition: place the second arrow at the first arrow's tip")
finish(fig, "03-addition", 2, "Adding vectors",
       "Follow the blue arrow, then the orange arrow. The green arrow reaches the same endpoint in one move; this is the worked example above.")

fig, axes = panels(3)
for ax, scale, title in zip(axes, [2, 0.5, -1], ["Stretch: × 2", "Shrink: × 0.5", "Reverse: × −1"]):
    plane(ax, (-3, 5, -2, 3))
    arrow(ax, (0, 0), (2, 1), GRAY)
    arrow(ax, (0, 0), (2*scale, scale), BLUE)
    ax.set_title(title)
    ax.text(0.03, 0.95, f"[2, 1] → [{2*scale:g}, {scale:g}]", transform=ax.transAxes, va="top", fontsize=10)
finish(fig, "03-scaling", 2, "Multiplying a vector by a number",
       "Gray is the original arrow. Scaling changes every component together: a positive factor keeps its direction, and a negative factor reverses it.")

fig, (ax,) = panels()
plane(ax, (-0.6, 4, -0.6, 5))
ax.plot([0, 3, 3], [0, 0, 4], color=ORANGE, marker="o")
arrow(ax, (0, 0), (3, 4), BLUE, "[3, 4]", (8, 3))
ax.text(1.4, -0.35, "3 right", ha="center", color=ORANGE)
ax.text(3.15, 1.7, "4 up", color=ORANGE)
ax.text(0.7, 2.5, "Straight-line length = 5", color=BLUE)
ax.set_title("Length: the vector is the long side of a right triangle")
finish(fig, "03-length", 3, "Length in 2D: Pythagoras",
       "The horizontal and vertical moves form a right triangle. The arrow's length is the square root of 3² + 4², rather than the total distance along the two sides.")

fig, (ax,) = panels()
plane(ax, (-1.3, 1.6, -1.2, 1.3))
t = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(t), np.sin(t), color=GRAY, lw=1.5)
angle = np.radians(35)
cx, sy = np.cos(angle), np.sin(angle)
arrow(ax, (0, 0), (cx, sy), BLUE)
ax.plot([0, cx, cx], [0, 0, sy], color=ORANGE, ls="--")
ax.text(cx/2, -0.16, "cos θ", ha="center", color=ORANGE)
ax.text(cx+0.08, sy/2, "sin θ", color=ORANGE)
ax.text(0.25, 0.09, "θ = 35°", fontsize=10)
ax.annotate("[cos θ, sin θ]", (cx, sy), xytext=(0, 18), textcoords="offset points", ha="center")
ax.set_title("A unit-circle point: horizontal = cosine, vertical = sine")
finish(fig, "03-angle", 4, "The picture that matters: a point on a circle",
       "Demonstration at 35°: the radius has length 1. Dropping straight down from its tip separates the horizontal cosine component from the vertical sine component.")

fig, axes = panels(3)
for ax, angle, title in zip(axes, [35, 90, 145], ["Positive: partly aligned", "Zero: perpendicular", "Negative: partly opposed"]):
    plane(ax, (-1.5, 1.5, -0.5, 1.5))
    arrow(ax, (0, 0), (1.2, 0), BLUE)
    arrow(ax, (0, 0), (np.cos(np.radians(angle)), np.sin(np.radians(angle))), ORANGE)
    ax.set_title(title, fontsize=11)
finish(fig, "03-dot-sign", 5, "What the sign tells you",
       "The sign of the dot product reflects the angle between the arrows. Their lengths also affect its size.")

fig, axes = panels(2)
for ax, length, title in zip(axes, [1.2, 3], ["Short vector, same angle", "Long vector, same angle"]):
    plane(ax, (-0.4, 3.6, -0.4, 2.4))
    arrow(ax, (0, 0), (2, 0), BLUE)
    arrow(ax, (0, 0), (length*np.cos(angle := np.radians(30)), length*np.sin(angle)), ORANGE)
    ax.set_title(title)
    ax.text(0.05, 0.94, "cosine similarity ≈ 0.866", transform=ax.transAxes, va="top")
finish(fig, "03-cosine", 6, "Remove the lengths",
       "Separate demonstration: changing the orange arrow's length changes its dot product with the blue arrow, but the 30° angle and cosine similarity stay the same.")

fig, (ax,) = panels()
plane(ax, (-0.5, 5, -0.5, 5))
ax.plot([-0.5, 5], [-0.5, 5], color=GRAY, lw=1)
arrow(ax, (0, 0), (3, 4), BLUE, "b = [3, 4]", (-110, 8))
arrow(ax, (0, 0), (3.5, 3.5), GREEN, "shadow = [3.5, 3.5]", (10, -15))
ax.plot([3, 3.5], [4, 3.5], color=ORANGE, ls="--")
ax.text(1.4, 0.7, "line in direction a = [1, 1]", rotation=45, color=GRAY, fontsize=10)
p = np.array([3.5, 3.5]); u = np.array([1, 1])/np.sqrt(2); v = np.array([-1, 1])/np.sqrt(2)
corner = np.array([p + .15*u, p + .15*u + .15*v, p + .15*v])
ax.plot(corner[:, 0], corner[:, 1], color=ORANGE, lw=1)
ax.set_title("Projection: the shortest gap to the line is perpendicular")
finish(fig, "03-projection", 7, "Worked example",
       "In the worked example, the green arrow is the projection of b onto the diagonal line. The dashed orange leftover meets that line at a right angle.")

fig, axes = panels(2)
plane(axes[0], (-3, 3, -3, 3)); plane(axes[1], (-3, 3, -3, 3))
for k in range(-2, 3):
    axes[0].plot([-2, 2], [k, k], color=BLUE, alpha=.25)
    axes[0].plot([k, k], [-2, 2], color=ORANGE, alpha=.25)
arrow(axes[0], (0, 0), (1, 0), BLUE); arrow(axes[0], (0, 0), (0, 1), ORANGE)
axes[0].set_title("Independent directions reach the plane")
axes[1].plot([-1.5, 1.5], [-3, 3], color=GRAY)
arrow(axes[1], (0, 0), (1, 2), BLUE); arrow(axes[1], (0, 0), (0.5, 1), ORANGE)
axes[1].set_title("Dependent directions only reach one line")
finish(fig, "03-span", 8, "Linear independence",
       "Multiples and sums of two independent directions can reach any point in the plane. If both directions lie on the same line, every combination stays on that line.")

fig, (ax,) = panels(height=3)
flow(ax, ["A\n2 rows × 3 columns", "x\n3 entries", "A x\n2 entries"],
     "Matrix × vector: each row produces one output", "Three matching entries → multiply and add → one number per row")
finish(fig, "03-matrix-vector", 10, "The shape rule",
       "The vector's entry count must match the matrix's column count. Each row uses the full vector to produce one output, so the output count matches the number of rows.")

fig, axes = panels(3, height=4)
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
for ax, A, title in zip(axes, [np.diag([2, 3]), np.array([[1, 1], [0, 1]]), np.array([[0, -1], [1, 0]])],
                        ["Stretch: x × 2, y × 3", "Shear: shift top sideways", "Rotate: 90° counterclockwise"]):
    plane(ax, (-1.4, 2.6, -0.5, 3.5))
    ax.add_patch(Polygon(square, fc="none", ec=GRAY, ls="--"))
    ax.add_patch(Polygon(square @ A.T, fc=BLUE, alpha=.18, ec=BLUE))
    arrow(ax, (0, 0), A[:, 0], BLUE); arrow(ax, (0, 0), A[:, 1], ORANGE)
    ax.set_title(title, fontsize=11)
finish(fig, "03-transformations", 11, "A catalog of transformations",
       "The dashed square is the input; the shaded shape is its image. Blue and orange arrows show where the two basis directions land. These are transformations from the catalog above.")

fig, axes = panels(2, height=3.2)
for ax, data, title in zip(axes, [[[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]],
                         ["A: 2 rows × 3 columns", "A transpose: 3 rows × 2 columns"]):
    ax.axis("off")
    table = ax.table(cellText=data, loc="center", cellLoc="center", colWidths=[.22]*len(data[0]))
    table.scale(1, 2.2)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("white")
        cell.set_facecolor("#e7f0fa" if (r == 0 if len(data)==2 else c == 0) else "#f1f5f9")
    ax.set_title(title)
finish(fig, "03-transpose", 13, "Transpose",
       "The highlighted first row becomes the highlighted first column. Transposing swaps row and column positions while keeping the values.")

fig, axes = panels(3)
for ax, A, title in zip(axes, [np.diag([2, 3]), np.array([[-1, 0], [0, 1]]), np.diag([1, 0])],
                        ["det = 6: area becomes 6", "det = −1: area 1, flipped", "det = 0: area collapses to 0"]):
    plane(ax, (-1.5, 2.5, -0.5, 3.5))
    ax.add_patch(Polygon(square, fc="none", ec=GRAY, ls="--"))
    transformed = square @ A.T
    ax.add_patch(Polygon(transformed, fc=BLUE, alpha=.2, ec=BLUE))
    ax.plot(*np.vstack([transformed, transformed[0]]).T, color=BLUE)
    arrow(ax, (0, 0), A[:, 0], BLUE); arrow(ax, (0, 0), A[:, 1], ORANGE)
    ax.set_title(title, fontsize=11)
finish(fig, "03-determinant", 14, "What the sign and zero mean",
       "The absolute determinant gives the area multiplier. A negative sign records an orientation flip; zero means a square has collapsed into a line or point.")

fig, axes = panels(3)
x = np.linspace(-2, 3, 100)
for ax, title, curves in zip(axes, ["One intersection", "Parallel: no intersection", "Same line: infinitely many"],
                            [[x, -x+2], [x, x+1], [x, x]]):
    ax.plot(x, curves[0], color=BLUE)
    ax.plot(x, curves[1], color=ORANGE, ls="--")
    plane(ax, (-2, 3, -2, 3)); ax.set_title(title, fontsize=11)
finish(fig, "03-systems", 16, "Three possible outcomes",
       "Separate demonstrations: a solution must lie on both lines. Crossing lines give one point, parallel distinct lines give none, and coincident lines share all their points.")

fig, axes = panels(2)
for ax, v, title in zip(axes, [np.array([1, 1]), np.array([1, 0])],
                       ["Eigenvector: stays on its line", "Other vector: changes direction"]):
    plane(ax, (-.5, 4, -.5, 4))
    Av = np.array([[2, 1], [1, 2]]) @ v
    arrow(ax, (0, 0), Av, ORANGE, f"A v = {Av.tolist()}", (0, 10))
    arrow(ax, (0, 0), v, BLUE, f"v = {v.tolist()}", (8, -18))
    ax.set_title(title, fontsize=12)
finish(fig, "03-eigenvectors", 18, "Definition",
       "For the matrix in this section, [1, 1] becomes three times longer on the same line. By comparison, [1, 0] turns when the matrix is applied.")

fig, axes = panels(3)
t = np.linspace(0, 2*np.pi, 200)
circle = np.vstack([np.cos(t), np.sin(t)])
marked = np.array([[1, 0], [0, 1]])
R = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
Vt, S, U = R(-np.pi/6), np.diag([2, .7]), R(np.pi/4)
for ax, M, title in zip(axes, [Vt, S @ Vt, U @ S @ Vt],
                        ["1. Rotate input directions", "2. Stretch along the axes", "3. Rotate the stretched shape"]):
    plane(ax, (-2.5, 2.5, -2.5, 2.5))
    shape = M @ circle; ax.plot(*shape, color=BLUE)
    for v, color in zip(marked, [BLUE, ORANGE]):
        arrow(ax, (0, 0), M @ v, color)
    ax.set_title(title, fontsize=11)
finish(fig, "03-svd", 19, "The statement",
       "A two-dimensional demonstration of SVD: apply V transpose, then the axis stretches, then U. The colored arrows track the same two input directions. Orthogonal factors can also include reflections.")

# 04 — Calculus
fig, axes = panels(2)
x = np.linspace(.5, 3.5, 200)
for ax, h in zip(axes, [1, .15]):
    ax.plot(x, x*x, color=BLUE, label="distance = t²")
    ax.plot(x, 4 + (4+h)*(x-2), color=ORANGE, label=f"secant: h = {h:g}")
    ax.plot(x, 4+4*(x-2), color=GREEN, ls="--", label="tangent: slope 4")
    ax.scatter([2, 2+h], [4, (2+h)**2], color=ORANGE, zorder=4)
    ax.set(xlabel="time t", ylabel="distance", ylim=(0, 13))
    ax.set_title("Wide interval" if h==1 else "Small interval")
    ax.legend(fontsize=9)
finish(fig, "04-secant", 1, "The picture",
       "As the second point approaches t = 2, the secant through both points approaches the tangent at that instant. The interval's average rate approaches the instantaneous rate.")

fig, (ax,) = panels()
h = np.linspace(-.5, .5, 200)
ax.plot(h, 4+h, color=BLUE)
ax.scatter([0], [4], s=100, facecolors="white", edgecolors=BLUE, linewidths=2, zorder=4)
arrow(ax, (-.4, 3.6), (-.08, 3.92), ORANGE)
arrow(ax, (.4, 4.4), (.08, 4.08), ORANGE)
ax.annotate("Hole at h = 0; nearby values approach 4", (0, 4), xytext=(-.46, 4.42), fontsize=11)
ax.set(xlabel="h", ylabel="((2 + h)² − 4) / h", title="A limit describes the approach, even when a value is missing")
ax.grid(alpha=.15)
finish(fig, "04-limit", 2, "Finding a limit: tables and algebra",
       "The original expression is undefined at h = 0, shown by the open circle. From either side, its nearby values approach 4.")

fig, axes = panels(2)
x = np.linspace(-2.5, 2.5, 200)
axes[0].plot(x, x*x, color=BLUE); axes[1].plot(x, 2*x, color=GREEN)
for ax in axes:
    ax.axhline(0, color=GRAY, lw=.8); ax.axvline(0, color=GRAY, lw=.8); ax.set_xlabel("x")
axes[0].set(title="Function: f(x) = x²", ylabel="f(x)")
axes[1].set(title="Derivative: f′(x) = 2x", ylabel="slope")
for p, label in [(-1.5, "negative"), (0, "zero"), (1.5, "positive")]:
    axes[1].scatter([p], [2*p], color=GREEN)
    axes[1].annotate(label, (p, 2*p), xytext=(4, 10), textcoords="offset points")
finish(fig, "04-derivative", 3, "What the sign of the derivative tells you",
       "Read the two graphs at the same x: negative slope means the function decreases, zero slope means it is locally flat, and positive slope means it increases.")

fig, (ax,) = panels(height=3)
flow(ax, ["x", "u = 3x + 1\nlocal rate: 3", "y = u²\nlocal rate: 2u"],
     "Chain rule: multiply the local rates", "At x = 1: u = 4, so the total rate is 3 × 8 = 24")
finish(fig, "04-chain", 5, "The rule",
       "The first function changes u when x changes; the second changes y when u changes. Multiply those local rates to obtain y's sensitivity to x. This previews worked example 1, not an exercise.")

fig, axes = panels(2)
x = np.linspace(-3, 3, 200)
axes[0].plot(x, x*x+4, color=BLUE); axes[0].set(title="Hold y = 2 fixed", xlabel="x", ylabel="f(x, 2) = x² + 4")
axes[1].plot(x, 1+x*x, color=ORANGE); axes[1].set(title="Hold x = 1 fixed", xlabel="y", ylabel="f(1, y) = 1 + y²")
for ax, p, slope in zip(axes, [1, 2], [2, 4]):
    ax.scatter([p], [5], color=GREEN, zorder=4)
    ax.plot(x, 5+slope*(x-p), color=GREEN, ls="--")
    ax.annotate(f"slope = {slope}", (p, 5), xytext=(-65, 20), textcoords="offset points")
    ax.set_ylim(-1, 14)
finish(fig, "04-partial", 6, "Partial derivatives",
       "For f(x, y) = x² + y², a partial derivative follows one slice while the other input stays fixed. Both highlighted points correspond to the same location (1, 2).")

fig, (ax,) = panels()
x = np.linspace(-3, 3, 120); X, Y = np.meshgrid(x, x)
c = ax.contour(X, Y, X*X+Y*Y, levels=[1, 2, 4, 5, 8, 12], colors=GRAY, alpha=.5)
ax.clabel(c, fontsize=9)
plane(ax, (-3, 3, -3, 3))
p = np.array([1, 2]); direction = p/np.linalg.norm(p)
ax.scatter(*p, color=BLUE, zorder=4)
arrow(ax, p, p+.9*direction, ORANGE, "uphill", (-65, 2))
arrow(ax, p, p-.9*direction, GREEN, "downhill", (-60, -15))
ax.set_title("Gradient direction on a bowl: f(x, y) = x² + y²")
finish(fig, "04-gradient", 7, "The three facts about the gradient",
       "Each contour joins points of equal height; its number is the function value. At (1, 2), the gradient points outward across the contour, and its negative points toward the bottom. Arrow lengths here are shortened for readability.")

fig, (ax,) = panels(height=3.5)
ax.axis("off")
table = ax.table(cellText=[["2", "1"], ["1", "4"]], rowLabels=["output 1: xy", "output 2: x + y²"],
                 colLabels=["nudge input x", "nudge input y"], cellLoc="center", loc="center", colWidths=[.28, .28])
table.scale(1, 2.2)
for (r, c), cell in table.get_celld().items():
    cell.set_edgecolor("white"); cell.set_facecolor("#e7f0fa" if r==0 or c==-1 else "#f1f5f9")
ax.set_title("Jacobian at (1, 2): one sensitivity per output–input pair")
ax.text(.5, .08, "Example: a small x-only nudge of 0.01 changes the outputs by about [0.02, 0.01].",
        transform=ax.transAxes, ha="center", fontsize=10)
finish(fig, "04-jacobian", 8, "Worked example",
       "Read down one column to see how one input affects every output. Read across one row to see all the sensitivities of one output. The numbers come from the worked example.")

fig, axes = panels(3)
x = np.linspace(-1.5, 1.5, 180)
for ax, y, title in zip(axes, [x*x, -x*x, x**3], ["Bends up: x²", "Bends down: −x²", "Flat slope, no extreme: x³"]):
    ax.plot(x, y, color=BLUE); ax.scatter([0], [0], color=ORANGE, zorder=4)
    ax.axhline(0, color=GRAY, lw=.8); ax.set(xlabel="x", ylabel="f(x)"); ax.set_title(title, fontsize=11)
finish(fig, "04-curvature", 9, "What it means",
       "The first two curves have a minimum and maximum respectively. The third keeps increasing through its flat point: slope zero alone does not establish a minimum or maximum.")

fig, axes = panels(3)
steps = np.arange(13)
for ax, rate, title in zip(axes, [.1, .9, 1.1], ["Small: approaches smoothly", "Larger: oscillates and settles", "Too large: diverges"]):
    values = 3*(1-2*rate)**steps
    ax.plot(steps, values, "o-", color=BLUE, ms=4)
    ax.axhline(0, color=GRAY, lw=.8)
    ax.set(xlabel="update number", ylabel="w", title=title)
    ax.set_title(title, fontsize=11)
    ax.text(.05, .94, f"step size = {rate}", transform=ax.transAxes, va="top", fontsize=10)
finish(fig, "04-descent", 11, "Worked example: one input",
       "These are the worked example's updates for f(w) = w², starting at w = 3. Crossing the bottom is not always a failure: the middle sequence still settles, while the right sequence grows farther away.")

fig, (ax,) = panels()
x = np.linspace(-.3, 2.5, 120); y = np.linspace(-.3, 1.5, 120); X, Y = np.meshgrid(x, y)
ax.contour(X, Y, X*X+2*Y*Y, levels=[.1, .5, 1, 2, 4, 6], colors=GRAY, alpha=.5)
points = np.array([[2*.8**i, .6**i] for i in range(13)])
ax.plot(*points.T, "o-", color=BLUE, ms=4)
for i in range(3):
    ax.annotate(str(i), points[i], xytext=(6, 8), textcoords="offset points")
ax.scatter([0], [0], color=GREEN, zorder=4)
ax.set(xlabel="x", ylabel="y", title="Two-input descent: steeper y direction shrinks faster")
ax.set_aspect("equal")
finish(fig, "04-descent-bowl", 11, "Worked example: two inputs",
       "The path follows the worked example's step size 0.1 from (2, 1). Contours show equal values of x² + 2y²; update 0 is the starting point.")

# 05 — Probability
fig, (ax,) = panels()
rng = np.random.default_rng(51)
flips = rng.integers(0, 2, 2000); counts = np.arange(1, len(flips)+1)
ax.plot(counts, np.cumsum(flips)/counts, color=BLUE)
ax.axhline(.5, color=ORANGE, ls="--", label="true heads probability: 0.5")
ax.set(xlabel="number of flips", ylabel="fraction of heads", ylim=(0, 1), title="Long-run frequency: one simulated fair coin")
ax.legend()
finish(fig, "05-frequency", 1, "The meaning: long-run frequency",
       "A simulated run fluctuates strongly at first and stabilizes as more flips accumulate. Stabilizing does not mean approaching the probability in a perfectly smooth sequence.")

fig, axes = panels(3, height=3.2)
xx, yy = np.meshgrid(np.linspace(-2, 2, 400), np.linspace(-1.4, 1.4, 280))
a = (xx+.55)**2+yy**2 <= 1; b = (xx-.55)**2+yy**2 <= 1
for ax, mask, title in zip(axes, [a & b, a | b, ~a], ["And: intersection", "Or: union", "Not A: complement"]):
    ax.imshow(np.where(mask, 1, np.nan), extent=(-2, 2, -1.4, 1.4), origin="lower", cmap="Blues", vmin=0, vmax=2)
    ax.add_patch(Circle((-.55, 0), 1, fill=False, ec=GRAY)); ax.add_patch(Circle((.55, 0), 1, fill=False, ec=GRAY))
    ax.text(-1, 0, "A"); ax.text(.9, 0, "B")
    ax.set(xlim=(-2, 2), ylim=(-1.4, 1.4)); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title)
finish(fig, "05-events", 2, '"Or": at least one happens',
       "Shading marks the included outcomes. And keeps the overlap; or includes either circle, including the overlap; not A includes everything in the rectangular outcome space outside A. Areas are schematic, not numerical probabilities.")

fig, (ax,) = panels(height=3.4)
ax.axis("off"); ax.set(xlim=(0, 1), ylim=(0, 1))
ax.text(.08, .5, "Choose a shirt", ha="center", va="center", fontsize=12)
for sy, shirt in [(0.75, "Blue"), (.25, "White")]:
    arrow(ax, (.19, .5), (.38, sy), BLUE)
    ax.text(.42, sy, shirt, va="center", color=BLUE)
    for dy, trousers in zip([.16, 0, -.16], ["Black", "Gray", "Tan"]):
        arrow(ax, (.52, sy), (.73, sy+dy), ORANGE)
        ax.text(.76, sy+dy, f"{shirt} + {trousers}", va="center", fontsize=10)
ax.set_title("Counting demonstration: 2 shirts × 3 trousers = 6 outfits")
finish(fig, "05-counting", 3, "The multiplication principle",
       "Each shirt choice branches into three trouser choices. Count complete paths through the tree to count the possible outfits.")

fig, axes = panels(2)
for ax, counts, title in zip(axes, [[15, 45, 30, 10], [30, 10]],
                            ["All 100 students", "Given second-year: only 40 remain"]):
    labels = ["First: coffee", "First: tea", "Second: coffee", "Second: tea"] if len(counts)==4 else ["Coffee", "Tea"]
    colors = [BLUE, GRAY, BLUE, GRAY] if len(counts)==4 else [BLUE, GRAY]
    ax.barh(labels, counts, color=colors); ax.invert_yaxis()
    for i, count in enumerate(counts): ax.text(count+1, i, str(count), va="center")
    ax.set(xlabel="number of students", xlim=(0, 53), title=title)
    ax.set_title(title, fontsize=12)
finish(fig, "05-conditional", 4, "A table of real counts",
       "The worked example conditions on second-year students: the first-year bars leave the group being counted. Coffee drinkers are then 30 of the remaining 40, rather than 30 of all 100.")

fig, (ax,) = panels(height=3.3)
ax.axis("off")
table = ax.table(cellText=[["H1", "H2", "H3", "H4", "H5", "H6"], ["T1", "T2", "T3", "T4", "T5", "T6"]],
                 rowLabels=["Heads", "Tails"], colLabels=list(range(1, 7)), loc="center", cellLoc="center")
table.scale(.8, 2)
for (r, c), cell in table.get_celld().items():
    cell.set_edgecolor("white"); cell.set_facecolor("#e7f0fa" if r==1 else "#f1f5f9")
ax.set_title("Independent coin and die: heads leaves all six die faces possible")
ax.text(.5, .06, "All 12 outcomes are equally likely; the heads row still contains faces 1 through 6.", ha="center", transform=ax.transAxes, fontsize=10)
finish(fig, "05-independence", 5, "Definition",
       "For an independent fair coin and fair die, knowing heads happened removes the tails row but does not favor any die face.")

fig, axes = panels(2)
axes[0].bar(["Sick", "Healthy"], [100, 9900], color=[BLUE, GRAY])
axes[0].set(ylabel="people", title="Start: 10,000 people")
axes[1].bar(["Sick + positive", "Healthy + positive"], [90, 495], color=[BLUE, ORANGE])
axes[1].set(ylabel="people testing positive", title="Condition on a positive test")
for ax, counts in zip(axes, [[100, 9900], [90, 495]]):
    ax.set_ylim(0, max(counts)*1.2)
    for i, v in enumerate(counts): ax.text(i, v, f"{v:,}", ha="center", va="bottom")
finish(fig, "05-bayes", 6, "Worked example: count first",
       "The worked example's rare disease creates a very large healthy group. Among 585 positives, 495 are false alarms and 90 are true positives. Notice that the two panels use different vertical scales.")

fig, axes = panels(2)
axes[0].bar([0, 1, 2], [.25, .5, .25], color=BLUE, width=.5)
axes[0].set(xticks=[0, 1, 2], xlabel="heads in two fair flips", ylabel="probability", ylim=(0, .65), title="Discrete: probability at each value")
x = np.linspace(-3.5, 3.5, 300); density = normal(x)
axes[1].plot(x, density, color=BLUE)
axes[1].fill_between(x, density, where=(x>=-.5)&(x<=1), color=ORANGE, alpha=.4)
axes[1].set(xlabel="continuous value", ylabel="density", title="Continuous: probability over a range")
finish(fig, "05-distributions", 7, "Density and area",
       "Left: bar heights are probabilities and sum to 1. Right: the orange area over a range is a probability; the curve's height alone is density, not probability. The right-hand curve is a separate standard-normal demonstration.")

fig, (ax,) = panels()
ax.plot([-.04, 0, 0, .25, .25, .3], [0, 0, 4, 4, 0, 0], color=BLUE)
ax.fill_between([.05, .15], [4, 4], color=ORANGE, alpha=.35)
ax.text(.1, 2, "width 0.10\n× height 4\n= probability 0.40", ha="center", va="center", fontsize=11)
ax.set(xlabel="value", ylabel="density", ylim=(0, 4.8), title="Uniform on [0, 0.25]: density 4, total area 1")
finish(fig, "05-density", 7, "Density is not probability",
       "The density may exceed 1 because probability is area. This worked example has height 4 over width 0.25, so the whole area is 1; the highlighted smaller interval has probability 0.40.")

fig, (ax,) = panels()
ax.bar([1, 2, 3, 4], [.1, .2, .4, .3], color=BLUE, width=.55)
ax.axvline(2.9, color=ORANGE, ls="--", label="weighted mean = 2.9")
ax.set(xticks=[1, 2, 3, 4], xlabel="outcome value", ylabel="probability", ylim=(0, .5), title="Expected value: average weighted by how often each value occurs")
ax.legend()
finish(fig, "05-expectation", 8, "Definition",
       "Separate demonstration: probabilities [0.1, 0.2, 0.4, 0.3] weight outcomes [1, 2, 3, 4]. Their weighted average is 2.9, even though 2.9 is not an individual possible outcome.")

fig, axes = panels(2)
for ax, vals, probs, title in zip(axes, [[5], [0, 10]], [[1], [.5, .5]], ["Game A: always 5", "Game B: 0 or 10"]):
    ax.bar(vals, probs, color=BLUE, width=.6)
    ax.axvline(5, color=ORANGE, ls="--", label="expected value = 5")
    ax.set(xlim=(-1, 11), ylim=(0, 1.2), xlabel="winnings", ylabel="probability", title=title)
    ax.legend(fontsize=9)
finish(fig, "05-variance", 9, "The problem",
       "Both games in the explanation have the same expected value. Their outcomes are distributed differently: one never varies, while the other puts all its probability far from the mean.")

fig, axes = panels(3)
axes[0].bar([0, 1], [.7, .3], color=BLUE, width=.5)
axes[0].set(xticks=[0, 1], title="Bernoulli: one trial", xlabel="success indicator", ylabel="probability")
k = np.arange(9); probs = [math.comb(8, int(i))*.3**i*.7**(8-i) for i in k]
axes[1].bar(k, probs, color=BLUE)
axes[1].set(title="Binomial: 8 independent trials", xlabel="number of successes", ylabel="probability")
x = np.linspace(-4, 4, 300)
axes[2].plot(x, normal(x), color=BLUE)
axes[2].set(title="Gaussian: continuous values", xlabel="value", ylabel="density")
for ax in axes: ax.set_title(ax.get_title(), fontsize=11)
finish(fig, "05-families", 10, "Gaussian (normal): the bell curve",
       "Separate examples compare one yes/no trial (success probability 0.3), the count of successes in eight such independent trials, and a standard Gaussian density. Probability bars and density curves have different vertical meanings.")

fig, (ax,) = panels()
x = np.linspace(-4, 4, 500); density = normal(x)
for width, color in [(3, "#e4ebf2"), (2, "#b9cfe5"), (1, "#6d9cc8")]:
    ax.fill_between(x, density, where=np.abs(x)<=width, color=color)
ax.plot(x, density, color=BLUE)
for width, yy, label in [(1, .28, "within 1 SD: about 68%"), (2, .13, "within 2 SD: about 95%"), (3, .035, "within 3 SD: about 99.7%")]:
    ax.annotate("", (width, yy), (-width, yy), arrowprops={"arrowstyle": "|-|", "color": GRAY})
    ax.text(0, yy+.012, label, ha="center", fontsize=10)
ax.set(xlabel="standard deviations from the mean", ylabel="density", title="Gaussian ranges are nested: wider intervals include more probability")
finish(fig, "05-normal-ranges", 10, "The 68–95–99.7 rule",
       "The ranges are centered on the mean and nested inside one another. Each percentage is the full area within that range, not the area of only its outer band.")

fig, axes = panels(2)
p = np.linspace(.01, .99, 400); likelihood = p**7*(1-p)**3
for ax, vals, title in zip(axes, [likelihood, np.log(likelihood)], ["Likelihood", "Log-likelihood"]):
    ax.plot(p, vals, color=BLUE); ax.axvline(.7, color=ORANGE, ls="--")
    ax.set(xlabel="candidate heads probability p", ylabel=title.lower(), title=title + ": same best p = 0.7")
    ax.set_title(ax.get_title(), fontsize=12)
finish(fig, "05-likelihood", 11, "Take the log first",
       "For the worked example's seven heads and three tails, both curves peak at p = 0.7. Taking the log changes the vertical scale but keeps the maximizing parameter value.")

# 06 — Statistics
fig, (ax,) = panels(height=3.3)
ax.axis("off"); ax.set(xlim=(0, 1), ylim=(0, 1))
ax.set_aspect("equal")
for i in range(8):
    for j in range(5):
        ax.add_patch(Circle((.06+i*.04, .25+j*.11), .012, color=GRAY, alpha=.65))
ax.text(.2, .9, "Population", ha="center", weight="bold")
for i, (px, py) in enumerate([(.55, .35), (.62, .42), (.58, .57), (.66, .65), (.54, .7)]):
    ax.add_patch(Circle((px, py), .018, color=BLUE))
ax.text(.6, .9, "Random sample", ha="center", weight="bold")
arrow(ax, (.36, .5), (.49, .5), GRAY)
arrow(ax, (.72, .5), (.82, .5), GRAY)
ax.text(.91, .5, "Calculate\na statistic", ha="center", va="center", bbox=dict(fc="#eef4fa", ec=BLUE, boxstyle="round,pad=.5"))
ax.text(.5, .06, "Use the sample statistic to estimate a population parameter.", ha="center", fontsize=11)
finish(fig, "06-sampling", 1, "Population vs. sample",
       "The dots illustrate the full group and a smaller group selected for measurement. A statistic is calculated from the sample; the population parameter is what you want to learn about.")

fig, (ax,) = panels()
data = [20, 25, 25, 30, 400]
ax.bar(range(5), data, color=[BLUE]*4+[ORANGE])
ax.axhline(100, color=GREEN, ls="--", label="mean = 100")
ax.axhline(25, color=GRAY, ls=":", label="median and mode = 25")
ax.set(xticks=range(5), xticklabels=["1", "2", "3", "4", "5"], xlabel="person", ylabel="income in thousands of pesos", title="One outlier pulls the mean away from most people")
ax.legend()
finish(fig, "06-center", 2, "Definitions",
       "The five incomes are the worked example's [20, 25, 25, 30, 400]. The mean rises to 100, while the median and mode remain 25.")

fig, axes = panels(2)
for ax, values, title in zip(axes, [[4, 5, 6], [1, 5, 9]], ["Same mean, small spread", "Same mean, large spread"]):
    ax.scatter(values, [0]*3, color=BLUE, s=70)
    for value in values: ax.plot([value, 5], [.12, .12], color=ORANGE, lw=2)
    ax.axvline(5, color=GREEN, ls="--")
    ax.set(xlim=(0, 10), ylim=(-.2, .4), yticks=[], xlabel="value", title=title)
    ax.text(5, .28, "mean = 5", ha="center", color=GREEN)
finish(fig, "06-spread", 3, "Sample variance",
       "Separate demonstrations: both samples average to 5, but their distances from 5 differ. Variance summarizes squared distances, while standard deviation returns to the original units.")

fig, axes = panels(3)
rng = np.random.default_rng(64); x = np.linspace(-2, 2, 80)
for ax, y, title in zip(axes, [x+rng.normal(0, .4, 80), -x+rng.normal(0, .4, 80), x*x],
                        ["Positive association", "Negative association", "Curved relation, correlation 0"]):
    ax.scatter(x, y, color=BLUE, s=14, alpha=.7)
    ax.set(xlabel="x", ylabel="y"); ax.set_title(title, fontsize=11)
finish(fig, "06-correlation", 4, "The picture: a scatter plot",
       "Separate demonstrations: correlation measures a straight-line tendency. The right plot has a clear U-shaped relationship, yet its symmetric x and x² values have zero correlation.")

fig, (ax,) = panels()
x = np.linspace(-4, 4, 400)
for n, color in [(1, GRAY), (4, BLUE), (16, GREEN)]:
    ax.plot(x, normal(x, sd=1/np.sqrt(n)), color=color, label=f"sample size {n}: SE = {1/np.sqrt(n):g}")
ax.set(xlabel="sample mean", ylabel="density", title="Larger samples make the sample mean less variable")
ax.legend()
finish(fig, "06-standard-error", 5, "The square root is important",
       "For independent samples from a normal population with mean 0 and standard deviation 1, the sample mean's standard error is 1 divided by the square root of the sample size. Quadrupling the sample size halves that spread.")

fig, (ax,) = panels(height=4.7)
rng = np.random.default_rng(66); estimates = rng.normal(0, 1, 40)
for i, estimate in enumerate(estimates):
    color = BLUE if abs(estimate)<=1.96 else ORANGE
    ax.plot([estimate-1.96, estimate+1.96], [i, i], color=color, lw=1.5)
    ax.scatter([estimate], [i], color=color, s=10)
ax.axvline(0, color=GREEN, ls="--", label="fixed true mean")
ax.set(xlabel="estimated mean and its interval", ylabel="independent sample", title="95% describes repeated interval coverage")
ax.legend(loc="upper right")
finish(fig, "06-intervals", 6, 'What "95% confidence" actually means',
       "Simulation of 40 independent normal-mean estimates with known standard error 1. Each interval extends 1.96 standard errors either way. Orange intervals miss the fixed true mean; a finite run need not contain exactly 95% successful intervals.")

fig, (ax,) = panels(height=3.2)
flow(ax, ["Observed sample\n[3, 6, 8, 11]", "Resample\n[6, 6, 3, 11]", "Compute statistic\nmean = 6.5"],
     "Bootstrap demonstration: draw from the observed sample with replacement",
     "Repeat many times → distribution of resampled statistics → interval")
finish(fig, "06-bootstrap", 6, "The bootstrap: intervals without a formula",
       "Separate demonstration: a resample has the same size as the original sample, but 6 appears twice and 8 is absent. Compute the statistic on every resample to approximate its sampling variability.")

fig, (ax,) = panels()
x = np.linspace(-4, 4, 500); density = normal(x)
ax.plot(x, density, color=BLUE)
ax.fill_between(x, density, where=np.abs(x)>=2.2, color=ORANGE, alpha=.5)
ax.axvline(2.2, color=ORANGE, ls="--", label="observed statistic = 2.2")
ax.set(xlabel="test statistic under the null hypothesis", ylabel="density", title="Two-sided p-value: outcomes at least as extreme under the null")
ax.legend()
finish(fig, "06-pvalue", 7, "The p-value",
       "Separate demonstration with a standard-normal null distribution: the p-value is the combined shaded area beyond −2.2 and +2.2. It is a probability about possible data under the null, not the probability that the null is true.")

fig, (ax,) = panels()
x = np.array([1, 2, 3]); y = np.array([2, 4, 7]); slope, intercept = np.polyfit(x, y, 1)
grid = np.linspace(.7, 3.3, 150)
ax.plot(grid, slope*grid+intercept, color=BLUE, label="fitted line")
ax.scatter(x, y, color=ORANGE, label="observed values", zorder=4)
for xx, yy in zip(x, y): ax.plot([xx, xx], [yy, slope*xx+intercept], color=GREEN, lw=3)
ax.set(xlabel="x", ylabel="y", title="Least squares: minimize the squared vertical residuals")
ax.legend()
finish(fig, "06-least-squares", 8, "Worked example",
       "The worked example's data are [1, 2, 3] and [2, 4, 7]. Green segments are vertical residuals between observations and fitted predictions; least squares minimizes the sum of their squares.")

fig, axes = plt.subplots(2, 2, figsize=(9.6, 6), layout="constrained")
rng = np.random.default_rng(69)
base = rng.normal(size=(40, 2)); base -= base.mean(axis=0)
for ax, bias, sd, title in zip(axes.flat, [0, 0, 1.1, 1.1], [.18, .7, .18, .7],
                             ["Low bias, low variance", "Low bias, high variance", "High bias, low variance", "High bias, high variance"]):
    for r in [.4, .8, 1.2]: ax.add_patch(Circle((0, 0), r, fill=False, ec=GRAY, alpha=.4))
    dots = base*sd + [bias, 0]
    ax.scatter(*dots.T, color=BLUE, s=16, alpha=.75)
    ax.scatter([0], [0], marker="+", color=ORANGE, s=110, linewidths=2)
    ax.set(xlim=(-2.3, 2.7), ylim=(-2, 2), xticks=[], yticks=[], title=title); ax.set_aspect("equal")
finish(fig, "06-bias-variance", 9, "The dartboard picture",
       "Schematic dartboards: the orange cross marks the truth, and each blue dot is an estimate from a different sample. Bias shifts the cluster's center; variance changes its spread.")

# 07 — ML mathematics
fig, (ax,) = panels(height=3.2)
flow(ax, ["Features", "Model + weights", "Prediction", "Loss vs. target"],
     "Training uses examples to improve the model", "Compute loss → compute gradients → adjust weights → predict again")
finish(fig, "07-training", 1, "Training",
       "Features enter the model, its prediction is compared with the known target, and the loss guides weight updates. After training, the learned model predicts on new features.")

fig, (ax,) = panels()
error = np.linspace(-3, 3, 300)
ax.plot(error, error**2, color=BLUE, label="squared error")
ax.plot(error, np.abs(error), color=ORANGE, label="absolute error")
ax.set(xlabel="prediction − target", ylabel="loss", title="Loss choice changes how strongly large errors are penalized")
ax.legend(); ax.grid(alpha=.15)
finish(fig, "07-loss", 2, "Choosing between them",
       "Both losses are zero at a correct prediction. For errors larger than 1 in these units, squared error rises more quickly and gives large errors more influence.")

fig, axes = panels(2)
data_x = np.array([1, 2, 3]); data_y = np.array([2, 4, 7]); grid = np.linspace(.7, 3.3, 150)
for ax, b, w, title in zip(axes, [0, 13/15], [0, 31/15], ["Before: predictions all zero", "After one step: predictions close to data"]):
    ax.scatter(data_x, data_y, color=ORANGE, zorder=4)
    ax.plot(grid, b+w*grid, color=BLUE)
    for xx, yy in zip(data_x, data_y): ax.plot([xx, xx], [yy, b+w*xx], color=GREEN, lw=2)
    ax.set(xlabel="feature x", ylabel="target / prediction", ylim=(-.6, 8))
    ax.set_title(title, fontsize=11)
finish(fig, "07-regression-step", 3, "Option B: gradient descent",
       "The worked example starts with bias and slope both zero. A single step of size 0.1 tilts and raises the line; the green error segments shrink substantially. This shows the first step only.")

fig, axes = panels(2)
error = np.linspace(-3, 3, 300)
axes[0].plot(error, normal(error), color=BLUE)
axes[0].set(xlabel="target − prediction", ylabel="density", title="Gaussian noise: large errors less likely")
axes[1].plot(error, .5*error**2, color=BLUE)
axes[1].set(xlabel="target − prediction", ylabel="negative log-density, constant removed", title="Take negative log: a squared-error bowl")
for ax in axes: ax.set_title(ax.get_title(), fontsize=11)
finish(fig, "07-gaussian-loss", 4, "The conclusion",
       "With fixed noise standard deviation 1, negative log-density equals half the squared error plus a constant. Making Gaussian errors more likely therefore favors the same predictions as minimizing squared error.")

fig, axes = panels(2)
z = np.linspace(-6, 6, 300); p = 1/(1+np.exp(-z))
axes[0].plot(z, p, color=BLUE); axes[0].axhline(.5, color=GRAY, ls="--")
axes[0].set(xlabel="linear score z", ylabel="predicted probability", title="Sigmoid converts a score to a probability")
p = np.linspace(.01, .99, 300)
axes[1].plot(p, -np.log(p), color=BLUE, label="true class 1")
axes[1].plot(p, -np.log(1-p), color=ORANGE, label="true class 0")
axes[1].set(xlabel="predicted probability of class 1", ylabel="binary cross-entropy", title="Confident wrong predictions cost more")
axes[1].legend()
for ax in axes: ax.set_title(ax.get_title(), fontsize=11)
finish(fig, "07-logistic", 5, "What the loss does",
       "The sigmoid maps the linear score into [0, 1]. Binary cross-entropy gets large when the model assigns very little probability to the true class.")

fig, axes = panels(2)
scores = np.array([1.5, .2, -.7]); probs = np.exp(scores)/np.exp(scores).sum()
axes[0].bar(["A", "B", "C"], scores, color=GRAY)
axes[0].set(ylabel="score", title="Separate demonstration: raw scores")
axes[1].bar(["A", "B", "C"], probs, color=[BLUE, ORANGE, GREEN])
axes[1].set(ylabel="probability", ylim=(0, 1), title="Softmax: positive probabilities sum to 1")
for i, prob in enumerate(probs): axes[1].text(i, prob+.03, f"{prob:.3f}", ha="center")
for ax in axes: ax.set_title(ax.get_title(), fontsize=11)
finish(fig, "07-softmax", 6, "The model",
       "For demonstration scores [1.5, 0.2, −0.7], softmax preserves which class ranks highest while turning all scores into positive probabilities. Displayed probabilities are rounded.")

fig, axes = panels(2)
rng = np.random.default_rng(77)
x = np.linspace(-1, 1, 10); y = .8*x + .4 + rng.normal(0, .18, 10)
grid = np.linspace(-1, 1, 400)
for ax, degree, title in zip(axes, [1, 9], ["Simple fit: captures the broad trend", "Flexible fit: passes through training points"]):
    curve = np.polynomial.Polynomial.fit(x, y, degree)(grid)
    ax.plot(grid, .8*grid+.4, color=GRAY, ls="--", label="underlying trend")
    ax.plot(grid, curve, color=BLUE, label="fitted model")
    ax.scatter(x, y, color=ORANGE, zorder=4, label="training points")
    ax.set(xlabel="feature", ylabel="target", ylim=(-1.5, 2.3))
    ax.set_title(title, fontsize=11); ax.legend(fontsize=9)
finish(fig, "07-overfitting", 7, "The problem: memorizing instead of learning",
       "Synthetic demonstration: the flexible curve exactly interpolates ten noisy training points, but invents swings between them. The simple fit misses some points while staying closer to the underlying trend.")

fig, (ax,) = panels()
w = np.linspace(-2, 2, 300)
ax.plot(w, w*w, color=BLUE, label="L2 penalty: w²")
ax.plot(w, np.abs(w), color=ORANGE, label="L1 penalty: |w|")
ax.set(xlabel="one weight w", ylabel="penalty", title="Regularization adds a cost for large weights")
ax.legend()
finish(fig, "07-penalties", 7, "L1 regularization",
       "A one-weight comparison: L2 has a smooth bowl with a slope that grows with the weight's magnitude. L1 has a corner at zero and a constant slope magnitude away from zero.")

fig, (ax,) = panels(height=3.2)
flow(ax, ["Input x", "Weighted sum\nW x + b", "Activation\ne.g. ReLU", "Output values"],
     "A layer: combine inputs, then apply a nonlinear function", "Forward: compute values →     Backward: propagate gradients ←")
finish(fig, "07-network", 8, "Training: we need every gradient",
       "Each layer combines inputs with a matrix and bias, then applies an activation to each value. Backpropagation sends sensitivities backward through these operations using the chain rule.")

if __name__ == "__main__":
    assert len(FIGURES) == len({item["name"] for item in FIGURES})
    assert all((OUT / (item["name"] + ".png")).is_file() for item in FIGURES)
    print(json.dumps(FIGURES, indent=2, ensure_ascii=False))
