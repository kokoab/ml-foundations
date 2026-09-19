# Phase 1 — Mathematics: Start Here

Read this once. It explains how to use every file in this folder.

## Who these files are for

These files assume you know **only basic arithmetic**: + − × ÷, fractions, and negative numbers. Everything else is built from there. Every symbol is explained the first time it appears, and no steps are skipped.

Files 01–06 are **pure theory**. File 07 is where that theory gets **applied** to machine learning.

## The order

| # | File | Hours | What you'll understand after it |
|---|---|---|---|
| 01 | [Algebra](01-Algebra.md) | 6 | Letters, equations, exponents, logs, Σ notation, lines, U-shaped curves |
| 02 | [Functions](02-Functions.md) | 5 | Function notation, composition, inverses, linear vs. nonlinear, $e$, ReLU, sigmoid, softmax |
| 03 | [Linear Algebra](03-Linear-Algebra.md) | 14 | Vectors, dot products, matrices as transformations, determinants, eigenvectors, SVD |
| 04 | [Calculus](04-Calculus.md) | 10 | Derivatives, the chain rule, gradients, finding minimums, gradient descent |
| 05 | [Probability](05-Probability.md) | 7 | Conditional probability, Bayes, expected value, variance, distributions, likelihood |
| 06 | [Statistics](06-Statistics.md) | 5 | Center and spread, correlation, standard error, hypothesis tests, fitting a line |
| 07 | [ML Mathematics](07-ML-Mathematics.md) | 8 | Linear and logistic regression, loss functions, regularization, backpropagation, **and the final checkpoint** |

**Total: about 55 focused hours.** At 15–25 hours a week, that's roughly 3 weeks. If a file takes longer, that's fine: understanding matters more than the calendar.

Linear Algebra is the longest on purpose. It's the foundation for almost everything after it.

## How each file is laid out

Every file has the same structure:

1. **Before you start:** what the file covers and how to read it
2. **Numbered sections.** Each one:
   - starts with **the problem**: why the idea exists
   - builds the idea with **pictures and numbers first**, then the formula
   - explains **every symbol** with a "read it aloud as" note
   - shows **worked examples** step by step, with a "what we did" column
   - ends with **exercises**, with collapsible hints and solutions
   - may have a short **"Why ML cares"** box at the end (motivation only, never needed to understand the math)
3. **Code lab:** a small Python script to write yourself, in the `math/` folder
4. **Common mistakes**
5. **Check yourself:** a closed-book quiz, taken **after** the file
6. **Definition of Done:** a checklist for deciding you've really finished
7. **Symbol cheat sheet**
8. **Resources:** 1–3 links, only for when you're stuck

## How to study each file

1. **Go in order.** Sections build on each other.
2. **For each worked example:** cover the solution and try it yourself first, even if you only get one step.
3. **For each exercise:**
   - **Pass 1:** try it on paper, without looking anything up.
   - **Pass 2:** stuck for more than 10 minutes? Open the **Hint**.
   - **Pass 3:** still stuck? Open the **Solution**, and find the **exact step** where your thinking went a different way. Write that step down.
   - **Pass 4:** the next day, redo every exercise you needed a solution for, without looking.
4. **Do the code lab** in `math/` with Copilot and autocomplete turned off.
5. **Take "Check yourself"** closed book. Reread the section for anything you missed.
6. **Tick the Definition of Done** only when every box is honestly true.
7. **Then ask your tutor for an oral quiz** on the file before moving on. (Attach [TEACHER.md](../../TEACHER.md) when you start the chat.)

## Rules

- **Paper first, code second.** If you can't do it by hand on a tiny example, code will just hide the confusion.
- **Wrong answers are data.** The useful question is "which step broke?", not "what's the answer?"
- **When an earlier idea feels shaky, go back.** Rereading Algebra while doing Calculus is normal, not a failure.
- **No extra videos beyond the listed resources.** Collecting tutorials feels productive but isn't.
- **Behind schedule?** Don't rush. Keep going in order at a pace where you actually understand.
