---
title: Dopamine neurons and the reward prediction error
date: 2026-08-10
status: draft
topics: [neuroscience, reinforcement-learning, dopamine]
sources:
  - title: "Schultz, Dayan & Montague (1997). A Neural Substrate of Prediction and Reward. Science 275(5306), 1593–1599"
    url: https://doi.org/10.1126/science.275.5306.1593
  - title: "Sutton (1988). Learning to predict by the methods of temporal differences. Machine Learning 3, 9–44"
    url: https://doi.org/10.1007/BF00115009
  - title: "Matsumoto & Hikosaka (2009). Two types of dopamine neuron distinctly convey positive and negative motivational signals. Nature 459, 837–841"
    url: https://doi.org/10.1038/nature08028
  - title: "Howe et al. (2013). Prolonged dopamine signalling in striatum signals proximity and value of distant rewards. Nature 500, 575–579"
    url: https://doi.org/10.1038/nature12475
  - title: "Steinberg et al. (2013). A causal link between prediction errors, dopamine neurons and learning. Nature Neuroscience 16, 966–973"
    url: https://doi.org/10.1038/nn.3413
  - title: "Dabney et al. (2020). A distributional code for value in dopamine-based reinforcement learning. Nature 577, 671–675"
    url: https://doi.org/10.1038/s41586-019-1924-6
---

# Dopamine neurons and the reward prediction error

Midbrain dopamine neurons in the macaque fire in a pattern that looks like the
error term of temporal-difference learning. The correspondence is close enough
that an algorithm published in 1988 predicted, in outline, what an electrode
would record in 1997. That is why the result matters, and it is also why it gets
overstated: a striking match between a theory and a measurement invites the
reader to collapse the two, and much of the work since has been about why they
should not be collapsed.

This note is about what the 1997 recordings established, what they left open,
and which later results actually move the conclusion rather than decorate it.

## The algorithm came first

Temporal-difference learning was not derived from neuroscience. Sutton
introduced it for a purely computational problem: how to learn to predict a
delayed outcome without waiting for the outcome every time.

The setup is an agent moving through states. It keeps an estimate `V(s)` of the
total future reward available from state `s`. On each step it observes the
immediate reward `r` and the next state `s′`, and forms the error

```
δ = r + γV(s′) − V(s)
```

where `γ` discounts future reward. The term `r + γV(s′)` is a fresh estimate of
what `s` was worth, built from one step of real experience plus the current
guess about everything after it. `V(s)` is the old estimate. Their difference is
the surprise, and the algorithm nudges `V(s)` toward the fresh estimate in
proportion to it.

Three properties of `δ` matter for what follows, and all three fall out of the
definition rather than being bolted on:

**Positive on unexpected reward.** If reward arrives where none was predicted,
`r` is large and `V(s)` is not, so `δ` is positive.

**Zero once prediction is accurate.** Once `V` has learned, the fresh estimate
agrees with the old one and the difference vanishes. A perfectly predicted
reward produces no error at all — the signal is about the *unpredicted* part,
not about the reward.

**It moves backwards in time.** When a cue reliably precedes reward, the cue's
own value rises and the error appears at the cue instead of at the reward. This
is not a separate rule; it follows from `γV(s′)` carrying value one step back on
each visit.

## What the recordings showed

Schultz, Dayan and Montague recorded single units in the midbrain of macaques
learning conditioned tasks, and reported three patterns.

**An unpredicted reward produces a burst.** Juice delivered without warning
drives a short, sharp increase in firing above baseline.

**Once a cue predicts the reward, the burst moves to the cue.** After
conditioning, the same juice at the expected moment produces nothing. The burst
has transferred to the earliest reliable predictor.

**Reward withheld produces a dip.** If the cue appears and the reward does not,
firing drops below baseline — and it drops at the moment the reward was due, not
when the trial ends.

Set those against the three properties above and they match one for one,
including the detail hardest to get by accident: the timing of the dip. A neuron
that simply reported "something good happened" has no reason to do anything at a
moment when nothing happens. A neuron reporting `δ` has to, because at that
moment `V(s)` predicts reward and the observation contradicts it.

## What that establishes, and what it does not

The correspondence is strong evidence that dopamine carries
prediction-error-like information. It is not evidence that dopamine *is* the
prediction error, and the distance between those two statements is where the
later work lives.

### The original design is correlational

Neurons are recorded while an animal learns. Nothing is manipulated, so the
design cannot separate a signal that *drives* learning from one that merely
accompanies it. A signal correlated with `δ` is consistent with dopamine
broadcasting the teaching signal, and equally consistent with dopamine reporting
something that co-varies with it.

