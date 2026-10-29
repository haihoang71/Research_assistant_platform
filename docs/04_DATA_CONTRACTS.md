# Data contracts

These contracts will become formal Pydantic and API schemas as features are implemented.

## Evidence-backed claim

Each claim must contain:

- claim text;
- source identifier;
- evidence span identifier;
- confidence;
- verification status.

## Insufficient evidence

The system must represent insufficient evidence explicitly. It must not fill missing values with plausible text.
