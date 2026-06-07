# Changelog

All notable changes to the industry-cycle-analysis skill will be documented in this file.

## [1.1.0] - 2025-06-05

### Added

#### SKILL.md
- **Step 9: Profit/Order Transmission Chain** - Map how demand signals propagate upstream through the industry chain
  - Track end demand → orders → revenue → margin → capex → upstream orders
  - Identify profit pool shifts during cycle turns
  - Distinguish order signals from revenue realization timing
- **Step 11: Observation Posts (Watchpoints)** - Define 3-5 specific, measurable indicators to track monthly
  - Each watchpoint includes: indicator name, data source, frequency, trigger threshold, signal meaning
  - Examples: utilization rate, order-to-revenue ratio, inventory days, margin trend, capex timing
- **Step 12: Cycle Timeline** - Construct historical cycle timeline with current position estimate
  - Map past 2-3 cycles if data allows
  - Estimate current position with date anchors
  - Identify expected transition to next phase
- **Updated Output Requirements** - Added 4 new mandatory deliverables:
  - Profit/order transmission chain
  - Observation posts (3-5 specific monthly watchpoints with thresholds)
  - Cycle timeline (historical turns + current position estimate)
  - Database-style tracking section (structured fields for ongoing updates)

#### report-template.md
- **Section 5.5: Profit/Order Transmission Chain**
  - Visual flow diagram of demand signal propagation
  - Profit pool redistribution table by chain stage
  - Key transmission lag quantification
- **Section 5.6: Transmission Mechanism**
  - Price pass-through analysis
  - Order book transmission
  - Inventory adjustment patterns
  - Capex cycle dynamics
  - Pricing power distribution
- **Section 7.5: Cycle Timeline**
  - Historical cycle turns table (start, peak, trough, duration, key driver)
  - Current position estimate with confidence level
  - Visual timeline showing current phase
- **Section 10.5: Observation Posts (Watchpoints)**
  - Structured table for 3-5 specific indicators
  - Current value, source, threshold, signal meaning, action
  - Update cadence definition
- **Section 11: Database-Style Tracking**
  - Latest Update section with structured fields (cycle stage, utilization, price, orders, inventory, margin, capex, policy)
  - History Log for tracking events and cycle stage transitions

#### quality-checklist.md
- **Profit Transmission Chain** section - Verify transmission chain mapping
- **Cycle Timeline** section - Verify historical cycle documentation and current position
- **Observation Posts** section - Verify watchpoint definitions and thresholds
- **Database-Style Tracking** section - Verify structured tracking sections
- **Delivery Verification** section - Prevent static conclusions and vague risk warnings:
  - Static Conclusion Check: forward-looking conditionals, specific thresholds, "what would prove this wrong"
  - Vague Risk Warning Check: specific trigger conditions, probability estimates, tie to observation posts
  - Actionability Check: reader can take action, conditional recommendations, executable tracking plan

### Changed
- Workflow now includes 14 steps (was 12) with explicit profit chain and observation post construction
- Report template expanded from 12 to 15 sections with new analytical frameworks
- Quality checklist expanded from 7 to 12 categories with delivery verification

## [1.0.0] - Initial Release

### Added
- Core skill definition with 12-step workflow
- Industry chain mapping framework
- Supply-demand conflict analysis
- Cycle stage classification (7 stages)
- Capital-market expectation mapping
- DeepSearch-style research protocol with search budgets
- Evidence matrix and source quality ranking
- Report template with 12 sections
- Quality checklist with 7 categories
- PDF export capability
- Log extraction utilities
