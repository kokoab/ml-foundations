# 06 — Statistics

**Time: ~5 hours** (spread it over 2 days) · **You need: [05 Probability](05-Probability.md), [04 Calculus](04-Calculus.md) §6 and §10 (for §2 and §8)** · **Code lab: `math/06_statistics.py`**

## Before you start

**Probability** starts from a known process and predicts what data will look like. **Statistics** goes the other way: it starts from **data you collected** and tries to learn about the process behind it, while being honest about how uncertain that is.

The single most useful skill in this file: telling whether a difference in numbers is **real** or just **luck**.

**How to read it:**

- Go **in order**. Each section uses the ones before it.
- When you see a worked example, **cover the solution and try it first**.
- Say each symbol aloud using its "read it aloud as" note.
- Lost on a symbol? Check the [symbol cheat sheet](#symbol-cheat-sheet) at the bottom.
- The **"Why ML cares"** boxes are motivation only.

**What you'll be able to do by the end:**

- Summarize data with the right measures of center and spread
- Measure how two variables move together
- Put error bars on an estimate, and decide whether a difference is real
- Fit a line to data with a formula you've derived yourself

---

## Contents

1. [From probability to statistics](#1-from-probability-to-statistics)
2. [The center: mean, median, mode](#2-the-center-mean-median-mode)
3. [The spread: variance and standard deviation](#3-the-spread-variance-and-standard-deviation)
4. [Two variables: covariance and correlation](#4-two-variables-covariance-and-correlation)
5. [How much does an estimate wobble? Standard error](#5-how-much-does-an-estimate-wobble-standard-error)
6. [Confidence intervals and the bootstrap](#6-confidence-intervals-and-the-bootstrap)
7. [Hypothesis testing](#7-hypothesis-testing)
8. [Fitting a line](#8-fitting-a-line)
9. [Bias and variance of an estimate](#9-bias-and-variance-of-an-estimate)
10. [Code lab](#code-lab--math06_statisticspy)
11. [Check yourself](#check-yourself)

---

## 1. From probability to statistics

### The problem

You want to know the average height of all adults in the Philippines. You can't measure 70 million people. So you measure 500, and use them to estimate the answer. How good is that estimate?

### Population vs. sample

| Word | Meaning | Height example |
|---|---|---|
| **Population** | everything you want to know about | all adults in the Philippines |
| **Sample** | the part you actually measured | the 500 people you measured |
| **Parameter** | a true number describing the population (usually unknown) | the true average height |
| **Statistic** | a number calculated from the sample | the average of your 500 measurements |

**The core idea:** a statistic is an **estimate** of a parameter. A different random sample of 500 would give a slightly different estimate. Statistics is about understanding that wobble.

### Notation: Greek for population, Latin for sample

| | Population (true, unknown) | Sample (calculated) |
|---|---|---|
| Mean | $\mu$ ("mu") | $\bar{x}$ ("x bar") |
| Standard deviation | $\sigma$ ("sigma") | $s$ |
| Variance | $\sigma^2$ | $s^2$ |
| Number of items | $N$ | $n$ |

### Exercise

**1.1.** A company tests 200 phones from a factory that made 50,000. 6 of the 200 are defective. What's the population, the sample, the parameter, and the statistic?

<details>
<summary>Solution</summary>

Population: all 50,000 phones. Sample: the 200 tested. Parameter: the true defect rate of all 50,000. Statistic: $\frac{6}{200} = 3\%$.

</details>

---

## 2. The center: mean, median, mode

### The problem

You have a list of numbers. What's the **typical** value? There are three common answers, and they can disagree a lot.

### Definitions

- **Mean** (average): add them up, divide by how many. $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ (Algebra §5).
- **Median:** sort the numbers and take the **middle** one. If there's an even count, average the two middle ones.
- **Mode:** the most common value.

**Example.** Monthly incomes (in ₱ thousands) of 5 people: $[20, 25, 25, 30, 400]$.

| Measure | Calculation | Result |
|---|---|---|
| Mean | $\frac{20 + 25 + 25 + 30 + 400}{5}$ | 100 |
| Median | middle of the sorted list | 25 |
| Mode | most common | 25 |

The mean says "typical income is ₱100k," but 4 out of 5 people earn ₱30k or less. **One extreme value (an outlier) dragged the mean way up.** The median didn't move.

**Rule of thumb:** for data with extreme values (incomes, house prices, contract amounts), the median usually describes "typical" better.

### A deeper connection: which "center" is closest?

Pick any number $c$ and measure how far the data is from it. There are two natural ways to measure "far":

**Way 1: total squared distance** $\sum_i (x_i - c)^2$. Which $c$ makes this smallest?

| Step | What we did |
|---|---|
| $\frac{d}{dc}\sum_i (x_i - c)^2 = \sum_i 2(x_i - c)(-1)$ | Differentiated each term (Calculus §5, chain rule) |
| $-2\sum_i (x_i - c) = 0$ | Set to zero (Calculus §10) |
| $\sum_i x_i - nc = 0$ | Split the sum (Algebra §5, Rules B and C) |
| $c = \frac{1}{n}\sum_i x_i = \bar{x}$ | That's the mean |

**The mean is the point with the smallest total squared distance to the data.**

**Way 2: total absolute distance** $\sum_i |x_i - c|$. Which $c$ makes this smallest?

Think about sliding $c$ along the number line. If more data points are to the right of $c$ than to the left, moving $c$ right brings it closer to more points than it moves away from, so the total goes down. You keep improving until there are equal numbers on each side, which is the **median**.

**The median is the point with the smallest total absolute distance to the data.**

**Why this explains the outlier effect:** squaring makes big distances **huge** (a distance of 370 squared is 136,900), so the mean moves toward the outlier to shrink that one giant term. Absolute distance treats 370 as just 370, so the median doesn't care much.

> **Why ML cares:** When training a model, you choose how to measure its errors. Squared error pushes predictions toward the **mean** and gets pulled by outliers. Absolute error pushes toward the **median** and resists outliers. That's a real design choice, and this section is the reason behind it.

### Exercises

**2.1.** Find the mean, median, and mode of $[3, 7, 7, 2, 9, 7, 5]$.

**2.2.** Find the median of $[10, 4, 8, 2]$.

**2.3.** For $[1, 2, 3, 100]$: find the mean and median. Which is more typical?

**2.4.** Calculate $\sum (x_i - c)^2$ for $x = [1, 2, 6]$ at $c = 2$ and at $c = 3$. Which is smaller? What's the mean?

<details>
<summary>Solutions</summary>

**2.1.** Sorted: $[2, 3, 5, 7, 7, 7, 9]$. Mean $\frac{40}{7} \approx 5.71$. Median 7. Mode 7.

**2.2.** Sorted: $[2, 4, 8, 10]$. Median $\frac{4 + 8}{2} = 6$.

**2.3.** Mean 26.5, median 2.5. The median.

**2.4.** $c = 2$: $1 + 0 + 16 = 17$. $c = 3$: $4 + 1 + 9 = 14$. $c = 3$ is smaller, and it's the mean.

</details>

---

## 3. The spread: variance and standard deviation

### Sample variance

In Probability §9, variance was the average squared distance from the true mean. For a **sample**, there's one surprising change:

$$
s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})^2
$$

**We divide by $n - 1$ instead of $n$.** And $s = \sqrt{s^2}$ is the sample standard deviation.

### Why $n - 1$?

The true spread is measured around the **true** mean $\mu$. But we don't know $\mu$, so we use the sample mean $\bar{x}$ instead.

Here's the catch: $\bar{x}$ is calculated **from these same data points**, so it's always sitting right in the middle of them. From §2, $\bar{x}$ is exactly the point that makes $\sum (x_i - c)^2$ as small as possible. So distances measured to $\bar{x}$ come out **a bit too small**, compared with distances to the true $\mu$.

Dividing by the slightly smaller number $n - 1$ makes the result slightly bigger, and that exactly corrects the underestimate on average. (This correction has a name: Bessel's correction.)

**How big is the effect?** Suppose the true variance is $\sigma^2$. If you divide by $n$, then on average you get $\frac{n - 1}{n}\sigma^2$:

| Sample size $n$ | Dividing by $n$ gives, on average |
|---|---|
| 2 | 50% of the true variance |
| 10 | 90% |
| 100 | 99% |

With small samples it matters a lot, and with big samples barely at all. You'll check this by simulation in the code lab.

### Worked example

$x = [2, 4, 6]$, $\bar{x} = 4$.

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 2 | −2 | 4 |
| 4 | 0 | 0 |
| 6 | 2 | 4 |
| | **Sum** | **8** |

- Divide by $n = 3$: $\frac{8}{3} \approx 2.67$
- Divide by $n - 1 = 2$: $s^2 = 4$, so $s = 2$

### A software trap

| Code | Divides by |
|---|---|
| `np.var(x)`, `np.std(x)` (NumPy default) | $n$ |
| `pd.Series(x).var()`, `.std()` (pandas default) | $n - 1$ |

Same data, different answers. Both libraries have a setting called `ddof` to choose.

### Standardizing: z-scores

Just like Probability §10, turn each value into "how many standard deviations from the mean":

$$
z_i = \frac{x_i - \bar{x}}{s}
$$

After standardizing, the data has mean 0 and standard deviation 1.

**Example.** $[2, 4, 6]$ with $\bar{x} = 4$, $s = 2$: $z = [-1, 0, 1]$.

> **Why ML cares:** Features in a dataset often have wildly different scales (floor area in the hundreds, number of rooms under 10). Many training methods work much better when every feature is standardized first, because of the step-size problem from Calculus §11: steep directions limit the step, and flat directions crawl.

### Exercises

**3.1.** Find the sample variance and standard deviation of $[5, 7, 9, 11]$.

**3.2.** For $[1, 3]$: calculate the variance dividing by $n$ and by $n - 1$.

**3.3.** Standardize $[10, 20, 30]$ using the sample standard deviation.

**3.4.** Explain in your own words why dividing by $n$ tends to underestimate the true spread.

<details>
<summary>Solutions</summary>

**3.1.** $\bar{x} = 8$. Squared distances: $9, 1, 1, 9$, sum 20. $s^2 = \frac{20}{3} \approx 6.67$, $s \approx 2.58$.

**3.2.** $\bar{x} = 2$, sum of squares 2. Divide by 2: 1. Divide by 1: 2.

**3.3.** $\bar{x} = 20$, $s^2 = \frac{100 + 0 + 100}{2} = 100$, $s = 10$. $z = [-1, 0, 1]$.

**3.4.** The sample mean is calculated from the same points, so it sits closer to them than the true mean does. Distances measured to it come out smaller than they should.

</details>

---

## 4. Two variables: covariance and correlation

### The problem

Do taller people tend to weigh more? Do houses with more rooms cost more? We want a number that says **how two things move together**.

### The picture: a scatter plot

Plot each person as a point $(x_i, y_i)$: height across, weight up. If the dots drift upward from left to right, the two variables rise together.

Now draw a vertical line at $\bar{x}$ and a horizontal line at $\bar{y}$. That splits the plot into four quadrants:

| Quadrant | $x_i - \bar{x}$ | $y_i - \bar{y}$ | Product |
|---|---|---|---|
| upper right | + | + | **+** |
| lower left | − | − | **+** |
| upper left | − | + | **−** |
| lower right | + | − | **−** |

If most points are upper right or lower left (both above average together, or both below average together), the products are **mostly positive**.

### Covariance

Average those products:

$$
s_{xy} = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$

Read $s_{xy}$ aloud as "the covariance of x and y."

| Covariance | Meaning |
|---|---|
| positive | they tend to rise together |
| negative | when one rises, the other tends to fall |
| near zero | no consistent straight-line pattern |

### The problem with covariance: units

Height in cm and weight in kg give a covariance in "cm·kg." Measure height in meters instead, and the covariance shrinks 100 times, **even though the relationship is identical**. So you can't look at a covariance and say whether it's strong.

### Correlation: covariance without units

Divide by both standard deviations to cancel the units:

$$
r = \frac{s_{xy}}{s_x\,s_y}
$$

Read $r$ aloud as "**the correlation**." It's always between $-1$ and $1$:

| $r$ | Meaning |
|---|---|
| $1$ | a perfect upward straight line |
| around $0.7$ | a strong upward trend |
| $0$ | no straight-line relationship |
| $-1$ | a perfect downward straight line |

### Worked example

$x = [1, 2, 3]$, $y = [2, 4, 7]$. Means: $\bar{x} = 2$, $\bar{y} = \frac{13}{3} \approx 4.333$.

| $x_i - \bar{x}$ | $y_i - \bar{y}$ | Product | $(x_i - \bar{x})^2$ | $(y_i - \bar{y})^2$ |
|---|---|---|---|---|
| −1 | −2.333 | 2.333 | 1 | 5.444 |
| 0 | −0.333 | 0 | 0 | 0.111 |
| 1 | 2.667 | 2.667 | 1 | 7.111 |
| **Sums** | | **5** | **2** | **12.667** |

| Quantity | Calculation | Value |
|---|---|---|
| $s_{xy}$ | $\frac{5}{2}$ | 2.5 |
| $s_x$ | $\sqrt{\frac{2}{2}}$ | 1 |
| $s_y$ | $\sqrt{\frac{12.667}{2}}$ | 2.517 |
| $r$ | $\frac{2.5}{1 \times 2.517}$ | **0.993** |

A very strong upward straight-line relationship.

### Correlation is cosine similarity in disguise

Let $\tilde{\mathbf{x}}$ be the list of $x_i - \bar{x}$ values, and $\tilde{\mathbf{y}}$ the list of $y_i - \bar{y}$ values. (These are called the **centered** data.) The $\frac{1}{n - 1}$ factors cancel, leaving:

$$
r = \frac{\tilde{\mathbf{x}} \cdot \tilde{\mathbf{y}}}{\lVert \tilde{\mathbf{x}} \rVert\,\lVert \tilde{\mathbf{y}} \rVert}
$$

That's exactly the cosine similarity formula from Linear Algebra §6. **Correlation measures how much the centered data vectors point the same way.**

### Two big warnings

**1. Correlation only sees straight-line relationships.** $x = [-1, 0, 1]$ and $y = x^2 = [1, 0, 1]$: $y$ is completely determined by $x$, but the correlation is 0 (the U shape has no overall upward or downward trend).

**2. Correlation doesn't mean causation.** Ice cream sales and drowning rates are correlated. Ice cream doesn't cause drowning: hot weather causes both.

> **Why ML cares:** When two features are very highly correlated, they carry nearly the same information. That's the "dependent columns" problem from Linear Algebra §8 and §15, and it can make some models unstable.

### Exercises

**4.1.** Find the covariance and correlation of $x = [1, 2, 3, 4]$ and $y = [8, 6, 4, 2]$.

**4.2.** Confirm that $x = [-1, 0, 1]$ and $y = [1, 0, 1]$ have correlation 0.

**4.3.** Temperature measured in °C and in °F for the same 30 days. What's their correlation? Why?

**4.4.** A study finds students who sleep more get better grades. Give one possible reason that isn't "sleep causes good grades."

<details>
<summary>Solutions</summary>

**4.1.** $\bar{x} = 2.5$, $\bar{y} = 5$. Products: $(-1.5)(3) + (-0.5)(1) + (0.5)(-1) + (1.5)(-3) = -10$. $s_{xy} = -\frac{10}{3}$. $s_x^2 = \frac{5}{3}$, $s_y^2 = \frac{20}{3}$. $r = \frac{-10/3}{\sqrt{5/3}\sqrt{20/3}} = \frac{-10/3}{10/3} = -1$. A perfect downward line.

**4.2.** $\bar{x} = 0$, $\bar{y} = \frac{2}{3}$. Products: $(-1)(\frac{1}{3}) + 0 + (1)(\frac{1}{3}) = 0$.

**4.3.** Exactly 1. °F $= 1.8 \times$ °C $+ 32$ is a perfect upward straight line.

**4.4.** A third factor could cause both, e.g. students with less stressful lives both sleep more and do better.

</details>

---

## 5. How much does an estimate wobble? Standard error

### The problem

You survey 500 people, and 90% say yes. A different random 500 might give 88%, or 91.5%. **How much does the result bounce around from sample to sample?** Without knowing that, you can't tell a real difference from luck.

### The sample mean is itself random

Every time you draw a new sample, you get a new $\bar{x}$. So $\bar{x}$ is a random variable with its own distribution, called its **sampling distribution**.

From Probability §9: averaging $n$ independent values with standard deviation $\sigma$ gives variance $\frac{\sigma^2}{n}$. Take the square root:

$$
\text{SE} = \frac{\sigma}{\sqrt{n}}
$$

This is the **standard error**: the standard deviation of an estimate. It measures **how much the estimate typically wobbles**. (In practice, $\sigma$ is unknown, so we plug in the sample's $s$.)

### The square root is important

| Sample size | Standard error |
|---|---|
| $n$ | $\frac{\sigma}{\sqrt{n}}$ |
| $4n$ | $\frac{\sigma}{2\sqrt{n}}$, half as much |
| $100n$ | $\frac{\sigma}{10\sqrt{n}}$, a tenth |

**To cut uncertainty in half, you need 4 times as much data.**

### Standard error of a percentage

A yes/no answer is a Bernoulli variable (Probability §10) with variance $p(1 - p)$. The percentage of "yes" is an average of those 0s and 1s, so:

$$
\text{SE} = \sqrt{\frac{p(1 - p)}{n}}
$$

**Example.** 500 people, 90% say yes:

$$
\text{SE} = \sqrt{\frac{0.9 \times 0.1}{500}} = \sqrt{0.00018} \approx 0.0134
$$

So the estimate typically wobbles by about **1.3 percentage points**.

### The central limit theorem

Here's the remarkable part. **No matter what the original data looks like** (lopsided, lumpy, anything), the average of many independent values follows approximately a **Gaussian** (bell curve) distribution. This is the **central limit theorem (CLT)**.

That means the 68–95–99.7 rule (Probability §10) applies to averages: about **95% of the time, a sample average lands within 2 standard errors of the truth**.

> **Why ML cares:** A model's accuracy on a test set is a percentage calculated from a sample. With 500 test examples and 90% accuracy, the standard error is about 1.3 points, so **91% vs. 92% on 500 examples could easily be pure luck**. Before believing an "improvement," compare it with the standard error.

### Exercises

**5.1.** One measurement has standard deviation 12. What's the standard error of an average of 36 measurements?

**5.2.** 90% yes from 5,000 people instead of 500. What's the standard error?

**5.3.** You want the standard error of a percentage near 80% to be about 0.03. Roughly how many people do you need?

**5.4.** Explain why doubling your sample doesn't halve the standard error.

<details>
<summary>Hint</summary>

5.3: solve $\sqrt{\frac{0.8 \times 0.2}{n}} = 0.03$. Square both sides first.

</details>

<details>
<summary>Solutions</summary>

**5.1.** $\frac{12}{\sqrt{36}} = 2$.

**5.2.** $\sqrt{\frac{0.09}{5000}} \approx 0.0042$.

**5.3.** $\frac{0.16}{n} = 0.0009$, so $n \approx 178$.

**5.4.** The standard error shrinks with $\sqrt{n}$, not $n$. Doubling $n$ divides it by $\sqrt{2} \approx 1.41$.

</details>

---

## 6. Confidence intervals and the bootstrap

### The idea

Instead of reporting just "90%," report a **range** that honestly shows the uncertainty. Since 95% of sample averages land within about 2 standard errors of the truth (§5):

$$
\text{estimate} \pm 1.96 \times \text{SE}
$$

This is a **95% confidence interval**. (1.96 is the more precise version of "about 2.")

**Example.** 90% from 500 people, $\text{SE} \approx 0.0134$:

$$
0.90 \pm 1.96 \times 0.0134 = 0.90 \pm 0.026 \quad\to\quad [0.874,\ 0.926]
$$

### What "95% confidence" actually means

Imagine repeating the whole survey many times, making a new interval each time. **About 95% of those intervals would contain the true value.**

It does **not** quite mean "there's a 95% chance the truth is in *this* interval." The truth is a fixed number, and it's either in there or not. The 95% describes how reliable the **method** is. It's a subtle distinction, but it avoids some wrong conclusions.

### The bootstrap: intervals without a formula

The $\pm 1.96 \times \text{SE}$ formula needs a formula for SE. For many quantities (a median, or complicated scores), there isn't a simple one. The **bootstrap** gets around this with computing power:

1. From your $n$ data points, draw $n$ points **at random, with replacement** (the same point can be picked more than once). This makes a "new" sample.
2. Calculate your statistic on it.
3. Repeat thousands of times.
4. Sort all the results. The middle 95% (from the 2.5th to the 97.5th percentile) is your interval.

**Why it works:** your sample is your best picture of the population. Resampling from it imitates "what if I had collected a different sample?"

### Exercises

**6.1.** A poll of 1,000 people finds 52% support. Compute a 95% confidence interval. Can you confidently say the majority supports it?

**6.2.** Explain, in your own words, what's wrong with saying "there's a 95% probability the true value is in [0.874, 0.926]."

**6.3.** Why do we resample **with** replacement in the bootstrap? What would happen without replacement?

<details>
<summary>Solutions</summary>

**6.1.** $\text{SE} = \sqrt{\frac{0.52 \times 0.48}{1000}} \approx 0.0158$. Interval: $0.52 \pm 0.031$, about $[0.489, 0.551]$. It includes values below 50%, so no.

**6.2.** The true value is fixed, not random. The 95% describes how often the interval-making method captures the truth over many repetitions.

**6.3.** Without replacement, drawing $n$ from $n$ gives back exactly the same data every time, so nothing varies.

</details>

---

## 7. Hypothesis testing

### The problem

A coin lands heads 60 times out of 100. Is the coin unfair, or was that just luck? We need a principled way to decide.

### The logic: assume nothing is going on, then check

1. **Null hypothesis** $H_0$ (read "H nought"): the boring explanation. "The coin is fair."
2. Ask: **if $H_0$ were true, how surprising is what I saw?**
3. If it would be very surprising, doubt $H_0$.

### The p-value

The **p-value** is: **assuming $H_0$ is true, the probability of seeing a result at least as extreme as the one you got.**

**Example.** Under $H_0$ (fair coin), 100 flips give a binomial with mean $np = 50$ and standard deviation $\sqrt{np(1 - p)} = \sqrt{25} = 5$ (Probability §10).

| Step | Value |
|---|---|
| How many standard deviations is 60 from 50? | $z = \frac{60 - 50}{5} = 2$ |
| From the 95% rule, being 2 or more SDs away (either direction) happens about | 5% of the time |
| More precisely, the p-value is | about 0.046 |

So if the coin were fair, a result this lopsided would happen only about 4.6% of the time.

### Deciding

Pick a cutoff in advance, usually $\alpha = 0.05$ (here $\alpha$ is a cutoff, not a step size).

- $p < \alpha$: reject $H_0$. The result is called **statistically significant**.
- $p \ge \alpha$: not enough evidence against $H_0$. (This is **not** proof $H_0$ is true.)

With $p \approx 0.046 < 0.05$, this coin is borderline suspicious.

### Two kinds of mistakes

| | $H_0$ actually true | $H_0$ actually false |
|---|---|---|
| **You reject $H_0$** | **Type I error** (false alarm) | correct |
| **You keep $H_0$** | correct | **Type II error** (missed it) |

The cutoff $\alpha$ is the false-alarm rate you're willing to accept.

### Three traps

**1. A p-value is NOT the probability that $H_0$ is true.** It's $P(\text{data this extreme} \mid H_0)$, not $P(H_0 \mid \text{data})$. That's the direction confusion from Probability §4 again.

**2. Testing many things guarantees some false alarms.** Test 20 useless ideas at $\alpha = 0.05$, and on average **one** will look "significant" by pure luck. If you try many options and report only the best one, you'll fool yourself.

**3. "Significant" doesn't mean "important."** With a huge sample, a tiny, useless difference can still be statistically significant.

> **Why ML cares:** When you try 30 different settings and one of them scores best, trap 2 applies directly. The honest fix is to confirm the winner on **fresh data** that wasn't used to pick it.

### Exercises

**7.1.** A coin lands heads 58 times out of 100. Find the z-score. Is it significant at $\alpha = 0.05$?

**7.2.** A researcher gets $p = 0.03$ and says "there's a 3% chance the null hypothesis is true." What's wrong?

**7.3.** You test 40 different lucky charms on dice rolls, and one gives $p = 0.02$. Should you believe it works? What would you do next?

<details>
<summary>Solutions</summary>

**7.1.** $z = \frac{58 - 50}{5} = 1.6$. That's less than 2 standard deviations, so not significant (the p-value is about 0.11).

**7.2.** The p-value is the probability of data this extreme **if** the null is true, not the probability the null is true.

**7.3.** No. With 40 tests, you'd expect about 2 false alarms at 0.05. Test that one charm again, on new rolls.

</details>

---

## 8. Fitting a line

### The problem

You have data points $(x_i, y_i)$ that roughly follow a straight line. Which line $y = mx + c$ fits **best**?

### What "best" means: least squares

For each point, the **residual** is the vertical gap between the actual $y_i$ and the line's prediction:

$$
\text{residual}_i = y_i - (mx_i + c)
$$

"Best" means: make the **total squared residual** as small as possible:

$$
S(m, c) = \sum_{i=1}^n \big(y_i - mx_i - c\big)^2
$$

(Squared, for the same reason as variance: so positive and negative gaps don't cancel. And from §2, squaring leads to mean-like answers.)

### Deriving the best line with calculus

$S$ is a function of two inputs, $m$ and $c$. Set both partial derivatives to zero (Calculus §6, §10).

**Step 1: the intercept $c$.**

| Step | What we did |
|---|---|
| $\frac{\partial S}{\partial c} = \sum_i 2(y_i - mx_i - c)(-1) = 0$ | Chain rule; inside has derivative $-1$ with respect to $c$ |
| $\sum_i y_i - m\sum_i x_i - nc = 0$ | Divided by $-2$ and split the sum |
| $c = \bar{y} - m\bar{x}$ | Divided by $n$ |

So **the best line always passes through the point $(\bar{x}, \bar{y})$**.

**Step 2: the slope $m$.**

| Step | What we did |
|---|---|
| $\frac{\partial S}{\partial m} = \sum_i 2(y_i - mx_i - c)(-x_i) = 0$ | Inside has derivative $-x_i$ with respect to $m$ |
| $\sum_i x_i\big(y_i - \bar{y} - m(x_i - \bar{x})\big) = 0$ | Divided by $-2$, and put in $c = \bar{y} - m\bar{x}$ |
| $\sum_i x_i(y_i - \bar{y}) = m\sum_i x_i(x_i - \bar{x})$ | Split into two sums |
| $\sum_i (x_i - \bar{x})(y_i - \bar{y}) = m\sum_i (x_i - \bar{x})^2$ | Replaced $x_i$ with $x_i - \bar{x}$ in front. That's allowed because $\sum_i \bar{x}(y_i - \bar{y}) = \bar{x} \cdot 0 = 0$ (Algebra Exercise 5.6) |

Divide both sides, and the $\frac{1}{n - 1}$ factors from §3 and §4 cancel:

$$
m = \frac{s_{xy}}{s_x^2}, \qquad c = \bar{y} - m\bar{x}
$$

**The slope is the covariance divided by the variance of $x$.**

### Worked example

Same data as §4: $x = [1, 2, 3]$, $y = [2, 4, 7]$, with $s_{xy} = 2.5$ and $s_x^2 = 1$.

| Step | Value |
|---|---|
| $m = \frac{2.5}{1}$ | 2.5 |
| $c = 4.333 - 2.5 \times 2$ | $-0.667$ |
| Line | $y = 2.5x - 0.667$ |

This is exactly the line from Linear Algebra §17, found with a completely different method. **Two independent derivations, same answer.**

| $x$ | $y$ | Prediction | Residual |
|---|---|---|---|
| 1 | 2 | 1.833 | 0.167 |
| 2 | 4 | 4.333 | −0.333 |
| 3 | 7 | 6.833 | 0.167 |

The residuals add up to 0. (That always happens with an intercept: it's exactly Step 1's equation.)

### How good is the fit? $R^2$

Compare the leftover squared error with the total spread of $y$:

$$
R^2 = 1 - \frac{\sum(\text{residuals})^2}{\sum(y_i - \bar{y})^2}
$$

Read $R^2$ aloud as "R squared." It's the **fraction of the variation in $y$ that the line explains**.

For our example: $\frac{0.028 + 0.111 + 0.028}{12.667} = \frac{0.167}{12.667} \approx 0.013$, so $R^2 \approx 0.987$. The line explains about 98.7% of the variation.

(For a straight-line fit, $R^2$ equals the correlation squared: $0.993^2 \approx 0.987$ ✓)

> **Why ML cares:** This is **linear regression**, the simplest ML model. In ML Mathematics, you'll derive it a third way (gradient descent on squared error), and extend it to many input features at once.

### Exercises

**8.1.** Fit a line to $x = [0, 1, 2]$, $y = [1, 3, 5]$. What's $R^2$, and why?

**8.2.** Fit a line to $x = [1, 2, 3, 4]$, $y = [2, 3, 5, 6]$.

**8.3.** Explain in words why the best line must pass through $(\bar{x}, \bar{y})$.

<details>
<summary>Hint</summary>

8.2: $\bar{x} = 2.5$, $\bar{y} = 4$. Make a table of $(x_i - \bar{x})$, $(y_i - \bar{y})$, and their product.

</details>

<details>
<summary>Solutions</summary>

**8.1.** $\bar{x} = 1$, $\bar{y} = 3$. $s_{xy} = \frac{(-1)(-2) + 0 + (1)(2)}{2} = 2$, $s_x^2 = 1$. So $m = 2$, $c = 1$. Every point is exactly on $y = 2x + 1$, so the residuals are all 0 and $R^2 = 1$.

**8.2.** Products: $(-1.5)(-2) + (-0.5)(-1) + (0.5)(1) + (1.5)(2) = 7$. $\sum(x_i - \bar{x})^2 = 5$. $m = \frac{7}{5} = 1.4$, and $c = 4 - 1.4 \times 2.5 = 0.5$. Line: $y = 1.4x + 0.5$.

**8.3.** Setting the intercept's derivative to zero forces the residuals to add up to zero. That means the line is balanced on the data's center point.

</details>

---

## 9. Bias and variance of an estimate

### The problem

A method for estimating something can go wrong in two very different ways: it can be **consistently off in one direction**, or it can **jump around a lot**. These need separate names.

### The dartboard picture

Imagine throwing many darts at the bullseye (the true value):

| | Low variance (tight cluster) | High variance (scattered) |
|---|---|---|
| **Low bias** (centered on bullseye) | ideal | right on average, but any single throw is unreliable |
| **High bias** (centered off to the side) | consistently wrong | wrong and scattered |

### Definitions

For an estimate $\hat{\theta}$ of a true value $\theta$ (Probability §11):

- **Bias:** $E[\hat{\theta}] - \theta$. How far off it is **on average**.
- **Variance:** $\text{Var}(\hat{\theta})$. How much it **jumps around** between samples.

An estimate with bias 0 is called **unbiased**.

**Example.** From §3: the variance calculated by dividing by $n$ is **biased**. On average it gives $\frac{n - 1}{n}\sigma^2$, not $\sigma^2$. Dividing by $n - 1$ is unbiased.

### Total error = bias² + variance

The overall average squared error of an estimate splits cleanly into the two:

$$
E\big[(\hat{\theta} - \theta)^2\big] = \text{Bias}^2 + \text{Variance}
$$

**Why:** let $a = E[\hat{\theta}]$ (the average estimate). Split the error into "distance from the average" plus "average's distance from the truth":

| Step | What we did |
|---|---|
| $\hat{\theta} - \theta = (\hat{\theta} - a) + (a - \theta)$ | Added and subtracted $a$ |
| $E[(\hat{\theta} - \theta)^2] = E[(\hat{\theta} - a)^2] + 2(a - \theta)\,E[\hat{\theta} - a] + (a - \theta)^2$ | Expanded the square; $(a - \theta)$ is a fixed number, so it moves outside $E$ |
| middle term: $E[\hat{\theta} - a] = a - a = 0$ | Linearity (Probability §8) |
| $= \text{Var}(\hat{\theta}) + \text{Bias}^2$ | The first term is the variance, and the last is bias squared |

### The tradeoff

Reducing one often increases the other. A method that always guesses "50" has **zero variance** but huge bias. A method that relies on just one data point is unbiased but has **huge variance**. Good methods balance the two.

> **Why ML cares:** This is one of the central ideas of machine learning. A model that's too simple is like the "always guess 50" method: **high bias**, called **underfitting**. A model that's too flexible memorizes the random quirks of its particular training data: **high variance**, called **overfitting**. The Classical ML phase is largely about managing this tradeoff.

### Exercises

**9.1.** An estimate is always exactly 3 higher than the truth. What are its bias and variance?

**9.2.** Estimate A has bias 2 and variance 1. Estimate B has bias 0 and variance 9. Which has the smaller total squared error?

**9.3.** Reproduce the proof of bias² + variance without looking.

<details>
<summary>Solutions</summary>

**9.1.** Bias 3, variance 0.

**9.2.** A: $4 + 1 = 5$. B: $0 + 9 = 9$. A is better overall, despite being biased.

</details>

---

## Code lab — `math/06_statistics.py`

### What you're doing and why

You'll implement the core statistics from scratch, check them against NumPy and pandas, and then use **simulation** to see the $n - 1$ correction, the central limit theorem, and "luck vs. real difference" with your own eyes.

**Rules:** no AI, no autocomplete, no copying.

### Python you need

- `sorted(x)` returns a sorted copy of a list.
- `len(x) // 2` is whole-number division (e.g. `5 // 2` is `2`).
- `rng.integers(0, n, size=n)` gives `n` random positions, which you can use to resample with replacement: `data[positions]`.
- `np.quantile(values, [0.025, 0.975])` gives the 2.5th and 97.5th percentiles.
- `np.polyfit(x, y, 1)` fits a straight line and returns `[slope, intercept]`.
- `plt.hist(values, bins=50)` draws a histogram.

### The tasks

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)

def mean(x): ...
def median(x): ...                     # sort, then take the middle (or average the two middle values)
def variance(x, ddof=1): ...           # divide by n - ddof
def covariance(x, y): ...              # divide by n - 1
def correlation(x, y): ...
def fit_line(x, y): ...                # return (slope, intercept) using §8's formulas
def bootstrap_interval(data, statistic, repeats=5000): ...   # return the 2.5th and 97.5th percentiles

if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 4.0, 7.0])
    assert mean([2, 4, 6]) == 4
    assert median([5, 1, 3, 2]) == 2.5
    assert np.isclose(variance(x, ddof=0), np.var(x))
    assert np.isclose(variance(x, ddof=1), pd.Series(x).var())
    assert np.isclose(correlation(x, y), np.corrcoef(x, y)[0, 1])
    assert np.allclose(fit_line(x, y), np.polyfit(x, y, 1))

    # 1) Why n - 1 (§3): draw 100,000 samples of size 2 from N(0, 1) (true variance 1).
    #    Average variance(sample, ddof=0) over all samples, then variance(sample, ddof=1).
    #    BEFORE running: predict both averages.

    # 2) Central limit theorem (§5): draw 10,000 averages, each of 30 values from rng.exponential(1.0).
    #    First plot a histogram of raw exponential values (very lopsided).
    #    Then plot a histogram of the 10,000 averages. What shape is it?

    # 3) Bootstrap (§6): make fake survey answers: answers = rng.random(500) < 0.9
    #    Compute bootstrap_interval(answers, np.mean). Compare with 0.9 ± 1.96 * sqrt(0.09 / 500).

    # 4) Luck vs. real (§5, §7): two methods that BOTH truly succeed 91.5% of the time.
    #    Simulate each on 500 trials, and repeat that 1,000 times.
    #    In what fraction of repeats do they differ by 1 percentage point or more?
    print("all checks passed")
```

<details>
<summary>Reference solution for median, bootstrap, and task 4 (only after your own attempt)</summary>

```python
def median(x):
    s = sorted(x)
    n = len(s)
    middle = n // 2
    if n % 2 == 1:
        return s[middle]
    return (s[middle - 1] + s[middle]) / 2

def bootstrap_interval(data, statistic, repeats=5000):
    data = np.asarray(data)
    n = len(data)
    results = []
    for _ in range(repeats):
        positions = rng.integers(0, n, size=n)
        results.append(statistic(data[positions]))
    return np.quantile(results, [0.025, 0.975])

# task 4
a = (rng.random((1000, 500)) < 0.915).mean(axis=1)
b = (rng.random((1000, 500)) < 0.915).mean(axis=1)
print("fraction differing by >= 1 point:", np.mean(np.abs(a - b) >= 0.01))
```

For task 1, expect about 0.5 (dividing by $n$) and about 1.0 (dividing by $n - 1$).

</details>

---

## Common mistakes

| Mistake | Why it's wrong |
|---|---|
| Using the mean for data with big outliers | §2: incomes $[20, 25, 25, 30, 400]$ have mean 100 but median 25 |
| Comparing covariances between different pairs of variables | Covariance depends on units; use correlation |
| "Correlation 0 means unrelated" | $y = x^2$ can have correlation 0 |
| "Correlated means one causes the other" | A third factor can cause both |
| Mixing up NumPy's and pandas' default variance | NumPy divides by $n$, pandas by $n - 1$ |
| Trusting a 1-point difference from a small sample | The standard error might be bigger than the difference |
| Reading a p-value as the probability the null hypothesis is true | It's the probability of the data, assuming the null |
| Testing many things and reporting only the best | Some will look significant by luck alone |

---

## Check yourself

Do this **after** working through the file. Closed book, 20 minutes.

1. Find the mean and median of $[2, 3, 3, 5, 100]$. Which describes a typical value better?
2. Find the variance of $[2, 4, 6]$ dividing by $n$, and by $n - 1$.
3. Height & weight have covariance 40, height & age have covariance 200. Which relationship is stronger?
4. $x = [-1, 0, 1]$, $y = x^2$. What's their correlation? Are they related?
5. A survey of 500 finds 90% yes. What's the standard error?
6. What does a p-value of 0.03 mean? What does it not mean?
7. Write the best-fit slope in terms of covariance and variance.
8. What do "high bias" and "high variance" mean for an estimate?
9. Prove that the mean minimizes $\sum (x_i - c)^2$.
10. Explain why dividing by $n - 1$ is used for sample variance.

<details>
<summary>Answers</summary>

**1.** Mean and median of $[2, 3, 3, 5, 100]$ → §2

*Mean* — add everything, divide by how many:

$$\bar{x} = \frac{2 + 3 + 3 + 5 + 100}{5} = \frac{113}{5} = 22.6$$

*Median* — sort, then take the middle value. The list is already sorted, and with $n = 5$ the middle is the 3rd value:

$$2,\ 3,\ \mathbf{3},\ 5,\ 100 \quad\Rightarrow\quad \text{median} = 3$$

*Which is more typical?* The **median**. Four of the five values sit between 2 and 5, yet the mean reports 22.6 — a number larger than 80% of the data. The single outlier 100 drags it there, because the mean adds every value at full weight. The median only cares about position, so one extreme value moves it barely at all.

*The rule of thumb:* skewed data or outliers (incomes, house prices, response times) → report the median. Roughly symmetric data → the mean is fine and carries more information.

---

**2.** Variance of $[2, 4, 6]$, dividing by $n$ and by $n-1$ → §3

*Step 1 — the mean:* $\bar{x} = \frac{2+4+6}{3} = 4$

*Step 2 — deviations from the mean:* $2-4 = -2$, $4-4 = 0$, $6-4 = 2$

*Step 3 — square them and add:* $4 + 0 + 4 = 8$

*Step 4 — divide, both ways:*

$$\text{divide by } n: \quad \frac{8}{3} \approx 2.67 \qquad \text{(population variance, } \sigma^2\text{)}$$

$$\text{divide by } n-1: \quad \frac{8}{2} = 4 \qquad \text{(sample variance, } s^2\text{)}$$

*Which to use:* if those three numbers are the entire population, divide by $n$. If they're a sample meant to estimate a bigger population's variance, divide by $n - 1$ (see Q10 for why).

---

**3.** Covariance 40 vs. covariance 200 — which relationship is stronger? → §4

**You can't tell.** Covariance is not comparable across different pairs of variables, because it carries the units of both variables multiplied together.

Height-and-weight covariance is measured in cm·kg. Height-and-age covariance is in cm·years. Those aren't the same kind of number, so 200 is not "bigger" than 40 in any meaningful sense — switching height from centimetres to millimetres would multiply both figures by 10 without a single relationship changing.

*The fix — correlation*, which is covariance with both standard deviations divided out:

$$r = \frac{\text{cov}(x, y)}{s_x s_y}$$

That cancels the units and confines the result to $[-1, 1]$, so different pairs of variables finally become comparable. Covariance tells you the **direction** of a relationship (positive or negative). Only correlation tells you the **strength**.

---

**4.** $x = [-1, 0, 1]$, $y = x^2$: correlation? are they related? → §4

*Compute it.* First $y = [1, 0, 1]$, with $\bar{x} = 0$ and $\bar{y} = \frac{2}{3}$.

Covariance is the average product of the paired deviations:

| $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | product |
|---|---|---|---|---|
| $-1$ | 1 | $-1$ | $\frac{1}{3}$ | $-\frac{1}{3}$ |
| 0 | 0 | 0 | $-\frac{2}{3}$ | 0 |
| 1 | 1 | 1 | $\frac{1}{3}$ | $\frac{1}{3}$ |

Sum of products: $-\frac{1}{3} + 0 + \frac{1}{3} = 0$. So covariance is 0, and correlation is **0**.

*Are they related?* Completely. $y$ is exactly determined by $x$ — there is zero randomness in the relationship.

*What this teaches:* correlation only detects **linear** relationships. This one is a perfect U-shape: $y$ falls as $x$ goes from $-1$ to $0$, then rises symmetrically. The two halves cancel, and correlation reports nothing. A correlation of 0 means "no straight-line trend," never "no relationship." Always plot the data — a correlation coefficient is blind to every curve.

---

**5.** Survey of 500, 90% say yes: standard error → §5

For a proportion, the standard error is:

$$\text{SE} = \sqrt{\frac{p(1-p)}{n}}$$

*Step 1 — the top:* $p(1-p) = 0.9 \times 0.1 = 0.09$

*Step 2 — divide by $n$:* $\frac{0.09}{500} = 0.00018$

*Step 3 — square root:*

$$\text{SE} = \sqrt{0.00018} \approx 0.0134$$

About 1.3 percentage points.

*What it means:* SE is the standard deviation of the estimate itself — how much the 90% figure would bounce around if the survey were repeated with fresh samples of 500. A rough 95% confidence interval is $\pm 2\,\text{SE}$, so roughly $90\% \pm 2.7\%$, i.e. about 87.3% to 92.7%.

*Note the $\sqrt{n}$:* quartering the error requires 16 times the sample. Precision gets expensive fast.

---

**6.** What does $p = 0.03$ mean, and what does it not? → §7

**What it means:** *if the null hypothesis were true*, data at least this extreme would turn up 3% of the time by chance alone. It's a statement about the data, computed under an assumption.

**What it does not mean:**

- ❌ "There's a 3% chance the null hypothesis is true." The p-value assumes the null is true; it can't then report the null's probability. That's the $P(A\mid B)$ vs. $P(B \mid A)$ swap again.
- ❌ "There's a 97% chance the effect is real."
- ❌ "The effect is large or important." A tiny, useless effect will produce a small p-value given a big enough sample. Statistical significance is not practical significance.

*The one-line version:* the p-value measures how surprising the data is under the null hypothesis — not how likely the null hypothesis is.

---

**7.** Best-fit slope in terms of covariance and variance → §8

$$m = \frac{s_{xy}}{s_x^2} = \frac{\text{cov}(x, y)}{\text{var}(x)}$$

*How to read it:* the top measures how $x$ and $y$ move together; the bottom normalizes by how much $x$ moves on its own. The result is "units of $y$ per unit of $x$" — exactly what a slope is.

*Sanity check the extremes:* if $x$ and $y$ don't move together at all, the top is 0 and the best-fit line is flat ✓ If $x$ barely varies, the bottom is tiny and the slope becomes huge and unstable — which is the honest answer, since you can't pin down a trend from inputs that never change.

---

**8.** High bias vs. high variance in an estimate → §9

Picture shooting at a target many times, once per dataset.

**High bias:** the shots cluster tightly, but centred away from the bullseye. The estimate is consistently wrong in the same direction, and more data won't rescue it — the method itself is off. (In ML: underfitting, a model too simple to capture the pattern.)

**High variance:** the shots scatter widely around the bullseye. On average it's right, but any single estimate could be far off. Resampling gives a very different answer each time. (In ML: overfitting, a model chasing the noise in its particular training set.)

*The tension:* reducing one typically raises the other. Total expected error decomposes as $\text{bias}^2 + \text{variance} + \text{irreducible noise}$, and the goal is minimizing the sum, not zeroing either term.

---

**9.** Prove the mean minimizes $\sum (x_i - c)^2$ → §2

We want the $c$ that makes the total squared distance to all data points as small as possible.

*Step 1 — name the function of $c$:*

$$g(c) = \sum_{i=1}^{n}(x_i - c)^2$$

*Step 2 — differentiate with respect to $c$.* Chain rule on each term: the derivative of $(x_i - c)^2$ is $2(x_i - c) \cdot (-1)$:

$$g'(c) = \sum_{i=1}^{n} -2(x_i - c) = -2\sum_{i=1}^{n}(x_i - c)$$

*Step 3 — set it to zero:*

$$-2\sum_{i=1}^{n}(x_i - c) = 0 \quad\Rightarrow\quad \sum_{i=1}^{n}(x_i - c) = 0$$

*Step 4 — split the sum.* Subtracting $c$ once per term, over $n$ terms, totals $nc$:

$$\sum_{i=1}^{n}x_i - nc = 0 \quad\Rightarrow\quad c = \frac{1}{n}\sum_{i=1}^{n}x_i = \bar{x}$$

*Step 5 — confirm it's a minimum:* $g''(c) = 2n > 0$, so the curve opens upward ✓

*What it means:* the mean is not an arbitrary convention — it is *defined* by this optimality property. It's the single number closest to all your data in the squared-distance sense. This is also why least-squares regression and mean-squared-error loss keep producing means: they're the same minimization, one step more general.

*(Footnote: swap squared distance for absolute distance $\sum|x_i - c|$ and the minimizer becomes the **median** instead. Different notion of "close," different centre.)*

---

**10.** Why divide by $n - 1$ for sample variance? → §3

Because you used the same data twice, and that double-use biases the result downward.

*The problem:* the true population mean $\mu$ is unknown, so you substitute the **sample** mean $\bar{x}$ — a number computed from these very data points. And by Q9, $\bar{x}$ is the value that makes $\sum(x_i - c)^2$ as small as it can possibly be. So measuring spread around $\bar{x}$ gives a total that is *guaranteed* to be no larger than the spread around the true $\mu$, and usually strictly smaller.

Divide that too-small total by $n$ and you systematically underestimate the population variance, every time. It's a bias, not bad luck — it doesn't average out.

*The fix:* divide by $n - 1$ instead. The smaller denominator inflates the estimate by exactly the right amount to cancel the bias.

*Why $n-1$ specifically — degrees of freedom:* once $\bar{x}$ is fixed, the deviations $x_i - \bar{x}$ must sum to zero. Given any $n-1$ of them, the last is forced. So there are only $n - 1$ freely varying pieces of information about spread, and you divide by the count of independent ones.

*Sanity check with $n = 1$:* one data point gives $\bar{x} = x_1$ and a deviation of 0. Dividing by $n$ reports variance 0 — absurdly confident from a single observation. Dividing by $n - 1 = 0$ gives undefined, which is the honest answer: one point tells you nothing about spread ✓

</details>

---

## Definition of Done

Tick a box only when it's honestly true **without looking at this file**.

- [ ] I can explain population vs. sample and parameter vs. statistic, with the notation.
- [ ] I can compute mean, median, and mode, choose between them, and prove the mean minimizes squared distance.
- [ ] I can compute sample variance and explain why it divides by $n - 1$.
- [ ] I can compute covariance and correlation by hand, and explain correlation as cosine similarity of centered data.
- [ ] I can explain correlation's two big limitations.
- [ ] I can compute a standard error and explain why it shrinks with $\sqrt{n}$.
- [ ] I can state the central limit theorem and build a 95% confidence interval.
- [ ] I can explain the bootstrap and why it works.
- [ ] I can explain p-values, the two error types, and the three traps.
- [ ] I can derive the least-squares line with partial derivatives, and compute $R^2$.
- [ ] I can explain bias and variance, and prove total error = bias² + variance.
- [ ] Check yourself: 10/10.
- [ ] Code lab done without AI.

---

## Symbol cheat sheet

| Symbol | Read it aloud as | Meaning | Section |
|---|---|---|---|
| $\mu$, $\sigma$ | "mu," "sigma" | population mean, standard deviation | §1 |
| $\bar{x}$, $s$ | "x bar," "s" | sample mean, standard deviation | §1 |
| $n$, $N$ | "n," "N" | sample size, population size | §1 |
| $s^2$ | "s squared" | sample variance (divides by $n - 1$) | §3 |
| $z_i$ | "z sub i" | standardized value | §3 |
| $s_{xy}$ | "covariance of x and y" | how $x$ and $y$ move together | §4 |
| $r$ | "r" or "correlation" | covariance without units, from $-1$ to $1$ | §4 |
| SE | "standard error" | how much an estimate wobbles | §5 |
| $H_0$ | "H nought" | the null hypothesis | §7 |
| $\alpha$ | "alpha" | significance cutoff (e.g. 0.05) | §7 |
| $R^2$ | "R squared" | fraction of variation a fitted line explains | §8 |
| $\hat{\theta}$ | "theta hat" | an estimate of $\theta$ | §9 |

---

## Resources (only if stuck)

1. **Best for intuition:** StatQuest videos on the matching topic: *Mean, Variance and Standard Deviation* (§2–§3), *Covariance* and *Pearson's Correlation* (§4), *Confidence Intervals* and *Bootstrapping* (§6), *p-values* (§7), *Linear Regression* (§8), *Bias and Variance* (§9). Find them on the [StatQuest video index](https://statquest.org/video-index/).
2. **Extra practice:** [Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability): units on summarizing data, sampling distributions, confidence intervals, and significance tests.
