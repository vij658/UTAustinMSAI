# Track A: AI math

The math you need to read the UT Austin MS in AI syllabi without freezing, built as a watch-while-riding path. It has **47 videos in 8 blocks** (Block 0 to Block 7). Every video below passed a YouTube oEmbed existence check (the lookup returned the same video ID, with the title and channel copied exactly). I did not watch them; see "Not checked" at the end.

**Hours:** only 8 of the 47 videos have a length I could confirm (together 2 h 58 m). For the rest YouTube blocked the length lookup, so they show "length ?". My expectation, not a measurement, is that the total lands in the low-to-mid 20s of hours. If you want more listening time, the "Optional extras" section lists more verified videos.

**Order logic:**

- Blocks run in dependency order: functions and notation (0), derivatives (1), vectors and matrices (2), multivariable calculus (3, which needs both 1 and 2), probability (4), statistics (5, which needs 4), optimization (6, which pulls together 1, 3 and 5), discrete math (7, light, last).
- Inside each block the visual-intuition video comes first (3Blue1Brown, Khan Academy, StatQuest, Steve Brunton), and the university lecture comes after it (MIT OpenCourseWare, Harvard Stat 110).
- Weighting follows the UT courses: SVD/PCA (Block 2), maximum likelihood and Bayesian inference (Block 5), gradient descent and convexity (Block 6), and probability and expectation (Block 4) get the most room. Block 7 is four videos.
- Each block ends with a "full circle" line (where the idea returns in machine learning) and three recap questions with hidden answers. Try to answer them out loud after the ride, before opening the answers.
- Where a video is a full university lecture, a note under the table says whether it is optional.



Conventions used in every table:

- **Level**: Start = no background needed. Deeper = university level. Scholar = research or proof depth.
- **Mode**: BIKE = you can ride and mostly listen, glancing at the screen. DESK = you need paper, code or pausing, so save it for a desk session.
- **Length**: copied from the YouTube page. "length ?" means the page would not show it (YouTube returned a bot-protection page), so the length is unconfirmed.
- **Status**: "verified" means the YouTube oEmbed lookup returned the same video ID, with the title and channel exactly as written in the table.
- Titles and channels are copied exactly as the oEmbed lookup returned them.

---

## Block 0: Warm-up (functions, exponents, logs, sigma, reading notation)

**Why AI needs this:** every model is a function with adjustable knobs, loss functions are written with Σ and log, and papers are unreadable until the notation stops being a wall of symbols.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1 | What is a function? \| Functions and their graphs \| Algebra II \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=kvGsIo1TmsM | length ? | Start | BIKE | The idea of a function as an input-to-output rule, and how to read f(x) notation. | verified |
| 2 | Zero, negative, and fractional exponents \| Pre-Algebra \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=tOuCdKqO6-s | 14:04 | Start | BIKE | What x^0, x^-2 and x^(1/2) mean, which you need before logs and e^x make sense. | verified |
| 3 | Introduction to Logarithms | Khan Academy | https://www.youtube.com/watch?v=mQTWzLpCcW0 | length ? | Start | BIKE | A log is the question "what power gives this number?"; the inverse of an exponent. | verified |
| 4 | Sigma notation for sums \| Sequences, series and induction \| Precalculus \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=5jwXThH6fg4 | length ? | Start | BIKE | How to read and expand Σ with its index and limits. Loss functions are sums like this. | verified |
| 5 | How to Read Math in Deep Learning Paper? | Deep Learning with Yacine | https://www.youtube.com/watch?v=YXWxVxQ6AeY | 27:17 | Start | DESK | A five-step method for reading formulas in a paper: identify, copy by hand, translate symbols into meaning, then compress to an intuition. Worked on the QHAdam optimizer. | verified |

**Full circle:** the cross-entropy loss −Σ yᵢ log(ŷᵢ) and the softmax e^zᵢ / Σ e^zⱼ are just the four things in this block (sum, log, exponent, function) wearing a suit.

**Recap questions** (answer out loud first, then open):

1. If h(x) = f(g(x)), which function is applied first?
2. Why does a log turn a product into a sum, and why do ML people like that?
3. Expand and evaluate Σ from i=1 to 3 of (2i + 1).

<details>
<summary>Answers</summary>

1. g is applied first, then f. A neural network is a long chain of such compositions, one per layer.
2. log(a·b) = log a + log b. A likelihood is a product of many small probabilities, which underflows and is awkward to differentiate; the sum of logs is stable and easy to differentiate.
3. (2·1+1) + (2·2+1) + (2·3+1) = 3 + 5 + 7 = 15.

</details>

---

## Block 1: Calculus I (derivatives, rules, chain rule)

