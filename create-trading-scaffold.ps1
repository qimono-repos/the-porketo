# ============================================================
# TRADING PROJECT - INITIAL SCAFFOLD
# ============================================================
#
# Creates the initial Trading knowledge/research repository
# inspired by the Qimono Migration Protocol.
#
# Philosophy:
#   Knowledge belongs to the project, not to the AI model.
#   Markdown = source
#   Obsidian = knowledge interface
#   Git = history
#   AI = interchangeable collaborators
#
# Safe to re-run:
#   Existing files are NOT overwritten.
#
# ============================================================

$ErrorActionPreference = "Stop"

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

$ProjectName = "trading"

# The project will be created in the current directory.
$Root = Join-Path (Get-Location) $ProjectName


# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

function New-Directory {
    param (
        [string]$Path
    )

    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "  [DIR]  $Path"
    }
}

function New-FileIfMissing {
    param (
        [string]$Path,
        [string]$Content = ""
    )

    if (-not (Test-Path $Path)) {
        Set-Content -Path $Path -Value $Content -Encoding UTF8
        Write-Host "  [FILE] $Path"
    }
}


# ------------------------------------------------------------
# CREATE ROOT
# ------------------------------------------------------------

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   TRADING PROJECT SCAFFOLD" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

New-Directory $Root


# ------------------------------------------------------------
# DIRECTORY STRUCTURE
# ------------------------------------------------------------

