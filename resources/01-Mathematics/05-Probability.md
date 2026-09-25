# 05 — Probability

**Time: ~7 hours** (spread it over 3 days) · **You need: [01 Algebra](01-Algebra.md), [02 Functions](02-Functions.md), [04 Calculus](04-Calculus.md) §3–§5 and §10 (only for §11)** · **Code lab: `math/05_probability.py`**

## Before you start

**Probability** is the math of **uncertainty**: putting numbers on how likely things are, and reasoning correctly with those numbers. Humans are famously bad at this by intuition, so this file leans heavily on **counting real examples** rather than trusting gut feelings.

**How to read it:**

- Go **in order**. Each section uses the ones before it.
- **When a formula confuses you, imagine 100 or 10,000 people and count.** Almost every probability formula is a shortcut for counting.
- When you see a worked example, **cover the solution and try it first**.
- Say each symbol aloud using its "read it aloud as" note.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.
- The **"Why ML cares"** boxes are motivation only.

**What you'll be able to do by the end:**

- Compute probabilities of combined events, and conditional probabilities
- Use Bayes' theorem correctly, including the "rare event" trap
- Compute expected value and variance, and recognize the common distributions
- Explain likelihood and find the best parameter for some data with maximum likelihood

---

## Contents

1. [What probability is](#1-what-probability-is)
2. [Combining events: not, and, or](#2-combining-events-not-and-or)
3. [Counting](#3-counting)
4. [Conditional probability](#4-conditional-probability)
5. [Independence](#5-independence)
6. [Bayes' theorem](#6-bayes-theorem)
7. [Random variables and distributions](#7-random-variables-and-distributions)
8. [Expected value](#8-expected-value)
9. [Variance and standard deviation](#9-variance-and-standard-deviation)
10. [Common distributions](#10-common-distributions)
11. [Likelihood and maximum likelihood](#11-likelihood-and-maximum-likelihood)
12. [Code lab](#code-lab--math05_probabilitypy)
13. [Check yourself](#check-yourself)

---

## 1. What probability is

### The problem

"There's a 70% chance of rain." "This coin is fair." "One in a million." We use these phrases constantly. What do they actually **mean**, and how do we calculate with them?

### The meaning: long-run frequency

A **probability** is a number from 0 to 1 that says how likely something is.

- $0$ = impossible
- $1$ = certain
- $0.5$ = as likely as not

One useful way to read it: **if you repeated the situation many, many times, the probability is the fraction of times it happens.** A fair coin landing heads with probability 0.5 means that over thousands of flips, about half are heads.

(Probabilities are often written as percentages too: $0.7 = 70\%$.)

### The vocabulary

| Word | Meaning | Die example |
|---|---|---|
| **Experiment** | something with an uncertain result | rolling a die once |
| **Outcome** | one possible result | rolling a 4 |
| **Sample space** | the set of all possible outcomes | $\{1, 2, 3, 4, 5, 6\}$ |
| **Event** | a group of outcomes we care about | "rolling an even number" = $\{2, 4, 6\}$ |

The sample space is written $\Omega$, the capital Greek letter **omega**. The curly brackets $\{\ \}$ mean "the set of" (as in Linear Algebra §8).

### Notation

$P(A)$ is read "**the probability of A**," where $A$ is an event.

### When all outcomes are equally likely

If every outcome is equally likely (a fair die, a fair coin, a well-shuffled deck), just count:

$$
P(A) = \frac{\text{number of outcomes in } A}{\text{total number of outcomes}}
$$

**Example.** Fair die. $P(\text{even}) = \frac{3}{6} = \frac{1}{2}$, because $\{2, 4, 6\}$ has 3 outcomes out of 6.

**Example.** Fair die. $P(\text{at least 5}) = \frac{2}{6} = \frac{1}{3}$, because $\{5, 6\}$.

### Listing outcomes for two things at once

Roll **two** dice. Each die has 6 outcomes, so there are $6 \times 6 = 36$ equally likely pairs. Write them as a grid:

| | **1** | **2** | **3** | **4** | **5** | **6** |
|---|---|---|---|---|---|---|
| **1** | 2 | 3 | 4 | 5 | 6 | **7** |
| **2** | 3 | 4 | 5 | 6 | **7** | 8 |
| **3** | 4 | 5 | 6 | **7** | 8 | 9 |
| **4** | 5 | 6 | **7** | 8 | 9 | 10 |
| **5** | 6 | **7** | 8 | 9 | 10 | 11 |
| **6** | **7** | 8 | 9 | 10 | 11 | 12 |

(Rows = first die, columns = second die, entries = the sum.)

$P(\text{sum is } 7) = \frac{6}{36} = \frac{1}{6}$. Count the bold 7s.

### The basic rules every probability follows

1. Every probability is between 0 and 1: $0 \le P(A) \le 1$.
2. Something in the sample space definitely happens: $P(\Omega) = 1$.
3. The probabilities of all the separate outcomes add up to 1.

> **Why ML cares:** When a model classifies something, it outputs a probability for each possible answer, like "cat: 0.8, dog: 0.15, bird: 0.05." Those must follow these rules: each between 0 and 1, and all adding to 1. That's exactly what softmax (Functions §10) guarantees.

### Exercises

**1.1.** A bag has 3 red, 5 blue, and 2 green marbles. You pick one at random. Find $P(\text{blue})$ and $P(\text{not red})$.

**1.2.** Using the two-dice grid: find $P(\text{sum} = 2)$, $P(\text{sum} \ge 10)$, and $P(\text{both dice show the same number})$.

**1.3.** Flip two coins. List the sample space. What's $P(\text{exactly one head})$?

<details>
<summary>Solutions</summary>

**1.1.** $\frac{5}{10} = 0.5$. $\frac{7}{10} = 0.7$.

**1.2.** $\frac{1}{36}$. Sums 10, 11, 12 appear $3 + 2 + 1 = 6$ times, so $\frac{6}{36} = \frac{1}{6}$. Doubles: 6 of them, so $\frac{1}{6}$.

**1.3.** $\{HH, HT, TH, TT\}$. Exactly one head: $HT$ and $TH$, so $\frac{2}{4} = \frac{1}{2}$.

</details>

---

## 2. Combining events: not, and, or

### "Not": the complement

The event "**not $A$**" contains every outcome that isn't in $A$. It's also written $A^c$ (read "**A complement**").

$$
P(\text{not } A) = 1 - P(A)
$$

**Why:** $A$ and "not $A$" together cover everything, and everything has probability 1.

**This is often the easiest route.** "At least one" questions are much simpler through "not."

**Example.** Roll two dice. $P(\text{at least one six})$?

Counting all the "at least one six" cases directly is messy. Instead:

| Step | What we did |
|---|---|
| "not (at least one six)" = "no sixes at all" | Flipped the question |
| $P(\text{no sixes}) = \frac{5}{6} \times \frac{5}{6} = \frac{25}{36}$ | Each die avoids 6 with probability $\frac{5}{6}$. (Why multiplying works comes in §5.) |
| $P(\text{at least one six}) = 1 - \frac{25}{36} = \frac{11}{36}$ | Complement rule |

### "And": both happen

"**$A$ and $B$**" means both events happen. It's written $A \cap B$ (read "**A intersect B**"). The symbol $\cap$ looks like an upside-down U. Think of it as the **overlap** of the two groups.

### "Or": at least one happens

"**$A$ or $B$**" means $A$ happens, or $B$ happens, or both. It's written $A \cup B$ (read "**A union B**"). The symbol $\cup$ looks like a U. Think of it as **everything in either group**.

### The addition rule

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Why subtract?** Picture two overlapping circles. Adding $P(A)$ and $P(B)$ counts the overlap **twice**, so subtract it once.

**Example.** Roll a die. $A$ = "even" = $\{2, 4, 6\}$. $B$ = "at least 4" = $\{4, 5, 6\}$.

| Piece | Outcomes | Probability |
|---|---|---|
| $A$ | $\{2, 4, 6\}$ | $\frac{3}{6}$ |
| $B$ | $\{4, 5, 6\}$ | $\frac{3}{6}$ |
| $A \cap B$ (overlap) | $\{4, 6\}$ | $\frac{2}{6}$ |
| $A \cup B$ by formula | | $\frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}$ |
| $A \cup B$ by counting | $\{2, 4, 5, 6\}$ | $\frac{4}{6}$ ✓ |

### Mutually exclusive events

If $A$ and $B$ **can't both happen** (like "roll a 1" and "roll a 6"), they're called **mutually exclusive**. Their overlap is empty, so $P(A \cap B) = 0$ and the rule simplifies to $P(A \cup B) = P(A) + P(B)$.

### Exercises

**2.1.** The probability it rains tomorrow is 0.3. What's the probability it doesn't?

**2.2.** Flip 3 coins. Use the complement to find $P(\text{at least one head})$.

**2.3.** In a class, 60% of students study math, 50% study physics, and 30% study both. What percentage study math or physics (or both)?

**2.4.** Roll a die. Are "roll an odd number" and "roll a 2" mutually exclusive? What's $P(\text{odd or 2})$?

<details>
<summary>Solutions</summary>

**2.1.** $0.7$.

**2.2.** $P(\text{no heads}) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$, so $1 - \frac{1}{8} = \frac{7}{8}$.

**2.3.** $60 + 50 - 30 = 80\%$.

**2.4.** Yes (2 isn't odd). $\frac{3}{6} + \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$.

</details>

---

## 3. Counting

### The problem

"Count the outcomes" is easy with a die. But how many ways can you pick 3 people out of 10 for a team? Listing them all takes forever. We need counting shortcuts. (You'll need these for §10.)

### The multiplication principle

If one choice has $a$ options and a second, separate choice has $b$ options, there are $a \times b$ combined options.

**Example.** 3 shirts and 2 pairs of pants give $3 \times 2 = 6$ outfits.

That's why two dice have $6 \times 6 = 36$ outcomes.

### Factorial: arranging things in order

How many ways can 4 people stand in a line?

- 4 choices for first place,
- then 3 people left for second,
- then 2 for third,
- then 1 for last.

$4 \times 3 \times 2 \times 1 = 24$.

This is written $4!$ and read "**four factorial**":

$$
n! = n \times (n - 1) \times \cdots \times 2 \times 1
$$

By definition, $0! = 1$. (There's exactly one way to arrange nothing.)

### Choosing a group where order doesn't matter

How many ways can you pick a **group** of 3 people from 5, where order doesn't matter (Ana-Ben-Cai is the same group as Cai-Ana-Ben)?

| Step | Reasoning |
|---|---|
| Pick 3 **in order** | $5 \times 4 \times 3 = 60$ ways |
| But each group of 3 got counted once per arrangement | A group of 3 can be arranged $3! = 6$ ways |
| So divide out the repeats | $\frac{60}{6} = 10$ groups |

The general formula is called "**n choose k**":

$$
\binom{n}{k} = \frac{n!}{k!\,(n - k)!}
$$

Read $\binom{n}{k}$ aloud as "n choose k." Check: $\binom{5}{3} = \frac{120}{6 \times 2} = 10$ ✓

### Exercises

**3.1.** Calculate $5!$ and $\frac{6!}{4!}$ (cancel before multiplying).

**3.2.** A PIN has 4 digits, each 0–9. How many PINs are possible?

**3.3.** Calculate $\binom{4}{2}$. Then list all the groups of 2 from $\{A, B, C, D\}$ to check.

**3.4.** How many ways can you pick 2 heads positions out of 5 coin flips? (For example, flips 1 and 3 are heads.)

<details>
<summary>Solutions</summary>

**3.1.** $120$. $\frac{6!}{4!} = 6 \times 5 = 30$.

**3.2.** $10^4 = 10{,}000$.

**3.3.** $\frac{24}{2 \times 2} = 6$: AB, AC, AD, BC, BD, CD.

**3.4.** $\binom{5}{2} = 10$.

</details>

---

## 4. Conditional probability

### The problem

Once you **learn something**, probabilities change. The chance a random person is over 180 cm tall is small. The chance a **professional basketball player** is over 180 cm is huge. The extra information shrinks the group you're looking at.

### A table of real counts

100 students were surveyed:

| | Coffee | Tea | **Total** |
|---|---|---|---|
| **First-year** | 15 | 45 | 60 |
| **Second-year** | 30 | 10 | 40 |
| **Total** | 45 | 55 | 100 |

**Question:** if you pick a second-year student, what's the probability they drink coffee?

Only look at the **second-year row**: 30 of those 40 drink coffee. So the answer is $\frac{30}{40} = 0.75$.

You **shrank the universe** from 100 students down to the 40 second-years, then counted inside it.

### Notation

$$
P(\text{coffee} \mid \text{second-year}) = 0.75
$$

The vertical bar $\mid$ is read "**given**." So this reads "the probability of coffee, given second-year."

**What's after the bar is what you already know.** It's the group you've shrunk down to.

### The formula

Counting inside the shrunken group, but using probabilities instead of counts:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

**Check with the table:** $P(\text{coffee} \cap \text{second-year}) = \frac{30}{100} = 0.30$, and $P(\text{second-year}) = \frac{40}{100} = 0.40$. So $\frac{0.30}{0.40} = 0.75$ ✓

In words: of all the probability in $B$, what fraction is also in $A$?

### The direction matters a lot

Now flip it: if you pick a coffee drinker, what's the probability they're a second-year?

Only look at the **coffee column**: 30 of those 45 are second-years. So $P(\text{second-year} \mid \text{coffee}) = \frac{30}{45} \approx 0.667$.

$$
P(\text{coffee} \mid \text{second-year}) = 0.75 \quad\ne\quad P(\text{second-year} \mid \text{coffee}) \approx 0.667
$$

**$P(A \mid B)$ and $P(B \mid A)$ are different questions with different answers.** Mixing them up is one of the most common reasoning errors there is.

An extreme example: $P(\text{is an animal} \mid \text{is a dog}) = 1$, but $P(\text{is a dog} \mid \text{is an animal})$ is tiny.

### The multiplication rule

Rearranging the formula gives a way to find "and" probabilities:

$$
P(A \cap B) = P(A \mid B) \cdot P(B)
$$

**Example.** Draw two cards without putting the first back. $P(\text{both aces})$?

| Step | Value |
|---|---|
| $P(\text{first is ace})$ | $\frac{4}{52}$ |
| $P(\text{second is ace} \mid \text{first was ace})$ | $\frac{3}{51}$ (3 aces left among 51 cards) |
| $P(\text{both aces})$ | $\frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} \approx 0.0045$ |

> **Why ML cares:** Two of the most important numbers for judging a classifier are conditional probabilities in **opposite directions**. "Of the actual spam emails, what fraction did we catch?" and "Of the emails we flagged, what fraction were actually spam?" You'll meet them as **recall** and **precision**.

### Exercises

**4.1.** Using the table: find $P(\text{tea} \mid \text{first-year})$ and $P(\text{first-year} \mid \text{tea})$.

**4.2.** Using the table: find $P(\text{coffee})$ and $P(\text{coffee} \mid \text{first-year})$. Does knowing someone is a first-year change the coffee probability?

**4.3.** Roll a die. Given that the result is even, what's the probability it's a 6?

**4.4.** A bag has 3 red and 5 blue marbles. Draw 2 without replacement. What's $P(\text{both red})$?

<details>
<summary>Solutions</summary>

**4.1.** $\frac{45}{60} = 0.75$ and $\frac{45}{55} \approx 0.818$.

**4.2.** $\frac{45}{100} = 0.45$ and $\frac{15}{60} = 0.25$. Yes, it lowers it a lot.

**4.3.** Shrink to $\{2, 4, 6\}$, so $\frac{1}{3}$.

**4.4.** $\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28} \approx 0.107$.

</details>

---

## 5. Independence

### The idea

Two events are **independent** if knowing one happened **doesn't change** the probability of the other.

A coin flip and a die roll are independent: seeing heads tells you nothing about the die.

### Definition

$$
P(A \mid B) = P(A)
$$

Put that into the multiplication rule from §4, and you get the more common form:

$$
A \text{ and } B \text{ are independent} \quad⟺\quad P(A \cap B) = P(A) \cdot P(B)
$$

**For independent events, "and" means multiply.** That's why we could multiply $\frac{5}{6} \times \frac{5}{6}$ in §2: the two dice don't affect each other.

### Checking independence with numbers

**Coin and die:** $P(\text{heads and 6}) = \frac{1}{12}$ (12 equally likely combinations). And $P(\text{heads}) \cdot P(6) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}$ ✓ **Independent.**

**Cards without replacement:** $P(\text{second ace} \mid \text{first ace}) = \frac{3}{51} \approx 0.059$, but $P(\text{second ace})$ on its own is $\frac{4}{52} \approx 0.077$. **Not independent**, because the first draw changes what's left.

**Coffee survey (§4):** $P(\text{coffee}) = 0.45$ but $P(\text{coffee} \mid \text{first-year}) = 0.25$. **Not independent.**

### Don't confuse independent with mutually exclusive

- **Mutually exclusive:** can't both happen. If one happens, the other definitely didn't. That's a very strong **connection**.
- **Independent:** no connection at all.

(The one exception is events with probability 0, which are both at once, trivially.)

### i.i.d.

When you collect a lot of data, a common assumption is that the data points are **i.i.d.**: **independent and identically distributed**.

- **Independent:** one data point doesn't affect another.
- **Identically distributed:** they all come from the same underlying process.

> **Why ML cares:** Most ML methods assume training examples are i.i.d. When they aren't, results can be badly misleading. For example: if many video clips of the **same person** end up in both the training data and the testing data, they aren't independent. The model can "recognize the person" instead of learning the real task, and the test score will look better than it really is.

### Exercises

**5.1.** Flip a coin 4 times. Using independence, what's $P(\text{all heads})$?

**5.2.** $P(A) = 0.3$, $P(B) = 0.5$, and they're independent. Find $P(A \cap B)$ and $P(A \cup B)$.

**5.3.** Roll a die. $A$ = "even," $B$ = "at most 2" = $\{1, 2\}$. Are $A$ and $B$ independent? Check with numbers.

**5.4.** Explain in your own words why "mutually exclusive" events (with nonzero probabilities) can never be independent.

<details>
<summary>Hint</summary>

5.2: after finding the "and," use the addition rule from §2.
5.3: compute $P(A \cap B)$ by listing outcomes, then compare with $P(A) \cdot P(B)$.

</details>

<details>
<summary>Solutions</summary>

**5.1.** $\left(\frac{1}{2}\right)^4 = \frac{1}{16}$.

**5.2.** $0.15$. $0.3 + 0.5 - 0.15 = 0.65$.

**5.3.** $A \cap B = \{2\}$, probability $\frac{1}{6}$. $P(A)P(B) = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$ ✓. Independent.

**5.4.** If they're mutually exclusive, learning $A$ happened tells you $B$ definitely didn't. That's the opposite of "knowing one tells you nothing about the other."

</details>

---

## 6. Bayes' theorem

### The problem

You often know $P(B \mid A)$ but want $P(A \mid B)$, the **opposite direction**.

A medical test's accuracy tells you $P(\text{positive result} \mid \text{sick})$. But a patient who tests positive wants to know $P(\text{sick} \mid \text{positive result})$. §4 showed these can be very different. **Bayes' theorem** converts one into the other.

### Deriving it (it's one line)

Write the "and" probability two ways, using the multiplication rule from §4:

$$
P(A \cap B) = P(A \mid B)\,P(B) \qquad\text{and}\qquad P(A \cap B) = P(B \mid A)\,P(A)
$$

Both equal the same thing, so set them equal and divide by $P(B)$:

$$
P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}
$$

### Names for each piece

| Piece | Name | Meaning in the medical example |
|---|---|---|
| $P(A)$ | **prior** | how common the disease is, before any test |
| $P(B \mid A)$ | **likelihood** | how often sick people test positive |
| $P(B)$ | **evidence** | how often anyone tests positive |
| $P(A \mid B)$ | **posterior** | chance of being sick, after testing positive |

### Finding the bottom: add up every way $B$ can happen

Usually you don't know $P(B)$ directly. A positive test can happen two ways, sick-and-positive or healthy-and-positive, so add both:

$$
P(B) = P(B \mid A)\,P(A) + P(B \mid \text{not } A)\,P(\text{not } A)
$$

This is called the **law of total probability**.

### Worked example: count first

A disease affects **1%** of people. A test catches **90%** of sick people, but also wrongly flags **5%** of healthy people. You test positive. What's the chance you're sick?

**Most people guess around 90%.** Let's count. Imagine **10,000 people**:

| Group | Count | Test positive |
|---|---|---|
| Sick (1%) | 100 | 90% of 100 = **90** |
| Healthy (99%) | 9,900 | 5% of 9,900 = **495** |
| **Total positives** | | **585** |

Of the 585 people who test positive, only 90 are actually sick:

$$
P(\text{sick} \mid \text{positive}) = \frac{90}{585} \approx 0.154 = 15.4\%
$$

**Same answer with the formula:**

| Piece | Value |
|---|---|
| $P(\text{positive} \mid \text{sick}) \cdot P(\text{sick})$ | $0.90 \times 0.01 = 0.009$ |
| $P(\text{positive} \mid \text{healthy}) \cdot P(\text{healthy})$ | $0.05 \times 0.99 = 0.0495$ |
| $P(\text{positive})$ | $0.009 + 0.0495 = 0.0585$ |
| $P(\text{sick} \mid \text{positive})$ | $\frac{0.009}{0.0585} \approx 0.154$ |

### Why the answer is so low: the base rate

The disease is **rare** (1%). Even a small false-alarm rate, applied to the huge healthy group, produces far more false alarms (495) than real cases (90).

Ignoring how rare something is to begin with is called the **base rate fallacy**. Whenever you're detecting something rare, expect most alarms to be false unless the false-alarm rate is extremely low.

> **Why ML cares:** Any system that flags rare things (fraud, spam, suspicious contracts, defects) runs into exactly this. A detector that "catches 95% of problems" can still be wrong about most of the things it flags. Bayes' theorem is how you figure out what a flag is actually worth.

### Exercises

**6.1.** Derive Bayes' theorem from the multiplication rule, without looking.

**6.2.** A building alarm: break-in attempts happen on 2% of nights. The alarm goes off for 95% of break-ins, and falsely goes off on 10% of normal nights. The alarm goes off. What's the probability of a real break-in? Use 10,000 nights.

**6.3.** In the disease example, what false-alarm rate would make $P(\text{sick} \mid \text{positive})$ equal to 50%?

**6.4.** Two bags: Bag 1 has 3 red and 1 blue marble, Bag 2 has 1 red and 3 blue. You pick a bag at random (50/50), then draw a marble. It's red. What's the probability you picked Bag 1?

<details>
<summary>Hint</summary>

6.3: 50% means the number of true positives equals the number of false positives.
6.4: $P(\text{red} \mid \text{Bag 1}) = \frac{3}{4}$. Imagine repeating this 800 times.

</details>

<details>
<summary>Solutions</summary>

**6.2.** 200 break-in nights give 190 alarms. 9,800 normal nights give 980 alarms. $\frac{190}{1170} \approx 16.2\%$.

**6.3.** Need $9{,}900 \times \text{rate} = 90$, so rate $\approx 0.91\%$.

**6.4.** In 800 tries: 400 from Bag 1 give 300 reds, and 400 from Bag 2 give 100 reds. $\frac{300}{400} = 0.75$.

</details>

---

## 7. Random variables and distributions

### The problem

So far, events have been descriptions ("even," "sick"). But often we care about a **number**: how many heads, how much money won, how tall someone is. We need a way to attach numbers to outcomes and describe how likely each number is.

### Random variable

A **random variable** is a rule that assigns a number to each outcome. (It's a function, from Functions §1, with outcomes as inputs.)

**Example.** Flip two coins. Let $X$ = number of heads.

| Outcome | HH | HT | TH | TT |
|---|---|---|---|---|
| $X$ | 2 | 1 | 1 | 0 |

**Notation:**

- Random variables use **capital letters**: $X$, $Y$.
- A specific value it might take uses a **lowercase** letter: $x$.
- $P(X = x)$ is read "the probability that X equals x."

### Distribution: the probability of each value

The **distribution** of $X$ lists every possible value and its probability:

| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $P(X = x)$ | $\frac{1}{4}$ | $\frac{2}{4}$ | $\frac{1}{4}$ |

The probabilities add up to 1 ✓

For a random variable with separate, countable values (like 0, 1, 2), this table is called the **probability mass function**, or **PMF**, often written $p(x)$.

### Continuous random variables

Some quantities can be **any value** in a range: height, time, temperature. These are **continuous**.

This creates a puzzle: what's the probability someone is **exactly** 170.000000… cm tall? There are infinitely many possible heights, so the chance of any single exact value is **0**.

Instead, we ask about **ranges**: $P(169.5 \le X \le 170.5)$.

### Density and area

A continuous variable is described by a **probability density function (PDF)**, $f(x)$. Its graph is a curve, and:

> **The probability of a range = the area under the curve over that range.**

The total area under the whole curve is 1.

**Notation for area:** the area under $f(x)$ from $a$ to $b$ is written

$$
\int_a^b f(x)\,dx
$$

Read aloud as "**the integral** from a to b of f of x, d x." You won't calculate these by hand in this curriculum. Just read $\int$ as "**the continuous version of $\Sigma$**": adding up infinitely many infinitely thin slices. (The symbol is a stretched-out S, for Sum.)

### Density is not probability

The **height** of a PDF isn't a probability. It's **probability per unit of width**, which means it **can be bigger than 1**.

**Example.** A number chosen uniformly between 0 and 0.25 has a flat PDF. The area must be 1 and the width is 0.25, so the height is $\frac{1}{0.25} = 4$. That's perfectly fine.

> **Why ML cares:** Model predictions are distributions. A classifier gives a PMF over categories. Some models predict a continuous value along with its uncertainty, using a density.

### Exercises

**7.1.** Roll a die. Let $X$ = the number shown. Write its PMF as a table.

**7.2.** Flip 3 coins. Let $X$ = number of heads. Write the PMF. (List all 8 outcomes first.)

**7.3.** A continuous variable is spread evenly between 2 and 6. What's the height of its PDF? What's $P(3 \le X \le 4)$?

**7.4.** Explain why $P(X = 3)$ is 0 for the variable in 7.3, even though 3 is a possible value.

<details>
<summary>Solutions</summary>

**7.1.** Each of 1–6 has probability $\frac{1}{6}$.

**7.2.** 0 heads: $\frac{1}{8}$, 1: $\frac{3}{8}$, 2: $\frac{3}{8}$, 3: $\frac{1}{8}$.

**7.3.** Width 4, so height $\frac{1}{4}$. Area from 3 to 4: $1 \times \frac{1}{4} = 0.25$.

**7.4.** A single point has zero width, so the area above it is zero.

</details>

---

## 8. Expected value

### The problem

A game costs ₱10 to play. You roll a die and win ₱3 times the number shown. **Should you play?** You can't know what one roll will give, but you can ask what happens **on average** over many plays.

### Where the formula comes from

Roll a die 600 times. You'd expect each face about 100 times. The average of all 600 rolls would be:

$$
\frac{100(1) + 100(2) + 100(3) + 100(4) + 100(5) + 100(6)}{600} = 1 \cdot \tfrac{1}{6} + 2 \cdot \tfrac{1}{6} + \cdots + 6 \cdot \tfrac{1}{6} = 3.5
$$

Each value gets weighted by **how often it happens**, which is its probability.

### Definition

The **expected value** of $X$ is the probability-weighted average of its values:

$$
E[X] = \sum_x x \cdot P(X = x)
$$

- Read $E[X]$ aloud as "**the expected value of X**" (or "the mean of X").
- It's also written $\mu$ (Greek **mu**).
- The $\sum_x$ means "add over every possible value $x$."
- For continuous variables, the same idea uses $\int$ instead of $\sum$.

It's the **long-run average**, and it doesn't have to be a value $X$ can actually take. You can't roll a 3.5.

### Worked example: the game

| Die shows | Win | Probability | Win × probability |
|---|---|---|---|
| 1 | ₱3 | $\frac{1}{6}$ | 0.5 |
| 2 | ₱6 | $\frac{1}{6}$ | 1.0 |
| 3 | ₱9 | $\frac{1}{6}$ | 1.5 |
| 4 | ₱12 | $\frac{1}{6}$ | 2.0 |
| 5 | ₱15 | $\frac{1}{6}$ | 2.5 |
| 6 | ₱18 | $\frac{1}{6}$ | 3.0 |
| **Total** | | | **₱10.50** |

Expected winnings ₱10.50, cost ₱10, so on average you gain **₱0.50 per game**.

### Linearity: the most useful property

$$
E[aX + b] = a\,E[X] + b \qquad\text{and}\qquad E[X + Y] = E[X] + E[Y]
$$

**The second one is true even if $X$ and $Y$ are not independent.** That makes it extremely handy.

**Check the game with linearity:** winnings $= 3X$ where $X$ is the die, so $E[3X] = 3 \times 3.5 = 10.5$ ✓. Much faster.

### Expected value of a function of $X$

To find the expected value of something calculated from $X$, like $X^2$, apply the function to each value and weight by the same probabilities:

$$
E[X^2] = \sum_x x^2 \cdot P(X = x)
$$

For a die: $E[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.17$.

**Warning:** $E[X^2] \ne (E[X])^2$ in general. Here $15.17 \ne 3.5^2 = 12.25$. (The difference turns out to be very meaningful. See §9.)

### The law of large numbers

As you repeat an experiment more and more times, the **average of your results gets closer and closer to the expected value**. That's why casinos always win in the long run, even though individual gamblers sometimes win big.

> **Why ML cares:** A model's "true" error is its expected error over all possible data, which is impossible to compute. So ML uses the average error over the data it has, and the law of large numbers is why that's a reasonable estimate.

### Exercises

**8.1.** Flip two coins, $X$ = number of heads (PMF in §7). Find $E[X]$.

**8.2.** A raffle ticket costs ₱20. There's a 1% chance of winning ₱1000 and otherwise nothing. What are the expected winnings? Expected profit?

**8.3.** For a die: find $E[2X + 1]$ two ways, with linearity and directly.

**8.4.** $E[X] = 4$ and $E[Y] = -1$. Find $E[3X - 2Y + 5]$.

<details>
<summary>Solutions</summary>

**8.1.** $0 \cdot \frac{1}{4} + 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} = 1$.

**8.2.** $0.01 \times 1000 = ₱10$. Profit: $10 - 20 = -₱10$ per ticket.

**8.3.** Linearity: $2(3.5) + 1 = 8$. Directly: values $3, 5, 7, 9, 11, 13$ average to $\frac{48}{6} = 8$ ✓

**8.4.** $12 + 2 + 5 = 19$.

</details>

---

## 9. Variance and standard deviation

### The problem

Two games, each costing nothing:

- **Game A:** you always win ₱5.
- **Game B:** flip a coin. Heads you win ₱10, tails you win ₱0.

Both have expected value ₱5. But they feel completely different: A is **guaranteed**, B is **risky**. We need a number for "how spread out" the results are.

### Building the definition

**Idea:** measure how far each result is from the mean, then average those distances.

**Problem:** distances above and below the mean cancel out. For Game B: $(10 - 5) + (0 - 5) = 0$.

**Fix:** **square** the distances first, so they're all positive, then average.

$$
\text{Var}(X) = E\big[(X - \mu)^2\big]
$$

Read $\text{Var}(X)$ aloud as "**the variance of X**." Here $\mu = E[X]$ is the mean.

### Calculating it

**Game A:** always 5, so every distance is 0. $\text{Var} = 0$. No spread at all.

**Game B:**

| Result | Probability | Distance from 5 | Squared | × probability |
|---|---|---|---|---|
| 10 | 0.5 | 5 | 25 | 12.5 |
| 0 | 0.5 | −5 | 25 | 12.5 |
| | | | **Variance** | **25** |

### Standard deviation: back to normal units

Variance is in **squared** units (squared pesos, which is weird). Taking the square root brings it back to normal units:

$$
\sigma = \sqrt{\text{Var}(X)}
$$

This is the **standard deviation**, written with $\sigma$ (lowercase Greek sigma). For Game B, $\sigma = \sqrt{25} = ₱5$: results are typically about ₱5 away from the mean.

**Symbol warning:** $\sigma$ has now meant the sigmoid function (Functions §9), a singular value (Linear Algebra §19), and standard deviation. Always check the context. In probability and statistics, it almost always means standard deviation.

### A shortcut formula

$$
\text{Var}(X) = E[X^2] - \mu^2
$$

**Why:**

| Step | What we did |
|---|---|
| $E[(X - \mu)^2]$ | Definition |
| $= E[X^2 - 2\mu X + \mu^2]$ | Expanded the square |
| $= E[X^2] - 2\mu\,E[X] + \mu^2$ | Linearity ($\mu$ is just a fixed number) |
| $= E[X^2] - 2\mu^2 + \mu^2$ | $E[X] = \mu$ |
| $= E[X^2] - \mu^2$ | |

**Die example:** $E[X^2] = 15.17$ (from §8) and $\mu = 3.5$. So $\text{Var} = 15.17 - 12.25 = 2.92$, and $\sigma \approx 1.71$.

### Variance rules

| Rule | Why |
|---|---|
| $\text{Var}(X + b) = \text{Var}(X)$ | Shifting everything doesn't change the spread |
| $\text{Var}(aX) = a^2\,\text{Var}(X)$ | Scaling by $a$ scales distances by $a$, and squared distances by $a^2$ |
| $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ | **Only if $X$ and $Y$ are independent** |

### Averaging reduces spread

Average $n$ independent copies of $X$ (each with variance $\sigma^2$):

| Step | Result |
|---|---|
| $\text{Var}(X_1 + \cdots + X_n)$ | $n\sigma^2$ (independent, so variances add) |
| $\text{Var}\left(\frac{1}{n}(X_1 + \cdots + X_n)\right)$ | $\frac{1}{n^2} \cdot n\sigma^2 = \frac{\sigma^2}{n}$ (scaling rule) |

**The average of $n$ independent measurements has $n$ times less variance** than a single measurement. That's why averaging more data gives more reliable answers.

> **Why ML cares:** Spread is everywhere in ML: how much predictions vary, how noisy measurements are, and how stable training is. Models often learn from small random batches of data, and bigger batches average more examples, so they give less noisy (lower variance) signals. Many neural network layers also explicitly compute a mean and variance to rescale their numbers.

### Exercises

**9.1.** For two coin flips, $X$ = number of heads ($E[X] = 1$). Find $\text{Var}(X)$ using the definition.

**9.2.** For a die, find $\text{Var}(3X + 2)$.

**9.3.** A variable is 1 with probability $p$ and 0 otherwise. Find its mean and variance in terms of $p$.

**9.4.** Using 9.3: which $p$ gives the largest variance? Why does that make sense?

**9.5.** One measurement has standard deviation 10. What's the standard deviation of the average of 100 independent measurements?

<details>
<summary>Hint</summary>

9.3: since the values are 0 and 1, $X^2 = X$. So $E[X^2] = E[X]$.
9.5: find the variance first, then take the square root.

</details>

<details>
<summary>Solutions</summary>

**9.1.** $(0 - 1)^2 \cdot \frac{1}{4} + (1 - 1)^2 \cdot \frac{1}{2} + (2 - 1)^2 \cdot \frac{1}{4} = \frac{1}{2}$.

**9.2.** $9 \times 2.92 \approx 26.25$.

**9.3.** Mean $p$. $E[X^2] = p$, so $\text{Var} = p - p^2 = p(1 - p)$.

**9.4.** $p = 0.5$: the most uncertain case. At $p = 0$ or $p = 1$ the result is certain, so there's no spread.

**9.5.** Variance $\frac{100}{100} = 1$, so standard deviation 1.

</details>

---

## 10. Common distributions

### The problem

Certain patterns of randomness show up again and again. Instead of building a PMF from scratch every time, we give these patterns names and learn them once.

### Bernoulli: one yes/no trial

One trial that succeeds (1) with probability $p$, or fails (0) otherwise. A single coin flip, or whether one email is spam.

$$
P(X = 1) = p, \quad P(X = 0) = 1 - p
$$

A compact way to write both at once:

$$
P(X = x) = p^x(1 - p)^{1 - x}
$$

(Check: $x = 1$ gives $p^1(1 - p)^0 = p$, and $x = 0$ gives $p^0(1 - p)^1 = 1 - p$ ✓)

Mean $p$, variance $p(1 - p)$ (from §9, exercise 9.3).

### Binomial: counting successes in $n$ trials

Repeat a Bernoulli trial $n$ independent times, and count the successes.

**Building the formula:** $P(\text{exactly 2 heads in 3 fair flips})$?

| Step | Reasoning |
|---|---|
| Sequences with exactly 2 heads | HHT, HTH, THH: that's $\binom{3}{2} = 3$ of them (§3) |
| Probability of each specific sequence | $\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$ (independent) |
| Add them up | $3 \times \frac{1}{8} = \frac{3}{8}$ |

In general, with success probability $p$:

$$
P(X = k) = \binom{n}{k}p^k(1 - p)^{n - k}
$$

In words: (number of ways to place $k$ successes) × (probability of $k$ successes) × (probability of the rest failing).

Mean $np$, variance $np(1 - p)$. (It's a sum of $n$ independent Bernoullis, so means and variances add.)

### Categorical: one trial with $K$ options

Like Bernoulli, but with more than two options: one die roll, or one classification into $K$ categories. Each option $k$ has probability $p_k$, and they add to 1.

### Uniform: everything equally likely

- **Discrete:** a fair die.
- **Continuous:** a flat density over a range $[a, b]$, with height $\frac{1}{b - a}$ (§7).

### Gaussian (normal): the bell curve

This is the most important continuous distribution. It describes quantities that come from **adding up many small, independent effects**, like heights or measurement errors.

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

It looks scary, so decode it piece by piece:

| Piece | What it does |
|---|---|
| $\mu$ | the **center** (mean) of the bell |
| $\sigma$ | the **width** (standard deviation) |
| $(x - \mu)^2$ | squared distance from the center |
| $\frac{(x - \mu)^2}{2\sigma^2}$ | that distance, measured relative to the width |
| $e^{-(\ldots)}$ | equals 1 at the center, and shrinks fast as you move away (Functions §6) |
| $\frac{1}{\sqrt{2\pi\sigma^2}}$ | a fixed number that makes the total area exactly 1 |

**The shape comes entirely from $e^{-(\text{distance})^2}$**: highest at the center, symmetric, and fading quickly on both sides.

It's written $\mathcal{N}(\mu, \sigma^2)$, read "**normal with mean mu and variance sigma squared**."

**Values for $\mathcal{N}(0, 1)$** (the **standard normal**):

| $x$ | 0 | ±1 | ±2 | ±3 |
|---|---|---|---|---|
| $f(x)$ | 0.399 | 0.242 | 0.054 | 0.004 |

### The 68–95–99.7 rule

For **any** Gaussian:

- about **68%** of values fall within $1\sigma$ of the mean
- about **95%** within $2\sigma$
- about **99.7%** within $3\sigma$

**Example.** Heights are $\mathcal{N}(165, 7^2)$ cm. About 95% of people are between $165 - 14 = 151$ and $165 + 14 = 179$ cm.

### Standardizing: the z-score

Any Gaussian can be turned into the standard normal by measuring "how many standard deviations from the mean":

$$
z = \frac{x - \mu}{\sigma}
$$

A 179 cm person has $z = \frac{179 - 165}{7} = 2$: two standard deviations above average.

> **Why ML cares:** Bernoulli describes yes/no predictions, categorical describes multi-class predictions, and the Gaussian describes noise and measurement error. In the ML Mathematics file, you'll see that choosing a distribution **determines** which error formula a model should use.

### Exercises

**10.1.** A Bernoulli variable has $p = 0.3$. Use the compact formula to find $P(X = 0)$.

**10.2.** $P(\text{exactly 3 heads in 5 fair flips})$?

**10.3.** A student guesses randomly on 10 true/false questions. What's the expected number correct? The variance?

**10.4.** A process succeeds 80% of the time on each independent step. What's the probability all 10 steps succeed? What does that tell you about long chains of steps?

**10.5.** Test scores are $\mathcal{N}(70, 10^2)$. About what percent score between 60 and 80? Above 90?

**10.6.** Find the z-score of a score of 55 on that test.

<details>
<summary>Hint</summary>

10.4: "all succeed" is a binomial with $k = n$, or just multiply.
10.5: "above 90" is beyond $2\sigma$. 95% are within, so 5% are outside, split evenly between the two sides.

</details>

<details>
<summary>Solutions</summary>

**10.1.** $0.3^0 \cdot 0.7^1 = 0.7$.

**10.2.** $\binom{5}{3} \cdot \frac{1}{32} = \frac{10}{32} = 0.3125$.

**10.3.** $np = 5$, $np(1 - p) = 2.5$.

**10.4.** $0.8^{10} \approx 0.107$. Only about 11%. Small per-step failure rates compound badly over long chains.

**10.5.** About 68%. About 2.5%.

**10.6.** $\frac{55 - 70}{10} = -1.5$.

</details>

---

## 11. Likelihood and maximum likelihood

### The problem

So far, we've **known** the probabilities (a fair coin has $p = 0.5$) and calculated what data to expect.

Now flip it around: you **observed some data** (7 heads in 10 flips) but you **don't know** $p$. What's the best guess for $p$?

This flip from "known process, predict data" to "known data, figure out the process" is the heart of how ML learns from data.

### The parameter $\theta$

The unknown number that controls a distribution (like $p$ for a coin) is called a **parameter**. Generically, parameters are written $\theta$ ("theta").

**Symbol warning:** $\theta$ meant an angle in Linear Algebra §4. Here it means "whatever parameter the distribution has."

### Likelihood

The **likelihood** of a parameter value is **the probability of the data you actually saw, if the parameter had that value**:

$$
\mathcal{L}(\theta) = P(\text{observed data} \mid \theta)
$$

Read $\mathcal{L}(\theta)$ aloud as "**the likelihood of theta**."

**It's the same formula as probability, read in a different direction:**

| | What's fixed | What varies |
|---|---|---|
| **Probability** | the parameter | the data |
| **Likelihood** | the data (what you saw) | the parameter (your guess) |

### Worked example: the coin

You saw 7 heads and 3 tails. For a coin with heads probability $p$, one specific sequence with 7 heads and 3 tails has probability $p^7(1 - p)^3$. (The $\binom{10}{7}$ factor is the same for every $p$, so it doesn't affect which $p$ is best, and we can leave it out.)

$$
\mathcal{L}(p) = p^7(1 - p)^3
$$

Try some guesses:

| Guess $p$ | $\mathcal{L}(p) = p^7(1 - p)^3$ |
|---|---|
| 0.3 | 0.0000750 |
| 0.5 | 0.000977 |
| **0.7** | **0.002224** ← highest |
| 0.9 | 0.000478 |

$p = 0.7$ makes the observed data **most probable**.

### Maximum likelihood estimation (MLE)

Choose the parameter value with the **highest likelihood**:

$$
\hat{\theta} = \arg\max_\theta\ \mathcal{L}(\theta)
$$

- $\hat{\theta}$ ("theta hat") = the best estimate. (The hat means "estimate" here.)
- $\arg\max_\theta$ is read "**the argument that maximizes**," meaning "**the value of $\theta$** that makes this biggest."

**$\arg\max$ vs. $\max$:** $\max$ gives the biggest **output**, and $\arg\max$ gives the **input** that produces it. In the table: $\max \mathcal{L} = 0.002224$, but $\arg\max = 0.7$.

### Take the log first

Likelihoods of lots of data are products of many small numbers, which underflow on computers (Algebra §4). And products are awkward to differentiate. So we maximize the **log-likelihood** instead:

$$
\ell(\theta) = \ln\mathcal{L}(\theta)
$$

Because $\ln$ is increasing (Functions §7), **the same $\theta$ maximizes both**.

For independent data points, the log turns the product into a sum (Algebra §5, product notation):

$$
\ln\left(\prod_i P(x_i \mid \theta)\right) = \sum_i \ln P(x_i \mid \theta)
$$

### Solving the coin exactly with calculus

$k$ heads in $n$ flips. Find the best $p$:

| Step | What we did |
|---|---|
| $\mathcal{L}(p) = p^k(1 - p)^{n - k}$ | Likelihood |
| $\ell(p) = k\ln p + (n - k)\ln(1 - p)$ | Took $\ln$ (Algebra §4, Rules 1 and 3) |
| $\ell'(p) = \frac{k}{p} - \frac{n - k}{1 - p}$ | Differentiated (Calculus §4–§5; the inside $1 - p$ has derivative $-1$) |
| $\frac{k}{p} = \frac{n - k}{1 - p}$ | Set to zero to find the peak (Calculus §10) |
| $k(1 - p) = (n - k)p$ | Cross-multiplied |
| $k - kp = np - kp$ | Expanded |
| $\hat{p} = \frac{k}{n}$ | The $-kp$ cancels on both sides |

**The best estimate is the fraction of heads you saw**: $\frac{7}{10} = 0.7$ ✓ (matches the table). The intuitive answer turns out to be the mathematically optimal one.

### From "maximize" to "minimize"

Maximizing $\ell(\theta)$ is the same as **minimizing $-\ell(\theta)$**, the **negative log-likelihood**. It's the same peak, flipped upside down into a valley.

> **Why ML cares:** This is the bridge from probability to machine learning. Training a model means choosing its parameters to make the training data as likely as possible, which is the same as minimizing the negative log-likelihood. Many of the "error" formulas used to train models are exactly this. You'll derive them in the ML Mathematics file.

### Exercises

**11.1.** You observe $[1, 0, 1, 1]$ from a Bernoulli$(p)$. Write $\mathcal{L}(p)$. Calculate $\mathcal{L}(0.5)$ and $\mathcal{L}(0.75)$. What's the MLE?

**11.2.** Explain the difference between $\max$ and $\arg\max$ using $f(x) = -(x - 3)^2 + 10$.

**11.3.** Explain in plain words the difference between "the probability of the data given $p$" and "the likelihood of $p$."

**11.4.** *(Challenge)* Data $x_1, \ldots, x_n$ comes from $\mathcal{N}(\mu, \sigma^2)$ with $\sigma$ known. Show that the MLE of $\mu$ is the average $\bar{x}$.

<details>
<summary>Hint</summary>

11.4: $\ln f(x_i) = -\frac{(x_i - \mu)^2}{2\sigma^2} + (\text{a number that doesn't involve } \mu)$. Add these up over all $i$, differentiate with respect to $\mu$, and set to zero.

</details>

<details>
<summary>Solutions</summary>

**11.1.** $p^3(1 - p)$. $\mathcal{L}(0.5) = 0.0625$. $\mathcal{L}(0.75) = 0.421875 \times 0.25 \approx 0.105$. MLE $= \frac{3}{4} = 0.75$.

**11.2.** The biggest value is $\max f = 10$. The input that gives it is $\arg\max f = 3$.

**11.3.** They're the same number. "Probability of the data" treats $p$ as known and asks about the data. "Likelihood of $p$" treats the data as known and compares different values of $p$.

**11.4.** $\ell(\mu) = -\frac{1}{2\sigma^2}\sum_i (x_i - \mu)^2 + \text{const}$. Derivative: $\frac{1}{\sigma^2}\sum_i (x_i - \mu) = 0$, so $\sum_i x_i = n\mu$ and $\hat{\mu} = \bar{x}$.

</details>

---

## Code lab — `math/05_probability.py`

### What you're doing and why

You'll **simulate** random experiments millions of times and check that the results match your formulas. When a formula and a simulation disagree, one of them is wrong. That's the best way to catch reasoning errors in probability.

**Rules:** no AI, no autocomplete, no copying.

### Python you need

- `rng = np.random.default_rng(0)` makes a random number generator (the 0 makes the results repeatable).
- `rng.random(n)` gives `n` random numbers between 0 and 1.
- `rng.random(n) < 0.3` gives an array of `True`/`False`, where each is `True` with probability 0.3. That's a simulated Bernoulli.
- `rng.integers(1, 7, size=n)` gives `n` die rolls (1 to 6).
- `rng.normal(mu, sigma, size=n)` gives Gaussian samples.
- `np.mean(bool_array)` gives the fraction that are `True`.
- `a & b` is elementwise "and" for boolean arrays.
- `np.cumsum(x)` gives running totals.

### The tasks

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb   # comb(n, k) is "n choose k"

rng = np.random.default_rng(0)

if __name__ == "__main__":
    # 1) Bayes (§6): simulate 1,000,000 people.
    #    Each is sick with probability 0.01.
    #    Sick people test positive with probability 0.90; healthy people with probability 0.05.
    #    Compute P(sick | positive) from the simulated counts. Assert it's within 0.01 of 0.154.

    # 2) Expected value and variance (§8, §9): simulate 100,000 die rolls.
    #    Assert the mean is within 0.05 of 3.5 and the variance within 0.05 of 2.917.

    # 3) Law of large numbers (§8): plot the running average of the die rolls
    #    (running total / number of rolls so far). Draw a horizontal line at 3.5.

    # 4) Binomial (§10): simulate 5 fair flips, 100,000 times. Count how often there are exactly 3 heads.
    #    Compare with comb(5, 3) * 0.5**5.

    # 5) Compounding (§10): simulate 100,000 chains of 10 steps, each succeeding with probability 0.8.
    #    Assert the fraction where all 10 succeed is within 0.01 of 0.107.

    # 6) 68-95-99.7 (§10): draw 100,000 samples from N(165, 7^2).
    #    Print the fraction within 1, 2, and 3 standard deviations of the mean.

    # 7) Maximum likelihood (§11): for 7 heads in 10 flips, compute the log-likelihood
    #    7*ln(p) + 3*ln(1-p) for p = 0.01, 0.02, ..., 0.99. Plot it.
    #    Find the p with the largest value (np.argmax gives its position). Assert it's 0.70.
    print("all checks passed")
```

Before task 1, **predict** the answer from your gut. After, compare.

<details>
<summary>Reference solution for tasks 1, 3, and 7 (only after your own attempt)</summary>

```python
# 1
n = 1_000_000
sick = rng.random(n) < 0.01
test_if_sick = rng.random(n) < 0.90
test_if_healthy = rng.random(n) < 0.05
positive = np.where(sick, test_if_sick, test_if_healthy)
p = np.sum(sick & positive) / np.sum(positive)
assert abs(p - 0.154) < 0.01

# 3
rolls = rng.integers(1, 7, size=100_000)
running_average = np.cumsum(rolls) / np.arange(1, len(rolls) + 1)
plt.plot(running_average)
plt.axhline(3.5)
plt.xscale("log")
plt.show()

# 7
ps = np.arange(1, 100) / 100
log_likelihood = 7 * np.log(ps) + 3 * np.log(1 - ps)
best = ps[np.argmax(log_likelihood)]
assert round(best, 2) == 0.70
```

</details>

---

## Common mistakes

| Mistake | Why it's wrong |
|---|---|
| Treating $P(A \mid B)$ and $P(B \mid A)$ as the same | §4: $0.75$ vs $0.667$ from the same table |
| Ignoring how rare something is (base rate) | §6: a "90% accurate" test can still be right only 15% of the time when it says positive |
| Multiplying probabilities that aren't independent | Cards without replacement: $\frac{4}{52} \cdot \frac{4}{52}$ is wrong; it's $\frac{4}{52} \cdot \frac{3}{51}$ |
| Adding "or" probabilities without subtracting the overlap | Double-counts outcomes in both events |
| Confusing mutually exclusive with independent | They're nearly opposites (§5) |
| Treating a PDF's height as a probability | It can be larger than 1. Only areas are probabilities |
| $E[X^2] = (E[X])^2$ | For a die: $15.17 \ne 12.25$ |
| $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ always | Only for independent variables |
| Mixing up $\sigma$ (standard deviation) and $\sigma^2$ (variance) | $\mathcal{N}(0, 4)$ has standard deviation 2, not 4 |
| Calling likelihood "the probability that the parameter is correct" | It's the probability of the data, compared across parameter values |

---

## Check yourself

Do this **after** working through the file. Closed book, 20 minutes.

1. Fair die: find $P(\text{even})$ and $P(\ge 5)$.
2. Flip two fair coins. Find $P(\text{at least one head})$.
3. $A$ and $B$ are independent, $P(A) = 0.3$, $P(B) = 0.5$. Find $P(A \cap B)$ and $P(A \cup B)$.
4. A disease affects 1% of people. A test catches 90% of sick people and falsely flags 5% of healthy people. You test positive. What's the probability you're sick?
5. Fair die: find $E[X]$ and $\text{Var}(X)$.
6. Flip a fair coin 3 times. Find $P(\text{exactly 2 heads})$.
7. 7 heads in 10 flips. What's the maximum likelihood estimate of $P(\text{heads})$?
8. Can a PDF have a value of 3 somewhere? Why?
9. A bag has 3 red and 5 blue balls. Draw 2 without replacement. Find $P(\text{both red})$.
10. Explain conditional probability in your own words, with an example where $P(A \mid B) \ne P(B \mid A)$.
11. Explain expected value and variance in your own words.
12. Explain the difference between probability and likelihood.

<details>
<summary>Answers</summary>

**1.** Fair die: $P(\text{even})$ and $P(\ge 5)$ → §1

When every outcome is equally likely, probability is just counting:

$$P(\text{event}) = \frac{\text{outcomes in the event}}{\text{total outcomes}}$$

The sample space is $\{1,2,3,4,5,6\}$, so 6 total outcomes.

*Even:* $\{2, 4, 6\}$, that's 3 outcomes.

$$P(\text{even}) = \frac{3}{6} = \frac{1}{2}$$

*At least 5:* $\{5, 6\}$, that's 2 outcomes.

$$P(\ge 5) = \frac{2}{6} = \frac{1}{3}$$

---

**2.** Two fair coins: $P(\text{at least one head})$ → §2

*The slow way — list the sample space.* Four equally likely outcomes: HH, HT, TH, TT. Three contain at least one head, so $\frac{3}{4}$.

*The fast way — use the complement.* "At least one head" is awkward to count directly, but its opposite is a single outcome: **no heads at all**.

$$P(\text{no heads}) = P(TT) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

$$P(\text{at least one head}) = 1 - \frac{1}{4} = \frac{3}{4}$$

*The habit worth keeping:* whenever you see "at least one," reach for the complement first. With 10 coins, listing 1024 outcomes is hopeless, but $1 - (\frac{1}{2})^{10}$ takes seconds.

---

**3.** Independent $A, B$ with $P(A) = 0.3$, $P(B) = 0.5$ → §2, §5

*Intersection ("both").* Independence is exactly what licenses multiplying:

$$P(A \cap B) = P(A) \cdot P(B) = 0.3 \times 0.5 = 0.15$$

*Union ("either").* Use the addition rule, subtracting the overlap:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.3 + 0.5 - 0.15 = 0.65$$

*Why subtract:* adding $P(A)$ and $P(B)$ counts the region where both happen **twice**, once in each term. Removing one copy fixes it. Skipping this step would give $0.8$, which is too big.

---

**4.** Disease: 1% prevalence, 90% detection, 5% false positives. You test positive — how likely are you sick? → §6

*The counting method: imagine 10,000 people.*

| | Sick (1% = 100) | Healthy (99% = 9,900) |
|---|---|---|
| **Test positive** | $90\% \times 100 = 90$ | $5\% \times 9{,}900 = 495$ |
| **Test negative** | 10 | 9,405 |

Positive tests total $90 + 495 = 585$. Of those, only 90 are actually sick:

$$P(\text{sick} \mid \text{positive}) = \frac{90}{585} \approx 0.154 = 15.4\%$$

*The same thing via Bayes:*

$$P(S \mid +) = \frac{P(+ \mid S)P(S)}{P(+)} = \frac{(0.9)(0.01)}{(0.9)(0.01) + (0.05)(0.99)} = \frac{0.009}{0.0585} \approx 0.154$$

*Why the answer feels wrong:* a "90% accurate" test sounds nearly certain, yet a positive result leaves you 85% likely to be fine. The reason is the base rate: healthy people outnumber sick people 99 to 1, so even a small 5% error rate applied to that huge group produces far more false positives (495) than the test produces true positives (90). Rare disease + imperfect test = most positives are false. Ignoring that is the **base rate fallacy**.

---

**5.** Fair die: $E[X]$ and $\text{Var}(X)$ → §8, §9

*Expected value* — each outcome weighted by its probability:

$$E[X] = \frac{1}{6}(1 + 2 + 3 + 4 + 5 + 6) = \frac{21}{6} = 3.5$$

Note that 3.5 is never actually rolled. Expected value is a long-run average, not a prediction.

*Variance* — the average squared distance from the mean. Use the shortcut $\text{Var}(X) = E[X^2] - (E[X])^2$.

$$E[X^2] = \frac{1}{6}(1 + 4 + 9 + 16 + 25 + 36) = \frac{91}{6} \approx 15.167$$

$$\text{Var}(X) = \frac{91}{6} - (3.5)^2 = 15.167 - 12.25 = 2.917 = \frac{35}{12}$$

*Sanity check:* the standard deviation is $\sqrt{2.917} \approx 1.71$. Typical rolls land within about 1.7 of 3.5, i.e. roughly 1.8 to 5.2 — reasonable for a spread of 1 to 6 ✓

---

**6.** Three fair flips: $P(\text{exactly 2 heads})$ → §10

*Step 1 — how many arrangements give 2 heads out of 3 flips?*

$$\binom{3}{2} = \frac{3!}{2!\,1!} = 3$$

Namely HHT, HTH, THH.

*Step 2 — probability of any one such sequence:* each flip is independent with probability $\frac{1}{2}$:

$$\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^1 = \frac{1}{8}$$

*Step 3 — multiply, since the 3 arrangements are mutually exclusive:*

$$3 \times \frac{1}{8} = \frac{3}{8}$$

This is the binomial formula $\binom{n}{k}p^k(1-p)^{n-k}$, assembled from scratch: *count the arrangements, then weight each by its probability.*

---

**7.** 7 heads in 10 flips: maximum likelihood estimate of $P(\text{heads})$ → §11

$$\hat{p} = \frac{7}{10} = 0.7$$

*Why that's the MLE, not just the obvious guess.* The likelihood of seeing this exact data, for a candidate value $p$, is:

$$L(p) = \binom{10}{7}p^7(1-p)^3$$

Maximum likelihood asks: which $p$ makes the observed data most probable? Differentiating $\ln L$ and setting it to zero gives $\frac{7}{p} - \frac{3}{1-p} = 0$, which solves to $p = 0.7$. In general, the MLE for a coin is $\frac{\text{heads}}{\text{flips}}$.

*Worth noticing:* the MLE picks the value that best explains the data *and nothing else*. With only 10 flips, 0.7 is a shaky estimate for a coin that may well be fair — MLE reports no uncertainty on its own.

---

**8.** Can a PDF have a value of 3? → §7

Yes. A probability density function can take any non-negative value, including values above 1.

*Why that isn't a contradiction:* density is not probability. For a continuous variable, probability is the **area** under the curve, not the height of it. The rule the PDF must satisfy is that its total area equals 1 — the height is unconstrained.

*Concrete example:* a uniform distribution on $[0, \frac{1}{3}]$ has height exactly 3 across that interval. Area $= 3 \times \frac{1}{3} = 1$ ✓ Squeeze the same probability into a narrower interval and the curve simply gets taller.

*Related fact:* for a continuous variable, $P(X = \text{exactly } 2.5) = 0$, because a single point has zero width and therefore zero area. Only intervals carry probability.

---

**9.** 3 red, 5 blue, draw 2 without replacement: $P(\text{both red})$ → §4

"Without replacement" means the second draw's odds depend on the first — so use the multiplication rule with a **conditional** second factor.

*First draw:* 3 red out of 8 balls.

$$P(\text{1st red}) = \frac{3}{8}$$

*Second draw, given the first was red:* one red is gone and the bag is smaller — 2 red out of 7.

$$P(\text{2nd red} \mid \text{1st red}) = \frac{2}{7}$$

*Multiply:*

$$P(\text{both red}) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28} \approx 0.107$$

*The trap:* using $\frac{3}{8} \times \frac{3}{8}$. That would be drawing **with** replacement, where the first ball goes back and the events are independent.

---

**10.** Conditional probability in your own words → §4

$P(A \mid B)$ is the probability of $A$ **after shrinking the universe down to the cases where $B$ already happened**. You're no longer asking about everyone, only about the $B$ group. That's what the formula does mechanically:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

The bottom renormalizes: $B$'s world becomes the new 100%.

*Example where direction matters:*

$$P(\text{animal} \mid \text{dog}) = 1 \quad\text{— every dog is an animal}$$

$$P(\text{dog} \mid \text{animal}) \approx \text{small} \quad\text{— most animals aren't dogs}$$

Same two events, wildly different answers. Swapping the two sides of the bar changes the question entirely, and mixing them up is exactly the error behind the disease-test surprise in Q4: $P(\text{positive} \mid \text{sick}) = 0.9$, but $P(\text{sick} \mid \text{positive}) = 0.154$.

---

**11.** Expected value and variance in your own words → §8, §9

**Expected value** is the long-run average if you repeated the random process forever, with each outcome weighted by how often it shows up. It's the balance point of the distribution, and it need not be an outcome you can actually observe (a die's 3.5).

**Variance** is the average squared distance from that mean — how spread out the outcomes are. Small variance means results cluster tightly around the average; large variance means they scatter.

*Why squared distances:* plain distances would cancel out, since values above and below the mean have opposite signs and sum to exactly zero. Squaring makes every deviation positive. The cost is that the units get squared too (pesos become pesos²), which is why standard deviation — the square root of variance — is usually the number people quote.

---

**12.** Probability vs. likelihood → §11

Same formula, opposite direction of reasoning:

- **Probability:** the parameter is known, and you ask about the data. *"This coin is fair — how likely am I to see 7 heads in 10 flips?"* Fix $p$, vary the data.
- **Likelihood:** the data is known and fixed, and you ask about the parameter. *"I saw 7 heads in 10 flips — how well does $p = 0.5$ explain that, compared with $p = 0.7$?"* Fix the data, vary $p$.

*The practical difference:* probabilities over all possible datasets sum to 1. Likelihoods across candidate parameter values do **not** sum to 1 — likelihood is not a probability distribution over parameters, so only its *relative* values are meaningful for comparison.

*Why ML cares:* training a model is maximizing likelihood. The data is whatever you collected and can't be changed; the parameters are what you tune to explain it best.

</details>

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can define sample space, outcome, and event, and compute probabilities by counting.
- [ ] I can use the complement, addition, and multiplication rules, and explain why each works.
- [ ] I can count arrangements and groups using $n!$ and $\binom{n}{k}$.
- [ ] I can compute conditional probabilities from a table, and explain why direction matters.
- [ ] I can test whether events are independent, and explain i.i.d.
- [ ] I can derive Bayes' theorem in one line and solve a rare-event problem by counting 10,000 cases.
- [ ] I can explain random variables, PMFs, and PDFs, including why density isn't probability.
- [ ] I can compute expected value, use linearity, and explain the law of large numbers.
- [ ] I can compute variance two ways, derive the shortcut formula, and explain why averaging reduces variance.
- [ ] I can describe Bernoulli, binomial, categorical, uniform, and Gaussian distributions, and derive the binomial formula.
- [ ] I can explain likelihood vs. probability, and derive $\hat{p} = \frac{k}{n}$ for a coin.
- [ ] Check yourself: 12/12.
- [ ] Code lab done without AI; every simulation matches its formula.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $P(A)$ | "probability of A" | how likely event $A$ is | §1 |
| $\Omega$ | "omega" | sample space: all possible outcomes | §1 |
| $\{\ldots\}$ | "the set of" | a collection of items | §1 |
| $A^c$ | "A complement" | not $A$ | §2 |
| $A \cap B$ | "A intersect B" | $A$ and $B$ both happen | §2 |
| $A \cup B$ | "A union B" | $A$ or $B$ (or both) | §2 |
| $n!$ | "n factorial" | $n \times (n - 1) \times \cdots \times 1$ | §3 |
| $\binom{n}{k}$ | "n choose k" | number of ways to choose a group of $k$ from $n$ | §3 |
| $P(A \mid B)$ | "probability of A given B" | probability of $A$ once you know $B$ happened | §4 |
| $X$ | "X" (capital) | a random variable | §7 |
| $P(X = x)$ | "probability X equals x" | chance $X$ takes value $x$ | §7 |
| $\int_a^b f(x)\,dx$ | "integral from a to b of f of x" | area under $f$ from $a$ to $b$ | §7 |
| $E[X]$ | "expected value of X" | probability-weighted average | §8 |
| $\mu$ | "mu" | the mean | §8 |
| $\text{Var}(X)$ | "variance of X" | average squared distance from the mean | §9 |
| $\sigma$ | "sigma" | standard deviation | §9 |
| $\mathcal{N}(\mu, \sigma^2)$ | "normal with mean mu, variance sigma squared" | Gaussian distribution | §10 |
| $z$ | "z-score" | standard deviations from the mean | §10 |
| $\theta$ | "theta" | a parameter | §11 |
| $\mathcal{L}(\theta)$ | "likelihood of theta" | probability of the observed data at $\theta$ | §11 |
| $\ell(\theta)$ | "log-likelihood" | $\ln \mathcal{L}(\theta)$ | §11 |
| $\hat{\theta}$ | "theta hat" | the estimate | §11 |
| $\arg\max$ | "arg max" | the input value that gives the largest output | §11 |

---

## Resources (only if stuck)

1. **Extra practice:** [Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability): the units on probability, counting, and random variables (§1–§10).
2. **Bayes' theorem intuition:** 3Blue1Brown, *Bayes theorem, the geometry of changing beliefs*, on [YouTube](https://www.youtube.com/@3blue1brown) or [3blue1brown.com](https://www.3blue1brown.com/) (§6).
3. **Likelihood:** StatQuest, *Probability is not Likelihood* and *Maximum Likelihood, clearly explained*. Find them on the [StatQuest video index](https://statquest.org/video-index/) (§11).