That gap was closed later, and it is worth being precise about how, because this
is the step that upgrades the story rather than repeating it.

Steinberg and colleagues used a **blocking** paradigm. In blocking, a second cue
introduced alongside an already-predictive first cue is normally *not* learned
about: the first cue already predicts the outcome, so there is no error left to
drive learning about the second. The theory's explanation for blocking is
exactly that `δ` is zero.

They then activated dopamine neurons optogenetically at the moment of reward —
precisely where the theory says the error should be zero — and animals learned
about the blocked cue anyway. An artificial `δ`, inserted where none existed,
produced the learning that a real `δ` would have.

That is causal, and it is a sharper test than it first appears: the manipulation
does not make the animal generally more attentive or the reward more pleasant.
It supplies one specific quantity at one specific moment, and the behaviour that
follows is the one the equation predicts.

### The population is treated as one signal

The 1997 account speaks of dopamine neurons as if they report a single scalar,
broadcast widely. Two later findings complicate that in different directions.

## What changes the reading

### The population is not homogeneous

Matsumoto and Hikosaka found two groups of dopamine neurons that behave
differently and sit in different places.

One group is excited by reward-predicting cues and inhibited by aversive ones —
the value-coding behaviour the RPE account expects. The other is excited by
*both* appetitive and aversive events, which is not value at all. It looks
closer to salience: "something important is happening", regardless of sign.

The two groups are anatomically separable, with value-coding neurons
concentrated more ventromedially and salience-like ones more dorsolaterally.

This does not overturn the 1997 result — the value-coding group behaves as
described. What it removes is the licence to speak of *the* dopamine signal. At
least one substantial population is doing something else, and an experiment that
samples the midbrain without regard to recording site will average across both
and report the blend as if it were one thing.

### The variability is not noise

Dabney and colleagues asked what the *spread* across dopamine neurons means. On
a scalar account, individual neurons are noisy copies of one quantity and the
differences between them are measurement error, to be averaged away.

The distributional account says otherwise. Neurons differ systematically in how
asymmetrically they treat positive and negative errors: some amplify positive
surprise relative to negative, others do the reverse. A neuron with that
asymmetry does not converge on the mean of future reward. It converges on a
**quantile** of the reward distribution, and which quantile is set by how
strongly it weights each direction.

A population with a spread of asymmetries therefore encodes a spread of
quantiles — a representation of the whole distribution over future reward rather
than of its expectation. The paper reports the asymmetry across recorded neurons
and decodes the implied distribution from it.

Under that reading, the 1997 experiments recorded the average of a population
code and named the average the code. The original observation survives; what it
was evidence *for* narrows.

### Ramping is still awkward

Howe and colleagues measured dopamine in the striatum with fast-scan cyclic
voltammetry while rats ran a maze for reward, and found slow ramps: dopamine
rising gradually as the animal approached the goal, over seconds.

A pure RPE should not do that. Once the path is well learned, each step is
predicted and the error should sit near zero throughout. A signal climbing
steadily with proximity looks more like value itself than like an error about
value.

Reconciliations exist — ramps as the derivative of a value function under
particular assumptions about state representation and discounting, or as a
distinct signal carried on a slower timescale by the same transmitter. What
matters here is that the ramp is a measurement in tension with the simple
version of the story, taken with a different method on a different timescale,
and it has not been dissolved by restating the theory.

## What would change this note

A demonstration that the value-coding and salience-coding populations are
separable by their **downstream targets**, not only by recording site, would
tighten the account considerably: it would turn an anatomical correlation into a
claim about what each signal is *for*.

A result showing the asymmetric scaling Dabney reports is an artefact of
recording or of the fitting procedure would return the population to a scalar
code and undo that section entirely.

A resolution of ramping that predicts *new* measurements, rather than
accommodating the existing ones, would close the loose end this note is
currently obliged to leave open.

## Why this sits in a machine learning repository

The traffic runs in both directions, and it is easy to mistake which way it is
running at any given moment.

TD learning was not copied from the brain. It came out of Sutton's work on
prediction, and the biology arrived afterwards as confirmation. Distributional
RL repeated the pattern in the same order: an algorithmic idea developed for
reasons internal to reinforcement learning, followed by a search for a neural
signature, which was then found.

So the honest summary is narrower than the popular one, and more interesting for
being narrower. Reinforcement learning did not learn its algorithms by looking
at brains. It produced theories precise enough that a brain could be used to
check them — which is a harder thing to do, and a better reason to care.

## Where it connects

Nothing yet. A note on distributional RL as an algorithm — quantile regression,
the asymmetric loss that produces the effect, and what predicting a distribution
buys over predicting a mean — belongs beside this one, and would let this note
stop explaining the algorithmic half in passing.
