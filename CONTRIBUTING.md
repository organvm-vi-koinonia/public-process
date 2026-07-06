# Contributing to public-process

Thank you for your interest in contributing to this project.

## Overview

Public Process is the essay publication platform for the organvm system. It is a Jekyll blog that hosts essays about building in public, creative systems, autonomous infrastructure, and the philosophy behind the eight-organ model. Essays are written in Markdown with YAML frontmatter.

**Stack:** Jekyll blog, Ruby, Markdown essays

If you are new to the system, read the [Quick Start](docs/quick-start.md)
before cloning any other ORGANVM repo.

## Prerequisites

- Git
- Ruby 3.3.x (see `.ruby-version`)
- Bundler 4.0.3 (see `Gemfile.lock`)
- A GitHub account

## Development Setup

```bash
# Clone the canonical repo or your fork
git clone https://github.com/organvm/public-process.git
cd public-process

# Ensure Homebrew Ruby/Bundler are first on PATH (macOS/Homebrew)
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"

# Install Ruby dependencies
gem install bundler:4.0.3
bundle install

# Serve locally
bundle exec jekyll serve --host 127.0.0.1

# Site available at http://127.0.0.1:4000/public-process/
```

## How to Contribute

### Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Use the provided issue templates when available
- Include clear reproduction steps for bugs
- For documentation issues, specify which file and section

### Making Changes

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create a branch** for your change:
   ```bash
   git checkout -b feat/your-feature-name
   ```
4. **Make your changes** following the code style guidelines below
5. **Test** your changes:
   ```bash
   bundle exec jekyll build --strict_front_matter --future
   ```
6. **Commit** with a clear, imperative-mood message:
   ```bash
   git commit -m "add validation for edge case in parser"
   ```
7. **Push** your branch and open a Pull Request

### Code Style

Essays use Markdown with YAML frontmatter (title, date, categories, tags, excerpt). Follow the existing essay style: clear prose, specific examples, honest reflection. Filenames follow Jekyll convention: YYYY-MM-DD-slug.md in _posts/.

### Commit Messages

- Use imperative mood: "add feature" not "added feature"
- Keep the title under 72 characters
- Reference issue numbers when applicable: "fix auth bug (#42)"
- Keep commits atomic and focused on a single change

## Pull Request Process

1. Fill out the PR template with a description of your changes
2. Reference any related issues
3. Ensure all CI checks pass
4. Request review from a maintainer
5. Address review feedback promptly

PRs should be focused — one feature or fix per PR. Large changes should be
discussed in an issue first.

## Code of Conduct

Be respectful, constructive, and honest. This project is part of the
[organvm system](https://github.com/organvm-v-logos), which values transparency
and building in public. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/).

## Questions?

Open an issue on this repository or start a discussion if discussions are
enabled. For system-wide questions, see
[orchestration-start-here](https://github.com/organvm-iv-taxis/orchestration-start-here).
