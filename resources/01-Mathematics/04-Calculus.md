# 04 — Calculus

**Time: ~10 hours** (spread it over 4 days) · **You need: [01 Algebra](01-Algebra.md), [02 Functions](02-Functions.md), [03 Linear Algebra](03-Linear-Algebra.md) §1–§5 and §9–§12** · **Code lab: `math/04_calculus.py`**

## Before you start

**Calculus** is the math of **change**: how fast something changes, and in which direction it changes most. That's exactly what's needed to find the lowest point of a complicated function, which is what "learning" means for a machine.

You will **not** learn integration techniques, trick limit problems, or trig identities here. Only what's needed for ML.

**How to read it:**

- Go **in order**. Each section uses the ones before it.
- **Check things with numbers.** Nearly every rule in this file can be checked by plugging in a tiny step on a calculator. Do it. That's how the rules stop feeling like magic.
- When you see a worked example, **cover the solution and try it first**.
- Say each symbol aloud using its "read it aloud as" note.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.
- The **"Why ML cares"** boxes are motivation only.

**What you'll be able to do by the end:**

- Explain what a derivative is, as a slope and as a sensitivity, and compute derivatives with the rules
- Use the chain rule on long chains of functions, step by step
- Compute partial derivatives and gradients, and explain why the gradient points uphill
- Find minimums, and run gradient descent by hand

---

## Contents

