# Root Cause Analysis

## Purpose

Define the project's standard method for performing **Root Cause Analysis (RCA)** when a deviation requires investigation of why the deviation occurred.

The project's standard RCA technique is the **Fishbone Diagram**, also known as the **Ishikawa Diagram** or **Cause-and-Effect Diagram**.

RCA is an investigation artifact. It should preserve the reasoning from an observed deviation to the causes supported by evidence and, where appropriate, to corrective or preventive action.

## Relationship to Deviations

A deviation records a difference between expected and actual behavior.

RCA asks a different question:

> **Why did the deviation happen?**

The relationship is:

**Expected behavior → Actual behavior → Deviation → Root Cause Analysis → Causes → Evidence → Action → Verification → Learning**

Not every deviation requires a full RCA.

RCA should be considered when a deviation is material, consequential, recurring, unexplained, caused by a control failure, or likely to reveal a systemic weakness.

The decision not to perform RCA on a deviation may itself be recorded when the reason is material.

## Fishbone as the Standard Technique

The Fishbone technique is a cause-and-effect method used to identify and organize possible causes of a problem into categories.

The project uses the Fishbone as the **default structure for RCA of deviations**.

The Fishbone is not itself proof of a root cause.

It is a structured way to generate and organize candidate causes. Candidate causes must be examined against evidence before being accepted as root causes or contributing causes.

This distinction is important:

**Fishbone → generates hypotheses.**

**Evidence → tests hypotheses.**

**RCA conclusion → identifies supported causes.**

The technique is commonly known as the Fishbone, Ishikawa, or Cause-and-Effect Diagram and is used to organize possible causes into categories and progressively investigate deeper causes. citeturn1view0turn1view1

## Standard Cause Categories

The original Ishikawa approach uses the 6M categories:

- Materials
- Machinery
- Methods
- Measurement
- Manpower
- Mother Nature / Environment

The project adapts those categories to its trading and governance context.

The recommended categories are:

### People

Human action, omission, interpretation, training, availability, communication, or responsibility.

### Method / Rule

Rules, procedures, thresholds, timing logic, specifications, assumptions, or process design.

### Technology / System

Software, automation, exchange or broker interfaces, connectivity, infrastructure, tooling, or system behavior.

### Data / Measurement

Prices, balances, quantities, timestamps, calculations, stale data, missing data, incorrect data, measurement methods, or derived values.

### Inputs / Material

Assets, positions, strategy lots, capital, liquidity, external inputs, or other material resources required for execution.

### Environment / Market

Market conditions, volatility, liquidity conditions, external events, timing constraints, or other circumstances outside the immediate process.

### Governance / Management

Authority, controls, oversight, decision structure, documentation, incentives, ownership, or gaps in the governance system.

The categories are prompts, not rigid boundaries.

A cause may belong to more than one category when appropriate.

## RCA Procedure

### 1. Define the Deviation

Start with the deviation, not with a presumed cause.

Record:

- what was expected;
- what actually happened;
- the concrete difference;
- when and where it occurred;
- the affected strategy, process, or rule; and
- the evidence establishing the deviation.

The problem statement should describe the effect without embedding an unverified explanation.

Good:

> Crisis harvest executed 24 hours later than the prescribed timing.

Avoid:

> Crisis harvest was late because the notification system failed.

The second statement already assumes a cause.

### 2. Define the Effect

Write the effect at the head of the Fishbone.

The effect should be observable and specific enough to investigate.

Examples:

- Harvest occurred after the prescribed deadline.
- The executed quantity differed from the planned quantity.
- A strategy lot was not preserved as required.
- A required notification was not produced.
- A position derived from source events did not reconcile.

### 3. Build the Fishbone

Create the major cause branches using the recommended categories.

For each category, ask:

> **What could have caused this deviation?**

Record candidate causes without prematurely deciding which one is correct.

Then ask:

> **Why could this cause produce the observed deviation?**

Continue into deeper branches where useful.

The objective is to expose the causal chain rather than stop at the first plausible explanation.

### 4. Separate Causes by Status

Each candidate cause should eventually be classified as one of:

- **Confirmed** — supported by sufficient evidence.
- **Probable** — supported by meaningful evidence but not fully verified.
- **Possible** — plausible but currently unverified.
- **Rejected** — investigated and not supported.
- **Unknown** — insufficient evidence to determine.

Do not promote a plausible explanation to confirmed root cause merely because it appears on the Fishbone.

### 5. Identify Root and Contributing Causes

The analysis should distinguish, where useful:

**Immediate cause** — the direct condition or action associated with the deviation.

**Contributing cause** — a factor that increased the likelihood or severity of the deviation.

**Root cause** — a deeper cause whose removal or control would address the underlying mechanism that allowed the deviation to occur.

There may be more than one root cause.

The project should not force a single root cause when the evidence supports multiple causal paths.

### 6. Validate Against Evidence

For each proposed root or contributing cause, record the evidence supporting it.

Useful evidence may include:

- source event logs;
- exchange or broker records;
- timestamps;
- notification records;
- system logs;
- configuration;
- calculations;
- strategy-lot records;
- market data;
- journal history;
- previous deviations; or
- controlled reproduction or testing.

