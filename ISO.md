# ISO

## Purpose

This document records the **rationale for project concepts that are inspired by ISO 9001 quality-management principles**.

The purpose is not to make ISO 9001 a binding rulebook for the Trading project.

Instead, ISO 9001 provides an external reference for a set of ideas that the project is adapting to its own governance model:

- define what is expected;
- preserve evidence of what actually happened;
- make differences between expected and actual behavior visible;
- understand risks before they become events;
- respond to problems and learn from them;
- preserve documented reasoning;
- evaluate outcomes; and
- continually improve the system.

The project therefore borrows the **discipline and reasoning pattern**, not a claim of compliance or certification.

## Scope of the Adaptation

ISO 9001 is a quality-management standard designed for organizations and their management systems. The Trading project is not a conventional quality-management system and does not claim to implement ISO 9001 in full.

The adaptation is intentionally selective.

Where an ISO 9001 concept is useful for making the project's operating rules, evidence, decisions, and learning more reliable, the project may adopt an analogous mechanism and give it a project-specific meaning.

The project should always distinguish:

**ISO concept -> project adaptation -> project-specific rule or mechanism.**

The project-specific mechanism is governed by the repository, not by ISO.

## Why ISO 9001 Is Useful as a Reference

ISO 9001 provides a structured way of thinking about how a system can consistently operate, evaluate its performance, address variation and risk, preserve relevant information, and improve over time.

ISO's current edition, ISO 9001:2026, continues to emphasize the process approach, risk-based thinking, documented information, performance evaluation, and continual improvement. It also places additional emphasis on leadership, quality culture, and the consideration of risks and opportunities. See the official ISO references at the end of this document.

Those ideas map naturally onto the governance problem this project is trying to solve: not merely executing trades, but being able to explain what the system expected, what actually happened, why it happened, and what should change afterward.

## Conceptual Mapping

### 1. Requirements -> Rules

**ISO-inspired idea:** A managed system needs defined requirements and controlled processes.

**Project adaptation:** The Trading project expresses important expectations as explicit rules, specifications, thresholds, and operating procedures.

The rationale is that an implicit rule is difficult to execute consistently and difficult to evaluate afterward.

A written rule creates a reference point against which actual behavior can be compared.

The project therefore treats rules as more than documentation. They are the reference state for execution, deviation analysis, and later jurisprudence.

### 2. Conformity / Nonconformity -> Expected vs. Actual Behavior

**ISO-inspired idea:** A system can evaluate whether requirements have been fulfilled.

**Project adaptation:** The project explicitly records the distinction between prescribed or planned behavior and observed or executed behavior.

This became the basis for the project's concept of **deviation**.

A deviation is not automatically an error or a nonconformity in the ISO sense. It is the project's broader concept for making a material difference between expected and actual behavior visible.

The rationale is:

> Before deciding whether something was wrong, the system should first preserve what was expected and what actually happened.

This allows intentional exceptions, forced departures, operational failures, and ordinary differences to be analyzed without collapsing them into one category.

See SPECS/DEVIATIONS.md.

### 3. Documented Information -> Journal and Evidence

**ISO-inspired idea:** A managed system depends on relevant documented information.

**Project adaptation:** The project separates source-of-truth records from the reasoning layer that explains decisions and evolution.

The journal is intended to preserve durable reasoning rather than become a full transcript of every conversation.

The rationale is that important decisions should remain understandable after the original conversation has disappeared from working memory.

The project should preserve enough information to answer questions such as:

- What was the rule?
- What evidence was available?
- What happened?
- Why was the decision made?
- What was the rationale?
- What was the outcome?
- What should a future case learn from it?

This supports traceability without turning the repository into a transcript archive.

### 4. Evidence -> Verifiable Operational Memory

**ISO-inspired idea:** Decisions and evaluations should be supported by appropriate information and evidence.

**Project adaptation:** The project distinguishes source records from derived views and from AI-generated reasoning.

The actual execution record remains the source of truth for executed events.

The journal does not replace that source truth. It explains what the project learned from it.

The rationale is to prevent the AI's interpretation from becoming confused with the underlying event itself.

In practical terms:

**Source event -> derived state -> interpretation / reasoning.**

Each layer has a different purpose.

### 5. Risk-Based Thinking -> RISK Architecture

**ISO-inspired idea:** Organizations should consider risks and opportunities when planning and operating their systems.

**Project adaptation:** Risk becomes an explicit governance object in the project's RISK/ architecture.

A risk describes a possibility and its potential effect.

A deviation describes an observed difference that has already occurred.

The distinction is:

**Risk -> may happen.**

**Deviation -> did happen differently.**

The rationale is to make uncertainty visible before it becomes an event, while preserving a separate record of what actually happened.

The project can therefore move through:

**Risk -> Trigger -> Event -> Deviation, when actual behavior differs -> Response -> Outcome -> Learning.**

See RISK/README.md.

### 6. Correction and Corrective Action -> Response and Learning

**ISO-inspired idea:** When a problem or nonconformity occurs, the system should respond and, where appropriate, address causes so that recurrence can be prevented.

**Project adaptation:** A deviation record includes the action taken, outcome, disposition, and, where relevant, the rationale for changing a rule or control.

The project deliberately avoids assuming that every deviation requires a correction.

Some deviations are intentional and justified. Others reveal an operational failure. Others reveal that the original rule was incomplete.

