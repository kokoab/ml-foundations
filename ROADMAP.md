# ML Foundations Roadmap

| Phase | Topic | Weeks | Main project |
|---|---|---|---|
| 1 | Mathematics | 1–3 | Mathematics final checkpoint |
| 2 | Python | 4 | `mean`, `variance`, `dot_product`, `sigmoid` from memory |
| 3 | Classical Machine Learning | 5–6 | Linear & logistic regression from scratch |
| 4 | Deep Learning | 7–8 | NumPy neural network on MNIST |
| 5 | PyTorch | 8 | Hand-written training loop |
| 6 | Computer Vision | 9–10 | Cats vs Dogs, transfer learning, object detection |
| 7 | Transformers | 10 | — |
| 8 | Machine Learning Engineering | 11 | Dataset → FastAPI → Docker pipeline |
| 9 | RAG / LLM Engineering | 12 | Upgrade DPWH Watchdog |

---

## Phase 1 — Mathematics

**Weeks 1–3**

This is the most important phase for you. But we're going to be ruthless about what actually matters for ML.

### 1. Algebra Refresh

#### Goal

You should be comfortable manipulating equations instead of feeling like you're rediscovering algebra every time.

#### Learn

- [ ] fractions
- [ ] exponents
- [ ] radicals
- [ ] logarithms
- [ ] equations
- [ ] inequalities
- [ ] functions
- [ ] inverse functions
- [ ] composition
- [ ] polynomial functions
- [ ] exponential functions
- [ ] logarithmic functions
- [ ] slopes
- [ ] coordinate geometry

#### Checkpoint

If:

$$
y = 3x + 2
$$

you should immediately understand:

- [ ] what $x$ represents
- [ ] what $y$ represents
- [ ] slope
- [ ] intercept
- [ ] how changing $x$ affects $y$
- [ ] how to solve for $x$
- [ ] what the graph looks like

#### Resource

