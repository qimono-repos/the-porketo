# Deviations

## Purpose

Define the project's concept of **deviation** as a durable governance concept.

The concept is inspired by quality-management practice associated with **ISO 9001**, particularly the treatment of requirements, nonconformity, documented evidence, correction, corrective action, and continual improvement.

This is an inspiration and adaptation for the Trading project. The project is **not** claiming ISO 9001 certification or adopting ISO 9001 as a binding external standard.

## Definition

A **deviation** is a material difference between prescribed or planned behavior and the behavior actually observed or executed.

A deviation can occur in:

- quantity;
- percentage;
- timing;
- sequence;
- frequency;
- scope; or
- condition.

A deviation is not automatically an error.

The purpose of recording a deviation is to preserve what was expected, what actually happened, why the difference occurred, what action was taken, and what was learned from the case.

## Minimum Deviation Record

When a deviation is material enough to become project knowledge, the journal should record:

1. **Expected behavior** — the rule, plan, threshold, timing, sequence, or other condition that applied.
2. **Actual behavior** — what actually occurred or was executed.
3. **Deviation** — the concrete difference between expected and actual behavior.
4. **Rationale** — why the deviation occurred or why the operator intentionally departed from the expected behavior.
5. **Action Taken** — what was actually done.
6. **Outcome** — what happened afterward and what evidence became available.
7. **Disposition** — the status of the case, such as Accepted, Rejected, or Unresolved.
8. **Precedent, when applicable** — the single best prior case identified by the AI.

## Deviation Is Not Automatically an Error

The project distinguishes deviation from error.

A deviation may be:

- intentional and justified;
- intentional but later rejected;
- forced by an external circumstance;
- caused by an operational failure;
- discovered after execution; or
- simply a difference that requires evaluation.

The journal therefore records the case before assigning judgment to it.

## Root Cause Analysis

A material deviation may require a **Root Cause Analysis (RCA)** to determine why the deviation occurred and whether the system should change as a result.

The project's standard RCA technique for deviations is the **Fishbone / Ishikawa / Cause-and-Effect Diagram**.

The Fishbone organizes candidate causes into useful categories. It does not by itself establish a root cause. Candidate causes must be evaluated against evidence before being classified as confirmed, probable, possible, rejected, or unresolved.

The RCA should preserve the reasoning from:

**Deviation → Effect → Candidate Causes → Evidence → Root Cause(s) → Action → Verification → Learning**

The complete RCA method and reusable record template are defined in `SPECS/ROOT_CAUSE_ANALYSIS.md`.

Not every deviation requires a full RCA. The decision to perform or not perform RCA should be based on the materiality and circumstances of the deviation, with rationale recorded when the decision is material.

## Relationship to Exceptions

An **exception** is a case in which the standard rule is intentionally not followed because a specific circumstance justifies a departure.

An exception is therefore a type of deviation.

The journal records the exception using the same reasoning structure:

**Rule → Exception / Deviation → Rationale → Action Taken → Outcome → Disposition.**

## Relationship to Precedent

The first occurrence of a new deviation type should receive fuller reasoning.

Later analogous deviations may use the earlier case as precedent. The AI should identify the **single best precedent** and record the relevant reasoning.

A precedent does not expire merely because time passes. A later case may distinguish or explicitly overrule a precedent, but the historical case remains preserved.

## ISO 9001 Inspiration

The project's deviation concept draws inspiration from the discipline used in ISO 9001 quality-management systems.

ISO's terminology distinguishes **conformity** as fulfillment of a requirement and **nonconformity** as non-fulfillment of a requirement. ISO also defines corrective action as action intended to eliminate the cause of a nonconformity and prevent recurrence. citeturn0search3

For the Trading project, this suggests a useful reasoning pattern:

**Requirement / expected behavior → evidence of what happened → identify the difference → analyze the reason → act → verify the outcome → preserve the learning.**

The project deliberately extends this quality-management idea to include deviations from trading rules, planned actions, timing, quantities, and other operational parameters even when the deviation is not a formal nonconformity.

ISO/IAF auditing guidance also emphasizes documenting the requirement, evidence, and statement of nonconformity, and maintaining systematic records for traceability and review. That documentation discipline is directly relevant to the project's goal of preserving operational jurisprudence. citeturn0search16

## Current ISO Reference

As of September 30, 2026, **ISO 9001:2026** is the current published edition. ISO states that it replaces ISO 9001:2015 and provides a framework for establishing, implementing, maintaining, and continually improving a quality management system. citeturn0search1turn0search2

ISO 9001:2015 is therefore retained here as historical context only. It was withdrawn and replaced by ISO 9001:2026. citeturn0search0

Primary reference:

- ISO 9001:2026 — Quality management systems — Requirements: https://www.iso.org/standard/9001

Historical reference:

- ISO 9001:2015 — Quality management systems — Requirements: https://www.iso.org/standard/62085.html

## Project Principle

> A deviation is not merely something that went differently. It is a documented difference between expected and actual behavior from which the project can learn.

The objective is not to eliminate every deviation.

The objective is to make deviations **visible, explainable, traceable, and useful for continual improvement**.