The rationale is therefore:

**Record first -> understand the cause -> decide the response -> observe the outcome -> determine whether the system should change.**

This is more useful for the project than treating every difference as an error.

### 7. Continual Improvement -> Rule Evolution

**ISO-inspired idea:** A quality-management system should continually improve its effectiveness.

**Project adaptation:** The Trading project's rules are allowed to evolve, but their evolution should remain visible.

When a risk, deviation, exception, or observed outcome reveals that a rule is incomplete or unsuitable, the project should preserve:

1. the original rule;
2. the case or evidence that exposed the limitation;
3. the rationale for the change; and
4. the resulting rule or control.

The rule should not simply be rewritten as though the previous version had never existed.

The rationale is that **historical reasoning is part of the system's knowledge**.

This is the foundation for the project's precedent and jurisprudence concepts.

### 8. Performance Evaluation -> Outcome and Review

**ISO-inspired idea:** A system should monitor, measure, analyze, and evaluate its performance.

**Project adaptation:** Project records should distinguish the intended result from the observed result and preserve the outcome when a decision, rule, exception, risk, or deviation has material consequences.

The rationale is that a decision cannot be properly evaluated from its intention alone.

The project needs to know:

**What did we intend? -> What did we do? -> What happened? -> What did we learn?**

### 9. Process Approach -> Explicit Operating Paths

**ISO-inspired idea:** A management system can be understood as interconnected processes rather than isolated actions.

**Project adaptation:** The project documents operating paths and relationships between source events, derived state, strategies, rules, decisions, execution, and learning.

The rationale is that failures and unexpected behavior often occur at the boundaries between processes.

Understanding the path makes it easier to identify where a risk arose, where a deviation occurred, and which layer should be changed.

### 10. Accountability and Leadership -> Operator + AI Governance

**ISO-inspired idea:** Effective management systems require clear responsibility and leadership involvement.

**Project adaptation:** The project distinguishes the human operator's authority from the AI's role as a reasoning, memory, and knowledge layer.

The AI can identify relevant rules, risks, deviations, precedents, and historical reasoning.

The operator remains able to make decisions, distinguish a precedent, or explicitly overrule prior reasoning.

The rationale is that durable governance should improve human decision-making without silently transferring authority to the memory system.

## The Resulting Governance Pattern

Taken together, these adaptations produce a recurring pattern:

**Rule / Requirement
-> Planned Behavior
-> Execution
-> Evidence
-> Observed Behavior
-> Deviation or Conformity Assessment
-> Risk / Cause Analysis
-> Response
-> Outcome
-> Learning
-> Precedent or Rule Evolution**

Not every case travels through every step.

The value is that the project has a common language for moving from execution to learning.

## Why Deviations Are a First-Class Concept

The deviation concept is one of the clearest examples of the ISO-inspired reasoning.

The project does not merely want to know that an action occurred.

It wants to know whether the action occurred as expected, and if not:

- how it differed;
- why it differed;
- whether the difference was intentional;
- what was done about it;
- what happened afterward; and
- whether the case should influence future rules.

That is why SPECS/DEVIATIONS.md exists as a project-specific specification.

The project is adapting a quality-management discipline to operational and trading behavior, rather than claiming that trading deviations are formally equivalent to ISO nonconformities.

## Why Risks Are a Separate Concept

Risk and deviation are deliberately separated because they occur at different points in time.

A risk is prospective:

> Something may happen and could affect an objective.

A deviation is retrospective or contemporaneous:

> Something happened differently from what was expected.

The distinction allows preventive thinking and historical learning to coexist.

The RISK/ architecture therefore handles the risk domain, while deviation governance remains in SPECS/DEVIATIONS.md.

## Why the Journal Matters

The journal is the project's memory of reasoning.

This is consistent with the broader ISO-inspired idea that a managed system should preserve relevant information, evaluate evidence, and improve based on what it learns.

The project's adaptation goes further by treating historical reasoning as a form of operational jurisprudence:

- the first occurrence receives fuller reasoning;
- later analogous cases may rely on precedent;
- the AI identifies the single best precedent;
- the operator may distinguish or overrule it;
- the original case remains preserved.

The rationale is simple:

> A system that forgets why its rules changed will eventually repeat the same reasoning work.

## What This Document Does Not Mean

This document does **not** mean:

- the Trading project is ISO 9001 certified;
- the project claims conformity with ISO 9001;
- every project rule is an ISO requirement;
- every project concept has an exact ISO equivalent;
- ISO governs the project's decisions; or
- the project should reproduce the ISO standard inside the repository.

ISO 9001 is being used as a **reference architecture for disciplined management, evidence, risk awareness, controlled variation, and continual improvement**.

The project's own rules remain the project's rules.

## Current Reference

The current published edition is **ISO 9001:2026 - Quality management systems - Requirements**, published in September 2026. ISO identifies it as the current edition and states that it replaces ISO 9001:2015.

Primary reference:

https://www.iso.org/standard/9001

Additional official explanatory reference:

https://www.iso.org/quality-management/iso-9001-2026

## Project Principle

> ISO 9001 is not the project's rulebook. It is one of the external bodies of knowledge from which the project deliberately borrows useful governance patterns.

The adaptation should remain explicit, selective, and explainable.

When a project concept is inspired by ISO, its **rationale should be documented here**, while the actual project rule or mechanism should live in the appropriate part of the repository.
