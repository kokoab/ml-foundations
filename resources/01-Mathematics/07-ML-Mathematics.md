# 07 — ML Mathematics

**Time: ~8 hours** (spread it over 3 days) · **You need: all of [01](01-Algebra.md)–[06](06-Statistics.md)** · **Code lab: `math/07_ml_math.py`**

## Before you start

Files 01–06 were **theory**. This file is where that theory gets **applied**: you'll use it to build and understand the core math of machine learning, step by step, and derive everything yourself.

Unlike the earlier files, ML words are the **main topic** here, not side notes. Every one is defined from scratch before it's used.

**How to read it:**

- Go **in order**. Each section builds on the ones before.
- When a section references an earlier file (like "Calculus §5"), and that idea feels shaky, **go back and reread it**. That's expected, not a failure.
- When you see a worked example, **cover the solution and try it first**.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.

**What you'll be able to do by the end:**

- Explain what a model, parameters, loss, and training are, in precise math terms
- Derive linear regression and logistic regression from scratch
- Explain **why** each loss formula is used, not just what it is
- Derive how regularization works, and backpropagation for a small neural network
- Pass the **Mathematics Final Checkpoint** that closes Phase 1

---

## Contents

1. [What machine learning is, in math](#1-what-machine-learning-is-in-math)
2. [Measuring error: loss functions](#2-measuring-error-loss-functions)
3. [Linear regression](#3-linear-regression)
4. [Why squared error? The probability answer](#4-why-squared-error-the-probability-answer)
5. [Logistic regression: predicting yes or no](#5-logistic-regression-predicting-yes-or-no)
6. [More than two classes: softmax and cross-entropy](#6-more-than-two-classes-softmax-and-cross-entropy)
7. [Overfitting and regularization](#7-overfitting-and-regularization)
8. [Neural networks and backpropagation](#8-neural-networks-and-backpropagation)
9. [Mathematics Final Checkpoint](#9-mathematics-final-checkpoint)
10. [Code lab](#code-lab--math07_ml_mathpy)

---

## 1. What machine learning is, in math

### The problem

Say you want to predict a house's price from its floor area. You could try to write a rule by hand, but you don't know the right numbers. Instead, you have **past examples**: houses whose area and price you already know.

**Machine learning** means: use examples to **automatically find** a rule that makes good predictions on **new** cases.

### The vocabulary, one word at a time

**Example (data point):** one case you know the answer to, like one house.

**Features (inputs):** the numbers describing an example, written $\mathbf{x}$. One house might be $\mathbf{x} = [\text{area}, \text{rooms}, \text{age}]$. That's a vector (Linear Algebra §1).

**Target (label):** the answer you want to predict, written $y$. For a house, $y$ = price.

**Dataset:** all your examples, written as pairs $(\mathbf{x}_i, y_i)$ for $i = 1, \ldots, n$. Here the subscript $i$ numbers the **examples** (Algebra §5), and $n$ is how many examples you have.

**Data matrix:** stack every example's features as rows of a matrix (Linear Algebra §9):

$$
X = \begin{bmatrix} \text{— } \mathbf{x}_1 \text{ —} \\ \text{— } \mathbf{x}_2 \text{ —} \\ \vdots \\ \text{— } \mathbf{x}_n \text{ —} \end{bmatrix} \in \mathbb{R}^{n \times d}
$$

**Rows are examples, columns are features.** $d$ is the number of features. The targets form a vector $\mathbf{y} \in \mathbb{R}^n$.

### Two kinds of task

| Task | Target is | Example |
|---|---|---|
| **Regression** | a number | predict a price, a temperature |
| **Classification** | a category | spam or not spam; which of 10 digits |

### The model

A **model** is a function (Functions §1) that takes features and gives a prediction:

$$
\hat{y} = f(\mathbf{x};\ \boldsymbol{\theta})
$$

- $\hat{y}$ ("y hat") is the **prediction**.
- $\boldsymbol{\theta}$ ("bold theta") is the model's **parameters**: the adjustable numbers inside the formula. The semicolon separates "input" from "settings."

**Example.** Predicting price from area: $\hat{y} = w \cdot \text{area} + b$. The parameters are $w$ and $b$.

- Parameters that multiply inputs are called **weights**, usually $w$ or $\mathbf{w}$.
- A parameter that's added on is called a **bias**, usually $b$. (This is **not** the "bias" from Statistics §9. Unfortunately, same word, different meaning.)

### Training

**Training** means finding parameter values that make the model's predictions close to the true targets on the examples. The whole recipe is three choices:

| Choice | Question it answers | Math tool |
|---|---|---|
| 1. **Model** | What shape of formula? | Functions, Linear Algebra |
| 2. **Loss** | How do we measure "wrong"? | this file, §2 |
| 3. **Optimizer** | How do we find the best parameters? | Calculus §10–§11 |

Every model in this curriculum, from a straight line up to a large neural network, fits this recipe.

### Exercises

**1.1.** A dataset has 2,000 emails, each described by 50 numbers, labeled spam or not spam. What are $n$ and $d$? What's the shape of $X$? Is this regression or classification?

**1.2.** For the model $\hat{y} = 3x_1 - 2x_2 + 5$: what are the weights, and what's the bias? What's the prediction for $\mathbf{x} = [2, 1]$?

**1.3.** In your own words: what's the difference between a feature, a target, and a parameter?

<details>
<summary>Solutions</summary>

**1.1.** $n = 2000$, $d = 50$, $X \in \mathbb{R}^{2000 \times 50}$. Classification.

**1.2.** Weights $[3, -2]$, bias $5$. Prediction: $6 - 2 + 5 = 9$.

**1.3.** Features are the known inputs describing an example. The target is the answer to predict. Parameters are the adjustable numbers inside the model, found by training.

</details>

---

## 2. Measuring error: loss functions

### The problem

To improve a model, we need a **single number** saying how wrong it is. Then "training" becomes "make that number small," which is a minimization problem, and Calculus showed how to solve those.

### Loss and cost

- A **loss function** $\ell(\hat{y}, y)$ measures how wrong **one** prediction is.
- The **cost function** $J(\boldsymbol{\theta})$ is the **average loss** over all examples:

$$
J(\boldsymbol{\theta}) = \frac{1}{n}\sum_{i=1}^n \ell(\hat{y}_i, y_i)
$$

(People often say "loss" for both.) **Training = find the $\boldsymbol{\theta}$ that minimizes $J$.**

### Squared error

$$
\ell = (y - \hat{y})^2
$$

The average of this is the **mean squared error (MSE)**. You built this formula in Algebra §5.

| True $y$ | Prediction $\hat{y}$ | Error | Squared error |
|---|---|---|---|
| 10 | 9 | 1 | 1 |
| 10 | 7 | 3 | 9 |
| 10 | 0 | 10 | **100** |

**Big mistakes are punished much more** than small ones (a 10× bigger error costs 100×).

### Absolute error

$$
\ell = |y - \hat{y}|
$$

The average of this is the **mean absolute error (MAE)**. Errors of 1, 3, and 10 cost 1, 3, and 10, so everything is punished in proportion.

### Choosing between them

From Statistics §2: minimizing squared distance gives the **mean**, which gets dragged by outliers. Minimizing absolute distance gives the **median**, which resists them.

- Few outliers, and big mistakes really are much worse: **MSE**.
- Messy data with extreme values: **MAE** is more robust.

§4 gives a deeper reason for MSE. For classification, we'll need a different loss entirely (§5).

### Exercises

**2.1.** True values $[3, 5, 8]$, predictions $[2, 5, 11]$. Calculate the MSE and the MAE.

**2.2.** Add one more example: true 10, predicted 30. Recalculate both. Which changed more, and why?

<details>
<summary>Solutions</summary>

**2.1.** Errors $[1, 0, -3]$. MSE $= \frac{1 + 0 + 9}{3} \approx 3.33$. MAE $= \frac{1 + 0 + 3}{3} \approx 1.33$.

**2.2.** Errors $[1, 0, -3, -20]$. MSE $= \frac{410}{4} = 102.5$. MAE $= \frac{24}{4} = 6$. MSE jumped about 30×, because squaring makes the big error dominate.

</details>

---

## 3. Linear regression

### The model

Predict a number as a **weighted sum of the features plus a bias**:

$$
\hat{y} = w_1x_1 + w_2x_2 + \cdots + w_dx_d + b = \mathbf{w} \cdot \mathbf{x} + b
$$

That's a dot product (Linear Algebra §5): the shopping-total idea, where each feature gets a weight.

With one feature, it's just the line $\hat{y} = wx + b$ from Algebra §6.

### Folding the bias into the weights

A handy trick: add a feature that's **always 1** to every example. Then its weight acts as the bias:

$$
\mathbf{x} = [1, x_1, \ldots, x_d], \qquad \mathbf{w} = [b, w_1, \ldots, w_d], \qquad \hat{y} = \mathbf{w} \cdot \mathbf{x}
$$

Now **all** predictions at once are a single matrix-vector product (Linear Algebra §10):

$$
\hat{\mathbf{y}} = X\mathbf{w}
$$

Row $i$ of $X$ dotted with $\mathbf{w}$ gives prediction $i$.

**Shape check:** $X$ is $n \times (d + 1)$, $\mathbf{w}$ has $d + 1$ entries, so $X\mathbf{w}$ has $n$ entries: one prediction per example ✓

### The cost

$$
J(\mathbf{w}) = \frac{1}{n}\sum_{i=1}^n (\hat{y}_i - y_i)^2 = \frac{1}{n}\lVert X\mathbf{w} - \mathbf{y} \rVert^2
$$

The second form uses the fact that a vector's squared length is the sum of its squared components (Linear Algebra §3).

### Deriving the gradient: one feature first

Start small: $\hat{y} = wx + b$, with cost $J(w, b) = \frac{1}{n}\sum_i (wx_i + b - y_i)^2$.

Call the error on example $i$: $e_i = wx_i + b - y_i$.

| Partial derivative | Chain rule (Calculus §5, §6) | Result |
|---|---|---|
| $\frac{\partial J}{\partial w}$ | $\frac{1}{n}\sum_i 2e_i \cdot \frac{\partial e_i}{\partial w}$, and $\frac{\partial e_i}{\partial w} = x_i$ | $\frac{2}{n}\sum_i e_i\,x_i$ |
| $\frac{\partial J}{\partial b}$ | $\frac{1}{n}\sum_i 2e_i \cdot \frac{\partial e_i}{\partial b}$, and $\frac{\partial e_i}{\partial b} = 1$ | $\frac{2}{n}\sum_i e_i$ |

**Read these in words:**

- $\frac{\partial J}{\partial w}$: each example's error, **weighted by its feature value**, averaged.
- $\frac{\partial J}{\partial b}$: the **average error**.

### The same thing in matrix form

Collect the errors into a vector: $\mathbf{e} = X\mathbf{w} - \mathbf{y}$. Each gradient component is "errors dotted with one feature column," and $X^\top\mathbf{e}$ computes exactly those dot products for every column at once (Linear Algebra §13). So:

$$
\nabla J(\mathbf{w}) = \frac{2}{n}X^\top(X\mathbf{w} - \mathbf{y})
$$

**Shape check:** $X^\top$ is $(d + 1) \times n$, and $\mathbf{e}$ has $n$ entries, so the result has $d + 1$ entries, the same shape as $\mathbf{w}$ ✓ (Calculus §8's rule)

### Option A: solve directly

Set the gradient to zero (Calculus §10):

$$
X^\top X\mathbf{w} = X^\top\mathbf{y}
$$

These are the **normal equations**, exactly what Linear Algebra §17 found using perpendicularity. **The calculus and the geometry agree.** The cost is convex (a bowl), so this is the global minimum.

**Worked example.** $x = [1, 2, 3]$, $y = [2, 4, 7]$. We already solved this in Linear Algebra §17: $b = -0.667$ and $w = 2.5$. Statistics §8 got the same line with covariance. **Three methods, one answer.**

### Option B: gradient descent

When there are too many features to solve directly, use gradient descent (Calculus §11):

$$
\mathbf{w} := \mathbf{w} - \alpha\,\nabla J(\mathbf{w})
$$

**Worked example.** Same data, starting at $\mathbf{w} = [b, w] = [0, 0]$ with step size $\alpha = 0.1$.

$$
X = \begin{bmatrix}1 & 1\\1 & 2\\1 & 3\end{bmatrix}, \quad \mathbf{y} = \begin{bmatrix}2\\4\\7\end{bmatrix}
$$

| Step | Calculation | Result |
|---|---|---|
| Predictions $X\mathbf{w}$ | all zero | $[0, 0, 0]$ |
| Errors $\mathbf{e} = X\mathbf{w} - \mathbf{y}$ | | $[-2, -4, -7]$ |
| $X^\top\mathbf{e}$ | column 1 (all 1s): $-2 - 4 - 7$; column 2: $-2 - 8 - 21$ | $[-13, -31]$ |
| Gradient $\frac{2}{3}X^\top\mathbf{e}$ | | $[-8.667, -20.667]$ |
| New $\mathbf{w} = \mathbf{w} - 0.1 \times \text{gradient}$ | | $[0.867, 2.067]$ |
| Cost before | $\frac{4 + 16 + 49}{3}$ | 23 |
| Cost after | predictions $[2.933, 5.0, 7.067]$, errors $[0.933, 1.0, 0.067]$ | $\approx 0.63$ |

One step cut the cost from 23 to 0.63. Many more steps converge to $[-0.667, 2.5]$.

### Exercises

**3.1.** Derive $\frac{\partial J}{\partial w}$ and $\frac{\partial J}{\partial b}$ for one feature, without looking.

**3.2.** Do a second gradient descent step from $\mathbf{w} = [0.867, 2.067]$. What's the new cost?

**3.3.** Explain in terms of rank (Linear Algebra §16) why the normal equations fail if two feature columns are identical.

**3.4.** A dataset has $n = 10{,}000$ examples and $d = 20$ features, plus the bias column. What's the shape of $X^\top X$? Of the gradient?

<details>
<summary>Hint</summary>

3.2: start from the "cost after" row: errors $[0.933, 1.0, 0.067]$.

</details>

<details>
<summary>Solutions</summary>

**3.2.** $X^\top\mathbf{e} = [0.933 + 1.0 + 0.067,\ 0.933 + 2.0 + 0.2] = [2.0, 3.133]$. Gradient $= [1.333, 2.089]$. New $\mathbf{w} \approx [0.733, 1.858]$. Predictions $[2.591, 4.449, 6.307]$, errors $[0.591, 0.449, -0.693]$, cost $\approx \frac{0.349 + 0.202 + 0.480}{3} \approx 0.34$. It went down again.

**3.3.** Identical columns are dependent, so $X$ doesn't have full rank, and $X^\top X$ has determinant 0 with no inverse. Many different weight combinations fit equally well.

**3.4.** $21 \times 21$ and 21 entries.

</details>

---

## 4. Why squared error? The probability answer

### The question

§2 said MSE punishes big errors more. But **why that particular formula**? Is there a principled reason, or is it just convenient?

Probability gives a real answer.

### The assumption: errors are Gaussian noise

Assume each true target is the model's prediction plus some random **noise**:

$$
y_i = \mathbf{w} \cdot \mathbf{x}_i + \varepsilon_i, \qquad \varepsilon_i \sim \mathcal{N}(0, \sigma^2)
$$

- $\varepsilon_i$ is the noise: the part the features can't explain.
- $\sim$ is read "**is distributed as**."
- So the noise is Gaussian (Probability §10), centered at 0, independent for each example.

That means each $y_i$ is Gaussian, centered at the prediction:

$$
P(y_i \mid \mathbf{x}_i, \mathbf{w}) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(y_i - \mathbf{w} \cdot \mathbf{x}_i)^2}{2\sigma^2}\right)
$$

($\exp(u)$ is just another way to write $e^u$, useful when $u$ is long.)

### Maximum likelihood

Find the $\mathbf{w}$ that makes the observed data most likely (Probability §11). Take the log-likelihood, which turns the product over independent examples into a sum:

| Step | What we did |
|---|---|
| $\ell(\mathbf{w}) = \sum_i \ln P(y_i \mid \mathbf{x}_i, \mathbf{w})$ | Log of a product = sum of logs |
| $= \sum_i \left[\ln\frac{1}{\sqrt{2\pi\sigma^2}} - \frac{(y_i - \mathbf{w} \cdot \mathbf{x}_i)^2}{2\sigma^2}\right]$ | $\ln(ab) = \ln a + \ln b$, and $\ln(e^u) = u$ |
| $= \underbrace{n\ln\frac{1}{\sqrt{2\pi\sigma^2}}}_{\text{doesn't involve } \mathbf{w}} - \frac{1}{2\sigma^2}\sum_i (y_i - \mathbf{w} \cdot \mathbf{x}_i)^2$ | Separated the parts |

To make $\ell$ as large as possible, the first part can't help (no $\mathbf{w}$ in it), and $\frac{1}{2\sigma^2}$ is a positive constant. So we just need the sum being subtracted to be **as small as possible**:

$$
\arg\max_{\mathbf{w}}\ \ell(\mathbf{w}) = \arg\min_{\mathbf{w}}\ \sum_i (y_i - \mathbf{w} \cdot \mathbf{x}_i)^2
$$

### The conclusion

**Minimizing squared error is exactly maximum likelihood, assuming Gaussian noise.**

So choosing MSE is secretly a **belief** about your data: errors are bell-shaped, and extreme errors are extremely rare. If your data has wild outliers, that belief is wrong, and MAE (which corresponds to a noise distribution with heavier tails) may be the better choice.

### Exercises

**4.1.** Reproduce the derivation without looking.

**4.2.** Why doesn't the value of $\sigma$ affect which $\mathbf{w}$ is best?

<details>
<summary>Solutions</summary>

**4.2.** $\sigma$ only appears in a term without $\mathbf{w}$, and in the positive multiplier $\frac{1}{2\sigma^2}$. Scaling a function by a positive number doesn't move where its minimum is.

</details>

---

## 5. Logistic regression: predicting yes or no

### The problem

Now the target is **yes (1) or no (0)**: spam or not, sick or healthy. A straight-line model $\mathbf{w} \cdot \mathbf{x} + b$ can output any number, like $-3$ or $47$. We want a **probability** between 0 and 1.

### The model

Take the straight-line score, and squash it with the sigmoid (Functions §9):

$$
z = \mathbf{w} \cdot \mathbf{x} + b, \qquad p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

- $z$ is the **score** (also called the **logit**), any real number.
- $p$ is the model's probability that the answer is **yes**: $P(y = 1 \mid \mathbf{x})$.

Despite the name, logistic "regression" is used for classification.

### The decision boundary

To give a firm yes/no, predict yes when $p \ge 0.5$. Since $\sigma(z) = 0.5$ exactly when $z = 0$:

$$
\text{predict yes} \iff \mathbf{w} \cdot \mathbf{x} + b \ge 0
$$

The boundary $\mathbf{w} \cdot \mathbf{x} + b = 0$ is a **straight line** (with 2 features) or a flat plane (with more). Logistic regression separates classes with a straight cut.

### Finding the right loss, using likelihood

Why not use squared error? We'll see below that it works badly. Instead, **use maximum likelihood**, the same method that justified MSE in §4.

Each label is a Bernoulli outcome with probability $p$ (Probability §10):

$$
P(y \mid \mathbf{x}) = p^y(1 - p)^{1 - y}
$$

(Check: $y = 1$ gives $p$, and $y = 0$ gives $1 - p$.)

The **negative** log-likelihood for one example is:

| Step | What we did |
|---|---|
| $-\ln\left[p^y(1 - p)^{1 - y}\right]$ | Negative log of the probability |
| $= -\left[y\ln p + (1 - y)\ln(1 - p)\right]$ | Log rules 1 and 3 (Algebra §4) |

$$
\ell = -\big[y\ln p + (1 - y)\ln(1 - p)\big]
$$

This is called **binary cross-entropy** (BCE). It wasn't invented arbitrarily: **it's what maximum likelihood gives for yes/no data.**

### What the loss does

Only one of the two terms is ever "on":

| True $y$ | Loss becomes | If $p = 0.9$ | If $p = 0.5$ | If $p = 0.1$ | If $p = 0.01$ |
|---|---|---|---|---|---|
| 1 | $-\ln p$ | 0.105 | 0.693 | 2.303 | 4.605 |
| 0 | $-\ln(1 - p)$ | 2.303 | 0.693 | 0.105 | 0.010 |

**Confident and right** costs almost nothing. **Confident and wrong** costs a lot, and the cost grows without limit as $p$ approaches the wrong extreme.

### Deriving the gradient

Chain rule through $p$ and $z$:

| Step | Result |
|---|---|
| $\frac{\partial \ell}{\partial p}$ | $-\frac{y}{p} + \frac{1 - y}{1 - p}$ (derivative of $\ln$, Calculus §4; the $\ln(1 - p)$ has inside derivative $-1$) |
| $\frac{\partial p}{\partial z}$ | $p(1 - p)$ (sigmoid derivative, Calculus §5) |
| $\frac{\partial \ell}{\partial z} = \frac{\partial \ell}{\partial p} \cdot \frac{\partial p}{\partial z}$ | $\left(-\frac{y}{p} + \frac{1 - y}{1 - p}\right)p(1 - p)$ |
| Multiply each term out | $-y(1 - p) + (1 - y)p$ |
| Expand | $-y + yp + p - yp$ |
| Simplify | $p - y$ |

$$
\frac{\partial \ell}{\partial z} = p - y
$$

**Prediction minus truth.** All the complicated pieces cancel.

Then $z = \mathbf{w} \cdot \mathbf{x} + b$, so $\frac{\partial z}{\partial w_j} = x_j$, and $\frac{\partial z}{\partial b} = 1$. Averaging over all examples:

$$
\nabla_{\mathbf{w}}J = \frac{1}{n}X^\top(\mathbf{p} - \mathbf{y})
$$

**Compare with linear regression:** $\frac{2}{n}X^\top(X\mathbf{w} - \mathbf{y})$. The same shape: (prediction − truth), weighted by the features. That's not a coincidence. Both come from maximum likelihood with a well-matched distribution.

### Worked example

One example: $\mathbf{x} = [1, 2]$, $y = 1$, weights $\mathbf{w} = [0.5, -0.25]$, no bias, step size $\alpha = 0.1$.

| Step | Calculation | Result |
|---|---|---|
| Score | $z = 0.5(1) + (-0.25)(2)$ | $0$ |
| Probability | $p = \sigma(0)$ | $0.5$ |
| Loss | $-\ln 0.5$ | $0.693$ |
| $\frac{\partial \ell}{\partial z}$ | $p - y = 0.5 - 1$ | $-0.5$ |
| Gradient | $-0.5 \times [1, 2]$ | $[-0.5, -1.0]$ |
| New weights | $[0.5, -0.25] - 0.1 \times [-0.5, -1.0]$ | $[0.55, -0.15]$ |
| New score | $0.55 - 0.30$ | $0.25$ |
| New probability | $\sigma(0.25)$ | $0.562$ |
| New loss | $-\ln 0.562$ | $0.576$ ✓ lower |

### Why not squared error for classification?

With $\ell = (p - y)^2$ and $p = \sigma(z)$:

$$
\frac{\partial \ell}{\partial z} = 2(p - y) \cdot p(1 - p)
$$

Say the model is **confidently wrong**: $y = 1$ but $p = 0.001$.

| Loss | $\frac{\partial \ell}{\partial z}$ |
|---|---|
| Squared error | $2(0.001 - 1)(0.001)(0.999) \approx -0.002$ ← almost no signal |
| Cross-entropy | $0.001 - 1 \approx -1$ ← strong signal |

With squared error, the sigmoid's flat end (saturation, Functions §9) multiplies the gradient by nearly zero, so **the model barely learns from its worst mistakes**. Cross-entropy's $\ln$ exactly cancels that flatness.

### Exercises

**5.1.** Derive $\frac{\partial \ell}{\partial z} = p - y$ without looking.

**5.2.** A model outputs $p = 0.8$. Find the loss if $y = 1$, and if $y = 0$.

**5.3.** Redo the worked example with $y = 0$ instead. Which way do the weights move, and why?

**5.4.** With weights $\mathbf{w} = [2, -1]$ and bias $b = -1$, is $\mathbf{x} = [1, 0.5]$ classified yes or no? Where's the decision boundary?

<details>
<summary>Solutions</summary>

**5.2.** $-\ln 0.8 \approx 0.223$ and $-\ln 0.2 \approx 1.609$.

**5.3.** $\frac{\partial \ell}{\partial z} = 0.5 - 0 = 0.5$, gradient $[0.5, 1.0]$, new $\mathbf{w} = [0.45, -0.35]$. New $z = 0.45 - 0.7 = -0.25$, so $p \approx 0.438$. The weights move to **lower** the score, pushing $p$ toward the true answer 0.

**5.4.** $z = 2 - 0.5 - 1 = 0.5 \ge 0$, so yes. Boundary: $2x_1 - x_2 - 1 = 0$, which is the line $x_2 = 2x_1 - 1$.

</details>

---

## 6. More than two classes: softmax and cross-entropy

### The model

With $K$ classes, compute **one score per class**, then turn the scores into probabilities with softmax (Functions §10):

$$
\mathbf{z} = [z_1, \ldots, z_K], \qquad s_k = \text{softmax}(\mathbf{z})_k = \frac{e^{z_k}}{\sum_j e^{z_j}}
$$

### One-hot targets

Write the true class as a vector with a 1 in the correct position and 0s elsewhere. This is called **one-hot** encoding. If the true class is 2 out of 3: $\mathbf{y} = [0, 1, 0]$.

### The loss: cross-entropy

Each example is a categorical outcome (Probability §10), so the likelihood is the probability the model gave to the **correct** class. The negative log-likelihood is:

$$
\ell = -\sum_{k=1}^{K} y_k \ln s_k = -\ln(s_{\text{correct class}})
$$

(Every term except the correct class is multiplied by $y_k = 0$ and disappears.)

**Example.** Scores $[2.0, 1.0, 0.1]$ give probabilities $[0.659, 0.242, 0.099]$ (Functions §10).

- True class 1: $\ell = -\ln 0.659 \approx 0.417$
- True class 3: $\ell = -\ln 0.099 \approx 2.31$

### The gradient

$$
\frac{\partial \ell}{\partial \mathbf{z}} = \mathbf{s} - \mathbf{y}
$$

**Prediction minus truth, again.** (It's derived in Exercise 6.3.)

**Example.** True class 1: $\mathbf{s} - \mathbf{y} = [0.659 - 1,\ 0.242,\ 0.099] = [-0.341, 0.242, 0.099]$.

Gradient descent **subtracts** the gradient, so:

- the correct class's score goes **up** (its component is negative), and
- each wrong class's score goes **down**, in proportion to how much probability it wrongly took.

### Exercises

**6.1.** Probabilities $[0.1, 0.7, 0.2]$, true class 2. Find the loss and $\frac{\partial \ell}{\partial \mathbf{z}}$.

**6.2.** Show that with $K = 2$, softmax cross-entropy is the same as binary cross-entropy. (Use Functions §10: 2-class softmax is sigmoid.)

**6.3.** *(Challenge)* Derive $\frac{\partial \ell}{\partial \mathbf{z}} = \mathbf{s} - \mathbf{y}$. You'll need the softmax Jacobian: $\frac{\partial s_k}{\partial z_j} = s_k(1 - s_j)$ if $k = j$, and $-s_k s_j$ if $k \ne j$.

<details>
<summary>Hint</summary>

6.3: $\frac{\partial \ell}{\partial z_j} = \sum_k \frac{\partial \ell}{\partial s_k}\frac{\partial s_k}{\partial z_j}$, with $\frac{\partial \ell}{\partial s_k} = -\frac{y_k}{s_k}$. Split the sum into the $k = j$ term and the rest, and use $\sum_k y_k = 1$.

</details>

<details>
<summary>Solutions</summary>

**6.1.** $-\ln 0.7 \approx 0.357$. Gradient $[0.1, -0.3, 0.2]$.

**6.2.** With scores $[z, 0]$: $s_1 = \sigma(z) = p$ and $s_2 = 1 - p$. The loss is $-[y_1\ln p + y_2\ln(1 - p)]$ with $y_2 = 1 - y_1$, which is exactly BCE.

**6.3.** The $k = j$ term: $-\frac{y_j}{s_j} \cdot s_j(1 - s_j) = -y_j + y_js_j$. The $k \ne j$ terms: $\sum_{k \ne j} -\frac{y_k}{s_k} \cdot (-s_ks_j) = s_j\sum_{k \ne j} y_k$. Total: $-y_j + s_j\left(y_j + \sum_{k \ne j} y_k\right) = -y_j + s_j \cdot 1 = s_j - y_j$.

</details>

---

## 7. Overfitting and regularization

### The problem: memorizing instead of learning

Imagine a student who memorizes the answers to last year's exam word for word. They'd score 100% on **that** exam, but fail a new one with slightly different questions.

Models can do the same thing. A very flexible model can bend to fit every tiny random quirk in its training examples, and then make **bad predictions on new data**. This is called **overfitting**. It's the high-variance problem from Statistics §9.

**Example.** 10 points roughly along a line, with some noise:

- A straight line misses each point a little, but captures the real trend. Good on new data.
- A wiggly curve that passes **exactly** through all 10 points has zero training error, but swings wildly between points. Terrible on new data.

The tell-tale sign of overfitting: **very low error on training data, much higher error on new data.**

One common symptom: the weights become **very large**, because big weights are what allow sharp wiggles.

### The idea: make large weights cost something

Add a **penalty** for large weights to the cost:

$$
J_{\text{regularized}}(\mathbf{w}) = J(\mathbf{w}) + \lambda \cdot \text{penalty}(\mathbf{w})
$$

- $\lambda$ ("lambda") is the **regularization strength**: how much we care about keeping weights small, compared with fitting the data. (Not the eigenvalue from Linear Algebra §18. Same letter, different use.)
- Adding a penalty like this is called **regularization**.

Now the model has to balance fitting the data against keeping its weights modest.

### L2 regularization

Penalize the **squared length** of the weight vector (Linear Algebra §3):

$$
\text{penalty} = \lVert \mathbf{w} \rVert^2 = \sum_j w_j^2
$$

**Gradient of the penalty:** $\frac{\partial}{\partial w_j}\lambda w_j^2 = 2\lambda w_j$. So:

$$
\nabla J_{\text{regularized}} = \nabla J + 2\lambda\mathbf{w}
$$

**The gradient descent update:**

| Step | What we did |
|---|---|
| $\mathbf{w} := \mathbf{w} - \alpha(\nabla J + 2\lambda\mathbf{w})$ | Gradient descent with the new gradient |
| $\mathbf{w} := \mathbf{w} - 2\alpha\lambda\mathbf{w} - \alpha\nabla J$ | Distributed $\alpha$ |
| $\mathbf{w} := (1 - 2\alpha\lambda)\,\mathbf{w} - \alpha\nabla J$ | Factored out $\mathbf{w}$ |

**Every step shrinks every weight by the same percentage** $(1 - 2\alpha\lambda)$, before the usual update. That's why L2 is also called **weight decay**.

**Closed form for linear regression:** the normal equations become $(X^\top X + \lambda I)\mathbf{w} = X^\top\mathbf{y}$. Adding $\lambda I$ raises every eigenvalue of $X^\top X$ by $\lambda$, so none are zero, and the matrix always has an inverse, even with dependent features (Linear Algebra §15, §18).

### L1 regularization

Penalize the **L1 length** (Linear Algebra §3):

$$
\text{penalty} = \lVert \mathbf{w} \rVert_1 = \sum_j |w_j|
$$

The slope of $|w|$ is $+1$ for positive $w$ and $-1$ for negative $w$ (the V shape, Functions §8). So each step moves every weight **toward zero by a fixed amount** $\alpha\lambda$.

### L2 vs. L1 with numbers

Weights $\mathbf{w} = [2, -0.5]$, $\alpha = 0.1$, $\lambda = 0.5$. Ignore $\nabla J$ to see just the penalty's effect:

| | Rule | New weights |
|---|---|---|
| **L2** | multiply by $1 - 2(0.1)(0.5) = 0.9$ | $[1.8,\ -0.45]$: each shrinks **10%** |
| **L1** | move toward 0 by $0.1 \times 0.5 = 0.05$ | $[1.95,\ -0.45]$: each shrinks by **0.05** |

Now a tiny weight, $\mathbf{w} = [0.03, 2]$:

| | New weights |
|---|---|
| **L2** | $[0.027,\ 1.8]$: small, but never exactly zero |
| **L1** | $0.03 - 0.05$ would overshoot past zero, so it's set to exactly **0**: $[0,\ 1.95]$ |

**L1 pushes small weights to exactly zero.** That means it switches off unhelpful features completely, which is called **sparsity**. L2 just makes everything smaller.

### The picture

Recall the shapes from Linear Algebra Exercise 3.5: all points with L2 length 1 form a **circle**, and L1 length 1 forms a **diamond**.

Regularization keeps the weights inside such a shape. The best-fitting weights usually touch the diamond at a **corner**, and corners sit on the axes, where some weights are exactly zero. A circle has no corners, so that rarely happens with L2.

### Exercises

**7.1.** Derive the weight-decay update form for L2, without looking.

**7.2.** Weights $[4, -1, 0.02]$, $\alpha = 0.1$, $\lambda = 0.2$. Apply one L2 penalty step, and one L1 penalty step (ignore $\nabla J$).

**7.3.** You have 200 features but suspect only 15 really matter. Which regularization would you choose, and why?

**7.4.** What happens to the weights if $\lambda$ is enormous? If $\lambda = 0$?

<details>
<summary>Solutions</summary>

**7.2.** L2: multiply by $1 - 0.04 = 0.96$, giving $[3.84, -0.96, 0.0192]$. L1: move each toward 0 by 0.02, giving $[3.98, -0.98, 0]$.

**7.3.** L1, because it drives unhelpful weights to exactly zero, which shows which features the model uses.

**7.4.** Enormous: the penalty dominates, and the weights are crushed toward zero (underfitting). Zero: no regularization at all.

</details>

---

## 8. Neural networks and backpropagation

### The problem: straight lines aren't enough

Linear and logistic regression can only draw **straight** decision boundaries (§5). Some patterns can't be separated by any straight line.

**Example (XOR):** points $(0, 0)$ and $(1, 1)$ are class 0, and $(0, 1)$ and $(1, 0)$ are class 1. Try drawing one straight line that separates them. You can't.

And from Functions §5: stacking straight-line steps **still** gives a straight line. We need to add nonlinearity.

### A neuron

A **neuron** is one weighted sum followed by a nonlinear function (an **activation**, like ReLU or sigmoid):

$$
a = \text{activation}(\mathbf{w} \cdot \mathbf{x} + b)
$$

That's exactly logistic regression if the activation is sigmoid.

### A layer

A **layer** is many neurons side by side, each with its own weights. Stack each neuron's weights as a row of a matrix $W$ and its bias into a vector $\mathbf{b}$. Then the whole layer is (Linear Algebra §10):

$$
\mathbf{a} = \text{activation}(W\mathbf{x} + \mathbf{b})
$$

with the activation applied **elementwise** (Functions §8).

### A 2-layer network

$$
\mathbf{z}_1 = W_1\mathbf{x} + \mathbf{b}_1 \quad\to\quad \mathbf{a}_1 = \text{ReLU}(\mathbf{z}_1) \quad\to\quad \mathbf{z}_2 = W_2\mathbf{a}_1 + \mathbf{b}_2 \quad\to\quad \hat{\mathbf{y}} = \text{softmax}(\mathbf{z}_2)
$$

The middle values $\mathbf{a}_1$ are called the **hidden layer**. The final output uses softmax and cross-entropy (§6).

**Why this is more powerful:** the first layer transforms the input into a new set of features, the ReLU bends that space, and the second layer draws a straight boundary **in the bent space**. That boundary can be curved in the original space.

### Shapes: the first thing to check

Example: 63 input features, 128 hidden neurons, 10 classes.

| Quantity | Shape | Why |
|---|---|---|
| $\mathbf{x}$ | $(63)$ | 63 features |
| $W_1$ | $(128 \times 63)$ | 128 neurons, each with 63 weights |
| $\mathbf{b}_1$ | $(128)$ | one bias per neuron |
| $\mathbf{z}_1$, $\mathbf{a}_1$ | $(128)$ | one value per neuron |
| $W_2$ | $(10 \times 128)$ | 10 outputs, each looking at 128 hidden values |
| $\mathbf{b}_2$ | $(10)$ | |
| $\mathbf{z}_2$, $\hat{\mathbf{y}}$ | $(10)$ | one score/probability per class |

**Parameter count:** $(128 \times 63 + 128) + (10 \times 128 + 10) = 8192 + 1290 = 9482$.

### Training: we need every gradient

To use gradient descent, we need $\frac{\partial \ell}{\partial W_1}$, $\frac{\partial \ell}{\partial \mathbf{b}_1}$, $\frac{\partial \ell}{\partial W_2}$, and $\frac{\partial \ell}{\partial \mathbf{b}_2}$. The network is a chain of functions, so we use the **forward-then-backward** method from Calculus §5. For neural networks, this is called **backpropagation**.

### Backpropagation on a tiny network, with real numbers

Start with one number per layer, so every step is visible:

$$
z_1 = w_1x + b_1, \quad a_1 = \text{ReLU}(z_1), \quad \hat{y} = w_2a_1 + b_2, \quad \ell = \tfrac{1}{2}(\hat{y} - y)^2
$$

(The $\frac{1}{2}$ just makes the derivative cleaner.) Values: $x = 2$, $w_1 = 0.5$, $b_1 = 0$, $w_2 = 2$, $b_2 = 0$, target $y = 3$.

**Forward pass: compute and save each value.**

| Quantity | Calculation | Value |
|---|---|---|
| $z_1$ | $0.5 \times 2 + 0$ | 1 |
| $a_1$ | $\text{ReLU}(1)$ | 1 |
| $\hat{y}$ | $2 \times 1 + 0$ | 2 |
| $\ell$ | $\frac{1}{2}(2 - 3)^2$ | 0.5 |

**Backward pass: start at the loss, multiply local derivatives going back.**

| Gradient | Chain rule | Value |
|---|---|---|
| $\frac{\partial \ell}{\partial \hat{y}}$ | $\hat{y} - y$ | $-1$ |
| $\frac{\partial \ell}{\partial w_2}$ | $\frac{\partial \ell}{\partial \hat{y}} \times a_1$ | $-1$ |
| $\frac{\partial \ell}{\partial b_2}$ | $\frac{\partial \ell}{\partial \hat{y}} \times 1$ | $-1$ |
| $\frac{\partial \ell}{\partial a_1}$ | $\frac{\partial \ell}{\partial \hat{y}} \times w_2$ | $-2$ |
| $\frac{\partial \ell}{\partial z_1}$ | $\frac{\partial \ell}{\partial a_1} \times \text{ReLU}'(z_1)$, which is 1 since $z_1 > 0$ | $-2$ |
| $\frac{\partial \ell}{\partial w_1}$ | $\frac{\partial \ell}{\partial z_1} \times x$ | $-4$ |
| $\frac{\partial \ell}{\partial b_1}$ | $\frac{\partial \ell}{\partial z_1} \times 1$ | $-2$ |

**Notice the reuse:** $\frac{\partial \ell}{\partial \hat{y}}$ gets used three times, and $\frac{\partial \ell}{\partial z_1}$ twice. Each gradient is built from the one just after it in the chain. That reuse is what makes backpropagation fast.

**Update with $\alpha = 0.05$:** $w_2 = 2.05$, $b_2 = 0.05$, $w_1 = 0.7$, $b_1 = 0.1$.

**New forward pass:** $z_1 = 0.7 \times 2 + 0.1 = 1.5$, $a_1 = 1.5$, $\hat{y} = 2.05 \times 1.5 + 0.05 = 3.125$, $\ell = \frac{1}{2}(0.125)^2 \approx 0.0078$.

**The loss dropped from 0.5 to 0.0078 in one step.**

### The same thing with vectors and matrices

For the 2-layer network with softmax and cross-entropy, the backward pass follows the same pattern:

| Step | Formula | Shape | Why |
|---|---|---|---|
| 1 | $\boldsymbol{\delta}_2 = \hat{\mathbf{y}} - \mathbf{y}$ | $(10)$ | softmax + cross-entropy (§6) |
| 2 | $\frac{\partial \ell}{\partial W_2} = \boldsymbol{\delta}_2\,\mathbf{a}_1^\top$ | $(10 \times 128)$ | since $z_{2,i} = \sum_j W_{2,ij}\,a_{1,j}$, the derivative with respect to $W_{2,ij}$ is $a_{1,j}$ |
| 3 | $\frac{\partial \ell}{\partial \mathbf{b}_2} = \boldsymbol{\delta}_2$ | $(10)$ | biases pass the gradient straight through |
| 4 | $\frac{\partial \ell}{\partial \mathbf{a}_1} = W_2^\top\boldsymbol{\delta}_2$ | $(128)$ | each hidden value affected every output, through its column of $W_2$ |
| 5 | $\boldsymbol{\delta}_1 = W_2^\top\boldsymbol{\delta}_2 \odot \mathbf{1}[\mathbf{z}_1 > 0]$ | $(128)$ | ReLU's slope is 1 or 0 for each neuron |
| 6 | $\frac{\partial \ell}{\partial W_1} = \boldsymbol{\delta}_1\,\mathbf{x}^\top$ | $(128 \times 63)$ | same pattern as step 2 |
| 7 | $\frac{\partial \ell}{\partial \mathbf{b}_1} = \boldsymbol{\delta}_1$ | $(128)$ | |

New notation:

- $\boldsymbol{\delta}$ ("bold delta") is the gradient with respect to a layer's $\mathbf{z}$ values. It's the "error signal" at that layer.
- $\boldsymbol{\delta}\,\mathbf{a}^\top$ is an outer product (Linear Algebra §19): a column times a row, which makes a matrix.
- $\odot$ is entry-by-entry multiplication (Linear Algebra §12).
- $\mathbf{1}[\mathbf{z}_1 > 0]$ is a vector with 1 where $z_1 > 0$ and 0 elsewhere.

**Each row matches the tiny example**, with numbers replaced by vectors and matrices. **Every gradient has the same shape as its parameter** (Calculus §8). If yours doesn't, it's wrong.

### Why deep networks can struggle: vanishing gradients

Backpropagation **multiplies** local derivatives along the chain. The sigmoid's slope is at most 0.25 (Calculus §5). Through 10 sigmoid layers, the gradient can shrink by up to $0.25^{10} \approx 0.000001$. Early layers then barely learn.

This is called the **vanishing gradient** problem. ReLU helps, because its slope is exactly 1 for active neurons, so multiplying by it doesn't shrink the signal.

### Exercises

**8.1.** Repeat the tiny example's update with $\alpha = 0.1$ instead. What's the new loss? What went wrong? (Think about Calculus §11.)

**8.2.** In the tiny example, suppose $b_1 = -3$ instead of 0. Redo the forward pass. What happens to $\frac{\partial \ell}{\partial w_1}$, and why?

**8.3.** A network has 784 inputs, 256 hidden neurons, and 10 outputs. Write the shapes of $W_1$, $\mathbf{b}_1$, $W_2$, $\mathbf{b}_2$, and count the parameters.

**8.4.** Write out all 7 backward-pass rows for the 2-layer network from memory, with shapes. Then check against the table.

**8.5.** Why is $\frac{\partial \ell}{\partial W_2} = \boldsymbol{\delta}_2\,\mathbf{a}_1^\top$ and not $\mathbf{a}_1\boldsymbol{\delta}_2^\top$? Use shapes.

<details>
<summary>Hint</summary>

8.2: what does ReLU output for a negative input, and what's its slope there?

</details>

<details>
<summary>Solutions</summary>

**8.1.** $w_2 = 2.1$, $b_2 = 0.1$, $w_1 = 0.9$, $b_1 = 0.2$. New forward: $z_1 = 2.0$, $\hat{y} = 4.3$, $\ell = \frac{1}{2}(1.3)^2 = 0.845$. **The loss went up.** The step was too big: the prediction jumped past the target (3) and landed farther away on the other side.

**8.2.** $z_1 = 1 - 3 = -2$, so $a_1 = 0$ and $\hat{y} = 0$. The ReLU slope is 0, so $\frac{\partial \ell}{\partial z_1} = 0$ and $\frac{\partial \ell}{\partial w_1} = 0$. An inactive ReLU passes no gradient back, so $w_1$ can't learn from this example. (If a neuron is inactive for **every** input, it's called a "dead" neuron.)

**8.3.** $W_1$: $256 \times 784$, $\mathbf{b}_1$: $256$, $W_2$: $10 \times 256$, $\mathbf{b}_2$: $10$. Total: $200{,}704 + 256 + 2{,}560 + 10 = 203{,}530$.

**8.5.** $W_2$ is $10 \times 128$. $\boldsymbol{\delta}_2\mathbf{a}_1^\top$ is $(10 \times 1)(1 \times 128) = 10 \times 128$ ✓. The other order gives $128 \times 10$ ✗.

</details>

---

## 9. Mathematics Final Checkpoint

**This is the gate out of Phase 1.** Closed book, no AI, pencil and paper.

- [ ] **A.** Given $\mathbf{a} = [1, 2, 3]$ and $\mathbf{b} = [4, 5, 6]$, calculate:
  - [ ] the dot product
  - [ ] both lengths
  - [ ] the cosine similarity
- [ ] **B.** Multiply by hand: $\begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}\begin{bmatrix}2 & 0\\1 & 3\end{bmatrix}$ and $\begin{bmatrix}1 & 0 & 2\\-1 & 3 & 1\end{bmatrix}\begin{bmatrix}3 & 1\\2 & 1\\1 & 0\end{bmatrix}$
- [ ] **C.** Differentiate $f(x) = 3x^3 + 2x^2 - 5x + 7$
- [ ] **D.** Find the partial derivatives of $f(x, y) = x^2 + 3xy + y^2$
- [ ] **E.** Explain $\nabla f$: what it is, what its direction means, what its length means
- [ ] **F.** A bag has 3 red and 5 blue balls. Draw 2 without replacement. Find $P(\text{both red})$
- [ ] **G.** Explain conditional probability, with an example where $P(A \mid B) \ne P(B \mid A)$
- [ ] **H.** Explain expected value and variance, and compute both for a fair die
- [ ] **I.** Explain why gradient descent moves in the negative gradient direction

<details>
<summary>Answers</summary>

**A.** $\mathbf{a} = [1,2,3]$, $\mathbf{b} = [4,5,6]$: dot product, both lengths, cosine similarity

*Dot product* — multiply matching entries, add:

$$\mathbf{a} \cdot \mathbf{b} = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32$$

*Lengths* — square each entry, add, take the root:

$$\lVert \mathbf{a} \rVert = \sqrt{1 + 4 + 9} = \sqrt{14} \approx 3.742$$

$$\lVert \mathbf{b} \rVert = \sqrt{16 + 25 + 36} = \sqrt{77} \approx 8.775$$

*Cosine similarity* — the dot product with both lengths divided out, leaving direction only:

$$\cos\theta = \frac{32}{\sqrt{14}\sqrt{77}} = \frac{32}{\sqrt{1078}} \approx \frac{32}{32.833} \approx 0.975$$

Very close to 1, so the two vectors point almost the same way despite $\mathbf{b}$ being more than twice as long. That length-blindness is why embeddings are compared with cosine similarity.

---

**B.** Two matrix products by hand

Entry $(i, j)$ = row $i$ of the left matrix dotted with column $j$ of the right.

*First:* $\begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}\begin{bmatrix}2 & 0\\1 & 3\end{bmatrix}$

- $(1,1)$: $(1)(2) + (2)(1) = 4$
- $(1,2)$: $(1)(0) + (2)(3) = 6$
- $(2,1)$: $(3)(2) + (4)(1) = 10$
- $(2,2)$: $(3)(0) + (4)(3) = 12$

$$= \begin{bmatrix}4 & 6\\10 & 12\end{bmatrix}$$

*Second:* $\begin{bmatrix}1 & 0 & 2\\-1 & 3 & 1\end{bmatrix}\begin{bmatrix}3 & 1\\2 & 1\\1 & 0\end{bmatrix}$

Shapes first: $(2 \times 3)(3 \times 2)$ — inner 3s match ✓, result is $2 \times 2$.

- $(1,1)$: $(1)(3) + (0)(2) + (2)(1) = 3 + 0 + 2 = 5$
- $(1,2)$: $(1)(1) + (0)(1) + (2)(0) = 1$
- $(2,1)$: $(-1)(3) + (3)(2) + (1)(1) = -3 + 6 + 1 = 4$
- $(2,2)$: $(-1)(1) + (3)(1) + (1)(0) = -1 + 3 = 2$

$$= \begin{bmatrix}5 & 1\\4 & 2\end{bmatrix}$$

Watch the signs on that $-1$ — dropping a minus is the most common hand-multiplication slip.

---

**C.** Differentiate $f(x) = 3x^3 + 2x^2 - 5x + 7$

Term by term, via the power rule ($\frac{d}{dx}x^n = nx^{n-1}$): multiply by the exponent, drop the exponent by one.

- $3x^3 \rightarrow 3 \cdot 3x^2 = 9x^2$
- $2x^2 \rightarrow 2 \cdot 2x = 4x$
- $-5x \rightarrow -5$
- $7 \rightarrow 0$ (a constant shifts the curve but changes no slope)

$$f'(x) = 9x^2 + 4x - 5$$

---

**D.** Partial derivatives of $f(x, y) = x^2 + 3xy + y^2$

Differentiate with respect to one variable, treating the other as a frozen constant.

*With respect to $x$* ($y$ held fixed): $x^2 \rightarrow 2x$, $3xy \rightarrow 3y$, $y^2 \rightarrow 0$.

$$\frac{\partial f}{\partial x} = 2x + 3y$$

*With respect to $y$* ($x$ held fixed): $x^2 \rightarrow 0$, $3xy \rightarrow 3x$, $y^2 \rightarrow 2y$.

$$\frac{\partial f}{\partial y} = 3x + 2y$$

*Example:* at $(1, 2)$ these give $8$ and $7$, so $\nabla f(1,2) = [8, 7]$.

---

**E.** Explain $\nabla f$: what it is, what its direction means, what its length means

**What it is:** the vector of all the partial derivatives, $\nabla f = \left[\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right]$. Entry $i$ answers: if I nudge input $i$ a little and hold everything else still, how much does the output move?

**Its direction:** the way of **steepest increase** — the single direction in which $f$ climbs fastest from this point. Proof in one line: the slope along a unit direction $\mathbf{u}$ is $\nabla f \cdot \mathbf{u} = \lVert\nabla f\rVert\cos\theta$, which is largest when $\theta = 0$, i.e. when $\mathbf{u}$ points along the gradient.

**Its length:** how steep that steepest climb is. A long gradient means a sharp slope; a short one means nearly flat terrain.

**At flat points** — minima, maxima, saddles — the gradient is the zero vector: no direction goes uphill. That's the condition optimization solves for, and the reason "set the gradient to zero" is the standard opening move.

---

**F.** 3 red, 5 blue, draw 2 without replacement: $P(\text{both red})$

Without replacement, the second draw's odds depend on the first, so the second factor is conditional.

$$P(\text{1st red}) = \frac{3}{8}$$

$$P(\text{2nd red} \mid \text{1st red}) = \frac{2}{7} \quad \text{(one red gone, one ball gone)}$$

$$P(\text{both red}) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28} \approx 0.107$$

*The trap:* $\frac{3}{8} \times \frac{3}{8}$ would be drawing **with** replacement.

---

**G.** Explain conditional probability, with an example where $P(A \mid B) \ne P(B \mid A)$

$P(A \mid B)$ is the probability of $A$ once the universe shrinks to only the cases where $B$ happened:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

The denominator renormalizes — $B$'s world becomes the new 100%.

*Example:*

$$P(\text{animal} \mid \text{dog}) = 1 \qquad P(\text{dog} \mid \text{animal}) \approx \text{small}$$

Every dog is an animal, but most animals aren't dogs. Same two events, opposite answers.

*Why this matters in practice:* a medical test with 90% detection on a disease affecting 1% of people gives $P(+ \mid \text{sick}) = 0.9$ but $P(\text{sick} \mid +) \approx 0.15$. Confusing the two directions is the base rate fallacy, and it's also exactly the error behind misreading a p-value.

---

**H.** Explain expected value and variance, and compute both for a fair die

**Expected value:** the long-run average, each outcome weighted by its probability. It's the balance point of the distribution, and needn't be an achievable outcome.

$$E[X] = \frac{1}{6}(1+2+3+4+5+6) = \frac{21}{6} = 3.5$$

**Variance:** the average squared distance from that mean — a measure of spread. Using the shortcut $\text{Var}(X) = E[X^2] - (E[X])^2$:

$$E[X^2] = \frac{1}{6}(1 + 4 + 9 + 16 + 25 + 36) = \frac{91}{6} \approx 15.167$$

$$\text{Var}(X) = 15.167 - 12.25 = 2.917 = \frac{35}{12}$$

*Why squared distances:* raw deviations from the mean always sum to exactly zero, cancelling out. Squaring makes them all positive. The price is squared units, which is why the standard deviation $\sqrt{35/12} \approx 1.71$ is usually what gets quoted.

---

**I.** Why does gradient descent move in the negative gradient direction?

Because $-\nabla f$ is provably the steepest descent direction, and the proof is one dot product.

The slope you experience moving along a unit direction $\mathbf{u}$ is the directional derivative:

$$\nabla f \cdot \mathbf{u} = \lVert \nabla f \rVert \lVert \mathbf{u} \rVert \cos\theta = \lVert \nabla f \rVert\cos\theta$$

At a given point $\lVert \nabla f \rVert$ is fixed, so the only adjustable quantity is $\cos\theta$, the angle between your step and the gradient. $\cos\theta$ reaches its minimum of $-1$ at $\theta = 180°$ — directly opposite the gradient. That makes the slope as negative as it can be, so the loss falls fastest.

Hence the update rule:

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla f(\mathbf{w})$$

*The caveat worth stating out loud:* "steepest" is a strictly **local** claim, valid only for a small enough step. It doesn't promise the shortest path to the minimum, and it doesn't promise the *global* minimum — just the best direction from where you're standing. That's also why $\alpha$ matters: too large a step overshoots the region where the linear approximation holds.

</details>

**If you can do all of these, your mathematical foundation is no longer what's holding you back.** Not perfect, but functional. Ask for an oral quiz on Phase 1 before moving to Phase 2.

---

## Code lab — `math/07_ml_math.py`

### What you're doing and why

The goal is **checking your derivations**, not building polished models. (That's the Classical ML phase.) Every gradient you derived by hand gets compared with a numerical estimate. If they match, your math is right.

**Rules:** no AI, no autocomplete, no copying.

### Python you need

- Everything from the earlier code labs.
- `np.c_[np.ones(n), x]` sticks a column of 1s in front of `x` (the bias trick from §3).
- `np.linalg.solve(A, b)` solves $A\mathbf{x} = \mathbf{b}$.
- `np.linalg.lstsq(X, y, rcond=None)[0]` gives the least-squares solution directly.
- `np.outer(a, b)` is the outer product $\mathbf{a}\mathbf{b}^\top$.

### The tasks

```python
import numpy as np

rng = np.random.default_rng(0)

def numerical_gradient(f, w, h=1e-5):
    """Copy this from your 04 code lab. Make it work for vectors AND matrices
    (loop over w.size and use w.flat[i])."""
    ...

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

if __name__ == "__main__":
    # 1) Linear regression three ways (§3). Make data: x = rng.random(200) * 10, y = 3 * x + 2 + rng.normal(0, 1, 200)
    #    Build X with a column of ones.
    #    (a) solve the normal equations with np.linalg.solve
    #    (b) run gradient descent with the gradient (2/n) X^T (Xw - y). Try alpha = 0.01 for 5000 steps.
    #    (c) np.linalg.lstsq
    #    Assert all three agree to 2 decimals. Are they close to [2, 3]? Why not exactly?
    #    Check your gradient formula with numerical_gradient at a random w.

    # 2) Logistic regression (§5). Make data:
    #    class 0: rng.normal([-1, -1], 1, (100, 2)); class 1: rng.normal([1, 1], 1, (100, 2))
    #    Write the BCE cost and its gradient (1/n) X^T (p - y). Check the gradient numerically.
    #    Train with gradient descent. Report accuracy (fraction where (p >= 0.5) equals y).

    # 3) Regularization (§7): add 20 columns of pure random noise to the data from task 1.
    #    Train linear regression with an L2 penalty, and separately with an L1 penalty
    #    (after each step, move each weight toward 0 by alpha*lambda, clipping at 0).
    #    Count how many weights are exactly 0 in each. Which one switched off the noise features?

    # 4) Backpropagation (§8): implement the tiny scalar network.
    #    Assert the gradients match the table: dw2=-1, db2=-1, dw1=-4, db1=-2.
    #    Do one update with alpha=0.05 and assert the new loss is about 0.0078.
    #    Then implement the 2-layer network (ReLU + softmax + cross-entropy) for ONE example
    #    with small sizes (4 inputs, 5 hidden, 3 classes). Check EVERY gradient numerically,
    #    and assert each gradient has the same shape as its parameter.
    print("all checks passed")
```

<details>
<summary>Reference: checking all gradients of the 2-layer network (only after your own attempt)</summary>

```python
def forward_loss(params, x, y_onehot):
    z1 = params["W1"] @ x + params["b1"]
    a1 = np.maximum(0, z1)
    z2 = params["W2"] @ a1 + params["b2"]
    z2 = z2 - z2.max()
    s = np.exp(z2) / np.exp(z2).sum()
    return -np.sum(y_onehot * np.log(s))

def backward(params, x, y_onehot):
    z1 = params["W1"] @ x + params["b1"]
    a1 = np.maximum(0, z1)
    z2 = params["W2"] @ a1 + params["b2"]
    s = np.exp(z2 - z2.max()) / np.exp(z2 - z2.max()).sum()
    d2 = s - y_onehot
    d1 = (params["W2"].T @ d2) * (z1 > 0)
    return {"W2": np.outer(d2, a1), "b2": d2, "W1": np.outer(d1, x), "b1": d1}

params = {"W1": rng.normal(size=(5, 4)), "b1": rng.normal(size=5),
          "W2": rng.normal(size=(3, 5)), "b2": rng.normal(size=3)}
x = rng.normal(size=4)
y_onehot = np.array([0.0, 1.0, 0.0])
grads = backward(params, x, y_onehot)

for name, P in params.items():
    def loss_of(P_new, name=name):
        saved = params[name]
        params[name] = P_new
        value = forward_loss(params, x, y_onehot)
        params[name] = saved
        return value
    numeric = numerical_gradient(loss_of, P.copy())
    assert grads[name].shape == P.shape, name
    assert np.allclose(grads[name], numeric, atol=1e-5), name
```

</details>

---

## Common mistakes

| Mistake | Why it's wrong |
|---|---|
| Thinking cross-entropy was chosen arbitrarily | It's the negative log-likelihood of Bernoulli/categorical data (§5, §6) |
| Using squared error with a sigmoid output | The gradient nearly vanishes when the model is confidently wrong (§5) |
| Confusing "bias" (the added parameter $b$) with "bias" (systematic error, Statistics §9) | Same word, different meanings |
| Confusing $\lambda$ (regularization strength) with $\lambda$ (eigenvalue) | Same letter, different uses |
| Writing $\frac{\partial \ell}{\partial W} = \mathbf{a}\boldsymbol{\delta}^\top$ | Wrong shape. It's $\boldsymbol{\delta}\mathbf{a}^\top$ |
| Stacking layers without an activation | They collapse into one straight-line layer (Functions §5) |
| Low training error = good model | Could be overfitting; always check on new data |
| Trusting a hand-derived gradient without a numerical check | Wrong gradients often still reduce the loss, just badly |

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can define example, feature, target, data matrix, model, parameter, weight, bias, loss, cost, and training.
- [ ] I can explain the difference between squared error and absolute error, and when each is appropriate.
- [ ] I can derive the linear regression gradient for one feature and in matrix form, and check its shape.
- [ ] I can explain why the normal equations from calculus match the ones from geometry.
- [ ] I can do a gradient descent step for linear regression by hand.
- [ ] I can derive that minimizing squared error = maximum likelihood with Gaussian noise.
- [ ] I can derive binary cross-entropy from the Bernoulli likelihood, and its gradient $p - y$.
- [ ] I can explain, with numbers, why squared error fails for classification.
- [ ] I can compute softmax cross-entropy and its gradient $\mathbf{s} - \mathbf{y}$, and interpret the signs.
- [ ] I can explain overfitting, derive L2's weight-decay form, and show with numbers why L1 creates exact zeros.
- [ ] I can explain why neural networks need activations, and write all layer shapes and parameter counts.
- [ ] I can do forward and backward passes for the tiny network by hand, and write the vector backward pass with shapes from memory.
- [ ] I can explain vanishing gradients.
- [ ] **Mathematics Final Checkpoint A–I passed, closed book.**
- [ ] Code lab done without AI; every analytic gradient passes its numerical check.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $\mathbf{x}_i$, $y_i$ | "x sub i," "y sub i" | features and target of example $i$ | §1 |
| $X$ | "X" | data matrix: rows = examples, columns = features | §1 |
| $n$, $d$ | "n," "d" | number of examples, number of features | §1 |
| $\hat{y}$ | "y hat" | prediction | §1 |
| $\boldsymbol{\theta}$ | "theta" | all the model's parameters | §1 |
| $\mathbf{w}$, $b$ | "weights," "bias" | parameters multiplying inputs, and added on | §1 |
| $\ell$ | "loss" | error for one example | §2 |
| $J$ | "J" or "cost" | average loss over all examples | §2 |
| $\varepsilon_i$ | "epsilon sub i" | noise in example $i$ | §4 |
| $\sim$ | "is distributed as" | follows this distribution | §4 |
| $\exp(u)$ | "exp of u" | $e^u$ | §4 |
| $z$ | "z" or "logit" | score before sigmoid/softmax | §5 |
| $p$ | "p" | predicted probability of class 1 | §5 |
| $\mathbf{s}$ | "s" | softmax output probabilities | §6 |
| $\lambda$ | "lambda" | regularization strength | §7 |
| $W$, $\mathbf{b}$ | "W," "bold b" | a layer's weight matrix and bias vector | §8 |
| $\mathbf{a}$ | "a" | a layer's activations (outputs) | §8 |
| $\boldsymbol{\delta}$ | "delta" | gradient with respect to a layer's $\mathbf{z}$ | §8 |
| $\mathbf{1}[\ldots]$ | "indicator" | 1 where the condition is true, 0 elsewhere | §8 |

---

## Resources (only if stuck)

1. **Linear and logistic regression, derived:** [Stanford CS229 lecture notes](https://cs229.stanford.edu/): the sections on linear regression (including its probabilistic interpretation) and logistic regression (§3–§5). More formal than this file, but the same derivations.
2. **Backpropagation intuition:** [3Blue1Brown — Neural Networks](https://www.3blue1brown.com/topics/neural-networks): *What is backpropagation really doing?* and *Backpropagation calculus* (§8).
3. **After this phase:** [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), lecture 1 (building "micrograd"). Watch it **after** you can do §8 by hand, not before.