**Why AI needs this:** training a model means nudging parameters to make the loss smaller, and the derivative is the tool that says which way to nudge and by how much.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6 | The essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=WUvTyaaNkzM | 17:04 | Start | BIKE | The big picture of calculus before any formulas. Watch this first. | verified |
| 7 | The paradox of the derivative \| Chapter 2, Essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=9vKqVkMQHKk | 16:50 | Start | BIKE | What a derivative is: the slope of a curve at one point, built up from tiny nudges. | verified |
| 8 | Derivative formulas through geometry \| Chapter 3, Essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=S0_qX4VJhMQ | 17:33 | Start | BIKE | Where the power rule and other basic derivative formulas come from, seen geometrically. | verified |
| 9 | Visualizing the chain rule and product rule \| Chapter 4, Essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=YG15m2VwSjA | length ? | Start | BIKE | The chain rule as nudges passing through stages. This is the idea behind backpropagation. | verified |
| 10 | What's so special about Euler's number e? \| Chapter 5, Essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=m2MIpDrF7Es | length ? | Start | BIKE | Why e^x is its own derivative, and how that connects to exponentials and logs from Block 0. | verified |

Practice tip: after #9, do three or four chain-rule exercises by hand on paper. A verified board-style lecture for extra practice is listed under "Optional extras" near the end.

**Full circle:** backpropagation is the chain rule applied layer by layer, and every gradient descent step uses the derivative of the loss. You will see this explicitly in Block 6 (3Blue1Brown, Backpropagation calculus).

**Recap questions:**

1. In plain words, what does f'(a) tell you about f near x = a?
2. State the chain rule for f(g(x)) and describe it as "nudges passing through stages".
3. What is d/dx of (3x + 1)², and what is d/dx of eˣ?

<details>
<summary>Answers</summary>

1. It is the slope of the tangent line at a, the instantaneous rate of change: a tiny nudge Δx changes f by about f'(a)·Δx.
2. d/dx f(g(x)) = f'(g(x)) · g'(x). A nudge in x changes g by g'(x) times as much, and that change in g changes f by f'(g) times as much, so the factors multiply.
3. With u = 3x + 1: 2(3x + 1)·3 = 6(3x + 1) = 18x + 6. And d/dx eˣ = eˣ, because its growth rate at every point equals its own value.

</details>

---

## Block 2: Vectors and linear algebra (vectors, dot product, matrices, determinant, eigen, SVD, PCA)

**Why AI needs this:** data points are vectors, every neural-network layer is a matrix acting on them, and SVD/PCA are how you find the few directions that actually matter in high-dimensional data.