$Directories = @(

    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------
    "AI",
    "AI\prompts",
    "AI\handoffs",
    "AI\reviews",

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------
    "MARKET",
    "MARKET\macro",
    "MARKET\equities",
    "MARKET\fixed-income",
    "MARKET\commodities",
    "MARKET\crypto",
    "MARKET\fx",
    "MARKET\sectors",
    "MARKET\indices",

    # --------------------------------------------------------
    # RESEARCH
    # --------------------------------------------------------
    "RESEARCH",
    "RESEARCH\macro",
    "RESEARCH\fundamental",
    "RESEARCH\technical",
    "RESEARCH\quantitative",
    "RESEARCH\market-structure",
    "RESEARCH\sentiment",
    "RESEARCH\geopolitics",

    # --------------------------------------------------------
    # STRATEGIES
    # --------------------------------------------------------
    "STRATEGIES",
    "STRATEGIES\discretionary",
    "STRATEGIES\systematic",
    "STRATEGIES\momentum",
    "STRATEGIES\mean-reversion",
    "STRATEGIES\trend-following",
    "STRATEGIES\event-driven",
    "STRATEGIES\options",

    # --------------------------------------------------------
    # WATCHLISTS
    # --------------------------------------------------------
    "WATCHLISTS",
    "WATCHLISTS\equities",
    "WATCHLISTS\crypto",
    "WATCHLISTS\macro",
    "WATCHLISTS\special-situations",

    # --------------------------------------------------------
    # THESIS
    # --------------------------------------------------------
    "THESIS",
    "THESIS\active",
    "THESIS\archived",
    "THESIS\sector",
    "THESIS\macro",

    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------
    "RISK",
    "RISK\frameworks",
    "RISK\position-sizing",
    "RISK\drawdowns",
    "RISK\correlations",
    "RISK\stress-tests",

    # --------------------------------------------------------
    # PORTFOLIO
    # --------------------------------------------------------
    "PORTFOLIO",
    "PORTFOLIO\positions",
    "PORTFOLIO\allocation",
    "PORTFOLIO\performance",
    "PORTFOLIO\reviews",

    # --------------------------------------------------------
    # TRADING
    # --------------------------------------------------------
    "TRADING",
    "TRADING\setups",
    "TRADING\entries",
    "TRADING\exits",
    "TRADING\execution",
    "TRADING\trade-plans",

    # --------------------------------------------------------
    # JOURNAL
    # --------------------------------------------------------
    "JOURNAL",
    "JOURNAL\daily",
    "JOURNAL\weekly",
    "JOURNAL\monthly",
    "JOURNAL\post-trade",

    # --------------------------------------------------------
    # BACKTESTS
    # --------------------------------------------------------
    "BACKTESTS",
    "BACKTESTS\strategies",
    "BACKTESTS\experiments",
    "BACKTESTS\results",
    "BACKTESTS\datasets",

    # --------------------------------------------------------
    # EXPERIMENTS
    # --------------------------------------------------------
    "EXPERIMENTS",
    "EXPERIMENTS\hypotheses",
    "EXPERIMENTS\results",
    "EXPERIMENTS\failed",

    # --------------------------------------------------------
    # DATA
    # --------------------------------------------------------
    "DATA",
    "DATA\raw",
    "DATA\processed",
    "DATA\external",
    "DATA\schemas",

    # --------------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------------
    "EVIDENCE",
    "EVIDENCE\research",
    "EVIDENCE\backtests",
    "EVIDENCE\trades",
    "EVIDENCE\experiments",

    # --------------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------------
    "INSIGHTS",
    "INSIGHTS\breakthroughs",
    "INSIGHTS\patterns",
    "INSIGHTS\mistakes",
    "INSIGHTS\misconceptions",

    # --------------------------------------------------------
    # DECISIONS
    # --------------------------------------------------------
    "DECISIONS",
    "DECISIONS\investment",
    "DECISIONS\strategy",
    "DECISIONS\risk",
    "DECISIONS\architecture",

    # --------------------------------------------------------
    # SPECS
    # --------------------------------------------------------
    "SPECS",
    "SPECS\strategies",
    "SPECS\systems",
    "SPECS\risk",
    "SPECS\data",

    # --------------------------------------------------------
    # REFERENCES
    # --------------------------------------------------------
    "REFERENCES",
    "REFERENCES\books",
    "REFERENCES\papers",
    "REFERENCES\web",
    "REFERENCES\documentation",
    "REFERENCES\tools",

    # --------------------------------------------------------
    # CONVERSATIONS
    # --------------------------------------------------------
    "CONVERSATIONS",
    "CONVERSATIONS\chatgpt",
    "CONVERSATIONS\grok",
    "CONVERSATIONS\claude",
    "CONVERSATIONS\other",
    "CONVERSATIONS\archive",

    # --------------------------------------------------------
    # REPORTS
    # --------------------------------------------------------
    "REPORTS",
    "REPORTS\daily",
    "REPORTS\weekly",
    "REPORTS\monthly",
    "REPORTS\quarterly",

    # --------------------------------------------------------
    # OPERATIONS
    # --------------------------------------------------------
    "OPS",
    "OPS\automation",
    "OPS\scripts",
    "OPS\configuration",

    # --------------------------------------------------------
    # ARCHIVE
    # --------------------------------------------------------
    "ARCHIVE",
    "ARCHIVE\research",
    "ARCHIVE\strategies",
    "ARCHIVE\thesis",
    "ARCHIVE\reports"
)


# ------------------------------------------------------------
# CREATE DIRECTORIES
# ------------------------------------------------------------

Write-Host ""
Write-Host "Creating directory structure..." -ForegroundColor Yellow
Write-Host ""

foreach ($Directory in $Directories) {
    New-Directory (Join-Path $Root $Directory)
}


# ------------------------------------------------------------
# CREATE README IN EVERY DIRECTORY
# ------------------------------------------------------------

Write-Host ""
Write-Host "Creating README.md files..." -ForegroundColor Yellow
Write-Host ""

# Root README
New-FileIfMissing (Join-Path $Root "README.md") @"
# Trading

A model-independent trading research, knowledge, experimentation, and decision system.

## Core Principle

> The knowledge belongs to the project, not to the model.

Markdown is the durable knowledge layer.

Obsidian is the human-facing knowledge interface.

Git provides history and reversibility.

AI systems are interchangeable collaborators.

## Repository Structure