[Khan Academy — Mathematics](https://www.khanacademy.org/math)

Don't watch everything. Use it diagnostically. If you already understand quadratic equations, don't spend six hours proving you understand them.

### 2. Functions

This is more important than people realize.

#### Learn

- [ ] domain/range
- [ ] function composition
- [ ] inverse functions
- [ ] linear functions
- [ ] nonlinear functions
- [ ] exponential functions
- [ ] logarithmic functions
- [ ] sigmoid
- [ ] ReLU
- [ ] softmax

#### Checkpoint

You should be able to look at:

$$
f(x)=\frac{1}{1+e^{-x}}
$$

and explain:

- [ ] what it does
- [ ] why it outputs between 0 and 1
- [ ] what happens when $x$ becomes very large
- [ ] what happens when $x$ becomes very negative
- [ ] why ML uses it

> [!IMPORTANT]
> If you can't explain that yet, don't move on.

### 3. Linear Algebra

This is your **#1 mathematical priority** for ML.

#### Learn

**Vectors**

- [ ] vectors
- [ ] vector addition
- [ ] scalar multiplication
- [ ] dot product
- [ ] vector magnitude
- [ ] distance
- [ ] cosine similarity

**Matrices**

- [ ] matrix representation
- [ ] matrix addition
- [ ] scalar multiplication
- [ ] matrix multiplication
- [ ] transpose
- [ ] identity matrix
- [ ] inverse
- [ ] determinant
- [ ] rank
- [ ] systems of equations

**Geometry**

- [ ] vector spaces
- [ ] linear transformations
- [ ] basis
- [ ] span
- [ ] orthogonality

#### ML connection

You need to understand

$$
y = Xw+b
$$

not just memorize it. You should know what every dimension means. For example:

```text
X  = 1000 × 10
w  =   10 × 1

Xw = 1000 × 1
```

That should eventually feel obvious.

#### Resources

- [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — excellent; has lectures, exercises, exams and notes.
- [3Blue1Brown — Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — pair it with MIT for visual explanations.

#### Checkpoint

- [ ] Explain: *"A matrix isn't just a spreadsheet of numbers. It can represent a transformation of vectors."*
- [ ] Actually demonstrate one in Python.

### 4. Calculus

You do not need to become a calculus monster. You need calculus that lets you understand learning.

#### Learn

- [ ] limits
- [ ] continuity
- [ ] derivative
- [ ] derivative rules
- [ ] chain rule
- [ ] partial derivatives
- [ ] gradients
- [ ] directional derivatives
- [ ] optimization
- [ ] minima/maxima

#### Especially

$$
\frac{d}{dx}x^2 = 2x
$$

Then:

$$
\frac{\partial f}{\partial x}
$$

Then:

$$
\nabla f
$$

Then:

$$
w := w-\alpha\nabla J(w)
$$

That final equation is **gradient descent**. This is where calculus becomes ML.

#### Resource

[3Blue1Brown — The Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — excellent because it emphasizes intuition rather than simply throwing derivative rules at you.

#### Checkpoint

Given

$$
f(x)=x^2+3x
$$

you should be able to:

- [ ] differentiate it
- [ ] calculate the derivative at a point
- [ ] explain what the derivative means geometrically
- [ ] find where the slope is zero
- [ ] connect this to optimization

### 5. Probability

This is where your future AI work starts becoming much more serious.

#### Learn

- [ ] probability basics
- [ ] sample spaces
- [ ] conditional probability
- [ ] independence
- [ ] Bayes theorem
- [ ] random variables
- [ ] probability distributions
- [ ] expected value
- [ ] variance
- [ ] standard deviation
- [ ] Gaussian distribution
- [ ] Bernoulli distribution
- [ ] binomial distribution

#### Especially

$$
P(A|B)
$$

and

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

You should understand *why* Bayes' theorem works. Not just memorize it.

#### Resource

[Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) has a very good progression through probability, conditional probability, Bayes, random variables, distributions and expected value.

### 6. Statistics

#### Learn

- [ ] mean
- [ ] median
- [ ] variance
- [ ] standard deviation
- [ ] covariance
- [ ] correlation
- [ ] distributions
- [ ] sampling
- [ ] confidence intervals
- [ ] hypothesis testing
- [ ] regression
- [ ] bias/variance

You don't need to become a statistician. But you need to understand what your model metrics actually mean.

### Mathematics Final Checkpoint

Before moving heavily into ML, you should be able to solve these **without AI**:

- [ ] **A.** Given vectors $a=[1,2,3]$ and $b=[4,5,6]$, calculate:
  - [ ] dot product
  - [ ] magnitude
  - [ ] cosine similarity
- [ ] **B.** Multiply two matrices manually.
- [ ] **C.** Differentiate $f(x)=3x^3+2x^2-5x+7$
- [ ] **D.** Find the partial derivatives of $f(x,y)=x^2+3xy+y^2$
- [ ] **E.** Explain $\nabla f$
- [ ] **F.** Calculate a basic probability.
- [ ] **G.** Explain conditional probability.
- [ ] **H.** Explain expectation and variance.
- [ ] **I.** Explain why gradient descent moves in the negative gradient direction.

If you can do those, your mathematical foundation is no longer the thing holding you back. Not perfect. But functional.

---

## Phase 2 — Python

**Week 4**

Now we make the math executable.

You already know some Python, so don't waste time doing a 30-hour beginner course. You need Python for scientific computing.

### Core Python

- [ ] variables
- [ ] conditionals
- [ ] loops
- [ ] functions
- [ ] parameters
- [ ] return values
- [ ] lists
- [ ] tuples
- [ ] dictionaries
- [ ] sets
- [ ] comprehensions
- [ ] modules
- [ ] imports
- [ ] exceptions
- [ ] file handling
- [ ] classes
- [ ] virtual environments
- [ ] packages

### NumPy

- [ ] arrays
- [ ] shape
- [ ] dtype
- [ ] indexing
- [ ] slicing
- [ ] broadcasting
- [ ] vectorization
- [ ] matrix multiplication
- [ ] transpose
- [ ] aggregation
- [ ] random
- [ ] linear algebra

### Pandas

- [ ] DataFrame
- [ ] Series
- [ ] loading CSV
- [ ] filtering
- [ ] grouping
- [ ] merging
- [ ] missing data
- [ ] aggregation

### Matplotlib

- [ ] line plots
- [ ] scatter plots
- [ ] histograms
- [ ] subplots
- [ ] labels
- [ ] interpreting graphs

### Python Checkpoint

Open a blank file and write each of these **without searching for the syntax**:

- [ ] `mean`

  ```python
  def mean(values):
      ...
  ```

- [ ] `variance`

  ```python
  def variance(values):
      ...
  ```

- [ ] `dot_product`

  ```python
  def dot_product(a, b):
      ...
  ```

- [ ] `sigmoid`

  ```python
  def sigmoid(x):
      ...
  ```

- [ ] Then implement matrix operations using NumPy.

---

## Phase 3 — Classical Machine Learning

**Weeks 5–6**

Now the mathematics finally pays off. Learn in this order:

### 1. Linear Regression

Understand:

$$
\hat y = Xw+b
$$

Then:

- [ ] loss function
- [ ] MSE
- [ ] gradient
- [ ] gradient descent
- [ ] learning rate
- [ ] convergence

#### First Big Project

- [ ] Implement linear regression from scratch using NumPy.

No sklearn. No PyTorch. Just:

- Python
- NumPy
- Math

### 2. Logistic Regression

#### Learn

- [ ] sigmoid
- [ ] binary classification
- [ ] decision boundary
- [ ] log loss
- [ ] gradient descent
- [ ] classification metrics

#### Project

- [ ] Implement logistic regression yourself.

#### Resource

[StatQuest](https://statquest.org/video-index/)'s logistic regression explanation is particularly useful as a conceptual companion.

### 3. Model Evaluation

#### Learn

- [ ] train/test split
- [ ] validation set
- [ ] cross-validation
- [ ] accuracy
- [ ] precision
- [ ] recall
- [ ] F1
- [ ] ROC-AUC
- [ ] confusion matrix
- [ ] regression metrics

> [!NOTE]
> A model being 95% accurate doesn't automatically mean it's good.

### 4. Overfitting

#### Learn

- [ ] underfitting
- [ ] overfitting
- [ ] bias
- [ ] variance
- [ ] regularization
- [ ] L1
- [ ] L2
- [ ] feature scaling

This is foundational.

### 5. Classical Algorithms

#### Learn

- [ ] linear regression
- [ ] logistic regression
- [ ] decision trees
- [ ] random forests
- [ ] gradient boosting
- [ ] k-nearest neighbors
- [ ] k-means
- [ ] PCA

Don't implement every single one from scratch. Implement the foundational ones. Use sklearn for the others.

#### Resource

[Andrew Ng — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) is a very good structured backbone here; it explicitly covers regression, classification, gradient descent, neural networks, decision trees, clustering, dimensionality reduction and model evaluation.

---

## Phase 4 — Deep Learning

**Weeks 7–8**

Now we get serious.

### Neural Networks

Understand:

$$
z = Wx+b
$$

$$
a=f(z)
$$

#### Learn

- [ ] neurons
- [ ] layers
- [ ] activation functions
- [ ] forward propagation
- [ ] loss
- [ ] gradient descent
- [ ] backpropagation

#### Project: Your First Deep-Learning Project

- [ ] Build a neural network from scratch using NumPy.
- [ ] Train it on MNIST.

Not a huge network. Something like:

```text
Input
  ↓
Linear
  ↓
ReLU
  ↓
Linear
  ↓
Softmax
```

#### Resources

- [3Blue1Brown — Neural Networks](https://www.3blue1brown.com/topics/neural-networks) — almost exactly what you need here. It covers neural networks, gradient descent, backpropagation and the mathematical mechanics behind learning.
- [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — particularly relevant to your goal because it starts from basic Python and builds neural networks by actually coding them. The first lecture builds micrograd and explicitly focuses on backpropagation.

---

## Phase 5 — PyTorch

**Week 8**

Now you earn the right to use frameworks.

### Learn

- [ ] tensors
- [ ] tensor shapes
- [ ] autograd
- [ ] datasets
- [ ] dataloaders
- [ ] models
- [ ] loss functions
- [ ] optimizers
- [ ] training loops
- [ ] validation loops
- [ ] checkpoints
- [ ] GPU/CPU
- [ ] inference

### Checkpoint

- [ ] Write a training loop yourself, without blindly copying it.

Something conceptually like:

```text
for epoch:
    for batch:
        prediction
        loss
        zero_grad
        backward
        optimizer.step()
```

---

## Phase 6 — Computer Vision

**Weeks 9–10**

This is where your existing ATLAS experience becomes useful.

### Learn

- [ ] image representation
- [ ] RGB
- [ ] tensors
- [ ] normalization
- [ ] convolution
- [ ] kernels
- [ ] padding
- [ ] stride
- [ ] pooling
- [ ] CNN architecture
- [ ] augmentation
- [ ] transfer learning
- [ ] embeddings
- [ ] classification
- [ ] object detection
- [ ] segmentation

### Projects

- [ ] Cats vs Dogs classifier from scratch using PyTorch
- [ ] Transfer-learning image classifier
- [ ] Small object detection project

You don't need to build YOLO from scratch. You need to understand what YOLO is doing.

---

## Phase 7 — Transformers

**Week 10**

You already have ATLAS exposure to transformers. Now understand the machinery.

### Learn

- [ ] embeddings
- [ ] positional encoding
- [ ] attention
- [ ] self-attention
- [ ] query/key/value
- [ ] multi-head attention
- [ ] feed-forward layers
- [ ] residual connections
- [ ] layer normalization
- [ ] encoder
- [ ] decoder
- [ ] autoregressive generation
- [ ] transformers vs RNNs

### Resource

[3Blue1Brown — But what is a GPT?](https://www.3blue1brown.com/lessons/gpt) — excellent for visual intuition; its neural-network topic collection includes the transformer and attention chapters.

---

## Phase 8 — Machine Learning Engineering

**Week 11**

This is where you stop being "someone who can train a model."

### Learn

- [ ] Git
- [ ] project structure
- [ ] configuration
- [ ] logging
- [ ] experiment tracking
- [ ] reproducibility
- [ ] data pipelines
- [ ] model serialization
- [ ] APIs
- [ ] Docker
- [ ] testing
- [ ] inference
- [ ] deployment

### Project

- [ ] Build the end-to-end pipeline:

```text
Dataset
   ↓
Preprocessing
   ↓
Training
   ↓
Evaluation
   ↓
Model
   ↓
FastAPI
   ↓
Docker
```

You already have backend experience. Use it. This is one of your advantages over someone who only knows notebooks.

---

## Phase 9 — RAG / LLM Engineering

**Week 12**

Now we touch the "AI Engineer" side.

### Learn

- [ ] embeddings
- [ ] vector similarity
- [ ] cosine similarity
- [ ] chunking
- [ ] retrieval
- [ ] reranking
- [ ] vector databases
- [ ] metadata filtering
- [ ] hybrid search
- [ ] prompt construction
- [ ] grounding
- [ ] hallucination
- [ ] RAG evaluation
- [ ] LLM APIs
- [ ] structured outputs

### Project: Upgrade DPWH Watchdog

You already have your DPWH Watchdog. Don't build another toy chatbot.

- [ ] Implement this pipeline:

```text
Question
  ↓
Query understanding
  ↓
Hybrid retrieval
  ↓
Metadata filtering
  ↓
Top-k documents
  ↓
Reranking
  ↓
LLM
  ↓
Grounded answer
  ↓
Sources
```

That would be far more impressive.
