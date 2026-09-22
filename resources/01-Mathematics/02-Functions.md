# 02 — Functions

**Time: ~5 hours** (spread it over 2 days) · **You need: [01 Algebra](01-Algebra.md)** · **Code lab: `math/02_functions.py`**

## Before you start

A **function** is the single most important idea in all of math for ML. Every model, every formula, every layer of a neural network is a function. This file builds the idea from nothing.

**How to read it:**

- Go **in order**. Each section uses the ones before it.
- When you see a worked example, **cover the solution and try it first**.
- Say each symbol aloud using its "read it aloud as" note.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.
- The **"Why ML cares"** boxes are motivation only. The math above them is complete without them.

**What you'll be able to do by the end:**

- Read function notation like $f(x)$, $f(g(x))$, and $f^{-1}(x)$
- Explain the difference between linear and nonlinear functions, and why it matters
- Work with exponential, logarithmic, and piecewise functions
- Compute and explain three special functions: ReLU, sigmoid, and softmax

---

## Contents

1. [What a function is](#1-what-a-function-is)
2. [Domain and range](#2-domain-and-range)
3. [Composition: functions in a chain](#3-composition-functions-in-a-chain)
4. [Inverse functions: undoing](#4-inverse-functions-undoing)
5. [Linear vs. nonlinear functions](#5-linear-vs-nonlinear-functions)
6. [Exponential functions and the number e](#6-exponential-functions-and-the-number-e)
7. [The logarithm as a function](#7-the-logarithm-as-a-function)
8. [Piecewise functions, absolute value, and ReLU](#8-piecewise-functions-absolute-value-and-relu)
9. [The sigmoid function](#9-the-sigmoid-function)
10. [The softmax function](#10-the-softmax-function)
11. [Code lab](#code-lab--math02_functionspy)
12. [Check yourself](#check-yourself)

---

## 1. What a function is

### The problem

In Algebra you wrote rules like $c = 15r$: the cost of $r$ jeepney rides. That rule takes a number in (rides) and gives a number out (cost).

Rules like this are everywhere: a temperature converter, a tax calculator, a phone plan's bill. We want one clear way to **name** such a rule, **use** it, and **talk about** it.

### The idea: a machine

A **function** is a machine:

```text
input  ──►  [ rule ]  ──►  output
```

You put a number in, the rule does something to it, and one number comes out.

**The one requirement:** the same input must **always** give the same output. A vending machine where pressing B3 sometimes gives chips and sometimes gives soda is broken. A function never does that.

### Notation: $f(x)$

We give the machine a name, usually $f$, and write:

$$
f(x) = 15x
$$

- Read it aloud as "**f of x** equals fifteen x."
- $f$ is the **name** of the function.
- $x$ is the **input**. Inside the parentheses, it's a placeholder for whatever number you feed in.
- $f(x)$ is the **output**: what comes out when you feed in $x$.

**Warning:** $f(x)$ does **NOT** mean $f$ times $x$. The parentheses here mean "feed this into." This is different from Algebra, where $2(x + 1)$ meant multiplication. You can tell them apart because $f$ is the name of a function, not a number.

### Using a function

To use a function, replace the input letter everywhere with your number.

**Example.** $f(x) = 3x + 2$. Find $f(4)$.

| Step | What we did |
|---|---|
| $f(4) = 3(4) + 2$ | Replaced every $x$ with $4$ |
| $= 14$ | Calculated |

Read $f(4) = 14$ aloud as "f of four is fourteen." It means: put 4 into machine $f$, and 14 comes out.

**Example with a messier input.** $f(x) = x^2 + 1$. Find $f(a + 1)$.

| Step | What we did |
|---|---|
| $f(a + 1) = (a + 1)^2 + 1$ | Replaced $x$ with the whole thing $(a + 1)$, in parentheses |
| $= a^2 + 2a + 1 + 1$ | Expanded the square (Algebra §7) |
| $= a^2 + 2a + 2$ | Combined |

### Different names, same idea

Functions can use any letters. $g(t) = t^2$ and $h(z) = 5 - z$ are also functions. The input letter doesn't matter: $f(x) = 2x$ and $f(t) = 2t$ are **the same machine**, because both double the input.

### Three ways to show a function

The same function $f(x) = 2x + 1$ can be shown as:

1. **A formula:** $f(x) = 2x + 1$
2. **A table:**

   | $x$ | 0 | 1 | 2 | 3 |
   |---|---|---|---|---|
   | $f(x)$ | 1 | 3 | 5 | 7 |

3. **A graph:** plot all points $(x, f(x))$. Here that's the straight line you drew in Algebra §6. $f(x)$ plays the role of $y$.

### Is it a function? The one-output test

**Not every rule is a function.** Consider "give me a number whose square is $x$." For $x = 4$, both $2$ and $-2$ work. Two outputs for one input means **not a function**.

On a graph, this becomes the **vertical line test**: if any vertical line crosses the graph more than once, one $x$ has more than one output, so it's not a function.

> **Why ML cares:** A trained ML model is literally a function: data goes in (a photo, a sentence, a hand position) and a prediction comes out. It must be a function, meaning the same input always gets the same prediction.

### Exercises

**1.1.** $f(x) = 4x - 3$. Find $f(0)$, $f(2)$, and $f(-1)$.

**1.2.** $g(t) = t^2 - t$. Find $g(3)$ and $g(-3)$.

**1.3.** $h(x) = 2x + 5$. Find $h(a + 2)$ and simplify.

**1.4.** Is "input: a person, output: their birthday" a function? What about "input: a birthday, output: a person born that day"? Why?

<details>
<summary>Hint</summary>

1.2: put $-3$ in parentheses: $(-3)^2 - (-3)$.
1.4: for each rule, ask whether one input could have two different outputs.

</details>

<details>
<summary>Solutions</summary>

**1.1.** $-3$, $5$, $-7$.

**1.2.** $9 - 3 = 6$. And $(-3)^2 - (-3) = 9 + 3 = 12$.

**1.3.** $2(a + 2) + 5 = 2a + 4 + 5 = 2a + 9$.

**1.4.** The first is a function: each person has exactly one birthday. The second isn't: many people share one birthday, so one input can have many outputs.

</details>

---

## 2. Domain and range

### The problem

Some machines **can't accept** certain inputs. A calculator shows "Error" if you divide by zero. We need a way to say which inputs are allowed and which outputs can actually come out.

### Definitions

- The **domain** is the set of all inputs the function accepts.
- The **range** is the set of all outputs that actually come out.

### Three things that are never allowed

From Algebra, three operations break on certain numbers:

| Operation | Not allowed | Why |
|---|---|---|
| $\frac{1}{x}$ (division) | $x = 0$ | You can't divide by zero |
| $\sqrt{x}$ | $x < 0$ | No real number squared is negative (Algebra §3) |
| $\ln(x)$ | $x \le 0$ | $e^{\text{anything}}$ is always positive (Algebra §4) |

**Finding a domain** means finding which inputs trigger one of these.

**Example.** Domain of $f(x) = \sqrt{x - 2}$.

The part under the root must not be negative: $x - 2 \ge 0$, so $x \ge 2$. The domain is "all numbers 2 or bigger."

**Example.** Domain of $g(x) = \frac{1}{x - 1}$.

The bottom can't be zero: $x - 1 \ne 0$, so $x \ne 1$. The domain is "every number except 1."

### Writing sets of numbers: interval notation

We need a short way to write "all numbers between 0 and 1" or "all numbers 2 or bigger."

| Notation | Read it aloud as | Meaning |
|---|---|---|
| $[2, 5]$ | "closed interval 2 to 5" | from 2 to 5, **including** 2 and 5 |
| $(0, 1)$ | "open interval 0 to 1" | between 0 and 1, **not including** 0 or 1 |
| $[0, 1)$ | | includes 0, doesn't include 1 |
| $[2, \infty)$ | "2 to infinity" | 2 and every bigger number |
| $(-\infty, \infty)$ | "negative infinity to infinity" | every number |

- **Square bracket** $[\ ]$ = the endpoint **is included**.
- **Round bracket** $(\ )$ = the endpoint **is not included**.
- $\infty$ is read "**infinity**." It is **not a number**; it means "keeps going forever." That's why it always gets a round bracket: you can never reach it.

**Warning:** $(0, 1)$ as an interval looks exactly like the point $(0, 1)$ from Algebra §6. Context tells you which: if we're talking about sets of numbers, it's an interval.

### The real numbers: $\mathbb{R}$

$\mathbb{R}$ (a bold or "double-struck" R) means **the set of all real numbers**: every number on the number line, including negatives, fractions, and numbers like $\sqrt{2}$ and $\pi$. It's the same as $(-\infty, \infty)$.

The symbol $\in$ means "**is in**" or "is a member of." So $x \in \mathbb{R}$ is read "x is in R" and means "x is a real number." You'll see $\in$ constantly in later files.

### Finding a range

The range is often trickier. The trick: think about what the output can and can't be.

**Example.** Range of $f(x) = x^2$. A square is never negative (Algebra §7), and it can be 0 (when $x = 0$) or any positive number. So the range is $[0, \infty)$.

**Example.** Range of $f(x) = e^x$. $e$ to any power is always positive, never zero (Algebra §4). So the range is $(0, \infty)$.

> **Why ML cares:** When a calculation in code tries an input outside a function's domain, you get `inf` (infinity) or `nan` ("not a number") instead of an error message. Most mysterious `nan` values in ML code come from dividing by zero, or taking the log of zero.

### Exercises

**2.1.** Find the domain of $f(x) = \frac{3}{x + 4}$.

**2.2.** Find the domain of $g(x) = \ln(1 - x)$.

**2.3.** Find the domain of $h(x) = \sqrt{2x - 6}$. Write it in interval notation.

**2.4.** Find the range of $f(x) = x^2 + 3$.

**2.5.** Write in interval notation: (a) every number greater than $-1$; (b) numbers from 0 to 10, including 0 but not 10.

<details>
<summary>Hint</summary>

2.2: the inside of $\ln$ must be greater than 0. Solve $1 - x > 0$ (remember the flip rule).
2.4: the smallest $x^2$ can be is 0.

</details>

<details>
<summary>Solutions</summary>

**2.1.** $x \ne -4$.

**2.2.** $1 - x > 0 \Rightarrow -x > -1 \Rightarrow x < 1$. Domain: $(-\infty, 1)$.

**2.3.** $2x - 6 \ge 0 \Rightarrow x \ge 3$. Domain: $[3, \infty)$.

**2.4.** $x^2 \ge 0$, so $x^2 + 3 \ge 3$. Range: $[3, \infty)$.

**2.5.** (a) $(-1, \infty)$. (b) $[0, 10)$.

</details>

---

## 3. Composition: functions in a chain

### The problem

Say you convert pesos to US dollars (divide by 56), then a remittance company adds a \$2 fee. That's **two machines in a row**: the output of the first becomes the input of the second.

We need notation for chaining functions together.

### Notation

$$
f(g(x))
$$

Read it aloud as "**f of g of x**."

It means: put $x$ into $g$ **first**, then put $g$'s output into $f$.

```text
x  ──►  [ g ]  ──►  g(x)  ──►  [ f ]  ──►  f(g(x))
```

You'll also see it written as $(f \circ g)(x)$, read "f composed with g of x," or "f after g." The small circle $\circ$ means "composed with." It does not mean multiply.

### Work from the inside out

**Example.** $f(x) = 2x + 1$ and $g(x) = x^2$. Find $f(g(3))$.

| Step | What we did |
|---|---|
| $g(3) = 3^2 = 9$ | Inside first: put 3 into $g$ |
| $f(9) = 2(9) + 1 = 19$ | Put $g$'s output into $f$ |

So $f(g(3)) = 19$.

### Order matters

Now swap the order: $g(f(3))$.

| Step | What we did |
|---|---|
| $f(3) = 2(3) + 1 = 7$ | Inside first: put 3 into $f$ |
| $g(7) = 7^2 = 49$ | Put $f$'s output into $g$ |

$f(g(3)) = 19$ but $g(f(3)) = 49$. **Changing the order changes the result.** Putting on socks then shoes isn't the same as shoes then socks.

### Finding a formula for a composition

Instead of a specific number, feed in the whole expression.

**Example.** Same $f$ and $g$. Find a formula for $f(g(x))$.

| Step | What we did |
|---|---|
| $f(g(x)) = f(x^2)$ | Replaced $g(x)$ with its formula |
| $= 2(x^2) + 1$ | $f$ doubles its input and adds 1. Its input is $x^2$. |
| $= 2x^2 + 1$ | |

Check with $x = 3$: $2(9) + 1 = 19$ ✓ (matches the table above)

### Breaking a function into a chain

Going backward is just as useful: take a complicated function and split it into simple steps.

**Example.** $h(x) = (3x + 1)^2$. What happens to $x$, in order?

1. Multiply by 3 and add 1: $u = 3x + 1$
2. Square it: $h = u^2$

So $h(x) = f(g(x))$ with $g(x) = 3x + 1$ and $f(u) = u^2$.

(Using a new letter like $u$ for the in-between value helps keep things clear.)

> **Why ML cares:** A neural network is a long chain of simple functions: the output of one step (called a **layer**) is the input to the next. In the Calculus file, you'll learn how to find how a change at the start of a chain affects the end. That tool (the chain rule) is exactly how neural networks learn.

### Exercises

**3.1.** $f(x) = x + 5$ and $g(x) = 3x$. Find $f(g(2))$ and $g(f(2))$.

**3.2.** Same functions. Find formulas for $f(g(x))$ and $g(f(x))$. Are they the same?

**3.3.** $f(x) = \sqrt{x}$ and $g(x) = x - 4$. Find $f(g(13))$. What's the domain of $f(g(x))$?

**3.4.** Break $h(x) = e^{2x}$ into two simple functions.

**3.5.** Break $k(x) = \ln(1 + e^{2x})$ into four simple steps, in order.

<details>
<summary>Hint</summary>

3.3: the input to the square root is $x - 4$. When is that allowed?
3.5: start with what happens to $x$ first. The first step is "multiply by 2."

</details>

<details>
<summary>Solutions</summary>

**3.1.** $g(2) = 6$, so $f(6) = 11$. $f(2) = 7$, so $g(7) = 21$.

**3.2.** $f(g(x)) = 3x + 5$ and $g(f(x)) = 3(x + 5) = 3x + 15$. Not the same.

**3.3.** $g(13) = 9$, so $f(9) = 3$. Domain: $x - 4 \ge 0$, so $x \ge 4$, or $[4, \infty)$.

**3.4.** $g(x) = 2x$, $f(u) = e^u$.

**3.5.** $u_1 = 2x$, then $u_2 = e^{u_1}$, then $u_3 = 1 + u_2$, then $k = \ln(u_3)$.

</details>

---

## 4. Inverse functions: undoing

### The problem

A function converts Celsius to Fahrenheit: $F = \frac{9}{5}C + 32$. Now you have a Fahrenheit reading and want Celsius back. You need a machine that **undoes** the first one.

### Notation

The function that undoes $f$ is called its **inverse**, written:

$$
f^{-1}(x)
$$

Read it aloud as "**f inverse of x**."

**Big warning:** the $-1$ here is **not an exponent**. $f^{-1}(x)$ does **NOT** mean $\frac{1}{f(x)}$. It's just a name meaning "the undo machine for $f$." This is one of the most confusing notations in math, and you just have to remember it.

### What "undo" means precisely

If $f$ turns $a$ into $b$, then $f^{-1}$ turns $b$ back into $a$:

$$
f^{-1}(f(x)) = x \qquad\text{and}\qquad f(f^{-1}(x)) = x
$$

**Example with numbers.** $f(x) = 2x$ (doubles) and $f^{-1}(x) = \frac{x}{2}$ (halves). $f(5) = 10$, and $f^{-1}(10) = 5$ ✓. You're back where you started.

### How to find an inverse

It's the "rearranging a formula" skill from Algebra §2.

**Example.** Find the inverse of $f(x) = 3x - 6$.

| Step | What we did | Why |
|---|---|---|
| $y = 3x - 6$ | Wrote $y$ for the output | Easier to rearrange |
| $y + 6 = 3x$ | Added 6 to both sides | Undo the "−6" |
| $\frac{y + 6}{3} = x$ | Divided both sides by 3 | Undo the "×3" |
| $f^{-1}(x) = \frac{x + 6}{3}$ | Renamed: the input letter is usually $x$ | |

**Check:** $f(4) = 12 - 6 = 6$. Then $f^{-1}(6) = \frac{12}{3} = 4$ ✓

Notice the inverse undoes the steps **in reverse order**, just like solving an equation.

### Not every function can be undone

$f(x) = x^2$ sends both $3$ and $-3$ to $9$. If someone hands you 9, you can't tell which one they started with. **No inverse exists.**

A function has an inverse only if **no two inputs give the same output**. Such a function is called **one-to-one**.

**The fix:** restrict the domain. If we only allow $x \ge 0$, then $x^2$ is one-to-one, and its inverse is $\sqrt{x}$.

### Inverse pairs you already know

| Function | Its inverse | Check |
|---|---|---|
| $x + 5$ | $x - 5$ | $(3 + 5) - 5 = 3$ |
| $2x$ | $\frac{x}{2}$ | $\frac{2 \cdot 3}{2} = 3$ |
| $x^2$ (for $x \ge 0$) | $\sqrt{x}$ | $\sqrt{3^2} = 3$ |
| $e^x$ | $\ln x$ | $\ln(e^3) = 3$ (Algebra §4, Rule 4) |

> **Why ML cares:** Data is often rescaled before a model sees it (for example, turning peso amounts into small numbers near 0). The model's predictions then come out in that rescaled form, and the inverse function converts them back into pesos.

### Exercises

**4.1.** Find the inverse of $f(x) = 5x + 2$. Check it with $x = 1$.

**4.2.** Find the inverse of $f(x) = \frac{x - 3}{4}$.

**4.3.** Find the inverse of $f(x) = e^{2x} + 1$. What's the domain of the inverse?

**4.4.** Does $f(x) = |x|$ have an inverse on all real numbers? (Here $|x|$ means "remove the negative sign": $|{-5}| = 5$, $|5| = 5$. It's covered fully in §8.)

**4.5.** Your friend says $f^{-1}(x) = \frac{1}{f(x)}$. Test this claim using $f(x) = 2x$ and $x = 4$.

<details>
<summary>Hint</summary>

4.3: subtract 1, then take $\ln$ of both sides, then divide by 2. The inside of $\ln$ must be positive.
4.4: find two inputs with the same output.

</details>

<details>
<summary>Solutions</summary>

**4.1.** $y = 5x + 2 \Rightarrow x = \frac{y - 2}{5}$, so $f^{-1}(x) = \frac{x - 2}{5}$. Check: $f(1) = 7$, $f^{-1}(7) = 1$ ✓

**4.2.** $4y = x - 3 \Rightarrow x = 4y + 3$, so $f^{-1}(x) = 4x + 3$.

**4.3.** $y - 1 = e^{2x} \Rightarrow \ln(y - 1) = 2x \Rightarrow x = \frac{\ln(y - 1)}{2}$. So $f^{-1}(x) = \frac{\ln(x - 1)}{2}$, with domain $x > 1$.

**4.4.** No. $|{-2}| = |2| = 2$, so two inputs share an output.

**4.5.** $f^{-1}(8)$ should give back 4, and the true inverse $\frac{8}{2} = 4$ does. The friend's version gives $\frac{1}{f(8)} = \frac{1}{16}$. Wrong.

</details>

---

## 5. Linear vs. nonlinear functions

### The problem

Some functions are "straight" and behave very predictably. Others curve. This difference turns out to be **the** reason neural networks need special ingredients, so it's worth being precise about.

### Linear functions

A function is **linear** if it has two properties. Check both with $f(x) = 3x$:

**Property 1: adding inputs adds outputs.**

$$
f(a + b) = f(a) + f(b)
$$

With $a = 2$, $b = 5$: $f(7) = 21$, and $f(2) + f(5) = 6 + 15 = 21$ ✓

**Property 2: scaling the input scales the output.**

$$
f(c \cdot a) = c \cdot f(a)
$$

With $c = 4$, $a = 2$: $f(8) = 24$, and $4 \cdot f(2) = 4 \cdot 6 = 24$ ✓

For functions of one number, the **only** linear functions are $f(x) = mx$: a straight line **through the origin**.

A consequence worth remembering: **a linear function always gives $f(0) = 0$.** (Use Property 2 with $c = 0$: $f(0) = 0 \cdot f(a) = 0$.)

### Affine functions: a line with a shift

What about $f(x) = 3x + 2$? Test Property 1:

$f(2 + 5) = f(7) = 23$, but $f(2) + f(5) = 8 + 17 = 25$. **Not equal.** So it's not linear in the strict sense. Also, $f(0) = 2$, not 0.

A function like $mx + b$ (a straight line that doesn't necessarily pass through the origin) is called **affine**.

In practice, lots of people (and ML libraries) loosely call affine functions "linear." Just know the precise meaning.

### Nonlinear functions

Anything that isn't a straight line is **nonlinear**: $x^2$, $e^x$, $\sqrt{x}$, $\ln x$.

Test $f(x) = x^2$: $f(1 + 2) = 9$, but $f(1) + f(2) = 1 + 4 = 5$. Not equal, so nonlinear.

### Key fact: chaining straight lines only gives a straight line

Take two affine functions and compose them (§3):

$f(x) = 2x + 1$ and $g(x) = 3x - 1$.

| Step | What we did |
|---|---|
| $g(f(x)) = 3(2x + 1) - 1$ | Put $f$'s formula into $g$ |
| $= 6x + 3 - 1$ | Distributed |
| $= 6x + 2$ | Still of the form $mx + b$! |

**Why:** the first function stretches by 2, the second stretches by 3, so together they stretch by $3 \times 2 = 6$. The shifts just add up to a new shift. No step ever creates a curve.

You could chain **a hundred** affine functions, and the result would still be a single straight line. Chaining never creates a bend.

**To get a curve out of a chain, at least one step must be nonlinear.**

> **Why ML cares:** A neural network chains many steps. If every step were a straight-line function, the whole network would collapse into one straight line, no smarter than a single step. So between the straight-line steps, networks insert nonlinear functions (called **activation functions**) to add bends. You'll meet the three most important ones in §8–§10.

### Exercises

**5.1.** For each function, decide whether it's linear, affine (but not linear), or nonlinear: $5x$, $5x - 1$, $x^3$, $0$, $\sqrt{x}$, $-x$.

**5.2.** Test Property 1 for $f(x) = 4x$ using $a = 3$, $b = -1$.

**5.3.** Compose $f(x) = -2x + 5$ and $g(x) = 4x + 1$ into $g(f(x))$. Is the result affine?

**5.4.** Explain in your own words, without formulas, why chaining 50 straight-line functions can't produce a curve.

<details>
<summary>Hint</summary>

5.1: check whether $f(0) = 0$, and whether the graph is a straight line.

</details>

<details>
<summary>Solutions</summary>

**5.1.** Linear: $5x$, $0$, $-x$. Affine: $5x - 1$. Nonlinear: $x^3$, $\sqrt{x}$.

**5.2.** $f(2) = 8$ and $f(3) + f(-1) = 12 - 4 = 8$ ✓

**5.3.** $4(-2x + 5) + 1 = -8x + 21$. Yes, affine.

**5.4.** Each straight-line step just stretches and shifts. A stretch followed by a stretch is still a stretch, and a shift followed by a shift is still a shift, so no step ever introduces any bending.

</details>

---

## 6. Exponential functions and the number e

### The problem

Some things grow by **adding** a fixed amount each step (₱100 saved every month). Others grow by **multiplying** by a fixed amount each step (a bacteria colony doubling every hour). The second kind is called **exponential** growth, and it behaves very differently.

### The exponential function $2^x$

The input is now **in the exponent**:

| $x$ | −2 | −1 | 0 | 1 | 2 | 3 | 4 | 10 |
|---|---|---|---|---|---|---|---|---|
| $2^x$ | 0.25 | 0.5 | 1 | 2 | 4 | 8 | 16 | 1024 |

(The negative and zero exponents come from Algebra §3.)

Features of the graph:

- **Always positive.** It gets close to 0 on the left but never reaches it.
- It passes through $(0, 1)$, because anything to the power 0 is 1.
- It **explodes** to the right.

### Linear vs. exponential growth

| $x$ | 1 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|
| $2x$ (adding) | 2 | 4 | 10 | 20 | 40 |
| $2^x$ (multiplying) | 2 | 4 | 32 | 1024 | 1,048,576 |

They start the same, then exponential growth leaves linear growth far behind.

### Exponential decay

If the base is between 0 and 1, the function **shrinks**:

$$
\left(\tfrac{1}{2}\right)^x = 2^{-x}
$$

Values: $1, 0.5, 0.25, 0.125, \ldots$ This is **decay**: halving each step.

### Where the number $e$ comes from

In Algebra, $e \approx 2.718$ appeared out of nowhere. Here's one place it comes from.

A bank gives **100% interest per year** on ₱1. How much do you have after a year, depending on how often they add the interest?

- **Once a year:** ₱1 × 2 = ₱2.
- **Twice a year** (50% each half-year): $1 \times 1.5 \times 1.5 = \left(1 + \frac{1}{2}\right)^2 = 2.25$.
- **$n$ times a year:** $\left(1 + \frac{1}{n}\right)^n$.

| Times per year $n$ | $\left(1 + \frac{1}{n}\right)^n$ |
|---|---|
| 1 | 2 |
| 2 | 2.25 |
| 12 (monthly) | 2.6130 |
| 365 (daily) | 2.7146 |
| 1,000,000 | 2.71828 |

Adding interest more and more often doesn't make you infinitely rich. The amount **settles toward one special number**: $e = 2.71828\ldots$

So $e$ is the number you get from growth that happens **continuously**, every instant. That's why it shows up whenever things change smoothly.

### The functions $e^x$ and $e^{-x}$

- $e^x$ is **exponential growth** with base $e$. Same shape as $2^x$, slightly steeper.
- $e^{-x}$ is **exponential decay**. It starts at 1 when $x = 0$ and shrinks toward 0.

| $x$ | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|
| $e^x$ | 0.135 | 0.368 | 1 | 2.718 | 7.389 | 20.09 |
| $e^{-x}$ | 7.389 | 2.718 | 1 | 0.368 | 0.135 | 0.050 |

In the Calculus file, you'll see $e^x$'s most special property: its steepness at every point equals its own value.

### A limit of computers

Exponentials get enormous fast. $e^{710}$ is too large for a computer to store (the largest regular decimal number is about $1.8 \times 10^{308}$). In Python, `np.exp(710)` gives `inf`. This is called **overflow**. Keep it in mind for §9 and §10.

> **Why ML cares:** Two of the most important ML functions (sigmoid and softmax, in §9 and §10) are built from $e^x$. They need it because $e^x$ turns **any** number, even a negative one, into a positive number.

### Exercises

**6.1.** Make a table of $3^x$ for $x = -2, -1, 0, 1, 2$.

**6.2.** Which is bigger at $x = 10$: $10x$ or $2^x$? At $x = 20$?

**6.3.** Without a calculator: is $e^{-3}$ bigger or smaller than 1? Is it positive or negative?

**6.4.** Calculate $\left(1 + \frac{1}{4}\right)^4$. Is it between 2.25 and 2.72?

**6.5.** Why is $e^x$ never zero or negative, no matter what $x$ is?

<details>
<summary>Hint</summary>

6.3: $e^{-3} = \frac{1}{e^3}$ (Algebra §3).
6.4: $1.25^4 = 1.25 \times 1.25 \times 1.25 \times 1.25$.

</details>

<details>
<summary>Solutions</summary>

**6.1.** $\frac{1}{9}, \frac{1}{3}, 1, 3, 9$.

**6.2.** At 10: $100$ vs $1024$, so $2^x$. At 20: $200$ vs $1{,}048{,}576$, so $2^x$ by far.

**6.3.** Smaller than 1 (it's $\frac{1}{e^3} = \frac{1}{20.09} \approx 0.05$), and positive.

**6.4.** $1.5625 \times 1.5625 \approx 2.441$. Yes, between them.

**6.5.** A positive number multiplied by itself stays positive. With a negative exponent you get "1 divided by a positive number," which is still positive. No operation involved ever reaches zero or crosses into negatives.

</details>

---

## 7. The logarithm as a function

### The idea

In Algebra, you used logs to answer "what exponent?" Now think of $\ln$ as a **function**: a machine that takes $x$ and outputs $\ln(x)$.

Since $\ln$ undoes $e^x$ (§4), $\ln(x)$ is the **inverse function** of $e^x$.

### Its graph

| $x$ | 0.1 | 0.5 | 1 | 2 | $e \approx 2.718$ | 10 | 100 |
|---|---|---|---|---|---|---|---|
| $\ln(x)$ | −2.303 | −0.693 | 0 | 0.693 | 1 | 2.303 | 4.605 |

Features:

- **Domain:** $(0, \infty)$. Only positive inputs (Algebra §4).
- **Range:** all real numbers $\mathbb{R}$.
- Passes through $(1, 0)$, because $\ln(1) = 0$.
- **Negative** for inputs between 0 and 1.
- **Grows very slowly.** Going from 10 to 100 only adds 2.3.
- As $x$ gets closer and closer to 0, $\ln(x)$ drops lower and lower without any limit. We say it "goes to negative infinity," written $\ln(x) \to -\infty$. The arrow $\to$ is read "**approaches**" or "goes to."

### Mirror images

The graph of an inverse function is the original graph **flipped across the diagonal line $y = x$**. $e^x$ passes through $(0, 1)$, and $\ln x$ passes through $(1, 0)$: the coordinates swapped.

### Always increasing

If $a < b$, then $\ln(a) < \ln(b)$. A bigger input always gives a bigger output. Functions with this property are called **increasing** (or **monotonic**).

This means taking the log of a list of numbers **keeps their order**. The biggest number still has the biggest log.

> **Why ML cares:** Because $\ln$ keeps order, finding the setting that makes a quantity largest gives the same answer as finding the setting that makes its **log** largest. And logs are much easier to work with (Algebra §4: they turn products into sums). ML relies on this trick constantly.

### Exercises

**7.1.** Without a calculator, is $\ln(0.3)$ positive or negative? What about $\ln(3)$?

**7.2.** Put in order from smallest to largest: $\ln(5)$, $\ln(0.5)$, $\ln(1)$, $\ln(50)$.

**7.3.** What happens to $\ln(x)$ as $x$ gets very close to 0, like $x = 0.0001$? Why does this cause problems when a computer calculates $\ln(0)$?

<details>
<summary>Solutions</summary>

**7.1.** $\ln(0.3)$ is negative (input between 0 and 1). $\ln(3)$ is positive.

**7.2.** $\ln(0.5) < \ln(1) < \ln(5) < \ln(50)$. Same order as the inputs, since $\ln$ is increasing.

**7.3.** $\ln(0.0001) \approx -9.2$, very negative, and it keeps dropping as $x$ approaches 0. At exactly 0 there's no answer at all, so the computer returns `-inf`, which then spreads into every later calculation.

</details>

---

## 8. Piecewise functions, absolute value, and ReLU

### The problem

Some rules **change depending on the input**. A delivery fee might be ₱50 flat for up to 3 km, but ₱50 + ₱10 per km beyond that. One formula can't describe both parts. We need a way to write "use this rule here, and that rule there."

### Piecewise notation

$$
f(x) = \begin{cases} 50 & \text{if } x \le 3 \\ 50 + 10(x - 3) & \text{if } x > 3 \end{cases}
$$

Read it aloud as: "f of x equals 50 if x is at most 3, and 50 plus 10 times x minus 3 if x is more than 3."

To evaluate: **first check which condition is true**, then use that row's formula.

| $x$ | Which row? | $f(x)$ |
|---|---|---|
| 2 | $x \le 3$ | $50$ |
| 3 | $x \le 3$ | $50$ |
| 5 | $x > 3$ | $50 + 10(2) = 70$ |

### Absolute value

The **absolute value** of a number is its distance from 0 on the number line. Distance is never negative.

$$
|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}
$$

Read $|x|$ aloud as "**the absolute value of x**."

- $|5| = 5$ (first row)
- $|{-5}| = -(-5) = 5$ (second row: the minus sign cancels the negative)
- $|0| = 0$

The graph is a **V shape** with its point at the origin.

### The maximum function

$\max(a, b)$ means "**the larger of $a$ and $b$**."

- $\max(3, 7) = 7$
- $\max(-2, 0) = 0$
- $\max(4, 4) = 4$

### ReLU

The **ReLU** function (short for "Rectified Linear Unit"; just a name) is:

$$
\text{ReLU}(x) = \max(0, x) = \begin{cases} x & \text{if } x > 0 \\ 0 & \text{if } x \le 0 \end{cases}
$$

In words: **positive numbers pass through unchanged, and negative numbers become 0.**

| $x$ | −3 | −1 | 0 | 0.5 | 2 | 5 |
|---|---|---|---|---|---|---|
| ReLU($x$) | 0 | 0 | 0 | 0.5 | 2 | 5 |

The graph is flat at 0 on the left, then a 45° line on the right, with a **corner** at the origin.

### ReLU is nonlinear

Each piece is a straight line, but the corner makes the whole function nonlinear. Test Property 1 from §5 with $a = -1$, $b = 1$:

- $\text{ReLU}(-1 + 1) = \text{ReLU}(0) = 0$
- $\text{ReLU}(-1) + \text{ReLU}(1) = 0 + 1 = 1$

$0 \ne 1$, so ReLU is not linear. **One corner is enough to break linearity.**

### Applying a function to a list

When a function like ReLU is applied to a **list** of numbers, it's applied to each number separately. This is called **elementwise**:

$$
\text{ReLU}([-1,\ 0.5,\ 2,\ -3]) = [0,\ 0.5,\ 2,\ 0]
$$

> **Why ML cares:** ReLU is the most common **activation function**: the nonlinear step placed between straight-line steps in a neural network (§5). It's popular because it's extremely cheap to compute and, as you'll see in Calculus, it keeps learning signals from fading away.

### Exercises

**8.1.** Evaluate the delivery-fee function at $x = 1$, $x = 3.5$, and $x = 10$.

**8.2.** Calculate $|{-7}|$, $|3 - 8|$, and $|0.5|$.

**8.3.** Calculate $\max(-4, -1)$ and $\max(0, -2.5)$.

**8.4.** Apply ReLU elementwise to $[4, -0.1, 0, -8, 1.5]$.

**8.5.** Is $|x|$ linear? Test Property 1 with $a = -2$, $b = 2$.

**8.6.** Write $f(x) = \max(0, x - 2)$ as a piecewise function. Where is the corner?

<details>
<summary>Hint</summary>

8.6: when is $x - 2$ positive? That decides which row you're in.

</details>

<details>
<summary>Solutions</summary>

**8.1.** $50$, $50 + 10(0.5) = 55$, $50 + 10(7) = 120$.

**8.2.** $7$, $|{-5}| = 5$, $0.5$.

**8.3.** $-1$ (it's larger than $-4$), and $0$.

**8.4.** $[4, 0, 0, 0, 1.5]$.

**8.5.** $|{-2} + 2| = 0$, but $|{-2}| + |2| = 4$. Not linear.

**8.6.** $f(x) = x - 2$ if $x > 2$, and $0$ if $x \le 2$. The corner is at $x = 2$.

</details>

---

## 9. The sigmoid function

### The problem

Sometimes we have a number that could be anything (like $-50$, $0.3$, or $1000$) and we need to turn it into a number **between 0 and 1**, so it can be read as a percentage or a probability.

It should do this smoothly: big positive numbers should become close to 1, big negative numbers close to 0, and 0 should land right in the middle at 0.5.

### The formula

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- $\sigma$ is the lowercase Greek letter **sigma**. Read $\sigma(z)$ aloud as "**sigma of z**."
- The input is called $z$ here. That's only a naming habit. It's still just the input, like $x$.
- This function is called the **sigmoid** (meaning "S-shaped").

### Build it up piece by piece

Don't read the formula all at once. It's a chain of simple steps (§3):

1. Take $z$ and flip its sign: $-z$
2. Raise $e$ to that power: $e^{-z}$ (always positive, from §6)
3. Add 1: $1 + e^{-z}$ (always bigger than 1)
4. Divide 1 by the result: $\frac{1}{1 + e^{-z}}$

Calculate it for three inputs:

| $z$ | $e^{-z}$ | $1 + e^{-z}$ | $\sigma(z) = \frac{1}{1 + e^{-z}}$ |
|---|---|---|---|
| $-2$ | $e^{2} \approx 7.389$ | $8.389$ | $\approx 0.119$ |
| $0$ | $e^{0} = 1$ | $2$ | $0.5$ |
| $2$ | $e^{-2} \approx 0.135$ | $1.135$ | $\approx 0.881$ |

More values:

| $z$ | −10 | −4 | −2 | 0 | 2 | 4 | 10 |
|---|---|---|---|---|---|---|---|
| $\sigma(z)$ | 0.00005 | 0.018 | 0.119 | 0.5 | 0.881 | 0.982 | 0.99995 |

Plotted, this makes a smooth **S-shaped curve**: flat near 0 on the far left, rising through 0.5 at the middle, flat near 1 on the far right.

### Why the output is always between 0 and 1

Follow the pieces:

- **Always less than 1:** $e^{-z} > 0$, so the bottom $1 + e^{-z}$ is **bigger than 1**. And 1 divided by something bigger than 1 is **less than 1**.
- **Always more than 0:** the bottom is a positive number, and 1 divided by a positive number is positive.

So $0 < \sigma(z) < 1$ for every $z$. The range is $(0, 1)$.

### What happens at the extremes

- **As $z$ gets very large** (e.g. $z = 100$): $e^{-100}$ is incredibly tiny, almost 0. So $\sigma \approx \frac{1}{1 + 0} = 1$. We write: as $z \to \infty$, $\sigma(z) \to 1$.
- **As $z$ gets very negative** (e.g. $z = -100$): $e^{100}$ is enormous. So $\sigma \approx \frac{1}{\text{huge}} \approx 0$. As $z \to -\infty$, $\sigma(z) \to 0$.

It gets **closer and closer** to 0 and 1, but never actually reaches them.

### Flat ends: saturation

Look at the table: going from $z = 4$ to $z = 10$ (a change of 6) only moves the output from 0.982 to 0.99995. At the far ends, **changing the input barely changes the output**. The curve is nearly flat there.

This is called **saturation**. Remember it. It becomes important in Calculus.

### A symmetry: $\sigma(-z) = 1 - \sigma(z)$

**Check with numbers:** $\sigma(2) \approx 0.881$ and $\sigma(-2) \approx 0.119$. And $1 - 0.881 = 0.119$ ✓

**Why:**

| Step | What we did |
|---|---|
| $1 - \frac{1}{1 + e^{-z}}$ | Start with $1 - \sigma(z)$ |
| $= \frac{1 + e^{-z}}{1 + e^{-z}} - \frac{1}{1 + e^{-z}}$ | Wrote 1 as a fraction with the same bottom |
| $= \frac{e^{-z}}{1 + e^{-z}}$ | Subtracted the tops |
| $= \frac{e^{-z} \cdot e^{z}}{(1 + e^{-z}) \cdot e^{z}}$ | Multiplied top and bottom by $e^z$ (this doesn't change the value) |
| $= \frac{1}{e^{z} + 1}$ | $e^{-z} \cdot e^{z} = e^0 = 1$ (Algebra §3, Rule 1) |
| $= \sigma(-z)$ | That's exactly the sigmoid formula with $-z$ in place of $z$ |

### Undoing the sigmoid

Given an output $p$ between 0 and 1, which input $z$ produced it? Find the inverse (§4):

| Step | What we did |
|---|---|
| $p = \frac{1}{1 + e^{-z}}$ | Start |
| $p(1 + e^{-z}) = 1$ | Multiplied both sides by the bottom |
| $1 + e^{-z} = \frac{1}{p}$ | Divided both sides by $p$ |
| $e^{-z} = \frac{1}{p} - 1 = \frac{1 - p}{p}$ | Subtracted 1, then wrote it as one fraction |
| $-z = \ln\left(\frac{1 - p}{p}\right)$ | Took $\ln$ of both sides |
| $z = \ln\left(\frac{p}{1 - p}\right)$ | Multiplied by $-1$. Flipping a fraction inside a log flips the sign: $-\ln\frac{a}{b} = \ln\frac{b}{a}$ |

This inverse is called the **logit** function.

**Check:** $p = 0.5$ gives $z = \ln(1) = 0$ ✓, which matches $\sigma(0) = 0.5$.

> **Why ML cares:** When a model must answer a yes/no question ("is this email spam?"), it first calculates a score $z$ that could be any number, then uses the sigmoid to turn that score into a probability between 0 and 1. The saturation you saw above is why deep networks mostly use ReLU instead of sigmoid in their middle steps.

### Exercises

**9.1.** Calculate $\sigma(\ln 3)$ exactly, without a calculator.

**9.2.** Use the table and the symmetry to find $\sigma(-4)$ from $\sigma(4)$.

**9.3.** Explain in two sentences why $\sigma(z)$ can never equal exactly 1.

**9.4.** Using the logit, find the $z$ that gives $\sigma(z) = 0.75$.

**9.5.** Without looking, re-derive $\sigma(-z) = 1 - \sigma(z)$.

<details>
<summary>Hint</summary>

9.1: $e^{-\ln 3} = \frac{1}{e^{\ln 3}} = \frac{1}{3}$.
9.4: $\frac{0.75}{0.25} = 3$.

</details>

<details>
<summary>Solutions</summary>

**9.1.** $\frac{1}{1 + \frac{1}{3}} = \frac{1}{\frac{4}{3}} = \frac{3}{4}$.

**9.2.** $1 - 0.982 = 0.018$ ✓ (matches the table).

**9.3.** For $\sigma$ to equal 1, the bottom $1 + e^{-z}$ would have to be exactly 1, which needs $e^{-z} = 0$. But $e^{\text{anything}}$ is never 0.

**9.4.** $z = \ln(3) \approx 1.099$. (Compare with 9.1.)

</details>

---

## 10. The softmax function

### The problem

Sigmoid turns **one** score into one probability. But what if there are **several options**? For example, three candidates with scores $[2.0, 1.0, 0.1]$. We want to turn those scores into percentages that:

1. are all positive, and
2. **add up to exactly 1** (100%), and
3. keep the order (the highest score gets the highest percentage).

### Why not just divide each score by the total?

Try scores $[2, -1, 0]$. The total is $1$. Dividing gives $[2, -1, 0]$: a "percentage" of $-1$ and one of $2$ (200%). **Broken.** Negative scores ruin simple division.

**The fix:** first make every score positive using $e^x$ (always positive, from §6), **then** divide by the total.

### New notation: a list with subscripts

Write the list of scores as $\mathbf{z} = [z_1, z_2, z_3]$. The bold $\mathbf{z}$ means "a whole list," and $z_1$, $z_2$, $z_3$ are its items (Algebra §5). The number of items is $K$.

### The formula

$$
\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\displaystyle\sum_{j=1}^{K} e^{z_j}}
$$

Read it aloud as: "the $i$-th output of softmax is $e$ to the $z_i$, divided by the sum of $e$ to the $z_j$, for $j$ from 1 to $K$."

Decode each piece:

| Piece | Meaning |
|---|---|
| $\text{softmax}(\mathbf{z})_i$ | the output for option number $i$ |
| $e^{z_i}$ (top) | make option $i$'s score positive |
| $\sum_{j=1}^{K} e^{z_j}$ (bottom) | make **every** score positive, then add them all up |

**Why two different counters, $i$ and $j$?** The top is about **one** specific option $i$. The bottom adds over **all** options. If we reused $i$ for the sum, it would get confused with the $i$ on top. So the sum gets its own counter, $j$.

### Worked example

$\mathbf{z} = [2.0,\ 1.0,\ 0.1]$

| Step | Option 1 | Option 2 | Option 3 |
|---|---|---|---|
| Score $z_i$ | 2.0 | 1.0 | 0.1 |
| Make positive: $e^{z_i}$ | 7.389 | 2.718 | 1.105 |
| Total of that row | | $7.389 + 2.718 + 1.105 = 11.212$ | |
| Divide by total | $\frac{7.389}{11.212} = 0.659$ | $\frac{2.718}{11.212} = 0.242$ | $\frac{1.105}{11.212} = 0.099$ |

Result: $[0.659,\ 0.242,\ 0.099]$. Check: $0.659 + 0.242 + 0.099 = 1.000$ ✓

### Why each property holds

1. **All positive:** each top $e^{z_i}$ is positive, and so is the bottom.
2. **Adds to 1:** adding all the tops gives exactly the bottom, and $\frac{\text{bottom}}{\text{bottom}} = 1$.
3. **Order kept:** $e^x$ is increasing (a bigger score gives a bigger $e^{\text{score}}$), and every option is divided by the same bottom.

### Adding the same number to every score changes nothing

Add 10 to every score: $[12, 11, 10.1]$.

$$
\frac{e^{z_i + 10}}{\sum_j e^{z_j + 10}} = \frac{e^{10} \cdot e^{z_i}}{e^{10} \cdot \sum_j e^{z_j}} = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

(Using $e^{a + b} = e^a \cdot e^b$ from Algebra §3. The $e^{10}$ on top and bottom cancel.)

**Only the differences between scores matter.**

### Using that to avoid overflow

Scores $[1000, 999]$: a computer can't calculate $e^{1000}$ (overflow, §6). But subtract 1000 from both, which is allowed by the property above, to get $[0, -1]$:

| | Option 1 | Option 2 |
|---|---|---|
| Shifted score | 0 | −1 |
| $e^{\text{score}}$ | 1 | 0.368 |
| Divide by total 1.368 | 0.731 | 0.269 |

**The trick:** subtract the largest score from every score before calculating.

### Temperature: making it sharper or flatter

Divide every score by a number $T$ (called the **temperature**) before applying softmax.

$[2, 1, 0.1]$ with $T = 0.5$ becomes $[4, 2, 0.2]$:

| | Option 1 | Option 2 | Option 3 |
|---|---|---|---|
| $e^{\text{score}}$ | 54.598 | 7.389 | 1.221 |
| Divide by total 63.208 | **0.864** | 0.117 | 0.019 |

Compare with $T = 1$: $[0.659, 0.242, 0.099]$.

- $T < 1$: **sharper**, and the top option dominates more.
- $T > 1$: **flatter**, and the options become more equal.

### Softmax with two options is the sigmoid

Take two scores: $[z, 0]$.

$$
\text{softmax}([z, 0])_1 = \frac{e^z}{e^z + e^0} = \frac{e^z}{e^z + 1}
$$

Now divide top and bottom by $e^z$:

$$
= \frac{1}{1 + e^{-z}} = \sigma(z)
$$

**Sigmoid is just softmax for two options.**

> **Why ML cares:** When a model picks between many categories (which of 10 digits is in a picture, which word comes next), softmax turns its scores into probabilities. The "temperature" setting on AI chat tools is exactly the $T$ above.

### Exercises

**10.1.** Calculate $\text{softmax}([1, 1, 1])$. Why does the answer make sense?

**10.2.** Calculate $\text{softmax}([0, \ln 3])$ exactly.

**10.3.** Calculate $\text{softmax}([3, 1])$. Then calculate $\text{softmax}([103, 101])$ using the subtract-the-largest trick.

**10.4.** Explain in two sentences why dividing scores by their total doesn't work, but softmax does.

**10.5.** Show that $\text{softmax}([z, 0])_2 = 1 - \sigma(z)$.

<details>
<summary>Hint</summary>

10.2: $e^0 = 1$ and $e^{\ln 3} = 3$.
10.3: $e^{-2} \approx 0.135$.

</details>

<details>
<summary>Solutions</summary>

**10.1.** Every $e^1$ is the same, so each gets $\frac{1}{3}$. Equal scores should get equal shares.

**10.2.** $[\frac{1}{4}, \frac{3}{4}]$.

**10.3.** Shift to $[0, -2]$: $e$ values $[1, 0.135]$, total $1.135$, result $[0.881, 0.119]$. The second calculation is identical after shifting: $[103, 101] \to [0, -2]$, same answer.

**10.4.** Dividing by the total fails when scores are negative or add up to zero. Softmax first makes every score positive with $e^x$, so dividing by the total always gives valid percentages.

**10.5.** $\frac{e^0}{e^z + 1} = \frac{1}{e^z + 1} = \sigma(-z) = 1 - \sigma(z)$, using the symmetry from §9.

</details>

---

## Code lab — `math/02_functions.py`

### What you're doing and why

You'll write ReLU, sigmoid, and softmax as Python functions, make them safe for huge inputs, and **see** the collapse from §5 happen in code.

**Rules:** no AI, no autocomplete, no copying.

### Python you need

- `np.array([1, 2, 3])` makes an array. Math on arrays is elementwise: `np.array([1, 2]) * 2` gives `[2, 4]`.
- `np.exp(x)` is $e^x$, and works on arrays.
- `np.maximum(0, x)` is elementwise $\max(0, x)$.
- `np.max(x)` gives the single largest item.
- `np.sum(x)` adds all the items.
- `np.abs(x)` is elementwise absolute value.
- `np.where(condition, a, b)` picks `a` where the condition is true and `b` where it's false.
- Plotting: `plt.plot(xs, ys)`, then `plt.show()`.

### The tasks

```python
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    """max(0, x), elementwise.  (§8)"""
    ...

def sigmoid(z):
    """1 / (1 + e^(-z)).  (§9)
    Must not overflow for z = -1000 or z = 1000."""
    ...

def softmax(z):
    """For a 1-D array of scores. Use the subtract-the-largest trick.  (§10)"""
    ...

if __name__ == "__main__":
    assert np.allclose(relu(np.array([-1, 0.5, 2, -3])), [0, 0.5, 2, 0])
    assert np.isclose(sigmoid(0.0), 0.5)
    assert np.isclose(sigmoid(np.log(3)), 0.75)
    assert np.all(np.isfinite(sigmoid(np.array([-1000.0, 1000.0]))))
    assert np.allclose(softmax(np.array([2.0, 1.0, 0.1])), [0.659, 0.242, 0.099], atol=1e-3)
    assert np.allclose(softmax(np.array([1000.0, 999.0])), [0.731, 0.269], atol=1e-3)
    assert np.isclose(softmax(np.array([5.0, -2.0, 0.3])).sum(), 1.0)

    # 1) The collapse from §5: chaining straight lines gives a straight line.
    #    f(x) = 2x + 1, g(x) = 3x - 1. Compute g(f(x)) for x = 0..9 and check it equals 6x + 2.
    #    Then put relu between them: g(relu(f(x))) for x = -5..5. Is it still a straight line? Plot both.

    # 2) Plot sigmoid for z from -8 to 8 (np.linspace(-8, 8, 200)).
    #    Mark the point (0, 0.5). Label the flat "saturated" ends.

    # 3) Check the symmetry: for 5 random z values, assert sigmoid(-z) is close to 1 - sigmoid(z).
    print("all checks passed")
```

Before running part 1, **predict** what the ReLU version's plot will look like.

<details>
<summary>Hint for a safe sigmoid</summary>

`1 / (1 + np.exp(-z))` overflows when $z$ is very negative, because $e^{-z}$ becomes huge.

For negative $z$, use the equivalent form $\frac{e^{z}}{1 + e^{z}}$ (multiply top and bottom by $e^z$), where $e^z$ is tiny instead of huge.

One neat way: let `t = np.exp(-np.abs(z))`. That's always $\le 1$, so it can't overflow. Then:
- where $z \ge 0$: the answer is $\frac{1}{1 + t}$
- where $z < 0$: the answer is $\frac{t}{1 + t}$

</details>

<details>
<summary>Reference solution (only after your own attempt)</summary>

```python
def relu(x):
    return np.maximum(0, x)

def sigmoid(z):
    z = np.asarray(z, dtype=float)
    t = np.exp(-np.abs(z))
    return np.where(z >= 0, 1 / (1 + t), t / (1 + t))

def softmax(z):
    shifted = z - np.max(z)
    e = np.exp(shifted)
    return e / np.sum(e)

# part 1
x = np.arange(10)
assert np.allclose(3 * (2 * x + 1) - 1, 6 * x + 2)
```

The ReLU version is flat for inputs where $2x + 1 \le 0$, then a straight line. Together that has a corner, so it's no longer a single straight line.

</details>

---

## Common mistakes

| Mistake | Why it's wrong |
|---|---|
| Reading $f(x)$ as "f times x" | It means "the output of $f$ when the input is $x$" |
| Reading $f^{-1}(x)$ as $\frac{1}{f(x)}$ | It means the **undo** function. For $f(x) = 2x$: $f^{-1}(8) = 4$, but $\frac{1}{f(8)} = \frac{1}{16}$ |
| Computing $f(g(x))$ by doing $f$ first | The inside ($g$) happens first |
| Calling $3x + 2$ strictly "linear" | It's affine: $f(0) = 2 \ne 0$ |
| Thinking $e^{-x}$ is negative | It's $\frac{1}{e^x}$, which is positive |
| Thinking sigmoid can output exactly 0 or 1 | It only gets closer and closer |
| Softmax without subtracting the largest score | Large scores overflow to `inf`, and you get `nan` |
| Mixing up $\sigma$ (lowercase sigma, the sigmoid function) and $\Sigma$ (capital sigma, sum) | Different symbols, different meanings |

---

## Check yourself

Do this **after** working through the file. Closed book, 15 minutes.

1. What's the domain of $f(x) = \sqrt{x - 2}$? Of $g(x) = \ln x$?
2. $f(x) = 2x + 1$ and $g(x) = x^2$. Calculate $f(g(3))$ and $g(f(3))$.
3. Find the inverse of $f(x) = 3x - 6$.
4. What's $\sigma(0)$? What's the range of $\sigma$?
5. Calculate ReLU($-2$) and ReLU($3$).
6. Calculate $\text{softmax}([0, \ln 3])$ exactly.
7. Is $f(x) = 2x + 3$ linear in the strict sense? Why or why not?
8. Why can't chaining 10 affine functions produce a curve?
9. Where does the number $e$ come from? Explain with the bank interest example.
10. Show that 2-option softmax $[z, 0]$ gives $\sigma(z)$.

<details>
<summary>Answers</summary>

**1.** Domains of $f(x) = \sqrt{x - 2}$ and $g(x) = \ln x$ → §2

The domain is every input the function is allowed to take. Find it by asking what would break.

*For $f$:* a square root of a negative number isn't a real number, so whatever is under the root must be $\ge 0$:

$$x - 2 \ge 0 \quad\Rightarrow\quad x \ge 2$$

In interval notation: $[2, \infty)$. The bracket $[$ means 2 **is** included, because $\sqrt{0} = 0$ is perfectly fine.

*For $g$:* $\ln x$ asks "$e$ to the what gives $x$?" No power of $e$ ever produces $0$ or a negative, so:

$$x > 0$$

That's $(0, \infty)$. The parenthesis $($ means 0 is **not** included.

---

**2.** $f(x) = 2x + 1$, $g(x) = x^2$: find $f(g(3))$ and $g(f(3))$ → §3

Work from the **inside out** — the inner function runs first.

*$f(g(3))$:*

$$g(3) = 3^2 = 9, \qquad f(9) = 2(9) + 1 = 19$$

*$g(f(3))$:*

$$f(3) = 2(3) + 1 = 7, \qquad g(7) = 7^2 = 49$$

*The point:* $19 \ne 49$. Order matters in composition. $f(g(x))$ and $g(f(x))$ are different functions.

---

**3.** Inverse of $f(x) = 3x - 6$ → §4

The inverse undoes the function: it takes an output back to the input that produced it.

*Step 1 — write it as an equation:* $y = 3x - 6$

*Step 2 — solve for $x$* (rearrange until $x$ is alone):

$$y + 6 = 3x \quad\Rightarrow\quad x = \frac{y + 6}{3}$$

*Step 3 — rename $y$ back to $x$*, since we always write functions in terms of their input:

$$f^{-1}(x) = \frac{x + 6}{3}$$

*Check:* $f(4) = 3(4) - 6 = 6$, and $f^{-1}(6) = \frac{6+6}{3} = 4$ ✓ Back where we started.

*Reading it as undoing steps:* $f$ multiplies by 3, then subtracts 6. The inverse reverses both the operations **and** their order: add 6, then divide by 3.

---

**4.** $\sigma(0)$ and the range of $\sigma$ → §9

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

*At $z = 0$:* anything to the power 0 is 1, so $e^{-0} = e^0 = 1$:

$$\sigma(0) = \frac{1}{1 + 1} = 0.5$$

*The range:* $e^{-z}$ is always positive, never zero. So the denominator $1 + e^{-z}$ is always strictly bigger than 1, which keeps the fraction strictly below 1. And since the denominator is finite, the fraction stays strictly above 0. Range: $(0, 1)$, open at both ends — sigmoid approaches 0 and 1 but never reaches them.

---

**5.** ReLU($-2$) and ReLU($3$) → §8

$$\text{ReLU}(x) = \max(0, x)$$

It passes positives through unchanged and flattens everything negative to zero.

$$\text{ReLU}(-2) = \max(0, -2) = 0, \qquad \text{ReLU}(3) = \max(0, 3) = 3$$

---

**6.** $\text{softmax}([0, \ln 3])$ → §10

Softmax exponentiates each score, then divides by the total so the results add to 1.

*Step 1 — exponentiate each entry:*

$$e^0 = 1, \qquad e^{\ln 3} = 3$$

(That second one is $e$ and $\ln$ cancelling — no calculator needed.)

*Step 2 — add them up:* $1 + 3 = 4$

*Step 3 — divide each by the total:*

$$\left[\frac{1}{4}, \frac{3}{4}\right] = [0.25, 0.75]$$

*Check:* both are between 0 and 1, and they sum to 1 ✓ The bigger score got the bigger share, and a score gap of $\ln 3$ produced exactly a 3:1 ratio.

---

**7.** Is $f(x) = 2x + 3$ linear in the strict sense? → §5

No. It's **affine**.

Strict linearity requires $f(ax + by) = af(x) + bf(y)$, and a quick consequence of that is $f(0) = 0$ — a linear function must pass through the origin. Here:

$$f(0) = 2(0) + 3 = 3 \ne 0$$

So it fails immediately. Directly: $f(1 + 1) = f(2) = 7$, but $f(1) + f(1) = 5 + 5 = 10$. Not equal.

*The vocabulary:* a straight-line graph is called "linear" in everyday use, but in the strict sense linear means *stretch only* ($mx$), while affine means *stretch plus shift* ($mx + b$). The $+3$ is the shift that breaks strict linearity.

---

**8.** Why can't chaining 10 affine functions produce a curve? → §5

Because affine-composed-with-affine is just another affine function, and that collapse repeats all the way down the chain.

Take two: $f(x) = ax + b$ and $g(x) = cx + d$. Compose them:

$$f(g(x)) = a(cx + d) + b = \underbrace{ac}_{\text{new stretch}}x + \underbrace{ad + b}_{\text{new shift}}$$

Still one stretch and one shift — still a straight line. Chain 10 and you're just doing that collapse 9 times: the result is one stretch and one shift.

*Why this matters in ML:* stacking 10 neural network layers with no nonlinearity between them is exactly this. All that depth buys you nothing, it's mathematically identical to a single layer. That's why ReLU, sigmoid, and friends sit between layers.

---

**9.** Where does $e$ come from? → §6

From compound interest taken to its limit.

Put \$1 in a bank at 100% annual interest. If it's paid once at year end, you have $\$2$. Pay it twice a year at 50% each: $(1 + \frac{1}{2})^2 = 2.25$. Four times at 25%: $(1 + \frac{1}{4})^4 \approx 2.441$. Twelve times: $\approx 2.613$. Daily: $\approx 2.7146$.

The general form for $n$ payments per year is:

$$\left(1 + \frac{1}{n}\right)^n$$

More frequent compounding keeps growing the total, but by less and less each time — it doesn't run away to infinity, it settles:

$$e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n \approx 2.71828$$

So $e$ is what continuous growth converges to. It's a constant that *emerged* from a process, like $\pi$ emerges from circles, rather than one anybody chose.

---

**10.** Show that 2-option softmax on $[z, 0]$ gives $\sigma(z)$ → §10

*Step 1 — write the softmax for the first entry:*

$$\text{softmax}([z, 0])_1 = \frac{e^z}{e^z + e^0} = \frac{e^z}{e^z + 1}$$

*Step 2 — divide top and bottom by $e^z$.* This is allowed because it's the same as multiplying by $\frac{1/e^z}{1/e^z} = 1$:

$$= \frac{e^z / e^z}{(e^z + 1)/e^z} = \frac{1}{1 + e^{-z}}$$

(using $\frac{1}{e^z} = e^{-z}$)

$$= \sigma(z)$$

*What this means:* sigmoid isn't a separate invention. It's exactly what softmax becomes when there are only two options, with the second score fixed at 0. Binary classification is the 2-class case of multi-class classification.

</details>

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can read and evaluate $f(x)$, $f(g(x))$, and $f^{-1}(x)$, and I know what $f^{-1}$ does NOT mean.
- [ ] I can find a domain by checking for division by zero, square roots of negatives, and logs of non-positive numbers.
- [ ] I can read interval notation, including $\infty$, $\mathbb{R}$, and $\in$.
- [ ] I can find an inverse by rearranging, and explain why $x^2$ has no inverse on all real numbers.
- [ ] I can explain linear vs. affine vs. nonlinear, and show with algebra why chaining affine functions stays affine.
- [ ] I can explain where $e$ comes from and describe the graphs of $e^x$, $e^{-x}$, and $\ln x$.
- [ ] I can evaluate piecewise functions, $|x|$, and ReLU, and show ReLU is nonlinear.
- [ ] I can compute sigmoid step by step, explain why its output is in $(0, 1)$, what happens at the extremes, and derive its symmetry and inverse.
- [ ] I can compute softmax by hand for 3 scores, explain each of its properties, use the overflow trick, and explain temperature.
- [ ] Check yourself: 10/10.
- [ ] Code lab passes, written without AI.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $f(x)$ | "f of x" | the output of function $f$ for input $x$ | §1 |
| $[a, b]$ | "closed interval a to b" | from $a$ to $b$, endpoints included | §2 |
| $(a, b)$ | "open interval a to b" | between $a$ and $b$, endpoints excluded | §2 |
| $\infty$ | "infinity" | keeps going forever (not a number) | §2 |
| $\mathbb{R}$ | "R" or "the reals" | all real numbers | §2 |
| $\in$ | "is in" | is a member of | §2 |
| $f(g(x))$ | "f of g of x" | do $g$ first, then $f$ | §3 |
| $f \circ g$ | "f composed with g" | same as $f(g(x))$ | §3 |
| $f^{-1}(x)$ | "f inverse of x" | the function that undoes $f$ | §4 |
| $e$ | "e" | $\approx 2.718$, the continuous-growth constant | §6 |
| $\to$ | "approaches" or "goes to" | gets closer and closer to | §7 |
| $\lvert x \rvert$ | "absolute value of x" | distance from 0 | §8 |
| $\max(a, b)$ | "max of a and b" | the larger one | §8 |
| $\text{ReLU}(x)$ | "ReLU of x" | $\max(0, x)$ | §8 |
| $\sigma(z)$ | "sigma of z" | the sigmoid function $\frac{1}{1 + e^{-z}}$ | §9 |
| $\mathbf{z}$ | "bold z" | a whole list of numbers | §10 |
| $K$ | "K" | number of options/items in the list | §10 |
| $T$ | "T" or "temperature" | softmax sharpness setting | §10 |

---

## Resources (only if stuck)

Use these for extra practice on one specific section. Don't watch them start to finish.

- [Khan Academy — Algebra 1](https://www.khanacademy.org/math/algebra): the "Functions" unit (§1–§2)
- [Khan Academy — Algebra 2](https://www.khanacademy.org/math/algebra2): composite functions, inverse functions, exponential and logarithmic functions (§3, §4, §6, §7)