Order logic: the 3Blue1Brown series (#11 to #17) is watched in its own chapter order, because each chapter assumes the previous one. The dot product (#16) comes after matrices as transformations because the video explains the dot product through them. Then eigenvectors, then SVD (visual first, Strang's lecture last), with PCA in between because it is SVD applied to data.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 11 | Vectors \| Chapter 1, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=fNk_zzaMoSs | length ? | Start | BIKE | Vectors as arrows, as lists of numbers, and the idea that vector addition and scaling are what matter. | verified |
| 12 | Linear combinations, span, and basis vectors \| Chapter 2, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=k7RM-ot2NWY | length ? | Start | BIKE | Linear combinations, span and basis vectors: the vocabulary for everything after. | verified |
| 13 | Linear transformations and matrices \| Chapter 3, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=kYB8IZa5AuE | length ? | Start | BIKE | A matrix as a transformation of space: the columns say where the basis vectors land. The key mental model of the whole track. | verified |
| 14 | Matrix multiplication as composition \| Chapter 4, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=XkY2DOUCWMU | length ? | Start | BIKE | Matrix multiplication as doing one transformation after another. | verified |
| 15 | The determinant \| Chapter 6, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=Ip3X9LOh2dk | 10:03 | Start | BIKE | The determinant as the factor by which a transformation scales area or volume. | verified |
| 16 | Dot products and duality \| Chapter 9, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=LyGKycYT2v0 | length ? | Start | BIKE | The dot product, why it measures alignment, and how it connects to transformations. Attention and embeddings use this everywhere. | verified |
| 17 | Eigenvectors and eigenvalues \| Chapter 14, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=PFDu9oVAE-g | length ? | Start | BIKE | Eigenvectors as the directions a transformation only stretches, and eigenvalues as the stretch factors. | verified |
| 18 | Singular Value Decomposition (SVD): Overview | Steve Brunton | https://www.youtube.com/watch?v=gXbThCXjZFM | length ? | Deeper | BIKE | The big picture of SVD as a factorization of any matrix and why it is useful for data. | verified |
| 19 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Deeper | BIKE | PCA worked through step by step, which makes the SVD idea concrete on data. | verified |
| 20 | 29. Singular Value Decomposition | MIT OpenCourseWare | https://www.youtube.com/watch?v=TX_vooSnhm8 | length ? | Scholar | DESK | The classic university lecture on SVD (MIT 18.06 numbering). Watch it after #18 and #19 so the formulas already have a picture behind them. | verified |

Note on #20: it is a full university lecture and its length is unconfirmed. I kept it because SVD is central to the UT courses and it is the one lecture-depth treatment I verified. Steve Brunton's "Mathematical Overview" (listed under Optional extras) is a possible alternative, but I could not confirm its length either. If you only want intuition, #18 and #19 are enough and you can skip #20.

**Full circle:** a dense layer is y = Wx + b, attention scores are dot products, embeddings are compared by dot product or cosine, PCA and SVD give dimensionality reduction, and low-rank ideas (including LoRA) are truncated SVD in spirit.

**Recap questions:**

1. What do the columns of a matrix tell you?
2. What does the determinant measure, and what does a determinant of 0 mean?
3. What is an eigenvector, and how are PCA and SVD related to it?

<details>
<summary>Answers</summary>

1. Where the basis vectors land after the transformation. Every other vector follows from that, because it is a linear combination of the basis vectors.
2. The factor by which the transformation scales area (2D) or volume (3D). A determinant of 0 means space is squashed into a lower dimension, so the matrix cannot be undone (not invertible). A negative sign means orientation flips.
3. An eigenvector is a direction that the transformation only stretches or shrinks (by its eigenvalue) without rotating it off its line. SVD writes any matrix as rotate, stretch along axes, rotate (A = UΣVᵀ). PCA applies this to centered data: the principal components are the directions of greatest variance, found from the top singular vectors (equivalently the top eigenvectors of the covariance matrix). Keep the top few to compress.

</details>

---

## Block 3: Multivariable calculus (partials, gradient, Jacobian)

**Why AI needs this:** a loss depends on millions of parameters at once, so you need a derivative that handles many inputs: the gradient for one output, the Jacobian for many.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 21 | Partial derivatives, introduction | Khan Academy | https://www.youtube.com/watch?v=AXqhWeUEtQU | length ? | Start | BIKE | Taking the derivative with respect to one variable while the others are held fixed. | verified |
| 22 | Gradient | Khan Academy | https://www.youtube.com/watch?v=tIpKfDc295M | length ? | Deeper | BIKE | The gradient as the vector of partial derivatives (title-based description; I did not confirm the content beyond the title). | verified |
| 23 | The Jacobian matrix | Khan Academy | https://www.youtube.com/watch?v=bohL918kXQk | length ? | Deeper | BIKE | The Jacobian as the matrix of partial derivatives, tying this block back to matrices from Block 2 (title-based description). | verified |
| 24 | Lec 12: Gradient; directional derivative; tangent plane \| MIT 18.02 Multivariable Calculus, Fall 07 | MIT OpenCourseWare | https://www.youtube.com/watch?v=2XraaWefBd8 | length ? | Deeper | DESK | A full university lecture on the gradient and directional derivatives, for after the shorter videos above. | verified |

Note on #24: it is a full lecture with unconfirmed length. It is optional: #21 to #23 cover what the later blocks use. Take it if the gradient still feels like symbols and not a direction.

**Full circle:** gradient descent moves every parameter along minus the gradient of the loss, and backpropagation computes that gradient by multiplying Jacobians layer by layer (you will see it done in Block 6).

**Recap questions:**

1. What is a partial derivative?
2. What does the gradient of a function point toward, and what does its length mean?
3. For f taking n numbers in and giving m numbers out, what shape is its Jacobian, and what does it represent?

<details>
<summary>Answers</summary>

1. The derivative with respect to one input while treating all the other inputs as constants.
2. The gradient is the vector of all partial derivatives. It points in the direction of steepest increase, and its length is how steep that increase is. To reduce a loss you step the opposite way.
3. An m × n matrix whose entry (i, j) is ∂fᵢ/∂xⱼ. It is the best linear (matrix) approximation of f near a point, so the chain rule for vector functions becomes multiplying Jacobians.

</details>

---

## Block 4: Probability (events, conditional probability, Bayes, random variables, expectation, distributions)

**Why AI needs this:** the world is noisy, models output probabilities, and almost every training objective is an expected value over data.

Order logic: Khan gives the first vocabulary, 3Blue1Brown gives the Bayes picture, then the Harvard Stat 110 lectures build the formal version. Blitzstein's lectures are story-driven, so I marked most of them BIKE, but pause for the derivations. That mode is my judgement from the format, not something I could check.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 25 | Probability explained \| Independent and dependent events \| Probability and Statistics \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=uzkc-qNVoOk | length ? | Start | BIKE | A gentle first pass at probability with independent and dependent events (title-based description). | verified |
| 26 | Bayes theorem, the geometry of changing beliefs | 3Blue1Brown | https://www.youtube.com/watch?v=HZGCoVF3YvM | length ? | Start | BIKE | Bayes' theorem as a picture of how evidence reshapes a belief. | verified |
| 27 | Lecture 4: Conditional Probability \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=P7NE4WF8j-Q | length ? | Deeper | BIKE | The formal treatment of conditional probability and how to think with it. | verified |
| 28 | Lecture 8: Random Variables and Their Distributions \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=k2BB0p8byGA | length ? | Deeper | BIKE | What a random variable is and how a distribution describes it. | verified |
| 29 | Lecture 9: Expectation, Indicator Random Variables, Linearity \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=LX2q356N2rU | length ? | Deeper | BIKE | Expectation, and the linearity trick with indicator variables that makes hard averages easy. | verified |
| 30 | Lecture 13: Normal distribution \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=72QjzHnYvL0 | length ? | Deeper | BIKE | The normal (Gaussian) distribution in depth. | verified |
| 31 | But what is the Central Limit Theorem? | 3Blue1Brown | https://www.youtube.com/watch?v=zeJD6dqJ5lo | length ? | Start | BIKE | Why sums and averages of many random things look normal. | verified |
| 32 | Lecture 28: Inequalities \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=UtXK_EQ3Pow | length ? | Scholar | DESK | Probability inequalities. This is the proof-flavoured background for the PAC-learning style bounds in the UT courses. | verified |

Note on lectures #27 to #30 and #32: each is a full university lecture and lengths are unconfirmed. I found no verified short video that covers conditional probability, random variables, expectation and the normal distribution at this depth. #25, #26 and #31 are the short on-ramps.

**Full circle:** a classifier's softmax output is a probability distribution, cross-entropy is an expected negative log probability, a mini-batch average estimates an expectation, MDPs are defined with expectations, and the inequalities in #32 are the starting point of generalization bounds.

**Recap questions:**

1. State the definition of P(A | B) and Bayes' rule.
2. Is E[X + Y] = E[X] + E[Y] only when X and Y are independent? Use it to find E for a Binomial(n, p).
3. What does the Central Limit Theorem say?

<details>
<summary>Answers</summary>

1. P(A | B) = P(A and B) / P(B). Bayes: P(A | B) = P(B | A) · P(A) / P(B). In words: update the prior P(A) by how likely the evidence is under A, relative to how likely it is overall.
2. No, linearity of expectation holds always, independent or not. A Binomial(n, p) is a sum of n indicator variables that each have expectation p, so its expectation is np.
3. The sum or average of many independent random variables with finite variance is approximately normal, whatever the shape of the original distribution. The sample mean is roughly N(μ, σ²/n).

</details>

---

## Block 5: Statistics (estimation, maximum likelihood, Bayesian inference basics)

**Why AI needs this:** training a model is estimating its parameters from data, and maximum likelihood and Bayesian inference are the two principled ways to say what "best estimate" means.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 33 | The standard error, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=XNgt7F6FqDU | length ? | Start | BIKE | How uncertain an estimate from a sample is, and how that uncertainty shrinks with more data. | verified |
| 34 | Maximum Likelihood, clearly explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=XepXtl9YKwc | length ? | Start | BIKE | The core idea of maximum likelihood: pick the parameters that make the observed data most probable. | verified |
| 35 | Maximum Likelihood For the Normal Distribution, step-by-step!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=Dn6b9fCIUpM | length ? | Deeper | DESK | A worked maximum-likelihood derivation for a normal distribution. Pause and follow on paper. | verified |
| 36 | Binomial distributions \| Probabilities of probabilities, part 1 | 3Blue1Brown | https://www.youtube.com/watch?v=8idr1WZ1A7Q | length ? | Start | BIKE | The binomial distribution, and the Bayesian idea of putting a probability distribution on an unknown probability (title-based description). | verified |
| 37 | Bayesian Maximum Aposteriori Estimation (MAP): Extending Maximum Likelihood Estimation | Steve Brunton | https://www.youtube.com/watch?v=xgfexqYxrDU | length ? | Deeper | BIKE | MAP as maximum likelihood plus a prior, which bridges to regularization. | verified |

**Full circle:** minimizing squared error or cross-entropy is maximum likelihood under a noise model, L2 regularization is MAP with a Gaussian prior on the weights, and the standard error is why more data and bigger batches give steadier estimates.

**Recap questions:**

1. How does a likelihood differ from a probability?
2. You flip a coin 10 times and see 7 heads. What is the maximum-likelihood estimate of p? If you had 4 times as much data, how would the standard error of the sample mean change?
3. How is MAP different from maximum likelihood?

<details>
<summary>Answers</summary>

1. Probability fixes the parameters and asks how likely different data are. Likelihood fixes the observed data and asks how plausible different parameter values are. A likelihood does not sum to 1 over the parameters.
2. p̂ = 7/10 = 0.7. The standard error of a sample mean is σ/√n, so 4 times the data halves it.
3. MAP maximizes likelihood times prior (the posterior), while maximum likelihood uses the likelihood alone. With a flat prior they coincide. A Gaussian prior on weights adds an L2 penalty, which is why it relates to regularization.

</details>

---

## Block 6: Optimization (gradient descent, learning rate, SGD, convexity intro, and backprop as the payoff)

**Why AI needs this:** this is the training loop itself: take the loss from Blocks 4 and 5, take the gradient from Blocks 1 and 3, and walk downhill.

Order logic: 3Blue1Brown first for the picture (it is chapter 2 of a series on neural networks; if the network diagram is completely new to you, chapter 1 is listed under "Optional extras", so watch that first), then StatQuest for numbers you can follow, then SGD, then a first look at convexity, and finally backpropagation, which pulls Blocks 1 to 3 together.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 38 | Gradient descent, how neural networks learn \| Deep Learning Chapter 2 | 3Blue1Brown | https://www.youtube.com/watch?v=IHZwWFHWa-w | length ? | Start | BIKE | Gradient descent as walking downhill on a cost surface, shown on a real network. | verified |
| 39 | Gradient Descent, Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=sDv4f4s2SB8 | length ? | Start | BIKE | Gradient descent with actual numbers: step size, learning rate, and when to stop. | verified |
| 40 | Stochastic Gradient Descent, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=vMh0zPT0tLI | length ? | Start | BIKE | Why using a random subset of the data per step still works. | verified |
| 41 | Convexity 101 [Optimization Bootcamp] | Steve Brunton | https://www.youtube.com/watch?v=9WXVgQFFsDI | length ? | Deeper | BIKE | A first look at convex sets and functions, and why convexity makes optimization easy. | verified |
| 42 | Backpropagation, intuitively \| Deep Learning Chapter 3 | 3Blue1Brown | https://www.youtube.com/watch?v=Ilg3gGewQ5U | length ? | Start | BIKE | What backpropagation is doing, with no calculus yet. | verified |
| 43 | Backpropagation calculus \| Deep Learning Chapter 4 | 3Blue1Brown | https://www.youtube.com/watch?v=tIeHLnjs5U8 | length ? | Deeper | DESK | Backpropagation as the chain rule from Block 1, written out. Pause and follow the derivatives on paper. | verified |

Note: I verified a full Stanford convex-optimization lecture exists (Boyd, EE364A, Lecture 1; see "Optional extras") but did not include it in the main path. #41 is the gentler on-ramp, and the full lectures are a time commitment you can decide on later.

**Full circle:** every optimizer used in deep learning (momentum, Adam) is a variation on #38 to #40, backpropagation (#43) is the chain rule from Block 1 computing the gradient from Block 3, and convexity (#41) is why classical models such as logistic regression and SVMs come with guarantees while deep nets do not.

**Recap questions:**

1. Write the gradient descent update and say what happens if the learning rate is too small or too large.
2. How does SGD differ from full gradient descent, and why does it help?
3. What is a convex function, and why does it make optimization easier?

<details>
<summary>Answers</summary>

1. θ ← θ − η ∇L(θ). Too small and training crawls; too large and the steps overshoot, bounce around or diverge.
2. SGD estimates the gradient from a random mini-batch instead of the whole dataset. The estimate is noisy but unbiased, each step is cheap, and the noise can help escape shallow bad spots, so you get many more updates per unit of compute.
3. A function where the straight line between any two points on its graph lies on or above the graph. Every local minimum is then a global minimum, so gradient descent with a suitable step size gets to the best answer.

</details>

---

## Block 7: Discrete math and proofs (light: logic, sets, induction, counting, graphs)

**Why AI needs this:** it is the language of algorithm analysis, learning theory (counting hypotheses), and anything built on graphs, from computation graphs to Bayesian networks and MDP state diagrams.

This block is deliberately light. Lecture topics for MIT 6.042J are taken from the official MIT OpenCourseWare lecture list (Lecture 2: Induction; Lecture 6: Graph Theory and Coloring; Lecture 16: Counting Rules I); the YouTube titles only say "Lec N", so the topic is by lecture number from that list.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 44 | Propositional Logic: The Complete Crash Course | TrevTutor | https://www.youtube.com/watch?v=AVl3wK2yTEc | 53:48 | Start | DESK | Propositions, truth tables, logical equivalence, conditionals and contrapositives, and basic inference (from the video's chapter list). | verified |
| 45 | Lec 2 \| MIT 6.042J Mathematics for Computer Science, Fall 2010 | MIT OpenCourseWare | https://www.youtube.com/watch?v=z8HKWUWS-lA | length ? | Deeper | DESK | Proof by induction. | verified |
| 46 | Lec 6 \| MIT 6.042J Mathematics for Computer Science, Fall 2010 | MIT OpenCourseWare | https://www.youtube.com/watch?v=h9wxtqoa1jY | length ? | Deeper | DESK | Graph theory and coloring. | verified |
| 47 | Lec 16 \| MIT 6.042J Mathematics for Computer Science, Fall 2010 | MIT OpenCourseWare | https://www.youtube.com/watch?v=pNt5Ll6hGqo | length ? | Deeper | DESK | Counting rules. | verified |

Note on #44: at 53:48 it is long, and I found no verified shorter propositional-logic video that also covers conditionals and inference, so I kept it. It has chapter marks, so you can do it in two rides. Sets have no dedicated video in the main path (see Gaps).

**Full circle:** induction is how you prove a recursive algorithm or a property of every layer of a network, counting gives the binomial coefficients behind probability and the size of hypothesis classes in PAC learning, and graphs are the structure of computation graphs, Bayesian networks and MDPs.

**Recap questions:**

1. What is the contrapositive of "if P then Q", and is it equivalent to the original?
2. What are the two parts of a proof by induction?
3. How many ways can you choose 3 items from 10 when order does not matter, and when it does?

<details>
<summary>Answers</summary>

1. "If not Q then not P". Yes, it is logically equivalent to the original statement (the converse and inverse are not).
2. The base case (the claim holds for the first value) and the inductive step (assuming it holds for k, show it holds for k + 1). Like dominoes: the first falls, and each one knocks over the next.
3. Order does not matter: C(10, 3) = 120. Order matters: 10 · 9 · 8 = 720.

</details>

---

## Optional extras (verified to exist, not counted in the main path)

These passed the same oEmbed check. Use them to deepen a block or to add listening hours if the main path feels too short. Lengths were not confirmed.

| Block | Title | Channel | Link | Length | Status |
|-------|-------|---------|------|--------|--------|
| 1 | Calculus 1 Lecture 2.6: Discussion of the Chain Rule for Derivatives of Functions | Professor Leonard | https://www.youtube.com/watch?v=8dr1dZjfhmc | length ? | verified |
| 0 | Introduction to logarithm properties \| Logarithms \| Algebra II \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=PupNgv49_WY | length ? | verified |
| 2 | Inverse matrices, column space and null space \| Chapter 7, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=uQhTuRlWMxw | length ? | verified |
| 2 | 21. Eigenvalues and Eigenvectors | MIT OpenCourseWare | https://www.youtube.com/watch?v=cdZnhQjJu4I | length ? | verified |
| 2 | Singular Value Decomposition (SVD): Mathematical Overview | Steve Brunton | https://www.youtube.com/watch?v=nbBvuuNVfco | length ? | verified |
| 3 | Computing a Jacobian matrix | Khan Academy | https://www.youtube.com/watch?v=CGbBbH1e7Yw | length ? | verified |
| 3 | Lec 8: Level curves; partial derivatives; tangent plane \| MIT 18.02 Multivariable Calculus, Fall 07 | MIT OpenCourseWare | https://www.youtube.com/watch?v=dK3NEf13nPc | length ? | verified |
| 4 | Lecture 1: Probability and Counting \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=KbB0FjPg0mw | length ? | verified |
| 4 | Lecture 5: Conditioning Continued, Law of Total Probability \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=JzDvVgNDxo8 | length ? | verified |
| 4 | Lecture 10: Expectation Continued \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=P1fSFvhPf7Q | length ? | verified |
| 4 | Lecture 11: The Poisson distribution \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=TD1N4hxqMzY | length ? | verified |
| 4 | Lecture 29: Law of Large Numbers and Central Limit Theorem \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=OprNqnHsVIA | length ? | verified |
| 4 | The medical test paradox, and redesigning Bayes' rule | 3Blue1Brown | https://www.youtube.com/watch?v=lG4VkPoG3ko | length ? | verified |
| 5 | Machine Learning Fundamentals: Bias and Variance | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=EuBBz3bI-aA | length ? | verified |
| 6 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | length ? | verified |
| 6 | Convexity Implies that Local Minima are Global Minima | Steve Brunton | https://www.youtube.com/watch?v=D-Qy9QfJgQg | length ? | verified |
| 6 | Stanford EE364A Convex Optimization I Stephen Boyd I 2023 I Lecture 1 | Stanford Online | https://www.youtube.com/watch?v=kV1ru-Inzl4 | length ? | verified |
| 7 | Lec 1 \| MIT 6.042J Mathematics for Computer Science, Fall 2010 (Introduction and Proofs, per the OCW list) | MIT OpenCourseWare | https://www.youtube.com/watch?v=L3LMbpZIKhQ | length ? | verified |
| 7 | Lec 3 \| MIT 6.042J Mathematics for Computer Science, Fall 2010 (Strong Induction, per the OCW list) | MIT OpenCourseWare | https://www.youtube.com/watch?v=NuGDkmwEObM | length ? | verified |
| 7 | Intersection of Sets, Union of Sets and Venn Diagrams | The Organic Chemistry Tutor | https://www.youtube.com/watch?v=xZELQc11ACY | length ? | verified |

Suggested use: if #20 or #27 feels like a cold start, do Stat 110 Lecture 1 and Lecture 5 first (probability and counting, then conditioning). If #44 feels too fast for induction, add MIT Lec 1 before #45.

---

## Gap-fill pass 1 (2026-11-10)

Method: every video below passed the same YouTube oEmbed check as the main path (the lookup returned the title and channel copied here, for the ID in the link). I did not watch any of them, and a length is shown only where I saw one on a page (the source is named); otherwise it says "length ?".

### Continuous random variables and densities (Block 4 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G1 | Why “probability of 0” does not mean “impossible” \| Probabilities of probabilities, part 2 | 3Blue1Brown | https://www.youtube.com/watch?v=ZA4JkHKZM50 | length ? | Start | BIKE | Why a single exact value of a continuous variable has probability 0, and how a density (height as probability per unit, area as probability) fixes that. | verified; content per rosetta.to page |
| G2 | Lecture 12: Discrete vs. Continuous, the Uniform \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=Tci---bVs60 | length ? | Deeper | BIKE | The PDF as a density and not a probability, PDF versus CDF, expectation and variance for continuous variables, LOTUS and the Uniform distribution. | verified; content per stat110-notes page |

Belongs after #29 (expectation) and before #30 (normal distribution): watch G1 first for the picture, then G2 for the formal version. G1 also continues #36, so you can leave it until then if you prefer.

### Bayesian inference beyond the basics (Block 5 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G3 | Explaining the intuition behind Bayesian inference | Ben Lambert | https://www.youtube.com/watch?v=yvWlpwnT1nw | length ? | Start | BIKE | An intuition-first look at Bayesian inference (title-based; I did not confirm the content beyond the title). | verified; title-based |
| G4 | Lecture 23: Beta distribution \| Statistics 110 | Harvard University | https://www.youtube.com/watch?v=UZjlBQbV1KU | length ? | Deeper | DESK | The Beta distribution as a prior for an unknown probability, and the Beta-Binomial update (a Beta prior plus Binomial data gives a Beta posterior). The page also lists a finance guest segment, which you can skip. | verified; content per stat110-notes page |

Belongs after #36 (probabilities of probabilities, part 1) and #37 (MAP): watch G3 right after #36, and G4 after G2 and #37, because it needs densities and the prior-times-likelihood idea. MAP versus maximum likelihood is already covered by #37, so I did not add a separate video for it.

### Momentum, Adam and learning-rate decay (Block 6 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G5 | L12.3 SGD with Momentum | Sebastian Raschka | https://www.youtube.com/watch?v=gMxvefj0YAM | length ? | Deeper | BIKE | Momentum added to SGD, the first step before the adaptive optimizers (title-based). | verified; title-based |
| G6 | L12.4 Adam: Combining Adaptive Learning Rates and Momentum | Sebastian Raschka | https://www.youtube.com/watch?v=eUOvUIRPSX8 | 15 min (per podwise, rounded) | Deeper | DESK | Adam as adaptive learning rates plus momentum (title-based). The update rules are formulas, so pause and follow them on paper. | verified; length per podwise, content title-based |
| G7 | L12.1 Learning Rate Decay | Sebastian Raschka | https://www.youtube.com/watch?v=Owm1H0ukjS4 | length ? | Deeper | BIKE | Why and how the learning rate is lowered during training (title-based). | verified; title-based |

Belongs after #40 (SGD): watch G5, then G6. G7 can go any time after #39 (gradient descent step by step), which is where the learning rate is first explained. These three come from one lecture series (L12.0 to L12.6); I used podwise only to see the lecture titles and one length. I did not find or check a verified RMSProp-only video, so RMSProp is covered only inside G6.

### Hessian and second-order conditions (Block 6 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G8 | The Hessian matrix \| Multivariable calculus \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=LbBcuZukCAw | length ? | Deeper | BIKE | The Hessian as the matrix that collects all second partial derivatives, with a worked two-variable example. | verified; content per rosetta.to page |
| G9 | Second partial derivative test intuition | Khan Academy | https://www.youtube.com/watch?v=sJo7D74PAak | length ? | Deeper | DESK | Why the sign of the second-derivative test separates local minimum, local maximum and saddle point for two variables, using xy and x^2 - y^2 as examples. | verified; content per rosetta.to page |
| G10 | Operations Research 10B: Hessian Matrix, Convex & Concave Functions | Yong Wang | https://www.youtube.com/watch?v=F3YoC5A6Avg | length ? | Deeper | DESK | Hessian, positive and negative semidefinite matrices, and convex and concave functions (title-based, plus the topic list on a third-party listing page that I could not tie to this exact video ID). | verified; title-based |

Belongs after #41 (Convexity 101) and before #42: watch G8, then G9, then G10, which is the only one aimed at semidefinite Hessians and convexity. G8 and G9 build on Block 3 (#21 to #23), so if second partial derivatives feel rusty, revisit #21 first. I could not judge the teaching quality of G10, so treat it as optional.

### Sets (Block 7 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G11 | Intersection and union of sets \| Probability and Statistics \| Khan Academy | Khan Academy | https://www.youtube.com/watch?v=jAfNg3ylZAI | length ? | Start | BIKE | Sets as collections of distinct objects, then intersection and union drawn with Venn diagrams. Complements are not mentioned on the page I read. | verified; content per rosetta.to page |
| G12 | Expressing Events with Set Operations | Dr. Dylan Spicker | https://www.youtube.com/watch?v=UU6e6hHSgxg | length ? | Start | BIKE | Writing probability events with set operations (title-based; I did not confirm whether complements are covered). | verified; title-based |

Belongs after #44 (propositional logic) and before #45 (induction): watch G11, then G12. G12 links sets back to events in Block 4, so it can also be done early if event notation in #25 to #27 looks unfamiliar. The Organic Chemistry Tutor video under Optional extras remains an alternative.

---

## Gaps

- **Sets (Block 7):** I verified only one basic Venn-diagram video (The Organic Chemistry Tutor, listed under Optional extras). I did not judge it good enough for the main path, so sets have no main-path video. Filled in gap-fill pass 1: G11, G12.
- **Learning-rate schedules, momentum and Adam (Block 6):** searches returned several candidates, but I did not run the oEmbed check on any of them, so none is listed. #39 covers the learning rate itself; the named optimizers are a gap. Filled in gap-fill pass 1: G5, G6, G7.
- **Hessian and second-order conditions for convexity (Block 6):** no candidate found that I could check. #41 covers convexity at the intuition level only. Filled in gap-fill pass 1: G8, G9, G10.
- **Bayesian inference beyond the basics (Block 5):** coverage is thin. #36 and #37 give the idea and the link to regularization, but there is no verified video on conjugate priors or posterior updating with a continuous prior in the main path. Filled in gap-fill pass 1: G3, G4.
- **Continuous random variables and densities (Block 4):** only covered inside the normal-distribution lecture (#30) and the CLT video (#31), with no dedicated video. Stat 110 lectures on this exist but were not checked. Filled in gap-fill pass 1: G1, G2.

## Not checked

- **Lengths:** only 8 of 47 main-path videos have a confirmed length (#2, #5, #6, #7, #8, #15, #19, #44). For the other 39 and for every optional extra, YouTube returned a bot-protection page and I did not work around it, so they show "length ?". The confirmed ones sum to 2 h 58 m 36 s.
- **Total hours is therefore not confirmed.** The 3Blue1Brown, Khan and StatQuest videos are usually short and the lectures are usually around an hour, so the total probably falls somewhere in the low-to-mid 20s of hours, which is at or just under the requested range. This is an expectation, not a measurement; check the lengths on the day before you plan a ride.
- **Content of videos:** I confirmed that each video exists, with the title and channel above, but I did not watch any of them. Descriptions in "What you will get" are drawn from titles, chapter lists and series context, and are marked "title-based" where I had nothing else (#22, #23, #25, #36). MIT 6.042J lecture topics come from the OCW lecture list, not from the YouTube pages.
- **Gap-fill rows (G1 to G12):** I did not watch any of them. Lengths are given only where I saw one on a page (G6, per podwise, rounded); every other row shows "length ?". Content notes come from the named listing pages or from titles only, as marked in the Status column.
- **Level and Mode tags** are my judgement from the format and creator, not something a lookup can verify.
- **Not included, not checked for content:** a PAC-learning and VC-dimension lecture (Caltech, "Lecture 07 - The VC Dimension", https://www.youtube.com/watch?v=Dc0sr0kdBVI) passed the existence check, but it belongs to ML theory rather than this math track, so I left it out. A Technion "Lecture 4-5: Convex sets and functions" (https://www.youtube.com/watch?v=knBF1VfjSz4) also exists, but I did not confirm its language, so I left it out. The 2023 Boyd Lecture 3 (convex functions) could not be verified (the oEmbed lookup failed), so it is not listed.
- **Passed the existence check but not used:** "The Mean Squared Error of an Estimator and the Bias Variance Tradeoff" (Mike, the Mathematician, https://www.youtube.com/watch?v=UAefABgvb84), "What are Maximum Likelihood (ML) and Maximum a posteriori (MAP)?" (Iain Explains Signals, Systems, and Digital Comms, https://www.youtube.com/watch?v=9Ahdh_8xAEI), "Explaining the intuition behind Bayesian inference" (Ben Lambert, https://www.youtube.com/watch?v=yvWlpwnT1nw), and "Maximum Likelihood Estimation (MLE): The Intuition" (IntuitiveML, https://www.youtube.com/watch?v=wbh730SeqeA). I did not check their length or content, so I did not put them in the path. The Ben Lambert one is the first to try if you want more Bayesian inference (see Gaps).