- `AI/` - AI collaboration and handoff material
- `MARKET/` - Market knowledge and observations
- `RESEARCH/` - Research
- `STRATEGIES/` - Trading and investment strategies
- `WATCHLISTS/` - Active areas of interest
- `THESIS/` - Investment and market theses
- `RISK/` - Risk management
- `PORTFOLIO/` - Portfolio structure and reviews
- `TRADING/` - Trade planning and execution
- `JOURNAL/` - Trading journal
- `BACKTESTS/` - Backtesting
- `EXPERIMENTS/` - Hypothesis-driven experiments
- `DATA/` - Data
- `EVIDENCE/` - Evidence supporting conclusions
- `INSIGHTS/` - Durable insights and lessons
- `DECISIONS/` - Important decisions and their reasoning
- `SPECS/` - Specifications
- `REFERENCES/` - External references
- `CONVERSATIONS/` - AI conversation archive
- `REPORTS/` - Periodic reports
- `OPS/` - Operational tooling
- `ARCHIVE/` - Historical material

## Important Rule

Conversations are source material.

Extract durable knowledge from conversations rather than automatically treating conversations as the knowledge base.
"@


# Project State
New-FileIfMissing (Join-Path $Root "PROJECT_STATE.md") @"
# Project State

## Project

Trading research and knowledge system.

## Current Phase

Initial repository scaffold.

## Current Focus

Define the knowledge architecture and establish the initial research workflow.

## Active Theses

None documented yet.

## Active Research

None documented yet.

## Open Questions

- What should the canonical trading workflow look like?
- Which information belongs in permanent knowledge?
- Which information should remain transient research?
- Which strategies require formal specifications?
- What evidence is required before accepting a trading hypothesis?

## Recent Decisions

Initial repository architecture created.

## Next Actions

1. Review the repository structure.
2. Open the repository as an Obsidian vault.
3. Review and refine the folder architecture.
4. Create the first meaningful knowledge documents.
5. Initialize the first Git checkpoint.

## Last Updated

$(Get-Date -Format "yyyy-MM-dd")
"@


# AI files
New-FileIfMissing (Join-Path $Root "AI\SYSTEM.md") @"
# AI System

## Purpose

Define how AI systems collaborate with the Trading project.

## Principle

The repository is the source of truth.

AI systems are workers operating on the repository.

They do not own the project's memory.

## Possible Roles

- Research
- Analysis
- Critique
- Alternative perspectives
- Summarization
- Data analysis
- Strategy review
- Documentation
- Automation

## Model Independence

The workflow should remain useful if any individual AI model is replaced.
"@

New-FileIfMissing (Join-Path $Root "AI\ROLES.md") @"
# AI Roles

Document the roles assigned to different AI systems.

| System | Role | Notes |
|---|---|---|
| ChatGPT | | |
| Grok | | |
| Claude | | |
| Other | | |

Assignments are operational conventions, not permanent dependencies.
"@


# Strategy specification
New-FileIfMissing (Join-Path $Root "SPECS\strategy-template.md") @"
# Strategy Specification

## Name

## Status

Draft / Testing / Active / Archived

## Hypothesis

## Market

## Time Horizon

## Entry Conditions

## Exit Conditions

## Position Sizing

## Risk Limits

## Expected Behaviour

## Failure Conditions

## Evidence Required

## Backtests

## Live Evidence

## Definition of Done

- [ ] Hypothesis clearly stated
- [ ] Entry conditions defined
- [ ] Exit conditions defined
- [ ] Risk defined
- [ ] Position sizing defined
- [ ] Backtest completed where appropriate
- [ ] Failure conditions documented
- [ ] Evidence recorded
- [ ] Review completed
"@


# Thesis template
New-FileIfMissing (Join-Path $Root "THESIS\thesis-template.md") @"
# Investment / Market Thesis

## Thesis

## Date

## Horizon

## Instrument / Market

## Core Argument

## Supporting Evidence

## Contradicting Evidence

## Key Assumptions

## Catalysts

## Risks