1. [How fast is something changing?](#1-how-fast-is-something-changing)
2. [Limits](#2-limits)
3. [The derivative](#3-the-derivative)
4. [Derivative rules](#4-derivative-rules)
5. [The chain rule](#5-the-chain-rule)
6. [Functions of several inputs and partial derivatives](#6-functions-of-several-inputs-and-partial-derivatives)
7. [The gradient](#7-the-gradient)
8. [The Jacobian](#8-the-jacobian)
9. [Second derivatives and curvature](#9-second-derivatives-and-curvature)
10. [Finding the lowest point](#10-finding-the-lowest-point)
11. [Gradient descent](#11-gradient-descent)
12. [Code lab](#code-lab--math04_calculuspy)
13. [Check yourself](#check-yourself)

---

## 1. How fast is something changing?

### The problem

A car starts from rest and speeds up. After $t$ seconds, it has traveled $d(t) = t^2$ meters.

| $t$ (seconds) | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $d(t)$ (meters) | 0 | 1 | 4 | 9 | 16 |

**How fast is the car going at exactly $t = 2$?**

### Average speed is easy

Average speed = distance traveled ÷ time taken. Between $t = 1$ and $t = 3$:

$$
\frac{d(3) - d(1)}{3 - 1} = \frac{9 - 1}{2} = 4 \text{ m/s}
$$

That's just the **slope between two points** on the graph (Algebra §6). It's called the **average rate of change**.

### Speed at one instant is hard

At exactly $t = 2$, there's no time interval: you'd be dividing $\frac{0}{0}$. But you can use **smaller and smaller** intervals starting at $t = 2$:

| Interval | Distance change | Time change | Average speed |
|---|---|---|---|
| 2 to 3 | $9 - 4 = 5$ | 1 | 5 |
| 2 to 2.1 | $4.41 - 4 = 0.41$ | 0.1 | 4.1 |
| 2 to 2.01 | $4.0401 - 4 = 0.0401$ | 0.01 | 4.01 |
| 2 to 2.001 | $4.004001 - 4 = 0.004001$ | 0.001 | 4.001 |

The average speeds are **heading toward 4**. So the speed at exactly $t = 2$ is **4 m/s**.

That process ("shrink the interval and see where the answer is heading") is the whole idea of calculus. The next two sections make it precise.

### The picture

On a graph of $d(t)$, the slope between two points is the slope of a straight line through both of them. As the second point slides closer to the first, that line turns into the **tangent line**: the straight line that just touches the curve at one point and points the same way the curve is going there.

**The instant rate of change = the slope of the tangent line.**

### Exercises

**1.1.** For $d(t) = t^2$, find the average speed from $t = 3$ to $t = 4$, and from $t = 3$ to $t = 3.01$. What do you think the speed at exactly $t = 3$ is?

**1.2.** For $f(x) = 3x + 1$, find the average rate of change from $x = 0$ to $x = 5$, and from $x = 2$ to $x = 2.01$. Why are they the same?

<details>
<summary>Solutions</summary>

**1.1.** $\frac{16 - 9}{1} = 7$ and $\frac{9.0601 - 9}{0.01} = 6.01$. Heading toward 6.

**1.2.** Both are 3. A straight line has the same slope everywhere.

</details>

---

## 2. Limits

### The idea

A **limit** describes where a function's output is **heading** as the input gets closer and closer to some value, even if you can't plug that value in directly.

### Notation

$$
\lim_{h \to 0} (4 + h) = 4
$$

Read aloud as "**the limit as h approaches zero** of four plus h equals four."

- $\lim$ is short for "limit."
- $h \to 0$ underneath means "$h$ gets closer and closer to 0." ($\to$ was introduced in Functions §7.)

### Finding a limit: tables and algebra

**Example.** $\lim_{h \to 0} \frac{(2 + h)^2 - 4}{h}$

You can't plug in $h = 0$: you'd get $\frac{0}{0}$. Two ways to find where it's heading:

**Way 1: a table** (this is exactly §1's table)

| $h$ | 0.1 | 0.01 | 0.001 |
|---|---|---|---|
| value | 4.1 | 4.01 | 4.001 |

**Way 2: simplify first, then plug in**

| Step | What we did |
|---|---|
| $\frac{(2 + h)^2 - 4}{h}$ | Start |
| $= \frac{4 + 4h + h^2 - 4}{h}$ | Expanded $(2 + h)^2$ (Algebra §7) |
| $= \frac{4h + h^2}{h}$ | The 4s cancel |
| $= 4 + h$ | Divided both terms by $h$ (allowed, because $h$ is close to 0, not equal to 0) |
| $\to 4$ as $h \to 0$ | Now plugging in $h = 0$ is fine |

**The key point:** the limit only cares about what happens **near** the value, never **at** it.

### Limits toward infinity

$\lim_{x \to \infty}$ asks where the output heads as $x$ grows without end.

- $\lim_{x \to \infty} \frac{1}{x} = 0$: dividing 1 by bigger and bigger numbers gives smaller and smaller results.
- $\lim_{x \to \infty} e^{-x} = 0$: same idea, since $e^{-x} = \frac{1}{e^x}$.

That's how we described the sigmoid's ends in Functions §9.

### Continuity

A function is **continuous** at a point if there's no jump, gap, or hole there: you could draw it without lifting your pen. Formally, the limit as you approach the point equals the actual value there.

- $x^2$, $e^x$, sigmoid, and ReLU are continuous everywhere.
- $\frac{1}{x}$ is not continuous at $x = 0$ (it blows up there).

### Exercises

**2.1.** Find $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$ by simplifying first.

**2.2.** Make a table for $\frac{(3 + h)^2 - 9}{h}$ with $h = 0.1, 0.01, 0.001$. What's the limit as $h \to 0$?

**2.3.** Find $\lim_{x \to \infty} \frac{5}{x + 2}$.

**2.4.** Is $|x|$ continuous at $x = 0$?

<details>
<summary>Hint</summary>

2.1: $x^2 - 1 = (x - 1)(x + 1)$. Check by expanding the right side.

</details>

<details>
<summary>Solutions</summary>

**2.1.** $\frac{(x - 1)(x + 1)}{x - 1} = x + 1 \to 2$.

**2.2.** $6.1, 6.01, 6.001$. The limit is 6.

**2.3.** The bottom grows without end, so the fraction heads to 0.

**2.4.** Yes. The V shape has a corner but no gap.

</details>

---

## 3. The derivative

### Definition

The **derivative** of a function $f$ at a point $x$ is the instant rate of change there: the slope of the tangent line. It's the "shrink the interval" process from §1, written as a limit:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Decode each piece:

| Piece | Meaning |
|---|---|
| $h$ | a small step to the right |
| $f(x + h) - f(x)$ | how much the output changed ("rise") |
| $\frac{\ldots}{h}$ | divided by how much the input changed ("run"): a slope |
| $\lim_{h \to 0}$ | shrink the step to nothing |

### Notation

Two ways to write the derivative, and you'll see both:

| Notation | Read it aloud as | Style |
|---|---|---|
| $f'(x)$ | "**f prime of x**" | short |
| $\frac{df}{dx}$ | "**d f d x**" | shows what's changing with respect to what |

$\frac{df}{dx}$ is **not** an ordinary fraction, but it's helpful to think of it as "a tiny change in $f$ divided by a tiny change in $x$." Sometimes it's written $\frac{d}{dx}f(x)$, read "the derivative with respect to x of f of x."

### Worked example: the derivative of $x^2$ from the definition

| Step | What we did |
|---|---|
| $\frac{(x + h)^2 - x^2}{h}$ | Put $f(x) = x^2$ into the definition |
| $= \frac{x^2 + 2xh + h^2 - x^2}{h}$ | Expanded $(x + h)^2$ |
| $= \frac{2xh + h^2}{h}$ | The $x^2$ terms cancel |
| $= 2x + h$ | Divided both terms by $h$ |
| $\to 2x$ | Let $h \to 0$ |

$$
\frac{d}{dx}x^2 = 2x
$$

**Check with §1:** at $x = 2$, the derivative is $2 \times 2 = 4$ ✓. That matches the speed we found by shrinking intervals.

**The derivative is itself a function.** For $f(x) = x^2$, the slope is different at every point: $f'(1) = 2$, $f'(3) = 6$, $f'(-1) = -2$. The formula $f'(x) = 2x$ gives the slope anywhere.

### What the sign of the derivative tells you

| $f'(x)$ | The function at that point is… |
|---|---|
| positive | going **up** (as you move right) |
| negative | going **down** |
| zero | **flat** (possibly a top or bottom) |
| large (positive or negative) | changing steeply |

For $x^2$: negative slope left of 0 (going down), zero at 0 (the bottom), positive to the right (going up). That's the U shape.

### The derivative as sensitivity

Here's another way to read the derivative, and it's the one ML uses most:

> **If you nudge the input by a tiny amount $\varepsilon$, the output changes by about $f'(x) \cdot \varepsilon$.**

$$
f(x + \varepsilon) \approx f(x) + f'(x) \cdot \varepsilon
$$

($\varepsilon$ is the Greek letter **epsilon**, commonly used for "a tiny number.")

**Check with numbers.** $f(x) = x^2$ at $x = 3$: $f(3) = 9$ and $f'(3) = 6$.

- Prediction: $f(3.01) \approx 9 + 6 \times 0.01 = 9.06$
- Actual: $3.01^2 = 9.0601$ ✓ very close

The derivative tells you how **sensitive** the output is to the input.

### Estimating a derivative with numbers

When you have a function but don't know its derivative formula, you can estimate it using a tiny step on **both** sides (more accurate than one side):

$$
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h} \qquad (\text{with } h \text{ tiny, like } 0.00001)
$$

This is called the **central difference**. You'll use it in the code lab to **check** derivatives you calculate by hand.

### Exercises

**3.1.** Use the definition to find the derivative of $f(x) = 3x$. Does the answer match what you know about the slope of a line?

**3.2.** Use the definition to find the derivative of $f(x) = x^3$.

**3.3.** $f(x) = x^3$. Use your answer to 3.2 and the sensitivity formula to estimate $f(2.05)$. Compare with the actual value.

**3.4.** Estimate the derivative of $f(x) = x^2$ at $x = 5$ using the central difference with $h = 0.1$.

**3.5.** For $f(x) = x^2$, where is the function going down? Going up? Flat?

<details>
<summary>Hint</summary>

3.2: $(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$. Check it by expanding $(x + h)(x + h)(x + h)$.

</details>

<details>
<summary>Solutions</summary>

**3.1.** $\frac{3(x + h) - 3x}{h} = \frac{3h}{h} = 3$. Yes, the slope of $3x$ is 3 everywhere.

**3.2.** $\frac{3x^2h + 3xh^2 + h^3}{h} = 3x^2 + 3xh + h^2 \to 3x^2$.

**3.3.** $f(2) = 8$, $f'(2) = 12$. Estimate: $8 + 12 \times 0.05 = 8.6$. Actual: $2.05^3 = 8.615$.

**3.4.** $\frac{5.1^2 - 4.9^2}{0.2} = \frac{26.01 - 24.01}{0.2} = 10$. The exact answer is $2 \times 5 = 10$ ✓

**3.5.** Down for $x < 0$, up for $x > 0$, flat at $x = 0$.

</details>

---

## 4. Derivative rules

### The problem

Using the limit definition every time is slow. Instead, we work out a few **rules** once, and then use them forever. Each rule below comes with a reason and a number check.

### Rule 1: constants have derivative 0

$$
\frac{d}{dx}\,c = 0
$$

**Why:** $f(x) = 5$ is a flat horizontal line. Its slope is 0 everywhere.

### Rule 2: the power rule

$$
\frac{d}{dx}\,x^n = n\,x^{n-1}
$$

In words: **bring the exponent down in front, then subtract 1 from the exponent.**

**Why:** we already showed $x^2 \to 2x$ and $x^3 \to 3x^2$ (§3). The pattern continues for every power. It works for **negative and fractional** powers too.

| Function | Rewrite (Algebra §3) | Power rule | Result |
|---|---|---|---|
| $x^5$ | | $5x^4$ | $5x^4$ |
| $x$ | $x^1$ | $1 \cdot x^0$ | $1$ |
| $\frac{1}{x}$ | $x^{-1}$ | $-1 \cdot x^{-2}$ | $-\frac{1}{x^2}$ |
| $\sqrt{x}$ | $x^{1/2}$ | $\frac{1}{2}x^{-1/2}$ | $\frac{1}{2\sqrt{x}}$ |

**Number check for $\frac{1}{x}$ at $x = 2$:** the rule says $-\frac{1}{4} = -0.25$. Central difference with $h = 0.001$: $\frac{\frac{1}{2.001} - \frac{1}{1.999}}{0.002} \approx \frac{0.49975 - 0.50025}{0.002} = -0.25$ ✓

### Rule 3: constant multiples come along

$$
\frac{d}{dx}\,[c \cdot f(x)] = c \cdot f'(x)
$$

**Why:** if you triple a function, every rise triples, so every slope triples.

Example: $\frac{d}{dx}\,7x^3 = 7 \cdot 3x^2 = 21x^2$.

### Rule 4: sums split up

$$
\frac{d}{dx}\,[f(x) + g(x)] = f'(x) + g'(x)
$$

**Why:** if two quantities are both changing, their total changes by the sum of their changes.

**Example.** $\frac{d}{dx}(3x^3 + 2x^2 - 5x + 7)$

| Term | Derivative | Rule used |
|---|---|---|
| $3x^3$ | $9x^2$ | power + constant multiple |
| $2x^2$ | $4x$ | power + constant multiple |
| $-5x$ | $-5$ | power + constant multiple |
| $7$ | $0$ | constant |
| **Total** | $9x^2 + 4x - 5$ | sum |

### Rule 5: $e^x$ is its own derivative

$$
\frac{d}{dx}\,e^x = e^x
$$

**This is what makes $e$ special.** At every point, the slope of $e^x$ equals its height. At $x = 0$ the height is 1, so the slope is 1. At $x = 2$ the height is 7.389, so the slope is 7.389.

**Number check at $x = 2$:** $\frac{e^{2.001} - e^{2}}{0.001} \approx \frac{7.396449 - 7.389056}{0.001} \approx 7.39$ ✓

(In fact, $e$ is exactly the base where this works. For $2^x$, the slope is about $0.693 \times 2^x$ instead. That $0.693$ is $\ln 2$.)

### Rule 6: the derivative of $\ln x$

$$
\frac{d}{dx}\,\ln x = \frac{1}{x}
$$

**Number check at $x = 2$:** the rule says $0.5$. $\frac{\ln(2.001) - \ln(2)}{0.001} \approx \frac{0.693647 - 0.693147}{0.001} = 0.5$ ✓

This matches the graph from Functions §7: $\ln$ is steep near 0 (large $\frac{1}{x}$) and flattens out for big $x$ (small $\frac{1}{x}$).

### Rule 7: the product rule

$$
\frac{d}{dx}\,[f(x) \cdot g(x)] = f'(x)\,g(x) + f(x)\,g'(x)
$$

**Warning:** it is **not** $f' \cdot g'$.

**Why, with a picture:** think of $f \cdot g$ as the area of a rectangle with width $f$ and height $g$. Nudge $x$ a tiny bit: the width grows by $\Delta f$ and the height grows by $\Delta g$. The area grows by two strips: $\Delta f \cdot g$ along one side and $f \cdot \Delta g$ along the other. (The tiny corner $\Delta f \cdot \Delta g$ is so small it disappears in the limit.) ($\Delta$ is the capital Greek letter **delta**, meaning "change in.")

**Example.** $\frac{d}{dx}(x^2 e^x)$

| Piece | Value |
|---|---|
| $f = x^2$, $f' = 2x$ | |
| $g = e^x$, $g' = e^x$ | |
| $f'g + fg'$ | $2x\,e^x + x^2 e^x = e^x(x^2 + 2x)$ |

### Summary table

| Function | Derivative |
|---|---|
| $c$ | $0$ |
| $x^n$ | $n x^{n-1}$ |
| $c \cdot f$ | $c \cdot f'$ |
| $f + g$ | $f' + g'$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |
| $f \cdot g$ | $f'g + fg'$ |

### Exercises

**4.1.** Differentiate $f(x) = 4x^3 - 6x + 2$.

**4.2.** Differentiate $f(x) = x^2 + 3x$. Then find $f'(2)$, and the $x$ where the slope is zero.

**4.3.** Differentiate $f(x) = \frac{3}{x^2}$ (rewrite it first).

**4.4.** Differentiate $f(x) = x\ln x$.

**4.5.** Differentiate $f(x) = 5e^x - x^4$.

**4.6.** Use a calculator to check your 4.2 answer at $x = 2$ with the central difference ($h = 0.001$).

<details>
<summary>Hint</summary>

4.3: $\frac{3}{x^2} = 3x^{-2}$.
4.4: product rule with $f = x$ and $g = \ln x$.

</details>

<details>
<summary>Solutions</summary>

**4.1.** $12x^2 - 6$.

**4.2.** $f'(x) = 2x + 3$. $f'(2) = 7$. Slope zero: $2x + 3 = 0$, so $x = -1.5$.

**4.3.** $3 \cdot (-2)x^{-3} = -\frac{6}{x^3}$.

**4.4.** $1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$.

**4.5.** $5e^x - 4x^3$.

**4.6.** $\frac{f(2.001) - f(1.999)}{0.002} = \frac{10.007001 - 9.993001}{0.002} = 7$ ✓

</details>

---

## 5. The chain rule

### The problem

How do you differentiate $(3x + 1)^2$, or $e^{2x}$, or $\ln(x^2 + 1)$? These are **compositions**: functions inside functions (Functions §3). None of the rules in §4 handle them directly.

### Intuition: gears

Picture three gears connected in a row: $x$ turns $u$, and $u$ turns $y$.

- If $u$ turns **3 times** as fast as $x$,
- and $y$ turns **2 times** as fast as $u$,
- then $y$ turns $2 \times 3 = $ **6 times** as fast as $x$.

**Rates of change multiply along a chain.**

### The rule

If $y$ depends on $u$, and $u$ depends on $x$:

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

Read aloud as "d y d x equals d y d u times d u d x."

In function notation, for $f(g(x))$:

$$
\frac{d}{dx}\,f(g(x)) = f'(g(x)) \cdot g'(x)
$$

In words: **the derivative of the outside function (evaluated at the inside), times the derivative of the inside.**

**Why it works:** for small changes, $\frac{\Delta y}{\Delta x} = \frac{\Delta y}{\Delta u} \cdot \frac{\Delta u}{\Delta x}$. That's true for ordinary fractions, because the $\Delta u$ cancels. Shrink the changes to zero and you get the rule.

### The recipe

1. **Name the inside** with a new letter, $u$.
2. Differentiate the **outside** with respect to $u$.
3. Differentiate the **inside** with respect to $x$.
4. **Multiply**, then put the inside back in place of $u$.

### Worked example 1: $(3x + 1)^2$

| Step | Result |
|---|---|
| Inside: $u = 3x + 1$ | Outside: $y = u^2$ |
| $\frac{dy}{du}$ | $2u$ |
| $\frac{du}{dx}$ | $3$ |
| Multiply | $2u \cdot 3 = 6u$ |
| Put $u$ back | $6(3x + 1)$ |

**Number check at $x = 1$:** the rule says $6 \times 4 = 24$. Actual: $\frac{(4.003)^2 - 16}{0.001} = \frac{16.024009 - 16}{0.001} \approx 24.009$ ✓

### Worked example 2: $e^{2x}$

| Step | Result |
|---|---|
| Inside: $u = 2x$ | Outside: $y = e^u$ |
| $\frac{dy}{du}$ | $e^u$ |
| $\frac{du}{dx}$ | $2$ |
| Result | $2e^{2x}$ |

### Worked example 3: $\ln(x^2 + 1)$

| Step | Result |
|---|---|
| Inside: $u = x^2 + 1$ | Outside: $y = \ln u$ |
| $\frac{dy}{du}$ | $\frac{1}{u}$ |
| $\frac{du}{dx}$ | $2x$ |
| Result | $\frac{2x}{x^2 + 1}$ |

### Worked example 4: the sigmoid's derivative

$\sigma(z) = \frac{1}{1 + e^{-z}}$ (Functions §9). Rewrite it as $(1 + e^{-z})^{-1}$.

| Step | What we did |
|---|---|
| Outside: $u^{-1}$, inside: $u = 1 + e^{-z}$ | Named the pieces |
| $\frac{d}{du}u^{-1} = -u^{-2}$ | Power rule |
| $\frac{du}{dz} = -e^{-z}$ | Derivative of $e^{-z}$ is $-e^{-z}$ (chain rule again, with inside $-z$) |
| $\sigma'(z) = -u^{-2} \cdot (-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2}$ | Multiplied; two minus signs make a plus |
| $= \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}}$ | Split the fraction into two factors |
| $= \sigma(z) \cdot (1 - \sigma(z))$ | The first factor is $\sigma$. The second is $1 - \sigma$ (shown in Functions §9's symmetry table, row 3) |

$$
\sigma'(z) = \sigma(z)\,\big(1 - \sigma(z)\big)
$$

What this tells you:

- At $z = 0$: $\sigma = 0.5$, so the slope is $0.5 \times 0.5 = 0.25$. That's the steepest the sigmoid ever gets.
- At $z = 5$: $\sigma \approx 0.993$, so the slope is $0.993 \times 0.007 \approx 0.0066$. Nearly flat. That's the **saturation** from Functions §9, now measured precisely.

### The derivative of ReLU

ReLU (Functions §8) is flat at 0 on the left and a 45° line on the right, so its slope is:

$$
\text{ReLU}'(x) = \begin{cases}1 & \text{if } x > 0\\0 & \text{if } x < 0\end{cases}
$$

At exactly $x = 0$ there's a corner, and no single slope. Software simply uses 0 there.

### Long chains: break into steps

For a long chain, give every step a name and multiply all the local derivatives.

**Example.** $y = (e^{2x})^2$ at $x = 0.5$.

**Forward: calculate each step's value.**

| Step | Formula | Value at $x = 0.5$ |
|---|---|---|
| 1 | $u = 2x$ | $1$ |
| 2 | $v = e^u$ | $e \approx 2.718$ |
| 3 | $y = v^2$ | $7.389$ |

**Backward: calculate each step's local derivative, then multiply.**

| Local derivative | Formula | Value |
|---|---|---|
| $\frac{dy}{dv}$ | $2v$ | $5.437$ |
| $\frac{dv}{du}$ | $e^u$ | $2.718$ |
| $\frac{du}{dx}$ | $2$ | $2$ |
| $\frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}$ | multiply | $5.437 \times 2.718 \times 2 \approx 29.56$ |

**Check another way:** $(e^{2x})^2 = e^{4x}$ (Algebra §3, Rule 3), whose derivative is $4e^{4x}$. At $x = 0.5$: $4e^2 \approx 29.56$ ✓

This forward-then-backward bookkeeping is worth practicing. It's exactly how computers calculate derivatives of huge chains.

> **Why ML cares:** A neural network is a long chain of functions (Functions §3). To learn, it needs the derivative of its final error with respect to every adjustable number deep inside the chain. The method, called **backpropagation**, is exactly the forward-then-backward table above, done automatically.

### Exercises

**5.1.** Differentiate $(5x - 2)^3$.

**5.2.** Differentiate $e^{-x^2}$.

**5.3.** Differentiate $\sqrt{4x + 1}$.

**5.4.** Show that $\frac{d}{dz}\ln(1 + e^z) = \sigma(z)$.

**5.5.** Differentiate $\ln(\sigma(z))$ and simplify as much as you can.

**5.6.** Make a forward and backward table for $y = \ln(1 + x^2)$ at $x = 2$. Then check your answer with the formula from worked example 3.

<details>
<summary>Hint</summary>

5.3: rewrite as $(4x + 1)^{1/2}$.
5.4: after differentiating you get $\frac{e^z}{1 + e^z}$. Divide the top and bottom by $e^z$.
5.5: outside is $\ln u$ with derivative $\frac{1}{u}$, and inside is $\sigma(z)$ with derivative $\sigma(1 - \sigma)$.

</details>

<details>
<summary>Solutions</summary>

**5.1.** $3(5x - 2)^2 \cdot 5 = 15(5x - 2)^2$.

**5.2.** $-2x\,e^{-x^2}$.

**5.3.** $\frac{1}{2}(4x + 1)^{-1/2} \cdot 4 = \frac{2}{\sqrt{4x + 1}}$.

**5.4.** $\frac{1}{1 + e^z} \cdot e^z = \frac{e^z}{1 + e^z} = \frac{1}{e^{-z} + 1} = \sigma(z)$.

**5.5.** $\frac{1}{\sigma(z)} \cdot \sigma(z)(1 - \sigma(z)) = 1 - \sigma(z)$.

**5.6.** Forward: $u = x^2 = 4$, $v = 1 + u = 5$, $y = \ln v \approx 1.609$. Backward: $\frac{dy}{dv} = \frac{1}{5} = 0.2$, $\frac{dv}{du} = 1$, $\frac{du}{dx} = 2x = 4$. Product: $0.8$. Formula: $\frac{2(2)}{4 + 1} = 0.8$ ✓

</details>

---

## 6. Functions of several inputs and partial derivatives

### The problem

So far, every function had **one** input. But most real quantities depend on **several** things. The price of a house depends on floor area **and** location **and** age. The height of land depends on how far east **and** how far north you are.

### Functions with two inputs

$$
f(x, y) = x^2 + y^2
$$

Read aloud as "f of x comma y." It takes two numbers in and gives one number out.

**The picture: terrain.** Think of $(x, y)$ as a location on a map, and $f(x, y)$ as the **height of the ground** there. The graph is a surface, like hills and valleys. $f(x, y) = x^2 + y^2$ is a bowl with its bottom at $(0, 0)$.

**Contour lines:** on a hiking map, a contour line connects all the points at the same height. For $x^2 + y^2$, the contour lines are circles around the origin.

### The question: how does it change?

Standing at a point, "how steep is it?" depends on **which direction you walk**. The simplest directions to ask about are straight east (changing only $x$) and straight north (changing only $y$).

### Partial derivatives

The **partial derivative with respect to $x$** asks: how fast does $f$ change if I nudge **only $x$**, keeping $y$ frozen?

$$
\frac{\partial f}{\partial x}
$$

- Read aloud as "**partial f partial x**" or "the partial derivative of f with respect to x."
- The curly $\partial$ (instead of $d$) signals that there are other inputs being held still.

**How to compute it: treat every other input as a constant number, then differentiate normally.**

### Worked example

$f(x, y) = x^2 + 3xy + y^2$

**With respect to $x$** (pretend $y$ is a fixed number, like 5):

| Term | Treat as | Derivative with respect to $x$ |
|---|---|---|
| $x^2$ | $x^2$ | $2x$ |
| $3xy$ | $(3y) \cdot x$, a constant times $x$ | $3y$ |
| $y^2$ | a constant | $0$ |
| **Total** | | $\frac{\partial f}{\partial x} = 2x + 3y$ |

**With respect to $y$** (pretend $x$ is fixed):

| Term | Treat as | Derivative with respect to $y$ |
|---|---|---|
| $x^2$ | a constant | $0$ |
| $3xy$ | $(3x) \cdot y$ | $3x$ |
| $y^2$ | $y^2$ | $2y$ |
| **Total** | | $\frac{\partial f}{\partial y} = 3x + 2y$ |

**Number check at $(1, 2)$:** $\frac{\partial f}{\partial x} = 2 + 6 = 8$. Now nudge only $x$: $f(1.001, 2) = 1.002001 + 6.006 + 4 = 11.008001$, and $f(1, 2) = 11$. Rate: $\frac{0.008001}{0.001} \approx 8.001$ ✓

**The picture:** slice the terrain with a vertical cut running east–west through your point. That slice is an ordinary curve, and $\frac{\partial f}{\partial x}$ is its slope.

### Exercises

**6.1.** $f(x, y) = 4x^3y^2$. Find both partial derivatives.

**6.2.** $f(x, y) = x^2y + e^{xy}$. Find both partial derivatives.

**6.3.** $f(x, y) = (x - 2)^2 + (y + 1)^2$. Find both partials. Where are **both** equal to zero? What's special about that point?

**6.4.** $f(w, b) = (6 - 2w - b)^2$. Find $\frac{\partial f}{\partial w}$ and $\frac{\partial f}{\partial b}$.

<details>
<summary>Hint</summary>

6.2: for $e^{xy}$ with respect to $x$, the inside is $xy$ and its derivative with respect to $x$ is $y$ (chain rule).
6.4: chain rule. The inside is $6 - 2w - b$.

</details>

<details>
<summary>Solutions</summary>

**6.1.** $\frac{\partial f}{\partial x} = 12x^2y^2$ and $\frac{\partial f}{\partial y} = 8x^3y$.

**6.2.** $\frac{\partial f}{\partial x} = 2xy + y\,e^{xy}$ and $\frac{\partial f}{\partial y} = x^2 + x\,e^{xy}$.

**6.3.** $2(x - 2)$ and $2(y + 1)$. Both zero at $(2, -1)$: the bottom of the bowl.

**6.4.** $\frac{\partial f}{\partial w} = 2(6 - 2w - b)(-2) = -4(6 - 2w - b)$ and $\frac{\partial f}{\partial b} = -2(6 - 2w - b)$.

</details>

---

## 7. The gradient

### The problem

Partial derivatives tell you the slope going east and the slope going north. But you can walk in **any** direction. Which direction is the **steepest** uphill? And how steep is it?

### Definition

The **gradient** puts all the partial derivatives into one vector (Linear Algebra §1):

$$
\nabla f = \left[\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y}\right]
$$

- $\nabla$ is read "**grad**" or "**nabla**" or "del." So $\nabla f$ is "grad f."
- With more inputs, the gradient just has more components, one per input.

**Example.** $f(x, y) = x^2 + y^2$: $\nabla f = [2x, 2y]$. At the point $(1, 2)$: $\nabla f = [2, 4]$.

### The three facts about the gradient

1. **Direction:** $\nabla f$ points in the direction of **steepest uphill**.
2. **Length:** $\lVert \nabla f \rVert$ is **how steep** that steepest direction is.
3. **Level ground:** at the very top of a hill or bottom of a valley, $\nabla f = \mathbf{0}$.

**Check fact 1 with the bowl:** at $(1, 2)$, $\nabla f = [2, 4]$ points **away from the origin**, which is exactly the uphill direction of a bowl centered at the origin ✓

### Why the gradient points the steepest way

**Step 1: the slope in any direction.** Walk from a point in direction $\mathbf{u} = [u_1, u_2]$, a unit vector (Linear Algebra §3), taking a tiny step of size $\varepsilon$. Your $x$ changes by $\varepsilon u_1$, and your $y$ changes by $\varepsilon u_2$.

Using the sensitivity idea from §3 for each input separately, and adding the two effects:

$$
\text{change in } f \approx \frac{\partial f}{\partial x}(\varepsilon u_1) + \frac{\partial f}{\partial y}(\varepsilon u_2) = \varepsilon\,(\nabla f \cdot \mathbf{u})
$$

So the slope in direction $\mathbf{u}$ is:

$$
D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}
$$

This is called the **directional derivative**, read "the derivative of f in direction u." It's a dot product (Linear Algebra §5).

**Step 2: which direction makes it biggest?** Use the geometric meaning of the dot product:

$$
\nabla f \cdot \mathbf{u} = \lVert \nabla f \rVert\,\lVert \mathbf{u} \rVert\cos\theta = \lVert \nabla f \rVert\cos\theta
$$

(since $\mathbf{u}$ has length 1). Here $\theta$ is the angle between $\mathbf{u}$ and the gradient.

| Direction you walk | $\theta$ | $\cos\theta$ | Slope |
|---|---|---|---|
| **along** the gradient | $0°$ | $1$ | $+\lVert \nabla f \rVert$: **steepest uphill** |
| perpendicular to the gradient | $90°$ | $0$ | $0$: level (along a contour line) |
| **opposite** the gradient | $180°$ | $-1$ | $-\lVert \nabla f \rVert$: **steepest downhill** |

**So $-\nabla f$ (the negative gradient) is the direction of steepest descent.** This one fact is the foundation of how ML models learn (§11).

### Worked example

$f(x, y) = x^2 + y^2$ at $(1, 2)$, where $\nabla f = [2, 4]$ and $\lVert \nabla f \rVert = \sqrt{20} \approx 4.47$.

| Direction $\mathbf{u}$ | $\nabla f \cdot \mathbf{u}$ |
|---|---|
| east: $[1, 0]$ | $2$ |
| north: $[0, 1]$ | $4$ |
| along the gradient: $\frac{[2, 4]}{4.47} = [0.447, 0.894]$ | $0.894 + 3.578 = 4.47$ ← the maximum |
| opposite the gradient: $[-0.447, -0.894]$ | $-4.47$ ← the minimum |

> **Why ML cares:** A model's error depends on many adjustable numbers, which makes a "terrain" in many dimensions. The gradient tells the model which way to adjust all of them at once to make the error go **up** fastest, so the model steps the **opposite** way.

### Exercises

**7.1.** Find $\nabla f$ for $f(x, y) = 3x^2 - 2xy + y^3$. Evaluate it at $(1, 1)$.

**7.2.** For $f(x, y) = x^2 + 3xy + y^2$ at $(1, 1)$: find $\nabla f$, the directional derivative in direction $\left[\frac{3}{5}, \frac{4}{5}\right]$, and the steepest possible slope.

**7.3.** Check that $\left[\frac{3}{5}, \frac{4}{5}\right]$ has length 1.

**7.4.** At some point, $\nabla f = [0, 0]$. What does the terrain look like right there?

**7.5.** In your own words, without formulas: why does walking opposite the gradient go downhill fastest?

<details>
<summary>Solutions</summary>

**7.1.** $[6x - 2y,\ -2x + 3y^2]$. At $(1, 1)$: $[4, 1]$.

**7.2.** $\nabla f = [5, 5]$. Directional derivative: $5(0.6) + 5(0.8) = 7$. Steepest: $\lVert [5, 5] \rVert = \sqrt{50} \approx 7.07$.

**7.3.** $0.36 + 0.64 = 1$ ✓

**7.4.** Flat in every direction: a top, a bottom, or a saddle (§9).

**7.5.** The slope in any direction is (steepness) × (how aligned you are with the gradient). Being as un-aligned as possible, pointing exactly opposite, gives the most negative slope.

</details>

---

## 8. The Jacobian

**Goal of this section:** understand what a Jacobian **is** and why it matters. You won't compute big ones by hand.

### The problem

The gradient handles functions with **many inputs and one output**. But some functions have **many outputs too**. A matrix transformation (Linear Algebra §11) takes a vector in and gives a vector out. How do we describe how each output changes with each input?

### Definition

For a function with $n$ inputs and $m$ outputs, the **Jacobian** is a matrix of **all** the partial derivatives:

$$
J = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots\\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots\\
\vdots & & \ddots
\end{bmatrix}
$$

- **Rows** = outputs. **Columns** = inputs. Shape $m \times n$.
- Entry $(i, j)$ = how output $i$ changes when input $j$ is nudged.
- **Each row is the gradient of one output.**

### Worked example

$\mathbf{f}(x, y) = [\,xy,\ \ x + y^2\,]$: two inputs, two outputs.

| | $\frac{\partial}{\partial x}$ | $\frac{\partial}{\partial y}$ |
|---|---|---|
| $f_1 = xy$ | $y$ | $x$ |
| $f_2 = x + y^2$ | $1$ | $2y$ |

$$
J = \begin{bmatrix}y & x\\1 & 2y\end{bmatrix}, \qquad \text{at } (1, 2):\ J = \begin{bmatrix}2 & 1\\1 & 4\end{bmatrix}
$$

### The Jacobian of a matrix transformation is the matrix itself

Take $\mathbf{f}(\mathbf{x}) = A\mathbf{x}$ with $A = \begin{bmatrix}2 & 3\\1 & 4\end{bmatrix}$. Multiplied out: $\mathbf{f}(x, y) = [\,2x + 3y,\ \ x + 4y\,]$.

Partial derivatives: row 1 is $[2, 3]$, row 2 is $[1, 4]$. **That's exactly $A$.**

This makes sense: a matrix transformation changes at the same rate everywhere, just like a straight line has the same slope everywhere.

### The Jacobian as the best matrix approximation

The sensitivity formula from §3 extends to vectors:

$$
\mathbf{f}(\mathbf{x} + \text{small nudge}) \approx \mathbf{f}(\mathbf{x}) + J \cdot (\text{small nudge})
$$

Close up, **any** smooth function looks like a matrix transformation, and that matrix is the Jacobian. It's the multi-dimensional version of the tangent line.

### The chain rule becomes matrix multiplication

For a chain of vector functions, the Jacobian of the whole chain is **the product of the individual Jacobians**, in order. It's the gears idea (§5), with matrices instead of numbers.

### One rule you'll use constantly

If the final output is a **single number** $L$, and $W$ is a matrix of inputs, then the collection of partial derivatives $\frac{\partial L}{\partial W}$ has **exactly the same shape as $W$**. One partial derivative per entry.

> **Why ML cares:** Each layer of a neural network turns a vector into a vector, so each layer has a Jacobian. Backpropagation multiplies these together from the end back to the start. The "same shape" rule is the quickest way to catch mistakes in hand-calculated derivatives.

### Exercises

**8.1.** Find the Jacobian of $\mathbf{f}(x, y) = [\,x^2,\ \ 3y,\ \ xy\,]$. What's its shape?

**8.2.** Find the Jacobian of $\mathbf{f}(\mathbf{x}) = \begin{bmatrix}5 & -1\\0 & 2\end{bmatrix}\mathbf{x}$ without calculating any partial derivatives. Explain.

**8.3.** $W$ is a $128 \times 63$ matrix, and $L$ is a single number that depends on it. What's the shape of $\frac{\partial L}{\partial W}$?

<details>
<summary>Solutions</summary>

**8.1.** $\begin{bmatrix}2x & 0\\0 & 3\\y & x\end{bmatrix}$, shape $3 \times 2$ (3 outputs, 2 inputs).

**8.2.** $\begin{bmatrix}5 & -1\\0 & 2\end{bmatrix}$. The Jacobian of $A\mathbf{x}$ is $A$.

**8.3.** $128 \times 63$.

</details>

---

## 9. Second derivatives and curvature

### The idea

The derivative tells you the slope. The **second derivative** tells you **how the slope itself is changing**: whether the curve is bending up or bending down.

### Notation and calculation

Take the derivative of the derivative:

$$
f''(x) = \frac{d^2f}{dx^2}
$$

Read $f''(x)$ aloud as "**f double prime of x**."

**Example.** $f(x) = x^3 - 3x$: $f'(x) = 3x^2 - 3$, and $f''(x) = 6x$.

### What it means

| $f''(x)$ | Shape | Picture |
|---|---|---|
| positive | curving **up** | like a U, a bowl that holds water |
| negative | curving **down** | like an ∩, a hill that spills water |
| zero | no bend, at that point | |

For $x^2$: $f'' = 2 > 0$ everywhere, so it's a U everywhere ✓

### Several inputs: saddles — *Good to know*

With two or more inputs, the terrain can curve **up in one direction and down in another**, like a horse saddle or a mountain pass. This is called a **saddle point**.

**Example:** $f(x, y) = x^2 - y^2$. Walking along the x-axis, $f = x^2$ curves up. Walking along the y-axis, $f = -y^2$ curves down. At $(0, 0)$ the gradient is zero, but it's neither a top nor a bottom.

(The full collection of second partial derivatives forms a matrix called the **Hessian**. Its eigenvalues (Linear Algebra §18) tell you the curvature in each principal direction: all positive means a bowl, and mixed signs mean a saddle.)

### Exercises

**9.1.** Find $f''(x)$ for $f(x) = 2x^4 - x^2$. Is the curve bending up or down at $x = 0$? At $x = 1$?

**9.2.** For $f(x, y) = x^2 + 3xy + y^2$, walk along the line $y = -x$ (so $f(t, -t)$). Simplify. Does it go up or down as you move away from the origin? What does that say about $(0, 0)$?

<details>
<summary>Solutions</summary>

**9.1.** $f' = 8x^3 - 2x$, $f'' = 24x^2 - 2$. At 0: $-2$, bending down. At 1: $22$, bending up.

**9.2.** $t^2 - 3t^2 + t^2 = -t^2$: goes down. But along $y = x$: $t^2 + 3t^2 + t^2 = 5t^2$, which goes up. So $(0, 0)$ is a saddle point, not a minimum.

</details>

---

## 10. Finding the lowest point

### The problem

Find the input that makes a function **as small as possible**. This is called **minimizing** the function, and the input is a **minimum**. (The largest is a **maximum**. Both are called **extremes**.)

### The key idea: the bottom is flat

At the very bottom of a smooth valley, the ground is **level**: slope zero. So:

**To find candidates for a minimum or maximum, solve $f'(x) = 0$.**

Points where $f'(x) = 0$ are called **critical points**.

### Then check: bottom, top, or neither?

Use the second derivative (§9):

- $f'' > 0$ (curving up) → **minimum**
- $f'' < 0$ (curving down) → **maximum**
- $f'' = 0$ → inconclusive, check another way

### Worked example

$f(x) = x^3 - 3x$

| Step | Result |
|---|---|
| $f'(x) = 3x^2 - 3$ | Differentiated |
| $3x^2 - 3 = 0 \Rightarrow x^2 = 1$ | Set to zero |
| $x = 1$ or $x = -1$ | Critical points |
| $f''(x) = 6x$ | Second derivative |
| $f''(1) = 6 > 0$ | $x = 1$ is a **minimum**, with $f(1) = -2$ |
| $f''(-1) = -6 < 0$ | $x = -1$ is a **maximum**, with $f(-1) = 2$ |

### Local vs. global

The minimum at $x = 1$ is only the lowest point **nearby**. Far to the left, $x^3 - 3x$ drops below $-2$ and keeps going down forever. A lowest-point-nearby is called a **local** minimum. The lowest point overall is the **global** minimum.

### Convex functions: the easy case

A function is **convex** if it's shaped like a bowl everywhere, curving up at every point. Convex functions have a wonderful property: **any local minimum is the global minimum.** There are no false valleys to get stuck in.

- $x^2$, $(x - 3)^2 + 1$, $e^x$: convex
- $x^3 - 3x$: not convex

### Payoff: the formula from Algebra §7, explained

In Algebra, you were told the lowest point of $ax^2 + bx + c$ (with $a > 0$) is at $x = \frac{-b}{2a}$. Now you can **prove** it:

| Step | What we did |
|---|---|
| $f'(x) = 2ax + b$ | Differentiated |
| $2ax + b = 0$ | Set to zero |
| $x = \frac{-b}{2a}$ | Solved for $x$ |
| $f''(x) = 2a > 0$ | Since $a > 0$, it's a minimum ✓ |

### Several inputs

Set **every** partial derivative to zero, i.e. solve $\nabla f = \mathbf{0}$.

**Example.** $f(x, y) = x^2 + y^2 - 2x + 4y$

| Step | Result |
|---|---|
| $\frac{\partial f}{\partial x} = 2x - 2 = 0$ | $x = 1$ |
| $\frac{\partial f}{\partial y} = 2y + 4 = 0$ | $y = -2$ |
| Critical point | $(1, -2)$ |

It's a bowl (both squared terms have positive signs), so this is the minimum.

### Exercises

**10.1.** Find and classify the critical points of $f(x) = x^2 - 4x + 1$.

**10.2.** Find and classify the critical points of $f(x) = 2x^3 - 6x$.

**10.3.** Minimize $f(w) = (w - 4)^2 + 2w$.

**10.4.** Find the critical point of $f(x, y) = 2x^2 + y^2 - 4x + 6y + 3$.

**10.5.** Explain in your own words why, for a convex function, you never have to worry about getting stuck in a "wrong" valley.

<details>
<summary>Solutions</summary>

**10.1.** $2x - 4 = 0$, so $x = 2$. $f'' = 2 > 0$: minimum, $f(2) = -3$.

**10.2.** $6x^2 - 6 = 0$, so $x = \pm 1$. $f'' = 12x$: $x = 1$ is a minimum ($f = -4$), and $x = -1$ is a maximum ($f = 4$).

**10.3.** $2(w - 4) + 2 = 0$, so $w = 3$. $f'' = 2 > 0$: minimum.

**10.4.** $4x - 4 = 0$ and $2y + 6 = 0$, so $(1, -3)$.

**10.5.** A bowl has only one valley. Wherever it's flat, that's the bottom of the only valley there is.

</details>

---

## 11. Gradient descent

### The problem

In §10, we found minimums by solving $\nabla f = \mathbf{0}$ with algebra. But for a function with **millions** of inputs, or a formula too messy to solve, that's impossible.

So instead of solving, we **walk downhill**.

### The algorithm in plain words

Imagine standing on a foggy hillside. You can't see the valley, but you can feel the slope under your feet.

1. Start somewhere.
2. Feel which way is steepest uphill (the gradient).
3. Take a small step the **opposite** way.
4. Repeat until the ground is flat.

### The formula

$$
\mathbf{w} := \mathbf{w} - \alpha\,\nabla f(\mathbf{w})
$$

| Piece | Read it aloud as | Meaning |
|---|---|---|
| $\mathbf{w}$ | "w" | where you currently are (the inputs being adjusted) |
| $:=$ | "becomes" or "is updated to" | replace the old value with the new one (like `=` in Python) |
| $\alpha$ | "**alpha**" | the **step size**: how far to step each time |
| $\nabla f(\mathbf{w})$ | "grad f at w" | the uphill direction at your current spot |
| $-\alpha\,\nabla f$ | | a small step downhill |

### Why each step goes down

Use the sensitivity idea (§3, §7). You move by $-\alpha\nabla f$, so $f$ changes by about:

$$
\nabla f \cdot (-\alpha\nabla f) = -\alpha\,(\nabla f \cdot \nabla f) = -\alpha\,\lVert \nabla f \rVert^2
$$

A squared length is never negative, and $\alpha$ is positive, so **the change is negative: $f$ goes down**, as long as the step is small enough for the sensitivity approximation to hold.

That "small enough" is important. Watch what happens when it isn't.

### Worked example: one input

$f(w) = w^2$, so $f'(w) = 2w$. Start at $w = 3$.

The update is $w := w - \alpha \cdot 2w = (1 - 2\alpha)\,w$.

| Step size $\alpha$ | Each step multiplies $w$ by | $w_1$ | $w_2$ | $w_3$ | What happens |
|---|---|---|---|---|---|
| 0.1 | 0.8 | 2.4 | 1.92 | 1.536 | Smoothly heads to 0 ✓ |
| 0.5 | 0 | 0 | 0 | 0 | Lands exactly at the bottom in one step |
| 0.9 | −0.8 | −2.4 | 1.92 | −1.536 | Jumps back and forth across the valley, but settles |
| 1.1 | −1.2 | −3.6 | 4.32 | −5.184 | **Overshoots more each time and blows up** ✗ |

**Too small** a step: slow. **Too big:** you leap over the valley and land higher up the other side, again and again.

For this function, it works when $|1 - 2\alpha| < 1$, which means $0 < \alpha < 1$ (Algebra §2's inequality rules).

### Worked example: two inputs

$f(x, y) = x^2 + 2y^2$ (a bowl that's steeper in the $y$ direction). $\nabla f = [2x, 4y]$. Start at $(2, 1)$ with $\alpha = 0.1$.

| Step | Position | $\nabla f$ | $\alpha\,\nabla f$ | New position |
|---|---|---|---|---|
| 1 | $(2, 1)$ | $[4, 4]$ | $[0.4, 0.4]$ | $(1.6, 0.6)$ |
| 2 | $(1.6, 0.6)$ | $[3.2, 2.4]$ | $[0.32, 0.24]$ | $(1.28, 0.36)$ |
| 3 | $(1.28, 0.36)$ | $[2.56, 1.44]$ | $[0.256, 0.144]$ | $(1.024, 0.216)$ |

Heading toward the bottom at $(0, 0)$ ✓. Notice $y$ shrinks faster than $x$, because the bowl is steeper in $y$.

### The steepest direction limits the step size

Look at each direction separately:

- $x$: update is $x := (1 - 2\alpha)x$, which is stable for $\alpha < 1$
- $y$: update is $y := (1 - 4\alpha)y$, which is stable only for $\alpha < 0.5$

So $\alpha$ must be below 0.5, or the $y$ direction blows up. But with $\alpha$ that small, the gentle $x$ direction moves slowly.

**The steepest direction limits how big a step you can take, and then the gentlest direction crawls.** That's a real, practical problem, and much of modern optimization is about working around it.

> **Why ML cares:** This is how nearly every ML model learns. $\mathbf{w}$ is the model's adjustable numbers, $f$ is how wrong the model is, and $\alpha$ is called the **learning rate**. In a program, one step of this update is often a single line: `optimizer.step()`.

### Exercises

**11.1.** $f(w) = (w - 5)^2$. Start at $w = 0$ with $\alpha = 0.25$. Do 3 steps by hand. Where is it heading?

**11.2.** For $f(w) = w^2$, what happens with $\alpha = 1$ exactly? Do 3 steps from $w = 3$.

**11.3.** $f(x, y) = x^2 + 2y^2$. Start at $(2, 1)$ with $\alpha = 0.6$. Do 2 steps. What goes wrong, and in which direction?

**11.4.** Explain in plain words, without formulas: why does gradient descent step in the negative gradient direction? And why can too big a step make things worse?

<details>
<summary>Hint</summary>

11.1: $f'(w) = 2(w - 5)$, so each step is $w := w - 0.5(w - 5)$.
11.3: the $x$ multiplier is $1 - 2(0.6)$, and the $y$ multiplier is $1 - 4(0.6)$.

</details>

<details>
<summary>Solutions</summary>

**11.1.** $w_1 = 0 - 0.5(-5) = 2.5$, $w_2 = 2.5 - 0.5(-2.5) = 3.75$, $w_3 = 3.75 - 0.5(-1.25) = 4.375$. Heading to 5 (halving the distance each step).

**11.2.** The multiplier is $1 - 2 = -1$: $-3, 3, -3$. It bounces between the two sides forever without settling.

**11.3.** $x$ multiplier $-0.2$ and $y$ multiplier $-1.4$. Step 1: $(-0.4, -1.4)$. Step 2: $(0.08, 1.96)$. $x$ is settling, but $y$ is growing: the step is too big for the steep $y$ direction.

**11.4.** The gradient points uphill, so its opposite is the fastest way down from where you stand. But the slope only describes the ground right under your feet. Step too far, and you land somewhere the slope was pointing differently, possibly higher up the other side of the valley.

</details>

---

## Code lab — `math/04_calculus.py`

### What you're doing and why

You'll build a tool that **estimates** derivatives with numbers, then use it to **check** derivatives you calculate by hand. Then you'll run gradient descent and watch it work, and fail, on a plot.

**Rules:** no AI, no autocomplete, no copying.

### Python you need

- Functions can be passed around like values: `def apply(f, x): return f(x)`.
- `np.zeros_like(x)` makes an array of zeros with the same shape as `x`.
- `x.copy()` makes a separate copy, so changing it doesn't change the original.
- `abs(a - b) < 1e-6` checks whether two numbers are nearly equal.
- `plt.contour(X, Y, Z)` draws contour lines. Build the grid with `X, Y = np.meshgrid(xs, ys)`.

### The tasks

```python
import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h=1e-5):
    """Central difference estimate of f'(x) for a one-input function.  (§3)"""
    ...

def numerical_gradient(f, point, h=1e-5):
    """Estimate the gradient of a function of a NumPy vector.  (§6, §7)
    Nudge one component at a time, both up and down, keeping the others fixed."""
    ...

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

if __name__ == "__main__":
    # 1) Check derivative rules with numbers (§4, §5)
    assert abs(numerical_derivative(lambda x: x**3, 2.0) - 12) < 1e-6
    assert abs(numerical_derivative(np.exp, 2.0) - np.exp(2.0)) < 1e-6
    assert abs(numerical_derivative(np.log, 2.0) - 0.5) < 1e-6
    for z in [-3.0, 0.0, 2.5]:
        by_hand = sigmoid(z) * (1 - sigmoid(z))
        assert abs(numerical_derivative(sigmoid, z) - by_hand) < 1e-8

    # 2) Check partial derivatives (§6)
    f = lambda p: p[0]**2 + 3*p[0]*p[1] + p[1]**2
    by_hand = np.array([2*1 + 3*2, 3*1 + 2*2])   # gradient at (1, 2)
    assert np.allclose(numerical_gradient(f, np.array([1.0, 2.0])), by_hand, atol=1e-6)

    # 3) Gradient descent on f(x, y) = x^2 + 2y^2, starting at (2, 1), 30 steps.  (§11)
    #    Try alpha = 0.1, 0.4, 0.49, 0.51.
    #    Plot the contour lines of f, and draw each path of positions on top.
    #    BEFORE running: predict which alpha values will reach (0, 0) and which will blow up.

    # 4) Gradient descent on f(x) = x^3 - 3x starting at x = 2, and again starting at x = -2.  (§10)
    #    Use alpha = 0.05 and 50 steps. Where does each run end up? Explain what happened.
    print("all checks passed")
```

<details>
<summary>Hint for numerical_gradient</summary>

For each component `i`: make a copy of the point with component `i` increased by `h`, and another copy with it decreased by `h`. The `i`-th gradient component is `(f(up) - f(down)) / (2 * h)`.

</details>

<details>
<summary>Reference solution (only after your own attempt)</summary>

```python
def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_gradient(f, point, h=1e-5):
    grad = np.zeros_like(point, dtype=float)
    for i in range(len(point)):
        up = point.copy()
        down = point.copy()
        up[i] += h
        down[i] -= h
        grad[i] = (f(up) - f(down)) / (2 * h)
    return grad

# part 3 (one alpha)
position = np.array([2.0, 1.0])
path = [position.copy()]
for step in range(30):
    gradient = np.array([2 * position[0], 4 * position[1]])
    position = position - 0.1 * gradient
    path.append(position.copy())
path = np.array(path)
```

Part 4: starting at 2 slides down into the local minimum at $x = 1$. Starting at $-2$ runs off toward $-\infty$, faster and faster (you may see overflow warnings), because the function keeps decreasing to the left and has no global minimum. Gradient descent only finds a nearby valley, if there is one.

</details>

---

## Common mistakes

| Mistake | Why it's wrong |
|---|---|
| $\frac{d}{dx}e^{2x} = e^{2x}$ | Forgot the chain rule: it's $2e^{2x}$ |
| $\frac{d}{dx}(fg) = f'g'$ | Product rule: $f'g + fg'$. Check with $x \cdot x$: $f'g' = 1$, but the derivative of $x^2$ is $2x$ |
| $\frac{d}{dx}\frac{1}{x} = \ln x$ | That's backwards: the derivative of $\ln x$ is $\frac{1}{x}$ |
| $\frac{d}{dx}x^{-1} = -1x^{-0}$ | Subtract 1 from the exponent: $-1 - 1 = -2$ |
| "Gradient is zero, so it's the minimum" | Could be a maximum or a saddle |
| Stepping **along** the gradient to minimize | That goes uphill; minimizing steps opposite |
| Treating $\alpha$ as a detail | Too big a step size makes gradient descent blow up |
| A hand-calculated $\frac{\partial L}{\partial W}$ with a different shape from $W$ | It must match exactly |

---

## Check yourself

Do this **after** working through the file. Closed book, 20 minutes.

1. Differentiate $3x^3 + 2x^2 - 5x + 7$.
2. Differentiate $e^{2x}$ and $\ln(x^2 + 1)$.
3. $f(x, y) = x^2 + 3xy + y^2$. Find $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$.
4. Same $f$: find $\nabla f$ at $(1, 2)$.
5. Find the minimum of $x^2 - 4x + 1$.
6. $f(w) = w^2$, $w = 3$, $\alpha = 0.1$. Do one gradient descent step.
7. Why does gradient descent move in the direction $-\nabla f$?
8. Find $\lim_{h \to 0} \frac{(2 + h)^2 - 4}{h}$.
9. Derive $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.
10. For $f(x) = x^2 + 3x$: find the derivative, its value at $x = 2$, what that value means geometrically, and where the slope is zero.
11. Explain in two sentences what a Jacobian is.
12. Derive the formula $x = \frac{-b}{2a}$ for the lowest point of $ax^2 + bx + c$.

<details>
<summary>Answers</summary>

**1.** Differentiate $3x^3 + 2x^2 - 5x + 7$ → §4

Differentiate term by term (the sum rule), using the power rule $\frac{d}{dx}x^n = nx^{n-1}$: multiply by the old exponent, then knock the exponent down by one.

| Term | Rule applied | Result |
|---|---|---|
| $3x^3$ | $3 \cdot 3x^{3-1}$ | $9x^2$ |
| $2x^2$ | $2 \cdot 2x^{2-1}$ | $4x$ |
| $-5x$ | $-5 \cdot 1x^{0} = -5 \cdot 1$ | $-5$ |
| $7$ | a constant never changes | $0$ |

$$f'(x) = 9x^2 + 4x - 5$$

*Why the $7$ vanishes:* the derivative measures how the output changes when the input moves. Adding 7 shifts the whole curve up but changes no slope anywhere, so it contributes nothing.

*Check numerically* (central difference at $x = 1$, $h = 0.001$): $f' \approx \frac{f(1.001) - f(0.999)}{0.002} \approx 8$, and the formula gives $9 + 4 - 5 = 8$ ✓

---

**2.** Differentiate $e^{2x}$ and $\ln(x^2 + 1)$ → §5

Both are chain rule: *derivative of the outside (leaving the inside alone), times the derivative of the inside.*

*For $e^{2x}$:* outside is $e^{\square}$, inside is $2x$.

$$\frac{d}{dx}e^{2x} = \underbrace{e^{2x}}_{\text{outside}} \cdot \underbrace{2}_{\text{inside}} = 2e^{2x}$$

($e^{\square}$ is its own derivative, which is what makes $e$ special.)

*For $\ln(x^2 + 1)$:* outside is $\ln(\square)$ whose derivative is $\frac{1}{\square}$, inside is $x^2 + 1$ whose derivative is $2x$.

$$\frac{d}{dx}\ln(x^2+1) = \frac{1}{x^2+1} \cdot 2x = \frac{2x}{x^2 + 1}$$

*Common trap:* writing $\frac{1}{x^2+1}$ and stopping. Forgetting to multiply by the inside derivative is the single most frequent chain rule mistake.

---

**3.** $f(x, y) = x^2 + 3xy + y^2$: both partial derivatives → §6

A partial derivative differentiates with respect to one variable while **freezing the other as a constant**.

*$\frac{\partial f}{\partial x}$ — treat $y$ as a fixed number:*

- $x^2 \rightarrow 2x$
- $3xy \rightarrow 3y$ (this is "a constant $3y$ times $x$," so the derivative is just that constant)
- $y^2 \rightarrow 0$ (a constant, as far as $x$ is concerned)

$$\frac{\partial f}{\partial x} = 2x + 3y$$

*$\frac{\partial f}{\partial y}$ — now freeze $x$:*

- $x^2 \rightarrow 0$
- $3xy \rightarrow 3x$
- $y^2 \rightarrow 2y$

$$\frac{\partial f}{\partial y} = 3x + 2y$$

*What $\partial$ means:* the curly $\partial$ instead of $d$ signals there are other inputs being held still.

---

**4.** $\nabla f$ at $(1, 2)$ → §7

The gradient is just both partials collected into a vector:

$$\nabla f = \left[\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y}\right] = [2x + 3y,\ 3x + 2y]$$

Substitute $x = 1$, $y = 2$:

$$2(1) + 3(2) = 8, \qquad 3(1) + 2(2) = 7$$

$$\nabla f(1, 2) = [8, 7]$$

*Reading it:* at that point, nudging $x$ raises $f$ about 8 times as fast as the nudge, and nudging $y$ about 7 times. The arrow $[8, 7]$ points in the steepest uphill direction, and its length $\sqrt{64 + 49} \approx 10.6$ is how steep that climb is.

---

**5.** Minimum of $x^2 - 4x + 1$ → §10

At a minimum the curve is momentarily flat, so the derivative is zero.

*Step 1 — differentiate:* $f'(x) = 2x - 4$

*Step 2 — set it to zero and solve:*

$$2x - 4 = 0 \quad\Rightarrow\quad x = 2$$

*Step 3 — get the value there:*

$$f(2) = 4 - 8 + 1 = -3$$

*Step 4 — confirm it's a minimum, not a maximum.* The second derivative is $f'' = 2 > 0$, so the curve bends upward: a valley, not a peak.

Minimum at $(2, -3)$.

---

**6.** One gradient descent step: $f(w) = w^2$, $w = 3$, $\alpha = 0.1$ → §11

The update rule is *new = old minus learning rate times slope*:

$$w_{\text{new}} = w - \alpha f'(w)$$

*Step 1 — the derivative:* $f'(w) = 2w$

*Step 2 — evaluate at the current $w$:* $f'(3) = 6$

*Step 3 — take the step:*

$$w_{\text{new}} = 3 - (0.1)(6) = 3 - 0.6 = 2.4$$

*Did it help?* $f(3) = 9$, and $f(2.4) = 5.76$. The loss went down ✓ The minimum is at $w = 0$, and we moved toward it. Note the step is *proportional to the slope*: steep places take big steps, and as $w$ approaches 0 the steps shrink automatically.

---

**7.** Why does gradient descent move along $-\nabla f$? → §7

Because that's provably the steepest downhill direction, and the proof is one dot product.

The slope you feel walking in a unit direction $\mathbf{u}$ is the directional derivative:

$$\nabla f \cdot \mathbf{u} = \lVert \nabla f \rVert \lVert \mathbf{u} \rVert \cos\theta = \lVert \nabla f \rVert \cos\theta$$

($\lVert \mathbf{u} \rVert = 1$ since it's a direction.) $\lVert \nabla f \rVert$ is fixed at this point, so the only thing you control is $\cos\theta$, the angle between your step and the gradient. And $\cos\theta$ bottoms out at $-1$ when $\theta = 180°$ — pointing exactly opposite the gradient.

So $-\nabla f$ is where the slope is **most negative**: the fastest possible descent. Any other direction descends more slowly, or climbs.

*The caveat:* this is only true locally, for a small enough step. It's the steepest direction *right here*, not a route to the global minimum.

---

**8.** $\lim_{h \to 0} \frac{(2+h)^2 - 4}{h}$ → §2

You can't substitute $h = 0$ directly — that gives $\frac{0}{0}$, which is meaningless. So simplify **first**, then substitute.

*Step 1 — expand the square:*

$$(2 + h)^2 = 4 + 4h + h^2$$

*Step 2 — subtract the 4:*

$$\frac{4 + 4h + h^2 - 4}{h} = \frac{4h + h^2}{h}$$

*Step 3 — cancel one $h$* (legal because $h \ne 0$ while it's still approaching):

$$= \frac{h(4 + h)}{h} = 4 + h$$

*Step 4 — now let $h \to 0$:*

$$\lim_{h \to 0}(4 + h) = 4$$

*What it actually was:* this is the limit definition of the derivative of $x^2$ at $x = 2$. And indeed $f'(x) = 2x$ gives $f'(2) = 4$ ✓

---

**9.** Derive $\sigma'(z) = \sigma(z)(1 - \sigma(z))$ → §5

Start from $\sigma(z) = \dfrac{1}{1 + e^{-z}}$.

*Step 1 — rewrite the fraction as a power,* so the chain rule applies cleanly:

$$\sigma(z) = (1 + e^{-z})^{-1}$$

*Step 2 — chain rule, outer layer.* Power rule on $\square^{-1}$ gives $-\square^{-2}$:

$$\sigma'(z) = -(1 + e^{-z})^{-2} \cdot \frac{d}{dz}(1 + e^{-z})$$

*Step 3 — chain rule, inner layer.* $\frac{d}{dz}e^{-z} = e^{-z} \cdot (-1) = -e^{-z}$, and the $1$ differentiates to 0:

$$\sigma'(z) = -(1 + e^{-z})^{-2} \cdot (-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2}$$

The two minus signs cancel — that's why the sigmoid's derivative is always positive.

*Step 4 — split the fraction deliberately:*

$$\frac{e^{-z}}{(1+e^{-z})^2} = \underbrace{\frac{1}{1 + e^{-z}}}_{\sigma(z)} \cdot \underbrace{\frac{e^{-z}}{1 + e^{-z}}}_{?}$$

*Step 5 — recognize the second piece.* Compute $1 - \sigma(z)$ over a common denominator:

$$1 - \frac{1}{1+e^{-z}} = \frac{(1 + e^{-z}) - 1}{1 + e^{-z}} = \frac{e^{-z}}{1 + e^{-z}}$$

That's exactly the second factor. Therefore:

$$\sigma'(z) = \sigma(z)\left(1 - \sigma(z)\right)$$

*Why this is beautiful and also a problem:* the derivative is computable from the output alone, no re-deriving needed — cheap in backprop. But it peaks at only $0.25$ (when $\sigma = 0.5$) and collapses toward 0 when $\sigma$ nears 0 or 1. Multiply many such factors through a deep network and the gradient vanishes. That's the saturation problem that pushed the field toward ReLU.

---

**10.** $f(x) = x^2 + 3x$: derivative, value at $x=2$, its meaning, where the slope is zero → §4

*The derivative:* $f'(x) = 2x + 3$

*At $x = 2$:* $f'(2) = 4 + 3 = 7$

*Geometrically:* $7$ is the slope of the tangent line touching the curve at $x = 2$. The curve is climbing 7 units of output per 1 unit of input right there. Equivalently, nudge $x$ by a tiny $0.001$ and $f$ rises by about $0.007$.

*Where the slope is zero:*

$$2x + 3 = 0 \quad\Rightarrow\quad x = -\frac{3}{2} = -1.5$$

Since $f'' = 2 > 0$, that flat point is the minimum of the parabola.

---

**11.** What is a Jacobian? → §8

A matrix holding **every** partial derivative of a function that takes several inputs and returns several outputs. If the function eats $n$ inputs and produces $m$ outputs, the Jacobian is $m \times n$, and entry $(i, j)$ is $\frac{\partial(\text{output } i)}{\partial(\text{input } j)}$ — how sensitive output $i$ is to input $j$.

Row $i$ is therefore the gradient of output $i$ on its own. A gradient is the special case with one output ($m = 1$): a Jacobian with a single row.

---

**12.** Derive $x = \frac{-b}{2a}$ for the vertex of $ax^2 + bx + c$ → §10

The vertex of a parabola is the one place where it's flat, so find where the derivative is zero.

*Step 1 — differentiate term by term:*

$$f(x) = ax^2 + bx + c \quad\Rightarrow\quad f'(x) = 2ax + b$$

($c$ is constant, so it drops out — the vertical shift never affects *where* the vertex sits, only how high it is.)

*Step 2 — set the slope to zero:*

$$2ax + b = 0$$

*Step 3 — solve for $x$:*

$$2ax = -b \quad\Rightarrow\quad x = \frac{-b}{2a}$$

*Step 4 — minimum or maximum?* $f''(x) = 2a$. If $a > 0$ the curve bends upward and it's a **minimum**; if $a < 0$ it bends downward and it's a maximum.

*Test it:* for $y = 2x^2 - 12x + 5$, $x = \frac{12}{4} = 3$, matching the algebra-file answer ✓ The formula you memorized earlier isn't a separate fact — it's one line of calculus.

</details>

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can explain the derivative as the limit of slopes between two points, and as sensitivity.
- [ ] I can derive $\frac{d}{dx}x^2 = 2x$ and $\frac{d}{dx}x^3 = 3x^2$ from the limit definition.
- [ ] I can use the power, sum, constant, $e^x$, $\ln x$, and product rules, and check any result with the central difference.
- [ ] I can apply the chain rule using the recipe, and explain it with the gears picture.
- [ ] I can derive the sigmoid's derivative and explain what it says about saturation.
- [ ] I can do a forward-then-backward table for a chain of 3+ steps.
- [ ] I can compute partial derivatives by freezing the other inputs.
- [ ] I can compute a gradient, and prove with the dot product that $-\nabla f$ is steepest descent.
- [ ] I can explain what a Jacobian is, and why $\frac{\partial L}{\partial W}$ has the same shape as $W$.
- [ ] I can find and classify critical points, and explain convexity.
- [ ] I can run gradient descent by hand, and predict when a step size is too large.
- [ ] Check yourself: 12/12.
- [ ] Code lab done without AI.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $\lim_{h \to 0}$ | "the limit as h approaches zero" | where the value heads as $h$ gets close to 0 | §2 |
| $f'(x)$ | "f prime of x" | the derivative of $f$ | §3 |
| $\frac{df}{dx}$ | "d f d x" | the derivative of $f$ with respect to $x$ | §3 |
| $\varepsilon$ | "epsilon" | a tiny number | §3 |
| $\Delta$ | "delta" | "change in" | §4 |
| $f(x, y)$ | "f of x comma y" | a function with two inputs | §6 |
| $\frac{\partial f}{\partial x}$ | "partial f partial x" | slope when only $x$ changes | §6 |
| $\nabla f$ | "grad f" | vector of all partial derivatives | §7 |
| $D_{\mathbf{u}}f$ | "directional derivative of f along u" | slope in direction $\mathbf{u}$: $\nabla f \cdot \mathbf{u}$ | §7 |
| $J$ | "the Jacobian" | matrix of partial derivatives, outputs × inputs | §8 |
| $f''(x)$ | "f double prime of x" | the second derivative; curvature | §9 |
| $:=$ | "becomes" | update: replace with a new value | §11 |
| $\alpha$ | "alpha" | step size (learning rate) | §11 |

---

## Resources (only if stuck)

1. **Best for intuition:** [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus). Watch the video matching the section you're stuck on: *The paradox of the derivative* (§1–§3), *Derivative formulas through geometry* (§4), *Visualizing the chain rule and product rule* (§4–§5), *What's so special about Euler's number e?* (§4, Rule 5).
2. **For partial derivatives and gradients:** [Khan Academy — Multivariable calculus](https://www.khanacademy.org/math/multivariable-calculus): the units on partial derivatives, the gradient, and directional derivatives (§6–§7).
