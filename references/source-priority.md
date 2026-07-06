# Source Priority

Use the highest-quality sources available. Treat AI answers as a starting index, not as evidence.

## Source Hierarchy

### Tier 1: Primary Evidence

- company annual reports, quarterly reports, prospectuses, investor presentations
- earnings-call transcripts and management Q&A
- exchange filings and regulatory announcements
- government statistics and customs data
- industry association data
- tender, bidding, procurement, export, and import records
- company capacity announcements with dates, locations, and numbers

### Tier 2: Specialist Evidence

- technical white papers
- conference presentations
- supply-chain expert interviews
- broker reports with disclosed assumptions
- specialized industry databases
- patent, certification, and customer qualification records

### Tier 3: Clues

- media reports
- social-media posts
- influencer commentary
- AI-generated summaries
- forum discussions
- chart screenshots without data source

Use Tier 3 only to discover questions or leads. Do not base a conclusion on it alone.

## Evidence Eligibility

The following are not evidence by themselves:

- search-result titles or snippets
- SearXNG or Exa result summaries without opening the source
- Jina output when the source identity or date cannot be verified
- social posts that merely repeat another report
- AI-generated summaries without an accessible original

Promote a clue to evidence only after opening the original or an authoritative reproduction and recording its publisher, publication date, period, geography, and definition. Social posts can serve as direct evidence only for the author's own statement or for capital-market narrative, not for an undisclosed industry fact.

## AI Usage

Use AI as an industry research assistant:

```text
Ask: who are the top wafer fabs in China?
Ask: what are their 2024-2026 expansion plans?
Ask: what monthly capacity is disclosed?
Ask: what equipment suppliers are involved?
Ask: what downstream customers are connected?
```

Do not ask:

```text
Recommend a stock.
Will this stock rise tomorrow?
Which ticker can 10x?
```

## Public Data Limitation

Assume free, accurate, monthly updated, complete capacity databases rarely exist.

Common problems:

- public data is stale
- public data is scattered
- broker/institutional reports may already reflect consensus
- sensitive yield and ramp-up data is usually non-public
- when a shortage is obvious in public data, market pricing may already be late

## Evidence Labeling

Label all key claims:

- Fact: directly sourced or quoted data.
- Inference: reasoned conclusion from multiple facts.
- Assumption: plausible but unverified condition that must be tracked.

If a number cannot be verified, write the uncertainty explicitly.

## Deep Research Evidence Rules

For a deep industry-cycle analysis, do not stop at one generic market report. Each major section needs a minimum evidence base:

- Industry chain: at least 2 reliable sources.
- Demand: at least 3 reliable sources.
- Supply and capacity: at least 3 reliable sources.
- Price/order/inventory/margin: at least 3 reliable sources or an explicit data-gap note.
- Capital-market expectation mapping: at least 2 sources, with a clear distinction between industrial reality and market narrative.

When the minimum cannot be reached within the search budget, write:

```text
Evidence gap: [what is missing]
Why unavailable: [not public / stale / proprietary / not found within budget]
How to track later: [source or indicator]
```

Do not continue searching indefinitely to hide an evidence gap.
