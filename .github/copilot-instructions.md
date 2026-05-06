# Copilot Instructions

Apply these rules to all work in this repository.

## Python Functions

- Every function and method you create must include a docstring.
- Keep docstrings concise and focused on purpose, inputs, outputs, or side effects when relevant.

## Backend Changes And Tests

- Every new or updated backend functionality must include a corresponding test case.
- Write tests using plain `assert` statements.
- Do not introduce external test frameworks or pytest-style dependencies for this requirement.
- Place tests in the existing Django test modules unless the surrounding codebase already uses a different local pattern.

## Scope

- Treat Django models, forms, views, URLs, admin behavior, and other server-side logic as backend functionality.
- Do not consider styling-only or client-side JavaScript changes as backend functionality.