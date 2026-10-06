# Fatal Error Report 004 — Repository Identification & Continuity Failure

**Failure class:** Internal-context / repository retrieval / continuity
**Affected workflow:** Trading project repository identification
**Repository:** the-porketo
**Workaround:** `project-links.md` canonical project reference file
**Corrective principle:** Search project context and canonical reference files before asking the user to restate established information.

## Incident Summary

This report supersedes Fatal Error Report 003 and records a continued
repository-identification failure in the trading project. The project had
already been established for more than two days and had a single known
repository. Nevertheless, the assistant was unable to reliably resolve that
repository from the project context and required the user to identify it.

The established repository was ultimately resolved as **the-porketo**. Within
the project, the user then established a simpler convention: this repository is
to be referred to simply as **the repository**.

## Fatal Error #1 — Failure to Use Established Project Context

The assistant treated an established project resource as if it were an unknown
external resource. Instead of using the project's existing conversation context,
prior work, and connected repository information to resolve the name, it asked
the user for the repository identity.

This is the same class of failure identified in Fatal Error Report 002:
retrieval failure was incorrectly allowed to become an assumption that the
information was unavailable. The corrective doctrine requires searching the
project surface before asking the user to restate established information.

## Fatal Error #2 — Failure to Recognise the Single-Repository Convention

The user explicitly pointed out that there is only one repository being used for
this project. Once that project-level fact is established, an ambiguous spoken
reference to "the repository" should be treated as a retrieval problem, not as a
request for the user to supply a new identifier.

The assistant should have resolved the phonetic/spoken reference against the
known project repository and continued the task without introducing unnecessary
friction.

## Workaround / Corrective Measure

A practical workaround was added to the project: create and maintain a small
project reference file that explicitly identifies the canonical repository and
the canonical trading book. This file provides a durable, machine-readable
anchor for future AI teammates and reduces the chance of another
repository-identification failure.

The reference file is `project-links.md`. It explicitly states that, in the
context of this project, the listed GitHub repository is the canonical
repository and the listed October workbook is the canonical book. It also
establishes the project terminology that "the repository" and "the book" refer
to those resources.

This workaround does not replace project-context retrieval. It adds an explicit
reference point so the canonical resources can be recovered quickly and
consistently.

## Corrective Rule

Before asking the user to identify an established project resource, search the
project context and its canonical reference files. Treat approximate spoken
names, phonetic spellings, and shorthand as retrieval clues. If a project
reference file exists, use it as the explicit canonical mapping.

## Primary Lesson

Project continuity is part of the task. Established infrastructure should remain
established across turns and across AI teammates. When retrieval is uncertain,
the correct response is archaeology and verification, not delegation of the
retrieval burden back to the user.
