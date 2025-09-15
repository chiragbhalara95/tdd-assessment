# TDD workflow & guidelines


This repo is intentionally small and focused to show the TDD progression. Suggested workflow while solving the kata:


1. Create a single failing test for the simplest behavior (empty string) and run pytest to see it fail.
2. Implement the minimal code to make it pass.
3. Refactor if needed.
4. Commit with a clear message describing the step, e.g. `test: add failing test for empty string` followed by `feat: return 0 for empty string`.
5. Repeat for single number, two numbers, multiple numbers, newlines, custom delimiter, negatives.


Commit early and often — reviewers want to see the step-by-step evolution.