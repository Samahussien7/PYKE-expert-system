# Family Law Expert System

## Overview

This repository contains an expert system built using the Pyke package in Python that provides legal guidance on family court matters, specifically focusing on child custody and alimony cases according to Personal Status Law. The system implements backward chaining reasoning to determine legal outcomes based on established rules and conditions.

## Domain of Law

The expert system addresses two main areas of family law:

1. **Child Custody**: Based on Article 20 of Law No. 20 of 1929 amended by Law No. 100 of 1985
2. **Alimony Cases**: Covering various financial support obligations following divorce

## Key Features

- Determines conditions for loss of custody from the mother
- Identifies when the father has the right to claim custody
- Specifies requirements for male custodians according to Article 144
- Calculates alimony obligations based on multiple factors
- Handles different divorce scenarios (normal divorce vs. divorce for harm)
- Considers various financial aspects including incubation costs, breastfeeding compensation, housing, and servant expenses

## System Architecture

The expert system uses backward chaining inference with Pyke, which means it:
- Starts with a hypothesis (desired outcome)
- Works backward through rules to find supporting evidence
- Validates conditions through user queries
- Provides legally sound conclusions based on established rules

## Installation Requirements

```bash
pip install pyke
```

## Knowledge Base

The system incorporates legal knowledge from:
- Personal Status Law Article 20 (amended)
- Custody transfer conditions
- Alimentation case rules
- Divorce settlement regulations

## Examples of Queries Handled

- Under what conditions can a mother lose custody?
- When can a father claim custody of children?
- What are the financial obligations in alimony cases?
- How are divorce settlements calculated?

## Legal Disclaimer

This expert system is designed for educational and informational purposes only. It does not constitute legal advice. For actual legal matters, please consult with a qualified attorney  specialized in family court affairs.
##Demo
[demo](https://github.com/user-attachments/assets/eca25c91-9d0b-438a-b2d7-d06a914798b7)



