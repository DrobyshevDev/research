---
title: Dopamine neurons and the reward prediction error
date: 2026-08-10
status: draft
topics: [neuroscience, reinforcement-learning, dopamine]
sources:
  - title: "Schultz, Dayan & Montague (1997). A Neural Substrate of Prediction and Reward. Science 275(5306), 1593–1599"
    url: https://doi.org/10.1126/science.275.5306.1593
  - title: "Matsumoto & Hikosaka (2009). Two types of dopamine neuron distinctly convey positive and negative motivational signals. Nature 459, 837–841"
    url: https://doi.org/10.1038/nature08028
  - title: "Dabney et al. (2020). A distributional code for value in dopamine-based reinforcement learning. Nature 577, 671–675"
    url: https://doi.org/10.1038/s41586-019-1924-6
---

# Dopamine neurons and the reward prediction error

Midbrain dopamine neurons in the macaque fire in a pattern that looks like the
error term of temporal-difference learning. The correspondence is close enough
that an algorithm written in 1988 predicted what an electrode would record in
1997. That is the reason this result matters, and also the reason it gets
overstated.

## What the paper claims

Schultz, Dayan and Montague report three response patterns in dopamine neurons
of monkeys learning a conditioned task:

- An unexpected reward produces a burst.
- Once a cue reliably predicts the reward, the burst moves to the cue, and
  delivery of the reward itself produces nothing.
- Expected reward withheld produces a dip below baseline, timed to the moment
  the reward should have arrived.

Those three are exactly the signs of the TD error δ = r + γV(s′) − V(s):
positive on surprise, zero once predicted, negative on omission. The paper's
claim is that dopamine broadcasts this error, and that it is the teaching signal
downstream structures learn from.

## What the evidence shows

The recordings support the shape of the correspondence: sign and timing move as
the theory says they should. That is a strong result and it has replicated
widely.

What the recordings do not establish is the equation. A signal that behaves like
an RPE under these conditions is consistent with dopamine carrying an RPE; it
does not rule out its carrying something correlated with one. The distinction
survives because the manipulations here are correlational — neurons are recorded
during learning, not silenced to see what learning does without them.

## What would change the reading

Two later results already have.

**Dopamine neurons are not one population.** Matsumoto and Hikosaka found
neurons excited by aversive as well as appetitive stimuli, sitting anatomically
apart from the value-coding ones. A single scalar teaching signal cannot account
for both groups; at least one of them is coding something closer to salience.

**The variability is not noise.** Dabney and colleagues showed that dopamine
neurons differ systematically in how optimistically or pessimistically they
respond, and that the spread across the population encodes a distribution over
future reward rather than its mean. Under that reading, the 1997 result recorded
the average of a population code and named it the code.

Neither overturns the original observation. Both change what it is evidence for:
the finding is that dopamine carries prediction-error-like information, not that
dopamine is the RPE.

## Why this sits in a machine learning repository

The traffic runs both ways, and it is easy to mistake which way it is running.
TD learning was not derived from neuroscience — it came out of Sutton's work on
prediction, and the biology arrived afterwards as confirmation. Distributional
RL then went the same direction: an algorithmic idea first, a neural signature
found second.

So the honest summary is narrower than the popular one. Reinforcement learning
did not copy the brain. It produced a theory precise enough to be checked
against one.

## Where it connects

Nothing yet. When there is a note on distributional RL as an algorithm rather
than a finding, it belongs here.