The RCA conclusion should be traceable to evidence rather than to intuition alone.

### 7. Determine the Response

For confirmed causes, determine what response is appropriate.

Possible responses include:

- correction of the immediate condition;
- corrective action addressing the cause;
- preventive control;
- rule clarification;
- specification change;
- monitoring;
- additional evidence collection;
- acceptance of the residual risk; or
- no action, with rationale.

The response should address the cause rather than merely the visible symptom when the cause is controllable and material.

### 8. Verify the Result

After action is taken, record whether the action achieved its intended result.

Where practical, verify that:

- the original deviation no longer occurs;
- the relevant control now behaves as intended;
- the underlying cause has been reduced or removed; and
- no new unacceptable behavior was introduced.

If the action does not resolve the issue, the RCA may need to be reopened or extended.

### 9. Capture the Learning

The RCA should conclude with the project's learning.

The outcome may lead to:

- a new precedent;
- an update to an existing precedent;
- a rule change;
- a new risk;
- a new control;
- a new monitoring requirement;
- an insight or mistake record; or
- no change, when the existing system is judged adequate.

The rationale for any rule change should be preserved.

## Minimum RCA Record

A completed RCA should contain, as applicable:

1. **Deviation** — reference to the deviation being analyzed.
2. **Problem / Effect** — precise description of what happened.
3. **Expected Behavior** — what should have happened.
4. **Actual Behavior** — what happened.
5. **Impact** — material consequence of the deviation.
6. **Fishbone Analysis** — categorized candidate causes.
7. **Evidence** — evidence examined for the candidate causes.
8. **Immediate Cause** — direct cause, when established.
9. **Contributing Causes** — additional supported factors.
10. **Root Cause(s)** — supported underlying cause or causes.
11. **Rejected / Unresolved Causes** — important hypotheses that remain unsupported or unresolved.
12. **Rationale** — reasoning for the RCA conclusion.
13. **Action** — correction, corrective action, preventive control, or other response.
14. **Verification** — evidence that the response worked, when available.
15. **Outcome** — what happened after the response.
16. **Precedent / Learning** — relevant precedent or new learning.
17. **Disposition** — final status of the RCA.

Not every case requires every field, but material RCA work should preserve enough information to reconstruct the reasoning.

## RCA Record Template

The following structure can be copied when creating a concrete RCA artifact:

```markdown
# Root Cause Analysis: <short title>

## Deviation
- Reference:
- Date:
- Rule / expected behavior:
- Actual behavior:
- Deviation:

## Problem / Effect

<Observable description of the effect. Do not embed an unverified cause.>

## Impact

<What was affected and how materially?>

## Fishbone Analysis

### People
- Candidate cause:
  - Evidence:
  - Status:

### Method / Rule
- Candidate cause:
  - Evidence:
  - Status:

### Technology / System
- Candidate cause:
  - Evidence:
  - Status:

### Data / Measurement
- Candidate cause:
  - Evidence:
  - Status:

### Inputs / Material
- Candidate cause:
  - Evidence:
  - Status:

### Environment / Market
- Candidate cause:
  - Evidence:
  - Status:

### Governance / Management
- Candidate cause:
  - Evidence:
  - Status:

## Cause Analysis

### Immediate Cause
-

### Contributing Causes
-

### Root Cause(s)
-

### Rejected / Unresolved Causes
-

## Rationale

<Why these causes are accepted, rejected, or left unresolved.>

## Action

- Correction:
- Corrective action:
- Preventive control:

## Verification

<How the result was or will be verified.>

## Outcome

<What happened after the action.>

## Learning / Precedent

<What future cases should remember.>

## Disposition

<Accepted / Resolved / Unresolved / Reopened / other project status>
```

## Relationship to Precedent

A completed RCA can become precedent when it contains durable reasoning that applies to later deviations.

The first occurrence of a new causal pattern should receive fuller documentation.

Later analogous cases may reference the **single best precedent** rather than repeating the entire analysis, unless new evidence or materially different circumstances require a fresh RCA.

A precedent does not expire merely because time passes.

A later case may distinguish or explicitly overrule a precedent, while preserving the historical RCA.

## Relationship to ISO-Inspired Governance

The RCA concept is consistent with the project's ISO-inspired emphasis on evidence, corrective action, documented reasoning, and continual improvement.

The project is not treating every deviation as an ISO nonconformity.

Instead, RCA is the project's mechanism for answering the deeper question that follows a material deviation:

> **What in the system allowed this to happen, and what should we learn or change as a result?**

## Project Principle

> A Fishbone analysis organizes possible causes; Root Cause Analysis determines which causes are supported by evidence and what the project should do about them.

The objective is not to produce a convincing story.

The objective is to produce a **traceable, evidence-based explanation that can improve the system**.

## Reference

American Society for Quality (ASQ), *Fishbone Diagram / Cause-and-Effect Diagram*:

https://asq.org/quality-resources/fishbone

American Society for Quality (ASQ), *Root Cause Analysis (RCA)*:

https://asq.org/quality-resources/root-cause-analysis
