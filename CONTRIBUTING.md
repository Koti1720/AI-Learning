# Contributing Guidelines

Thank you for considering contributing to this project! Please follow the guidelines below to make the process smooth and collaborative.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Coding Standards](#coding-standards)
- [Commit Message Format](#commit-message-format)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [License](#license)

## Code of Conduct
We expect all contributors to adhere to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

## Getting Started
1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/<repo>.git
   cd <repo>
   ```
3. **Create a new branch** for your work:
   ```bash
   git checkout -b <feature-or-bugfix-name>
   ```
4. Install any project dependencies as described in the project's README.

## Coding Standards
- **Language**: Follow the language‑specific style guide (e.g., PEP 8 for Python, Google's JavaScript style guide, etc.).
- **Formatting**: Use an automated formatter (e.g., `black` for Python, `prettier` for JavaScript) and ensure the code passes linting.
- **Naming**:
  - Variables, functions, and methods should use `snake_case` (Python) or `camelCase` (JavaScript).
  - Classes should use `PascalCase`.
- **Documentation**: Add docstrings/comments where appropriate. Public APIs must have clear documentation.
- **Testing**: Write unit tests for new features or bug fixes. Aim for at least 80 % coverage.

## Commit Message Format
We follow the **Conventional Commits** specification:
```
<type>(<scope>): <subject>

<body>

<footer>
```
- **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`
- **scope** (optional): the part of the codebase the change affects, e.g., `auth`, `api`
- **subject**: short description (max 50 characters)
- **body** (optional): detailed explanation, wrapped at 72 characters
- **footer** (optional): references to issues (`Closes #123`)

### Example
```
feat(auth): add JWT authentication

Implemented token generation and verification using PyJWT.

Closes #45
```

## Pull Request Process
1. **Push your branch** to your fork:
   ```bash
   git push origin <feature-or-bugfix-name>
   ```
2. **Open a Pull Request** against the `main` branch of the upstream repository.
3. **PR Title**: Use a concise title that follows the commit message format (type, scope, subject).
4. **PR Description**:
   - Briefly describe what the PR does.
   - Reference related issues (e.g., `Fixes #123`).
   - Mention any breaking changes.
5. **Review**: Request review from at least one maintainer. Address any feedback.
6. **Merge**: Once approved and all checks pass, the maintainer will merge the PR.

## Reporting Issues
If you encounter a bug or have a feature request, please open an issue with:
- A clear title.
- Steps to reproduce (for bugs).
- Expected vs. actual behavior.
- Any relevant logs or screenshots.

## License
By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
