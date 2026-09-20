# 01 — Algebra

**Time: ~6 hours** (spread it over 2–3 days) · **You need: + − × ÷, fractions, negative numbers** · **Code lab: `math/01_algebra.py`**

## Before you start

This file assumes you know **only basic arithmetic**. Every symbol is explained the first time it appears. Nothing is skipped.

**How to read it:**

- Go **in order**. Each section uses the ones before it.
- When you see a worked example, **cover the solution and try it first**, even if you only get one line.
- Every symbol also has a "read it aloud as" note. Say it out loud. It sounds silly, but it makes notation stick.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.
- The **"Why ML cares"** boxes are for motivation only. You don't need them to understand the math, and nothing in them will be tested.

**What you'll be able to do by the end:**

- Read and simplify expressions with letters, exponents, and logarithms
- Solve equations and rearrange formulas
- Read and expand $\Sigma$ ("sum") notation
- Understand what a line's equation means, and find the lowest point of a U-shaped curve

---

## Contents

1. [Letters that stand for numbers](#1-letters-that-stand-for-numbers)
2. [Solving equations](#2-solving-equations)
3. [Exponents and roots](#3-exponents-and-roots)
4. [Logarithms](#4-logarithms)
5. [Subscripts and summation](#5-subscripts-and-summation)
6. [Graphs and lines](#6-graphs-and-lines)
7. [Squares, U-shaped curves, and the lowest point](#7-squares-u-shaped-curves-and-the-lowest-point)
8. [Code lab](#code-lab--math01_algebrapy)
9. [Check yourself](#check-yourself)

---

## 1. Letters that stand for numbers

### The problem

Say you pay ₱15 per jeepney ride. The total cost depends on how many rides you take:

- 2 rides → $15 \times 2 = 30$
- 5 rides → $15 \times 5 = 75$
- 10 rides → $15 \times 10 = 150$

Writing a new line for every possible number is tedious. Instead we write **one rule** that works for all of them:

$$
\text{cost} = 15 \times \text{rides}
$$

And since words get long, we use a short letter:

$$
c = 15 \times r
$$

### What a variable is

A **variable** is a letter that stands for a number. It's either a number we don't know yet, or a number that can change.

Think of it as a **labeled box**. The box $r$ can hold 2, or 5, or 10. It's the same idea as a variable in Python: `r = 5`.

### How multiplication is written

In algebra, the $\times$ sign is usually **left out**, because it looks too much like the letter $x$.

| You'll see | It means | Read it aloud as |
|---|---|---|
| $15r$ | $15 \times r$ | "fifteen r" |
| $3x$ | $3 \times x$ | "three x" |
| $xy$ | $x \times y$ | "x y" |
| $2(x + 1)$ | $2 \times (x + 1)$ | "two times the quantity x plus one" |
| $3 \cdot 4$ | $3 \times 4$ | "three times four" (the raised dot $\cdot$ also means multiply) |

So $c = 15r$ is the same rule as $c = 15 \times r$.

### How division is written

Division is usually written as a **fraction bar**:

$$
\frac{x}{2} \quad\text{means}\quad x \div 2
$$

Read it aloud as "x over two" or "x divided by two."

The fraction bar also **groups** things. Everything on top is calculated first, and everything on the bottom is calculated first:

$$
\frac{6 + 4}{2} = \frac{10}{2} = 5
$$

### Expression vs. equation

- An **expression** is a calculation with no equals sign: $3x + 2$. It's like a recipe that hasn't been cooked yet.
- An **equation** says two things are equal: $3x + 2 = 14$. It's a statement that can be true or false.

### Evaluating: plugging in a number

To **evaluate** an expression, replace the letter with a number and calculate.

**Example.** Evaluate $3x + 2$ when $x = 4$.

| Step | What we did |
|---|---|
| $3(4) + 2$ | Replaced $x$ with $4$. Put it in parentheses so the multiplication stays clear. |
| $12 + 2$ | Multiplied $3 \times 4$ |
| $14$ | Added |

**Always put the number in parentheses when you substitute**, especially negative numbers. That habit prevents most beginner mistakes (you'll see why in a moment).

### Order of operations

When a calculation has several operations, do them in this order:

1. **Parentheses** (and anything grouped by a fraction bar)
2. **Exponents** (the small raised numbers, like the 2 in $4^2$; explained fully in §3. For now, $4^2$ means $4 \times 4$)
3. **Multiply and divide**, left to right
4. **Add and subtract**, left to right

**Example.** $2 + 3 \cdot 4^2$

| Step | What we did |
|---|---|
| $2 + 3 \cdot 16$ | Exponent first: $4^2 = 4 \times 4 = 16$ |
| $2 + 48$ | Multiply: $3 \times 16 = 48$ |
| $50$ | Add |

If you'd gone left to right instead, you'd get $(2 + 3) \times 16 = 80$. That's wrong. Order matters.

### Negative numbers: the sign rules

| Operation | Result | Example |
|---|---|---|
| positive × positive | positive | $3 \times 2 = 6$ |
| positive × negative | negative | $3 \times (-2) = -6$ |
| negative × negative | **positive** | $(-3) \times (-2) = 6$ |

Division follows the same sign rules.

**Why is negative × negative positive?** Think of multiplying by $-1$ as **turning around** on the number line. $3 \times (-1) = -3$: you turned to face the negative side. Multiply by $-1$ again and you turn around again, back to facing positive. Two turns = facing the original direction.

### The trap: $-3^2$ vs. $(-3)^2$

- $(-3)^2 = (-3) \times (-3) = 9$ (the negative is inside the parentheses, so it gets squared)
- $-3^2 = -(3 \times 3) = -9$ (exponents happen before the minus sign is applied)

This is exactly why you should put substituted numbers in parentheses. If $x = -3$, then $x^2 = (-3)^2 = 9$.

### Distributing: multiplying into parentheses

$$
3(x + 2) = 3x + 6
$$

The 3 multiplies **everything** inside the parentheses.

**Why?** $3(x + 2)$ means "three copies of $(x + 2)$":

$$
(x + 2) + (x + 2) + (x + 2) = x + x + x + 2 + 2 + 2 = 3x + 6
$$

With negatives, the sign gets multiplied in too:

$$
-2(x - 5) = (-2)(x) + (-2)(-5) = -2x + 10
$$

### Combining like terms

$3x + 5x = 8x$. Why? 3 boxes of $x$ plus 5 boxes of $x$ is 8 boxes of $x$.

But $3x + 5$ **can't** be combined. One is "3 boxes of $x$" and the other is just the number 5. They're different kinds of things, like adding 3 apples to 5 pesos.

> **Why ML cares:** An ML model is basically a formula with letters in it. Some letters are the input (like the size of a house), and some are adjustable numbers the computer tunes. Everything in ML starts with being comfortable reading formulas like $3x + 2$.

### Exercises

**1.1.** Evaluate $5x - 3$ when $x = 2$, and when $x = -2$.

**1.2.** Calculate $10 - 2 \cdot 3^2$.

**1.3.** Evaluate $x^2 + 1$ when $x = -4$.

**1.4.** Expand $4(2x - 3)$, then expand $-(x + 7)$.

**1.5.** Simplify $2x + 3 + 5x - 1$.

<details>
<summary>Hint</summary>

1.2: exponent first, then multiply, then subtract.
1.4: $-(x + 7)$ is the same as $-1 \cdot (x + 7)$.
1.5: group the $x$ terms together and the plain numbers together.

</details>

<details>
<summary>Solutions</summary>

**1.1.** $5(2) - 3 = 7$. $5(-2) - 3 = -10 - 3 = -13$.

**1.2.** $10 - 2 \cdot 9 = 10 - 18 = -8$.

**1.3.** $(-4)^2 + 1 = 16 + 1 = 17$.

**1.4.** $8x - 12$. And $-x - 7$.

**1.5.** $(2x + 5x) + (3 - 1) = 7x + 2$.

</details>

---

## 2. Solving equations

### The problem

You took some jeepney rides at ₱15 each, plus one ₱5 candy, and spent ₱50 total. How many rides?

$$
15r + 5 = 50
$$

**Solving** means finding the value of $r$ that makes this equation true.

### The balance scale

Picture the equals sign as the center of a balance scale. Both sides weigh the same.

**If you do something to one side, you must do the exact same thing to the other side**, or the scale tips and the equation becomes false.

### Undoing operations

Every operation has an opposite that undoes it:

| Operation | Undo it with |
|---|---|
| add 5 | subtract 5 |
| subtract 5 | add 5 |
| multiply by 15 | divide by 15 |
| divide by 15 | multiply by 15 |

### Undo in reverse order

In $15r + 5$, two things happened to $r$: **first** it was multiplied by 15, **then** 5 was added.

To get $r$ alone, undo them in **reverse**: first undo the $+5$, then undo the $\times 15$. It's like unwrapping a gift: the last layer of wrapping comes off first.

**Example.** Solve $15r + 5 = 50$.

| Step | What we did | Why |
|---|---|---|
| $15r + 5 = 50$ | Start | |
| $15r = 45$ | Subtracted 5 from both sides | Undo the "+5" |
| $r = 3$ | Divided both sides by 15 | Undo the "×15" |

**Check:** $15(3) + 5 = 45 + 5 = 50$ ✓. Always plug your answer back in. It takes 10 seconds and catches most mistakes.

### When the letter is on both sides

**Example.** Solve $3(x - 2) = 2x + 5$.

| Step | What we did | Why |
|---|---|---|
| $3x - 6 = 2x + 5$ | Distributed the 3 | Get rid of the parentheses |
| $x - 6 = 5$ | Subtracted $2x$ from both sides | Collect all the $x$ terms on one side |
| $x = 11$ | Added 6 to both sides | Undo the "−6" |

**Check:** Left: $3(11 - 2) = 3 \cdot 9 = 27$. Right: $2(11) + 5 = 27$ ✓

### Rearranging a formula

Sometimes you don't have numbers. You want to **rewrite a formula** so a different letter is alone. The steps are exactly the same.

**Example.** $y = 3x + 2$. Rewrite it so $x$ is alone (this is called "solving for $x$").

| Step | What we did |
|---|---|
| $y = 3x + 2$ | Start |
| $y - 2 = 3x$ | Subtracted 2 from both sides |
| $\frac{y - 2}{3} = x$ | Divided both sides by 3 |

So $x = \frac{y - 2}{3}$. If someone tells you $y = 14$, then $x = \frac{12}{3} = 4$.

### Inequalities

An **inequality** compares two sides that aren't necessarily equal.

| Symbol | Read it aloud as | Example that's true |
|---|---|---|
| $<$ | "is less than" | $2 < 5$ |
| $>$ | "is greater than" | $5 > 2$ |
| $\le$ | "is less than or equal to" | $3 \le 3$ |
| $\ge$ | "is greater than or equal to" | $4 \ge 3$ |
| $\ne$ | "is not equal to" | $2 \ne 3$ |

**Memory trick:** the wide open side of $<$ or $>$ faces the bigger number.

The answer to an inequality is usually a **range** of numbers, not a single number. $x > 3$ means "any number bigger than 3."

### Solving inequalities: one extra rule

Solve them exactly like equations, **except**:

> **When you multiply or divide both sides by a negative number, flip the inequality sign.**

**Why?** Start with something true: $2 < 3$. Multiply both sides by $-1$: you get $-2$ and $-3$.

On the number line, $-2$ is to the **right** of $-3$, so $-2 > -3$. The order reversed. Multiplying by a negative mirrors the number line, so the bigger number becomes the smaller one.

**Example.** Solve $-2x + 4 > 10$.

| Step | What we did |
|---|---|
| $-2x > 6$ | Subtracted 4 from both sides (no flip, subtraction doesn't flip) |
| $x < -3$ | Divided both sides by $-2$ and **flipped** $>$ to $<$ |

**Check** with a number in the range, like $x = -4$: $-2(-4) + 4 = 12$, and $12 > 10$ ✓. Try one outside the range, like $x = 0$: $4 > 10$ is false ✓.

> **Why ML cares:** ML formulas get rearranged all the time. For example, you'll rewrite a formula to find which setting of a number makes a model's error smallest. The steps are exactly the ones in this section.

### Exercises

**2.1.** Solve $4x - 7 = 13$. Check your answer.

**2.2.** Solve $5(x + 1) = 3x + 11$.

**2.3.** Solve for $x$: $ax + b = c$. (Treat $a$, $b$, $c$ as numbers you don't know yet.) What goes wrong if $a = 0$?

**2.4.** Solve $3 - x \le 8$.

**2.5.** A phone plan costs ₱300 per month plus ₱2 per MB of data over the limit. Your bill was ₱420. Write an equation and solve it for the extra MB.

<details>
<summary>Hint</summary>

2.3: do the same steps as for $15r + 5 = 50$, just with letters.
2.4: to get $x$ alone you'll end up dividing by $-1$.
2.5: let $m$ be the extra MB. Total = fixed part + per-MB part.

</details>

<details>
<summary>Solutions</summary>

**2.1.** $4x = 20$, so $x = 5$. Check: $20 - 7 = 13$ ✓

**2.2.** $5x + 5 = 3x + 11$, then $2x + 5 = 11$, then $2x = 6$, so $x = 3$. Check: $5(4) = 20$ and $9 + 11 = 20$ ✓

**2.3.** $ax = c - b$, so $x = \frac{c - b}{a}$. If $a = 0$ you'd be dividing by zero, which isn't allowed. The equation becomes $b = c$, which is either always true or never true.

**2.4.** $-x \le 5$. Divide by $-1$ and flip: $x \ge -5$.

**2.5.** $300 + 2m = 420$, then $2m = 120$, so $m = 60$ MB.

</details>

---

## 3. Exponents and roots

### The problem

Multiplication is a shortcut for repeated adding: $2 + 2 + 2 = 3 \times 2$.

We also need a shortcut for **repeated multiplying**: $2 \times 2 \times 2 \times 2 \times 2$ is tedious to write, especially with 50 twos.

### Notation

$$
2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32
$$

- The big number (2) is the **base**: the number being multiplied.
- The small raised number (5) is the **exponent** or **power**: how many copies.
- Read $2^5$ aloud as "two to the power of five" or "two to the fifth."

Two special names:

- $x^2$ is "**x squared**," because a square with side $x$ has area $x \times x$.
- $x^3$ is "**x cubed**," because a cube with side $x$ has volume $x \times x \times x$.

**Trap:** $2^3$ is **not** $2 \times 3$. It's $2 \times 2 \times 2 = 8$.

### The exponent rules, discovered by writing things out

You don't need to memorize these. Each one comes from **writing out the multiplication and counting**.

**Rule 1: multiplying same base → add exponents.**

$$
2^3 \cdot 2^2 = (2 \cdot 2 \cdot 2) \cdot (2 \cdot 2) = 2^5
$$

Three 2s and then two more 2s makes five 2s. So $a^m \cdot a^n = a^{m+n}$.

**Rule 2: dividing same base → subtract exponents.**

$$
\frac{2^5}{2^2} = \frac{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}{2 \cdot 2} = 2 \cdot 2 \cdot 2 = 2^3
$$

Two 2s on the bottom cancel two 2s on top, leaving three. So $\frac{a^m}{a^n} = a^{m-n}$.

**Rule 3: power of a power → multiply exponents.**

$$
(2^2)^3 = 2^2 \cdot 2^2 \cdot 2^2 = (2 \cdot 2)(2 \cdot 2)(2 \cdot 2) = 2^6
$$

Three groups of two 2s makes six 2s. So $(a^m)^n = a^{m \cdot n}$.

**Rule 4: power of a product → each factor gets the power.**

$$
(2 \cdot 5)^2 = (2 \cdot 5)(2 \cdot 5) = 2 \cdot 2 \cdot 5 \cdot 5 = 2^2 \cdot 5^2
$$

So $(ab)^n = a^n b^n$. Check: $10^2 = 100$ and $4 \times 25 = 100$ ✓

### What does an exponent of 0 mean?

"Multiply zero copies of 2" doesn't make sense by itself. So look at the pattern:

| Power | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
|---|---|---|---|---|---|
| Value | 16 | 8 | 4 | 2 | **?** |

Every step to the right **divides by 2**. So the next value is $2 \div 2 = 1$.

$$
a^0 = 1 \quad (\text{for any } a \ne 0)
$$

Rule 2 agrees: $\frac{2^3}{2^3} = 1$, and also $= 2^{3-3} = 2^0$. So $2^0 = 1$.

### What does a negative exponent mean?

Keep the same pattern going, dividing by 2 each step:

| Power | $2^1$ | $2^0$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ |
|---|---|---|---|---|---|
| Value | 2 | 1 | $\frac{1}{2}$ | $\frac{1}{4}$ | $\frac{1}{8}$ |

$$
a^{-n} = \frac{1}{a^n}
$$

**A negative exponent does NOT make the number negative.** It means "one divided by." $2^{-3} = \frac{1}{8}$, which is small but positive.

### Powers of 10 and scientific notation

| $10^3$ | $10^2$ | $10^1$ | $10^0$ | $10^{-1}$ | $10^{-2}$ | $10^{-3}$ |
|---|---|---|---|---|---|---|
| 1000 | 100 | 10 | 1 | 0.1 | 0.01 | 0.001 |

The exponent tells you how many places to move the decimal point.

Very big or very small numbers are written as **scientific notation**:

- $3.2 \times 10^5 = 320{,}000$
- $1 \times 10^{-3} = 0.001$

In Python, this is written with an `e`: `3.2e5` means $3.2 \times 10^5$, and `1e-3` means $0.001$.

### Roots: undoing a square

The **square root** of 9 asks: "what number, multiplied by itself, gives 9?" The answer is 3.

$$
\sqrt{9} = 3 \quad\text{because}\quad 3^2 = 9
$$

Read $\sqrt{9}$ aloud as "the square root of nine." ($-3$ also squares to 9, but the $\sqrt{\ }$ symbol means the positive one.)

The **cube root** asks the same about cubes: $\sqrt[3]{8} = 2$ because $2^3 = 8$.

You can't take the square root of a negative number (with the numbers we're using). No number times itself gives a negative, because of the sign rules in §1.

### Fractional exponents

What should $9^{1/2}$ mean? Use Rule 3 to find out:

$$
\left(9^{1/2}\right)^2 = 9^{\frac{1}{2} \cdot 2} = 9^1 = 9
$$

So $9^{1/2}$ is a number that, squared, gives 9. That's exactly $\sqrt{9} = 3$.

$$
a^{1/2} = \sqrt{a}, \qquad a^{1/3} = \sqrt[3]{a}
$$

And $a^{m/n}$ means "take the $n$-th root, then raise to the $m$-th power":

$$
8^{2/3} = \left(8^{1/3}\right)^2 = 2^2 = 4
$$

### Summary

| Rule | Example |
|---|---|
| $a^m \cdot a^n = a^{m+n}$ | $x^3 \cdot x^4 = x^7$ |
| $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{x^5}{x^2} = x^3$ |
| $(a^m)^n = a^{mn}$ | $(x^2)^3 = x^6$ |
| $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| $a^0 = 1$ | $7^0 = 1$ |
| $a^{-n} = \frac{1}{a^n}$ | $x^{-2} = \frac{1}{x^2}$ |
| $a^{1/n} = \sqrt[n]{a}$ | $x^{1/2} = \sqrt{x}$ |

> **Why ML cares:** Tiny numbers like `1e-3` (0.001) show up constantly as settings, for example how big a step the computer takes when adjusting a model. Square roots show up whenever you measure a distance (§6).

### Exercises

**3.1.** Calculate $3^4$, $5^0$, and $4^{-2}$.

**3.2.** Simplify $x^4 \cdot x^3$ and $\frac{y^7}{y^2}$.

**3.3.** Simplify $(x^3)^2 \cdot x^{-4}$.

**3.4.** Calculate $25^{1/2}$ and $27^{2/3}$.

**3.5.** Write $\frac{1}{x^3}$ using a negative exponent, and $\sqrt{x}$ using a fractional exponent.

**3.6.** Write $0.00005$ in scientific notation and in Python's `e` notation.

<details>
<summary>Hint</summary>

3.3: do the power-of-a-power first, then multiply using Rule 1. Adding a negative exponent is subtracting.
3.4: $27^{1/3}$ asks "what number cubed is 27?"

</details>

<details>
<summary>Solutions</summary>

**3.1.** $81$, $1$, $\frac{1}{16}$.

**3.2.** $x^7$ and $y^5$.

**3.3.** $x^6 \cdot x^{-4} = x^{6 + (-4)} = x^2$.

**3.4.** $\sqrt{25} = 5$. $27^{1/3} = 3$, then $3^2 = 9$.

**3.5.** $x^{-3}$ and $x^{1/2}$.

**3.6.** $5 \times 10^{-5}$, `5e-5`.

</details>

---

## 4. Logarithms

### The problem

Exponents answer: "2 to the power 3 is **what**?" → $2^3 = 8$.

But sometimes you know the result and want the exponent: "2 to the power **what** is 8?"

That backwards question is what a **logarithm** answers.

### Notation

$$
\log_2(8) = 3 \quad\text{because}\quad 2^3 = 8
$$

- Read it aloud as "log base two of eight."
- The small number (2) is the **base**, the same base as in the exponent.
- The answer (3) is the **exponent** you were looking for.

**The definition, in both directions:**

$$
\log_b(x) = y \quad\text{means exactly the same as}\quad b^y = x
$$

Whenever a log confuses you, rewrite it as an exponent.

### Build intuition with a table

| Question | Exponent form | Answer |
|---|---|---|
| $\log_2(1)$ | $2^{?} = 1$ | $0$ |
| $\log_2(2)$ | $2^{?} = 2$ | $1$ |
| $\log_2(4)$ | $2^{?} = 4$ | $2$ |
| $\log_2(16)$ | $2^{?} = 16$ | $4$ |
| $\log_2\left(\frac{1}{2}\right)$ | $2^{?} = \frac{1}{2}$ | $-1$ |
| $\log_{10}(1000)$ | $10^{?} = 1000$ | $3$ |
| $\log_{10}(0.01)$ | $10^{?} = 0.01$ | $-2$ |

Two things to notice:

1. **Logs grow slowly.** $\log_{10}$ of one million is only 6. Logs squash huge ranges into small ones.
2. **The log of a number between 0 and 1 is negative**, because you need a negative exponent to make a small number.

### You can't take the log of zero or a negative number

$2^{\text{anything}}$ is always positive. No exponent turns 2 into 0 or into $-5$. So $\log_2(0)$ and $\log_2(-5)$ **don't exist**.

In Python, `np.log(0)` gives `-inf` (negative infinity), and `np.log(-5)` gives `nan` ("not a number"). If you ever see `nan` in a calculation, a log of zero or a negative number is a common culprit.

### The special number $e$ and the natural log

There's a special number called $e$:

$$
e \approx 2.71828\ldots
$$

(The symbol $\approx$ means "approximately equal to.")

Like $\pi$ (3.14159…), $e$ is a constant that shows up naturally all over math. You don't need to know *why* yet; that comes in the Functions and Calculus files. For now, just treat it as a number around 2.718.

A log with base $e$ is so common that it gets its own name and symbol:

$$
\ln(x) = \log_e(x)
$$

- Read $\ln$ aloud as "natural log" (or "L N").
- $\ln(1) = 0$ because $e^0 = 1$.
- $\ln(e) = 1$ because $e^1 = e$.
- **In Python, `np.log` and `math.log` are $\ln$** (base $e$), not base 10.
- In ML papers, when you see "$\log$" with no base written, it almost always means $\ln$.

### The log rules, discovered from exponent rules

Logs are just exponents in disguise, so every exponent rule becomes a log rule. Check each one with numbers first.

**Rule 1: log of a product → sum of logs.**

Numbers: $\log_2(8 \cdot 4) = \log_2(32) = 5$, and $\log_2(8) + \log_2(4) = 3 + 2 = 5$ ✓

Why: $8 = 2^3$ and $4 = 2^2$, so $8 \cdot 4 = 2^3 \cdot 2^2 = 2^{3+2}$ (exponent Rule 1). The exponent is $3 + 2$, and the log finds the exponent.

$$
\log(a \cdot b) = \log(a) + \log(b)
$$

**Rule 2: log of a division → difference of logs.**

Numbers: $\log_2\left(\frac{16}{4}\right) = \log_2(4) = 2$, and $\log_2(16) - \log_2(4) = 4 - 2 = 2$ ✓

$$
\log\left(\frac{a}{b}\right) = \log(a) - \log(b)
$$

**Rule 3: log of a power → multiply.**

Numbers: $\log_2(8^2) = \log_2(64) = 6$, and $2 \cdot \log_2(8) = 2 \cdot 3 = 6$ ✓

Why: $8^2 = 8 \cdot 8$, so by Rule 1 its log is $\log_2(8) + \log_2(8) = 2\log_2(8)$.

$$
\log(a^k) = k \cdot \log(a)
$$

**Rule 4: logs and exponents undo each other.**

$$
\log_2(2^5) = 5, \qquad 2^{\log_2(8)} = 8, \qquad \ln(e^x) = x, \qquad e^{\ln(x)} = x
$$

### The rule that does NOT exist

$$
\log(a + b) \ne \log(a) + \log(b)
$$

Check: $\log_2(4 + 4) = \log_2(8) = 3$, but $\log_2(4) + \log_2(4) = 2 + 2 = 4$. Not equal. There's no simple rule for the log of a sum.

### Solving equations where the unknown is in the exponent

**Example.** Solve $2^x = 20$.

$x$ is stuck up in the exponent. Taking the log of both sides brings it down, using Rule 3.

| Step | What we did |
|---|---|
| $2^x = 20$ | Start |
| $\ln(2^x) = \ln(20)$ | Took $\ln$ of both sides (same thing to both sides keeps the balance) |
| $x \cdot \ln(2) = \ln(20)$ | Rule 3 brought the exponent down |
| $x = \frac{\ln(20)}{\ln(2)}$ | Divided both sides by $\ln(2)$ |
| $x \approx \frac{2.996}{0.693} \approx 4.32$ | Calculator |

**Check:** $2^4 = 16$ and $2^5 = 32$, so the answer should be between 4 and 5 ✓

**Example.** Solve $e^{2x} = 5$.

| Step | What we did |
|---|---|
| $\ln(e^{2x}) = \ln(5)$ | Took $\ln$ of both sides |
| $2x = \ln(5)$ | Rule 4: $\ln$ undoes $e$ |
| $x = \frac{\ln(5)}{2} \approx \frac{1.609}{2} \approx 0.805$ | Divided by 2 |

> **Why ML cares:**
>
> A **probability** is a number from 0 to 1 saying how likely something is (0 = impossible, 1 = certain, 0.5 = coin flip). When you want the chance of many independent things *all* happening, you **multiply** their probabilities.
>
> Multiply 1000 probabilities of 0.01 and you get $0.01^{1000} = 10^{-2000}$. Computers can't store numbers smaller than about $10^{-308}$, so it silently becomes **0**. That's called **underflow**.
>
> Take logs instead (Rule 3): $\ln(0.01^{1000}) = 1000 \cdot \ln(0.01) \approx 1000 \times (-4.605) = -4605$. A normal number, no problem.
>
> And since a bigger number always has a bigger log, comparing logs gives the same winner as comparing the original numbers. That's why ML formulas are full of $\ln$.

### Exercises

**4.1.** Rewrite each as an exponent question, then answer: $\log_3(9)$, $\log_5(125)$, $\log_{10}(0.1)$.

**4.2.** Use the log rules to write $\ln(x^3 y)$ as a sum of simple logs.

**4.3.** Write $\ln\left(\frac{a^2}{b}\right)$ as simple logs.

**4.4.** Solve $3^x = 50$. Between which two whole numbers should the answer be? (Use a calculator for the final value.)

**4.5.** Is $\log_{10}(100 + 100) = \log_{10}(100) + \log_{10}(100)$? Calculate both sides.

**4.6.** Solve $e^{x} = 10$.

<details>
<summary>Hint</summary>

4.2: first split the product (Rule 1), then handle the power (Rule 3).
4.4: $3^3 = 27$ and $3^4 = 81$.
4.5: $\log_{10}(200)$ is a bit more than 2.

</details>

<details>
<summary>Solutions</summary>

**4.1.** $3^{?} = 9 \Rightarrow 2$. $5^{?} = 125 \Rightarrow 3$. $10^{?} = 0.1 \Rightarrow -1$.

**4.2.** $\ln(x^3) + \ln(y) = 3\ln(x) + \ln(y)$.

**4.3.** $2\ln(a) - \ln(b)$.

**4.4.** Between 3 and 4. $x = \frac{\ln 50}{\ln 3} \approx \frac{3.912}{1.099} \approx 3.56$.

**4.5.** No. Left: $\log_{10}(200) \approx 2.301$. Right: $2 + 2 = 4$.

**4.6.** $x = \ln(10) \approx 2.303$.

</details>

---

## 5. Subscripts and summation

### The problem

Suppose you record your daily steps for 5 days: 4000, 6500, 3000, 8000, 5500.

To talk about "the steps on day 3" without writing the actual number, and to write "add up all the days" in a formula that works for **any** number of days, we need two new tools: **subscripts** and **summation**.

### Subscripts: numbering a list

We give the whole list one name, $x$, and use a small lowered number to say **which item**:

| Symbol | Read it aloud as | Value |
|---|---|---|
| $x_1$ | "x sub one" or "x one" | 4000 |
| $x_2$ | "x sub two" | 6500 |
| $x_3$ | "x sub three" | 3000 |
| $x_4$ | "x sub four" | 8000 |
| $x_5$ | "x sub five" | 5500 |

**Subscripts are labels, not math.** $x_2$ does NOT mean $x \times 2$ or $x^2$. It just means "item number 2."

This is exactly like a Python list, with one difference: **math usually starts counting at 1**, and Python starts at 0. So $x_1$ is `x[0]`.

Two more letters you'll see constantly:

- $n$ = **how many** items there are. Here, $n = 5$.
- $x_i$ = "**the $i$-th item**," read aloud as "x sub i." Here $i$ is a counter that can be 1, 2, 3, and so on. It's like the `i` in a `for` loop.

### Summation: the $\Sigma$ symbol

$\Sigma$ is the Greek capital letter **sigma**, the Greek "S," for **S**um. It means "add up a bunch of things."

Here's how to read every part:

$$
\sum_{i=1}^{5} x_i
$$

| Part | Where it is | What it means |
|---|---|---|
| $i = 1$ | below the $\Sigma$ | start the counter $i$ at 1 |
| $5$ | above the $\Sigma$ | stop when $i$ reaches 5 |
| $x_i$ | to the right | the thing to add for each value of $i$ |

Read aloud as: "the sum of x sub i, for i from 1 to 5."

It means:

$$
\sum_{i=1}^{5} x_i = x_1 + x_2 + x_3 + x_4 + x_5 = 4000 + 6500 + 3000 + 8000 + 5500 = 27000
$$

### $\Sigma$ is a `for` loop

$$
\sum_{i=1}^{n} x_i
$$

is exactly this Python code:

```python
total = 0
for i in range(n):      # Python counts 0..n-1; math counts 1..n
    total += x[i]
```

If a $\Sigma$ ever looks scary, rewrite it as a loop in your head.

### Expanding a sum step by step

The expression to the right of $\Sigma$ can be a formula in $i$, not just $x_i$.

**Example.** $\displaystyle\sum_{i=1}^{4} (2i + 1)$

| $i$ | $2i + 1$ |
|---|---|
| 1 | $2(1) + 1 = 3$ |
| 2 | $2(2) + 1 = 5$ |
| 3 | $2(3) + 1 = 7$ |
| 4 | $2(4) + 1 = 9$ |
| **Total** | $3 + 5 + 7 + 9 = 24$ |

### Building a real formula: the average

"The average" means: add everything up, then divide by how many there are.

In words → in symbols, one piece at a time:

| In words | In symbols |
|---|---|
| add up all the values | $\sum_{i=1}^{n} x_i$ |
| divide by how many | $\frac{1}{n} \cdot \sum_{i=1}^{n} x_i$ |

(Multiplying by $\frac{1}{n}$ is the same as dividing by $n$.)

The average is written $\bar{x}$, read aloud as "**x bar**":

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

**Example.** Steps: $\bar{x} = \frac{1}{5} \cdot 27000 = 5400$.

### Three rules for sums (each checked with numbers)

Use $x = [1, 2, 3]$ for the checks.

**Rule A: a constant multiplier can move outside.**

$$
\sum_{i=1}^{n} c \cdot x_i = c \sum_{i=1}^{n} x_i
$$

Check with $c = 10$: $10 + 20 + 30 = 60$, and $10 \times (1 + 2 + 3) = 60$ ✓

**Rule B: a sum of two things splits into two sums.**

$$
\sum_{i=1}^{n} (x_i + y_i) = \sum_{i=1}^{n} x_i + \sum_{i=1}^{n} y_i
$$

(Adding in a different order gives the same total.)

**Rule C: adding the same number $n$ times is multiplication.**

$$
\sum_{i=1}^{n} c = n \cdot c
$$

Check: $\sum_{i=1}^{3} 5 = 5 + 5 + 5 = 15 = 3 \times 5$ ✓

### Watch where the exponent sits

$$
\sum x_i^2 \quad\ne\quad \left(\sum x_i\right)^2
$$

- $\sum x_i^2$: square each item **first**, then add. $1 + 4 + 9 = 14$
- $\left(\sum x_i\right)^2$: add first, then square the total. $(1 + 2 + 3)^2 = 36$

### Product notation $\Pi$ — *Optional*

$\Pi$ is the Greek capital **pi** (the Greek "P," for **P**roduct). It works exactly like $\Sigma$, but **multiplies** instead of adding:

$$
\prod_{i=1}^{3} x_i = x_1 \cdot x_2 \cdot x_3
$$

Log Rule 1 turns a product into a sum: $\ln\left(\prod x_i\right) = \sum \ln(x_i)$. That's the underflow fix from §4, written in this notation.

> **Why ML cares:**
>
> A **model** makes a **prediction** (a guess), which we compare with the **true value**. The difference is the **error**.
>
> To judge a model on many examples, we square each error (so negatives don't cancel out positives), then average. Say the true values are $y = [3, 5]$ and the model guessed $\hat{y} = [2, 7]$ (read $\hat{y}$ as "y hat," meaning "the guess for y"):
>
> $$\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \frac{(3-2)^2 + (5-7)^2}{2} = \frac{1 + 4}{2} = 2.5$$
>
> That formula is called **mean squared error**, and you just read it using only this section.

### Exercises

**5.1.** $x = [2, 4, 9]$. What are $n$, $x_1$, and $x_3$? What's $x_2$ in Python indexing?

**5.2.** Expand and calculate $\displaystyle\sum_{i=1}^{3} i^2$.

**5.3.** For $x = [2, 4, 9]$, calculate $\bar{x}$ using the formula, writing out each step.

**5.4.** Translate this Python code into $\Sigma$ notation:

```python
total = 0
for i in range(n):
    total += w[i] * x[i]
```

**5.5.** For $x = [1, 3, 5]$: calculate $\sum x_i^2$ and $\left(\sum x_i\right)^2$.

**5.6.** *(Challenge)* Show that $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$ for any list of numbers. First test it on $x = [2, 4, 9]$. Then use Rules B and C, plus the formula for $\bar{x}$.

<details>
<summary>Hint</summary>

5.4: what gets added in each loop step? Both lists use the same counter.
5.6: Rule B splits it into $\sum x_i - \sum \bar{x}$. $\bar{x}$ is a single fixed number, so use Rule C on the second part. Then, from the formula, $\sum x_i = n \cdot \bar{x}$.

</details>

<details>
<summary>Solutions</summary>

**5.1.** $n = 3$, $x_1 = 2$, $x_3 = 9$. $x_2$ (which is 4) is `x[1]` in Python.

**5.2.** $1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.

**5.3.** $\sum x_i = 2 + 4 + 9 = 15$, then $\bar{x} = \frac{1}{3} \cdot 15 = 5$.

**5.4.** $\displaystyle\sum_{i=1}^{n} w_i x_i$

**5.5.** $1 + 9 + 25 = 35$. $(1 + 3 + 5)^2 = 81$.

**5.6.** Test: $\bar{x} = 5$, and $(2 - 5) + (4 - 5) + (9 - 5) = -3 - 1 + 4 = 0$ ✓

General: $\sum (x_i - \bar{x}) = \sum x_i - \sum \bar{x}$ (Rule B) $= \sum x_i - n\bar{x}$ (Rule C). Since $\bar{x} = \frac{1}{n}\sum x_i$, multiplying both sides by $n$ gives $\sum x_i = n\bar{x}$. So the result is $n\bar{x} - n\bar{x} = 0$.

</details>

---

## 6. Graphs and lines

### The problem

A formula like $y = 2x + 1$ gives a different $y$ for every $x$. A **graph** lets you see all of those pairs at once, as a picture.

### The coordinate plane

Take two number lines and cross them at a right angle:

- The horizontal one is the **x-axis**.
- The vertical one is the **y-axis**.
- They cross at the **origin**, the point $(0, 0)$.

A **point** is written $(x, y)$: "go $x$ steps right, then $y$ steps up."

- $(2, 3)$: right 2, up 3
- $(-1, 4)$: **left** 1 (negative means left), up 4
- $(3, -2)$: right 3, **down** 2 (negative means down)

The order matters: $(2, 3)$ and $(3, 2)$ are different points. $x$ always comes first.

### What "the graph of an equation" means

The graph of $y = 2x + 1$ is **every point $(x, y)$ that makes the equation true**.

Build a table by choosing some $x$ values and calculating $y$:

| $x$ | $y = 2x + 1$ | Point |
|---|---|---|
| 0 | 1 | $(0, 1)$ |
| 1 | 3 | $(1, 3)$ |
| 2 | 5 | $(2, 5)$ |
| 3 | 7 | $(3, 7)$ |

Plot those points and they fall on a **straight line**. That's why equations like this are called **linear**.

### Slope: how steep a line is

Look at the table again. **Every time $x$ goes up by 1, $y$ goes up by 2.** That "2" is the **slope**.

$$
\text{slope} = \frac{\text{rise}}{\text{run}} = \frac{\text{how much } y \text{ changes}}{\text{how much } x \text{ changes}}
$$

Slope is usually called $m$.

**Formula from two points.** Given two points $(x_1, y_1)$ and $(x_2, y_2)$ (the subscripts just mean "point 1" and "point 2," like in §5):

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

**Example.** From $(1, 3)$ to $(3, 7)$: $m = \frac{7 - 3}{3 - 1} = \frac{4}{2} = 2$ ✓

What slope values look like:

| Slope | The line… |
|---|---|
| positive (e.g. 2) | goes **up** as you move right |
| negative (e.g. −2) | goes **down** as you move right |
| 0 | is flat (horizontal) |
| bigger number, like 10 vs 2 | is steeper |

### Intercept: where the line crosses the y-axis

The **y-intercept** is the $y$ value when $x = 0$. From the table, $y = 1$ when $x = 0$. The intercept is usually called $b$.

### The form $y = mx + b$

Every non-vertical straight line can be written as:

$$
y = mx + b
$$

- $m$ = slope (how much $y$ changes when $x$ goes up by 1)
- $b$ = intercept (the value of $y$ when $x = 0$)

In $y = 2x + 1$: slope $m = 2$, intercept $b = 1$. Both match the table.

### Walk-through: $y = 3x + 2$

Given $y = 3x + 2$, you should be able to say all of this right away:

| Question | Answer |
|---|---|
| What is $x$? | The input: the number you choose |
| What is $y$? | The output: what the formula gives back |
| Slope? | 3: every +1 in $x$ adds +3 to $y$ |
| Intercept? | 2: when $x = 0$, $y = 2$ |
| How does changing $x$ affect $y$? | Increase $x$ by 5 → $y$ increases by $3 \times 5 = 15$ |
| How do you solve for $x$? | $x = \frac{y - 2}{3}$ (from §2) |
| What does the graph look like? | A straight line crossing the y-axis at 2, rising steeply to the right |

### Finding a line's equation from two points

**Example.** Find the line through $(1, 3)$ and $(3, 7)$.

| Step | What we did |
|---|---|
| $m = \frac{7 - 3}{3 - 1} = 2$ | Slope formula |
| $y = 2x + b$ | Put the slope into $y = mx + b$. $b$ is still unknown. |
| $3 = 2(1) + b$ | Plugged in the point $(1, 3)$, since it must be on the line |
| $b = 1$ | Solved: subtracted 2 from both sides |
| $y = 2x + 1$ | Final answer |

**Check** with the other point: $2(3) + 1 = 7$ ✓

### Distance between two points

**Pythagoras' theorem:** in a right triangle (one corner is a square 90° corner), if the two short sides are $a$ and $b$ and the long side is $c$:

$$
a^2 + b^2 = c^2
$$

Example: sides 3 and 4 give $9 + 16 = 25 = c^2$, so $c = \sqrt{25} = 5$.

To find the distance between two points, draw a right triangle between them: the horizontal side is the change in $x$, the vertical side is the change in $y$, and the distance is the long side.

$$
\text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

**Example.** From $(1, 2)$ to $(4, 6)$: horizontal side $= 3$, vertical side $= 4$, so the distance is $\sqrt{9 + 16} = 5$.

> **Why ML cares:**
>
> The simplest ML model is a line: $\text{prediction} = m \cdot \text{input} + b$. For example, predicting a road project's cost from its length in kilometers.
>
> "Training" the model means the computer finds the $m$ and $b$ that fit past data best. The distance formula is also how ML measures how "far apart" two things are, like two similar hand poses or two similar documents.

### Exercises

**6.1.** Make a table for $y = -x + 4$ with $x = 0, 1, 2, 3$. What's the slope? The intercept? Does the line go up or down?

**6.2.** Find the slope between $(2, 5)$ and $(6, 3)$.

**6.3.** Find the equation of the line through $(0, -1)$ and $(2, 5)$.

**6.4.** For $y = 4x - 3$: what's $y$ when $x = 2$? If $x$ increases by 10, how much does $y$ change?

**6.5.** Find the distance between $(-1, 1)$ and $(5, 9)$.

<details>
<summary>Hint</summary>

6.3: one of the points has $x = 0$. What does that tell you about $b$ immediately?
6.5: horizontal change $5 - (-1)$, vertical change $9 - 1$.

</details>

<details>
<summary>Solutions</summary>

**6.1.** Points $(0, 4), (1, 3), (2, 2), (3, 1)$. Slope $-1$, intercept $4$, goes down.

**6.2.** $\frac{3 - 5}{6 - 2} = \frac{-2}{4} = -\frac{1}{2}$.

**6.3.** $b = -1$ (the point where $x = 0$). $m = \frac{5 - (-1)}{2 - 0} = 3$. So $y = 3x - 1$.

**6.4.** $y = 5$. Changes by $4 \times 10 = 40$.

**6.5.** $\sqrt{6^2 + 8^2} = \sqrt{100} = 10$.

</details>

---

## 7. Squares, U-shaped curves, and the lowest point

### The problem

Lines are straight. But lots of important formulas make **curves**, and often we want to find a curve's **lowest point**. This section shows the simplest such curve and how to find its bottom.

### The graph of $y = x^2$

| $x$ | −3 | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| $y = x^2$ | 9 | 4 | 1 | 0 | 1 | 4 | 9 |

Plot these points and you get a **U shape**, called a **parabola**.

Two key facts:

1. **A square is never negative.** Positive × positive is positive, and negative × negative is also positive (§1). So $x^2 \ge 0$ always.
2. The **lowest point** is at $x = 0$, where $y = 0$.

### Moving the U shape

What about $y = (x - 3)^2 + 1$?

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $(x - 3)^2$ | 4 | 1 | **0** | 1 | 4 |
| $y = (x - 3)^2 + 1$ | 5 | 2 | **1** | 2 | 5 |

- The square $(x - 3)^2$ is smallest (zero) when the inside is zero, which happens at $x = 3$.
- The $+1$ lifts the whole curve up by 1.
- So the lowest point is at $x = 3$, with $y = 1$.

**You found the lowest point just by reasoning** that a square can't go below zero. No formula needed.

### Expanding a square

Often the formula isn't written as a neat square. It's "expanded." To go from one form to the other, you need:

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

**Why?** $(a + b)^2 = (a + b)(a + b)$. Distribute (from §1) each part of the first bracket over the second:

| Step | What we did |
|---|---|
| $a(a + b) + b(a + b)$ | Distributed the first bracket |
| $a^2 + ab + ba + b^2$ | Distributed again |
| $a^2 + 2ab + b^2$ | $ab$ and $ba$ are the same thing, so they combine |

**Trap:** $(a + b)^2 \ne a^2 + b^2$. Check: $(1 + 2)^2 = 9$, but $1^2 + 2^2 = 5$.

**Example.** Expand $(x - 3)^2$:

$$
(x - 3)^2 = x^2 + 2(x)(-3) + (-3)^2 = x^2 - 6x + 9
$$

So $(x - 3)^2 + 1 = x^2 - 6x + 10$. Same curve, different way of writing it.

### The lowest point of any U shape

A formula like $ax^2 + bx + c$ (where $a$, $b$, $c$ are numbers) always makes a parabola.

- If $a > 0$, it opens **upward** (a U), so it has a lowest point.
- The lowest point is at:

$$
x = \frac{-b}{2a}
$$

**Check with the curve we already know:** $x^2 - 6x + 10$ has $a = 1$, $b = -6$, $c = 10$. So $x = \frac{-(-6)}{2 \cdot 1} = \frac{6}{2} = 3$ ✓. That matches the table.

For now, take this formula as a **tool you've verified with an example**. In the Calculus file you'll see exactly *why* it works.

> **Why ML cares:**
>
> Say a model predicts $\text{prediction} = w \cdot \text{input}$, where $w$ is the adjustable number. You have one example: input $= 2$, true answer $= 6$. The squared error is:
>
> $$\text{error}(w) = (6 - 2w)^2$$
>
> Try some values of $w$:
>
> | $w$ | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|
> | error | 16 | 4 | **0** | 4 | 16 |
>
> It's a U shape, and the best $w$ is at the **bottom**: $w = 3$ (and indeed $3 \times 2 = 6$).
>
> **Training a model = finding the bottom of an error curve.** With millions of adjustable numbers you can't make a table, so Calculus gives you a way to walk downhill instead.

### Exercises

**7.1.** Make a table for $y = (x + 2)^2$ with $x = -4, -3, -2, -1, 0$. Where's the lowest point?

**7.2.** Without a table, find the lowest point of $y = (x - 5)^2 + 7$. Explain your reasoning in one sentence.

**7.3.** Expand $(x + 4)^2$ and $(2x - 1)^2$.

**7.4.** Find the lowest point of $y = x^2 - 8x + 3$ using $x = \frac{-b}{2a}$. Then find the $y$ value there.

**7.5.** Two examples: (input 1, answer 2) and (input 2, answer 5). The model is $\text{prediction} = w \cdot \text{input}$. The total squared error is:

$$
\text{error}(w) = (2 - w)^2 + (5 - 2w)^2
$$

Expand it into the form $aw^2 + bw + c$, then find the best $w$.

**7.6.** *(Optional challenge)* Solve $x^2 - 5x + 6 = 0$ by finding two numbers that multiply to 6 and add to $-5$.

<details>
<summary>Hint</summary>

7.2: when is $(x - 5)^2$ equal to zero?
7.5: expand each square separately using $(a + b)^2 = a^2 + 2ab + b^2$, then combine like terms.
7.6: the numbers are both negative. Then $x^2 - 5x + 6 = (x - \_)(x - \_)$.

</details>

<details>
<summary>Solutions</summary>

**7.1.** $y$ values: $4, 1, 0, 1, 4$. Lowest point at $x = -2$, $y = 0$.

**7.2.** $x = 5$, $y = 7$. The square is never negative and equals zero at $x = 5$, so the smallest $y$ is $0 + 7$.

**7.3.** $x^2 + 8x + 16$. And $(2x)^2 + 2(2x)(-1) + (-1)^2 = 4x^2 - 4x + 1$.

**7.4.** $a = 1$, $b = -8$, so $x = \frac{8}{2} = 4$. Then $y = 16 - 32 + 3 = -13$.

**7.5.** $(2 - w)^2 = 4 - 4w + w^2$ and $(5 - 2w)^2 = 25 - 20w + 4w^2$. Total: $5w^2 - 24w + 29$. Best $w = \frac{24}{2 \cdot 5} = 2.4$.

**7.6.** $-2$ and $-3$, so $(x - 2)(x - 3) = 0$. That means $x = 2$ or $x = 3$ (if a product is zero, one of the factors must be zero).

</details>

---

## Code lab — `math/01_algebra.py`

### What you're doing and why

You'll write the formulas from this file as Python functions. Writing $\Sigma$ as a loop makes it concrete, and seeing underflow happen on your own screen makes §4 real.

**Rules:** no AI, no autocomplete, no copying. It's fine to be slow.

### Python you need

- A `for` loop over a list: `for value in values:`
- `len(values)` gives $n$
- `math.log(p)` is $\ln(p)$
- `x ** 2` is $x^2$ in Python (not `x ^ 2`, which means something else)

### The tasks

Create `math/01_algebra.py`, and fill in each function using **a plain `for` loop**:

```python
import math
import numpy as np

def mean(values):
    """The average: (1/n) * sum of x_i.  (§5)"""
    ...

def mean_squared_error(true_values, guesses):
    """(1/n) * sum of (y_i - yhat_i)^2.  (§5, Why ML cares box)
    Hint: zip(true_values, guesses) gives you pairs."""
    ...

def sum_of_logs(probabilities):
    """sum of ln(p_i).  (§4 and §5)"""
    ...

def lowest_point(a, b):
    """x-position of the lowest point of a*x^2 + b*x + c.  (§7)"""
    ...

if __name__ == "__main__":
    assert mean([2, 4, 9]) == 5
    assert mean_squared_error([3, 5], [2, 7]) == 2.5
    assert abs(sum_of_logs([0.01] * 1000) - (-4605.17)) < 0.01
    assert lowest_point(1, -6) == 3
    assert lowest_point(5, -24) == 2.4

    # See underflow with your own eyes (§4):
    probs = np.full(1000, 0.01)          # a list of 1000 copies of 0.01
    print("multiply them all:", np.prod(probs))
    print("add their logs:  ", np.sum(np.log(probs)))

    print("all checks passed")
```

Run it with `python math/01_algebra.py`. Before you run it, **write down what you expect the two printed lines to show**. Then compare.

### Then, one more step

Below each loop version, write a one-line NumPy version and check that it gives the same answer:

- `np.mean(values)`
- `np.mean((np.array(true_values) - np.array(guesses)) ** 2)`
- `np.sum(np.log(probabilities))`

<details>
<summary>Reference solution (only after your own attempt)</summary>

```python
def mean(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)

def mean_squared_error(true_values, guesses):
    total = 0
    for y, y_hat in zip(true_values, guesses):
        total += (y - y_hat) ** 2
    return total / len(true_values)

def sum_of_logs(probabilities):
    total = 0
    for p in probabilities:
        total += math.log(p)
    return total

def lowest_point(a, b):
    return -b / (2 * a)
```

Expected output: the product prints `0.0` (underflow), and the sum of logs prints about `-4605.17`.

</details>

---

## Common mistakes

Each one comes with a number check, so you can see it's wrong instead of just being told.

| Mistake | Why it's wrong |
|---|---|
| $-3^2 = 9$ | Exponent happens first: $-3^2 = -9$. Only $(-3)^2 = 9$. |
| $2^3 = 6$ | $2^3 = 2 \times 2 \times 2 = 8$ |
| $2^{-1} = -2$ | A negative exponent means "one over": $2^{-1} = \frac{1}{2}$ |
| $(a + b)^2 = a^2 + b^2$ | $(1 + 2)^2 = 9$, but $1 + 4 = 5$ |
| $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$ | $\sqrt{9 + 16} = 5$, but $3 + 4 = 7$ |
| $\log(a + b) = \log a + \log b$ | $\log_2(4 + 4) = 3$, but $2 + 2 = 4$ |
| $\sum x_i^2 = \left(\sum x_i\right)^2$ | For $[1, 2, 3]$: $14 \ne 36$ |
| $x_2$ means $x \times 2$ | A subscript is a label: "item number 2" |
| Forgetting to flip $<$ when dividing by a negative | $2 < 3$, but $-2 > -3$ |
| `x ^ 2` in Python | In Python, `^` is not a power. Use `x ** 2`. |

---

## Check yourself

Do this **after** working through the file. Closed book, no calculator except for Q9, 15 minutes.

1. Calculate $\frac{2}{3} \div \frac{4}{9}$.
2. Simplify $\dfrac{x^5 \cdot x^{-2}}{x^{1/2}}$.
3. Calculate $\log_2(64)$ and $\ln(e^3)$.
4. Write $\log\left(\dfrac{a^2 b}{c}\right)$ as simple logs added and subtracted.
5. Solve $3(x - 2) = 2x + 5$.
6. Solve $-2x + 4 > 10$.
7. Calculate $\displaystyle\sum_{i=1}^{4} (2i + 1)$.
8. Find the equation of the line through $(1, 3)$ and $(3, 7)$.
9. Solve $e^{2x} = 5$.
10. Find the lowest point of $y = 2x^2 - 12x + 5$.

<details>
<summary>Answers</summary>

**1.** $\frac{2}{3} \div \frac{4}{9}$ → §1

Dividing by a fraction means multiplying by its flip (its reciprocal):

$$\frac{2}{3} \div \frac{4}{9} = \frac{2}{3} \cdot \frac{9}{4} = \frac{2 \cdot 9}{3 \cdot 4} = \frac{18}{12} = \frac{3}{2}$$

*Why the flip works:* "$\frac{2}{3} \div \frac{4}{9}$" asks *how many $\frac{4}{9}$ fit inside $\frac{2}{3}$*. Since $\frac{4}{9}$ is smaller than $\frac{2}{3}$, the answer must be bigger than 1, and $\frac{3}{2} = 1.5$ is. Sanity check: $\frac{4}{9} \cdot \frac{3}{2} = \frac{12}{18} = \frac{2}{3}$ ✓

---

**2.** $\dfrac{x^5 \cdot x^{-2}}{x^{1/2}}$ → §3

*Step 1 — combine the top.* Multiplying powers of the same base adds the exponents:

$$x^5 \cdot x^{-2} = x^{5 + (-2)} = x^3$$

*Step 2 — handle the division.* Dividing powers of the same base subtracts the exponents:

$$\frac{x^3}{x^{1/2}} = x^{3 - 1/2}$$

*Step 3 — do the fraction subtraction.* Rewrite $3$ with denominator 2, because you can only subtract halves from halves:

$$3 - \frac{1}{2} = \frac{6}{2} - \frac{1}{2} = \frac{5}{2}$$

So the answer is $x^{5/2}$.

*Common trap:* moving $x^{1/2}$ to the top as $x^{-1}$. Crossing the fraction bar **negates** the exponent, it doesn't replace it, so $\frac{1}{x^{1/2}} = x^{-1/2}$. Check with $x = 4$: original is $\frac{4^5 \cdot 4^{-2}}{4^{1/2}} = \frac{64}{2} = 32$, and $4^{5/2} = (\sqrt{4})^5 = 2^5 = 32$ ✓

---

**3.** $\log_2(64)$ and $\ln(e^3)$ → §4

A logarithm asks: *what exponent turns the base into this number?*

$\log_2(64)$ asks "2 to the what gives 64?" Count up: $2^1 = 2$, $2^2 = 4$, $2^3 = 8$, $2^4 = 16$, $2^5 = 32$, $2^6 = 64$. So $\log_2(64) = 6$.

$\ln(e^3)$ asks "$e$ to the what gives $e^3$?" The exponent is written right there: $3$. In general $\ln(e^k) = k$, because $\ln$ and $e^x$ undo each other.

---

**4.** $\log\left(\dfrac{a^2 b}{c}\right)$ → §4

Apply one rule at a time.

*Step 1 — the division rule* ($\log\frac{M}{N} = \log M - \log N$):

$$\log\left(\frac{a^2 b}{c}\right) = \log(a^2 b) - \log c$$

*Step 2 — the product rule* ($\log(MN) = \log M + \log N$):

$$= \log(a^2) + \log b - \log c$$

*Step 3 — the power rule* ($\log(M^k) = k\log M$):

$$= 2\log a + \log b - \log c$$

*Note the signs:* everything on top of the fraction ends up added, everything on the bottom ends up subtracted.

---

**5.** $3(x - 2) = 2x + 5$ → §2

*Step 1 — expand the bracket.* Multiply the $3$ into both terms:

$$3x - 6 = 2x + 5$$

*Step 2 — collect the $x$ terms on one side.* Subtract $2x$ from **both** sides:

$$x - 6 = 5$$

*Step 3 — isolate $x$.* Add $6$ to both sides:

$$x = 11$$

*Check* (always substitute back into the **original**): left side $3(11 - 2) = 3 \cdot 9 = 27$; right side $2(11) + 5 = 27$ ✓

---

**6.** $-2x + 4 > 10$ → §2

*Step 1 — subtract 4 from both sides:*

$$-2x > 6$$

*Step 2 — divide both sides by $-2$, and flip the inequality sign:*

$$x < -3$$

*Why the flip:* multiplying or dividing an inequality by a negative number reverses the order. Test it: $3 > 2$ is true, but multiply both sides by $-1$ and $-3 > -2$ is false; $-3 < -2$ is the truth.

*Check:* try $x = -4$ (which satisfies $x < -3$): $-2(-4) + 4 = 12 > 10$ ✓. Try $x = 0$: $4 > 10$ is false ✓

---

**7.** $\displaystyle\sum_{i=1}^{4} (2i + 1)$ → §5

*The direct way — just expand it.* Substitute $i = 1, 2, 3, 4$ and add:

$$(2 \cdot 1 + 1) + (2 \cdot 2 + 1) + (2 \cdot 3 + 1) + (2 \cdot 4 + 1) = 3 + 5 + 7 + 9 = 24$$

*The rules way.* First split the sum (Rule B), which gives two **independent** sums:

$$\sum_{i=1}^{4}(2i + 1) = \sum_{i=1}^{4} 2i \;+\; \sum_{i=1}^{4} 1$$

Left sum: pull the constant out (Rule A), then $1+2+3+4 = 10$:

$$\sum_{i=1}^{4} 2i = 2\sum_{i=1}^{4} i = 2 \cdot 10 = 20$$

Right sum: adding $1$ once per term, over 4 terms (Rule C): $4 \cdot 1 = 4$.

$$20 + 4 = 24$$

*Common trap:* writing $2\left((1+2+3+4) + 4\right) = 28$. The $4$ came from the **other** half of the split, so it was never inside the bracket the $2$ multiplies. Adding it inside makes the $2$ scale it too, giving $+8$ instead of $+4$.

---

**8.** Line through $(1, 3)$ and $(3, 7)$ → §6

Every straight line is $y = mx + b$, so there are two unknowns to find, one at a time.

*Step 1 — the slope $m$.* Rise over run, from one point to the other:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{7 - 3}{3 - 1} = \frac{4}{2} = 2$$

So far: $y = 2x + b$.

*Step 2 — the intercept $b$.* $b$ is the $y$ value when $x = 0$, and neither point has $x = 0$, so it can't be read off — it has to be solved for. Both points lie **on** the line, which means each one makes the equation true. Substitute $(1, 3)$:

$$3 = 2(1) + b \quad\Rightarrow\quad 3 = 2 + b \quad\Rightarrow\quad b = 1$$

$$y = 2x + 1$$

*Step 3 — verify with the point you didn't use.* At $x = 3$: $2(3) + 1 = 7$ ✓ matches $(3, 7)$.

*The key idea:* "on the line" means "satisfies the equation." That's what lets you substitute a known point to pin down an unknown constant.

---

**9.** $e^{2x} = 5$ → §4

The unknown is stuck in an exponent, and $\ln$ is the tool that brings exponents down.

*Step 1 — take $\ln$ of both sides:*

$$\ln(e^{2x}) = \ln 5$$

*Step 2 — simplify the left.* $\ln$ and $e$ cancel, leaving the exponent:

$$2x = \ln 5$$

*Step 3 — divide by 2:*

$$x = \frac{\ln 5}{2} \approx \frac{1.609}{2} \approx 0.805$$

*Check:* $e^{2(0.805)} = e^{1.609} \approx 5$ ✓

---

**10.** Lowest point of $y = 2x^2 - 12x + 5$ → §7

This is a U-shaped parabola ($a = 2$ is positive, so it opens upward and has a lowest point).

*Step 1 — find the $x$ of the vertex* using $x = \frac{-b}{2a}$, with $a = 2$ and $b = -12$:

$$x = \frac{-(-12)}{2 \cdot 2} = \frac{12}{4} = 3$$

*Step 2 — find the $y$ there* by substituting $x = 3$ back in:

$$y = 2(3)^2 - 12(3) + 5 = 2 \cdot 9 - 36 + 5 = 18 - 36 + 5 = -13$$

Careful with the order here: $18 - 36 + 5$ is worked **left to right**, since $+$ and $-$ sit on the same tier. That's $-18 + 5 = -13$. Grouping it as $18 - (36 + 5) = -23$ is wrong — those parentheses aren't there.

The lowest point is $(3, -13)$.

*Sanity check:* try $x = 2$ and $x = 4$, one step either side. $y(2) = 8 - 24 + 5 = -11$ and $y(4) = 32 - 48 + 5 = -11$. Both are higher than $-13$, and equal to each other, which is exactly what you expect on either side of a vertex ✓

---

**Scoring:** Anything wrong → reread that section and redo its exercises tomorrow without looking at the solutions.

</details>

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can explain what a variable is, and evaluate expressions with negative numbers correctly.
- [ ] I can solve an equation step by step, say *why* each step is allowed, and check my answer.
- [ ] I can explain why $2^0 = 1$ and why $2^{-1} = \frac{1}{2}$, using the halving pattern.
- [ ] I can explain what a logarithm asks, rewrite any log as an exponent, and show why $\log(ab) = \log a + \log b$ with numbers.
- [ ] I can explain, with numbers, why computers use sums of logs instead of multiplying many small probabilities.
- [ ] I can read $\sum_{i=1}^{n} x_i$ aloud, expand it, and write it as a Python loop.
- [ ] Given $y = 3x + 2$, I can explain the input, output, slope, and intercept, solve for $x$, and describe the graph.
- [ ] I can find the lowest point of a U-shaped curve, both by reasoning about squares and with $x = \frac{-b}{2a}$.
- [ ] Check yourself: 10/10.
- [ ] Code lab passes, written without AI.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $3x$ | "three x" | $3 \times x$ | §1 |
| $\cdot$ | "times" | multiply | §1 |
| $\frac{a}{b}$ | "a over b" | $a \div b$ | §1 |
| $\ne$ | "not equal to" | the two sides are different | §2 |
| $<$, $>$ | "less than," "greater than" | compares size | §2 |
| $\le$, $\ge$ | "less than or equal to," "greater than or equal to" | compares size, equality allowed | §2 |
| $\approx$ | "approximately equal to" | close, but rounded | §4 |
| $a^n$ | "a to the power n" | $a$ multiplied by itself $n$ times | §3 |
| $x^2$, $x^3$ | "x squared," "x cubed" | $x \cdot x$, $x \cdot x \cdot x$ | §3 |
| $\sqrt{a}$ | "square root of a" | the number that squares to $a$ | §3 |
| $\log_b(x)$ | "log base b of x" | the exponent that turns $b$ into $x$ | §4 |
| $e$ | "e" | a constant, about 2.718 | §4 |
| $\ln(x)$ | "natural log of x" | $\log_e(x)$ | §4 |
| $x_i$ | "x sub i" | the $i$-th item in a list | §5 |
| $n$ | "n" | how many items | §5 |
| $\sum$ | "sum" (Greek sigma) | add up | §5 |
| $\prod$ | "product" (Greek pi) | multiply together | §5 |
| $\bar{x}$ | "x bar" | the average of the $x$ values | §5 |
| $\hat{y}$ | "y hat" | a guess or prediction for $y$ | §5 |
| $(x, y)$ | "the point x comma y" | a location on a graph | §6 |
| $m$, $b$ | "slope," "intercept" | in $y = mx + b$ | §6 |

---

## Resources (only if stuck)

Use these for extra practice on one specific section. Don't watch them start to finish.

- [Khan Academy — Pre-algebra](https://www.khanacademy.org/math/pre-algebra): negative numbers, order of operations, exponents (§1, §3)
- [Khan Academy — Algebra 1](https://www.khanacademy.org/math/algebra): solving equations, inequalities, graphing lines, slope (§2, §6, §7)
- [Khan Academy — Algebra 2](https://www.khanacademy.org/math/algebra2): logarithms (§4)