## Invalidating Conditions

## What Would Change My Mind?

## Current Status

Active / Under Review / Invalidated / Archived

## References
"@


# Experiment template
New-FileIfMissing (Join-Path $Root "EXPERIMENTS\experiment-template.md") @"
# Experiment

## Hypothesis

## Question

## Prediction

## Method

## Data

## Experiment

## Result

## Interpretation

## What Was Learned?

## Does the Evidence Support the Hypothesis?

## Follow-up

## References
"@


# Decision template
New-FileIfMissing (Join-Path $Root "DECISIONS\decision-template.md") @"
# Decision

## Decision

## Date

## Context

## Alternatives Considered

## Reasoning

## Evidence

## Risks

## Expected Consequences

## Reversal Conditions

## Outcome

## Review Date
"@


# Trade plan template
New-FileIfMissing (Join-Path $Root "TRADING\trade-plan-template.md") @"
# Trade Plan

## Instrument

## Direction

## Thesis

## Setup

## Entry

## Stop

## Target

## Position Size

## Risk

## Time Horizon

## Invalidation

## Execution Notes

## Post-Trade Review
"@


# ------------------------------------------------------------
# README FOR EVERY DIRECTORY
# ------------------------------------------------------------

foreach ($Directory in $Directories) {

    $FullPath = Join-Path $Root $Directory
    $ReadmePath = Join-Path $FullPath "README.md"

    if (-not (Test-Path $ReadmePath)) {

        $FolderName = Split-Path $Directory -Leaf

        $Content = @"
# $FolderName

This directory is part of the Trading project knowledge system.

## Purpose

Document the purpose and scope of this area.

## What Belongs Here

Add durable project material relevant to this directory.

## What Does Not Belong Here

Do not use this directory as a general dumping ground.

Prefer small, meaningful Markdown documents.

## Relationships

Link relevant concepts, evidence, decisions, theses, strategies, and references using Obsidian links.

## Notes

This README can evolve as the project architecture becomes clearer.
"@

        New-FileIfMissing $ReadmePath $Content
    }
}


# ------------------------------------------------------------
# GITIGNORE
# ------------------------------------------------------------

New-FileIfMissing (Join-Path $Root ".gitignore") @"
# OS
.DS_Store
Thumbs.db
desktop.ini

# Temporary files
*.tmp
*.temp
*.bak
*.swp
*.swo

# Logs
*.log

# Python
__pycache__/
*.py[cod]
.venv/
venv/
.env

# Node
node_modules/
npm-debug.log*
yarn-debug.log*

# Data artifacts
*.parquet
*.feather

# Local secrets
secrets/
credentials/
*.secret

# Obsidian
# Keep the vault configuration under version control,
# but ignore volatile workspace state.

.obsidian/workspace.json
.obsidian/workspace-mobile.json
"@


# ------------------------------------------------------------
# OPTIONAL GIT INITIALIZATION
# ------------------------------------------------------------

Write-Host ""
Write-Host "Initializing Git repository..." -ForegroundColor Yellow
Write-Host ""

Push-Location $Root

if (-not (Test-Path ".git")) {
    git init
    Write-Host "  [GIT] Repository initialized." -ForegroundColor Green
}
else {
    Write-Host "  [GIT] Repository already exists. Skipping." -ForegroundColor DarkYellow
}

Pop-Location


# ------------------------------------------------------------
# FINISHED
# ------------------------------------------------------------

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "   TRADING SCAFFOLD COMPLETE" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""

Write-Host "Project created at:"
Write-Host "  $Root" -ForegroundColor Cyan
Write-Host ""

Write-Host "Next steps:"
Write-Host "  1. Open the folder in Obsidian."
Write-Host "  2. Review the structure."
Write-Host "  3. Edit PROJECT_STATE.md."
Write-Host "  4. Review the README files."
Write-Host "  5. Make the first Git commit."
Write-Host ""

Write-Host "The landing zone is ready. No historical conversations were imported."
Write-Host ""
