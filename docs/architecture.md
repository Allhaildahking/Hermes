# MARS architecture

## Core
Own orchestration and stable interfaces. The core must not depend on one model vendor.

## Memory
Planned:
- short-term conversation state
- long-term user and project memory
- searchable memories
- explicit save and forget operations
- timestamps and provenance

## Tools
Planned:
- web and research
- filesystem
- code execution
- GitHub
- calculator and data analysis
- external APIs

Every tool will declare permissions and input/output contracts.

## Capabilities
Initial boundaries:
- writing
- programming
- research
- market analysis
- task planning
- automation

## Trading
Trading stays isolated.

Flow:
analysis -> strategy -> risk validation -> permission -> execution

The trading layer must enforce capital-protection rules independently of model output.

## Interfaces
The core should work through:
- CLI during development
- web application
- Telegram
- future voice interface

Interfaces must not contain core reasoning logic.

## Provider abstraction
The model provider is replaceable. No single vendor should become a hard dependency.
