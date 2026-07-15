# Source Priority and Evidence Gates

Use the highest-quality source available. Treat AI answers and search results as an index, not evidence.

## Source hierarchy

### Tier 1: primary evidence

- company filings, annual/quarterly reports, investor presentations, earnings calls and management Q&A
- exchange/regulatory announcements, government statistics, customs data and industry-association data
- tenders, procurement records, certification records and dated company capacity/project disclosures

### Tier 2: specialist evidence

- technical white papers, conference presentations, expert interviews and disclosed-assumption broker research
- specialist databases, patents, qualification records and credible supply-chain surveys

### Tier 3: discovery or narrative clues

- media, social posts, influencer commentary, AI summaries, forums and unsourced chart screenshots

Use Tier 3 only for discovery, direct first-party statements, or market-narrative evidence. Do not use it alone for an undisclosed industry fact.

## Evidence eligibility

A result is not evidence by itself when it is only:

- a search title or snippet;
- an SearXNG/Exa summary without an opened original;
- a Jina rendering whose source identity or date is unverified;
- a repost or social summary;
- an AI-generated statement.

Promote a claim only after opening an original or authoritative reproduction and recording publisher, publication date, access date, period, geography, unit/definition, locator, actual/forecast status, and limitations.

## Freshness rules

- Determine freshness per metric, not per document. A full-year figure may remain the latest annual actual while the same company has a newer quarterly release.
- Check the source’s actual release calendar. Do not assume Q2, Q3, or Q4 results exist from the current month alone.
- Label monthly/weekly data inside an unfinished quarter as `partial actual`.
- Label guidance, announced capacity, qualification targets and production plans separately from actual output.
- Mark an older source `superseded` when a newer release uses the same definition.

## Full-research minimums

- Industry chain and relationships: at least 2 opened reliable sources.
- Demand: at least 3 opened reliable sources.
- Supply and effective capacity: at least 3 opened reliable sources.
- Price/order/inventory/margin: at least 3 opened sources or a precise evidence-gap note.
- Capital-market expectation mapping: at least 2 market-pricing or narrative sources, or a precise evidence-gap note.

An explicit gap finishes the search subtask but does not raise conclusion confidence. If a core lane is missing, keep the stage provisional.

Use this format:

```text
Evidence gap: [missing metric or definition]
Why unavailable: [not public / stale / proprietary / not found within budget]
How to track later: [specific source, page or release]
Effect on conclusion: [what must remain provisional]
```

## Claim labels

- **Fact:** directly supported by an opened source.
- **Guidance/Plan:** management or policy target that has not yet occurred.
- **Forecast:** model-based future estimate.
- **Inference:** reasoning from named evidence IDs.
- **Assumption:** unverified condition with a falsifier.

Never average unresolved definitions or hide a missing metric behind precise-looking prose.
