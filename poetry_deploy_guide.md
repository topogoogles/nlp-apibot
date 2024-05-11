# Poetry Deploy Guide

## Basic steps to deploy your project

### 1. Install Poetry

If you haven't already installed Poetry, you can do so by following the instructions on the official Poetry website. For most users, the recommended way to install Poetry is via the installer script:

```bash
curl -sSL https://install.python-poetry.org | python -
```

### 2. Initialize Your Project with Poetry

Navigate to your project directory and run:

```bash
poetry init
```

This command will guide you through creating your `pyproject.toml` file, where you'll specify your project's dependencies and other configurations.

### 3. Check the Project's Environment

Poetry manages its own virtual environments. Ensure that you are working within the correct environment for your project. You can activate the project's environment by running

```bash
poetry shell
```

### 4. Verify Dependencies

Make sure that all the necessary dependencies are correctly added to your `pyproject.toml` file. You can add dependencies by running `poetry add <package_name>` for each package you need.

For your project, you might need to add packages like `googlesearch`, `requests`, `lxml`, `beautifulsoup4`, `nltk`, `scikit-learn`, and `tkinter`. For example:

```bash
poetry add googlesearch requests lxml beautifulsoup4 nltk scikit-learn
```

After adding dependencies, run `poetry install` to ensure they are installed in the project's environment.

### 5. Build Your Application

With Poetry, you can build your application by creating a distribution package. This is useful for deployment. Run:

```bash
poetry build
```

This command will create a `.tar.gz` file in the `dist/` directory, which is your application's distribution package.

## Troubleshooting Import Errors

- **Check for Conflicting Dependencies**: Sometimes, dependencies can conflict with each other, leading to import errors. You can check for dependency conflicts by running `poetry show --tree`. This command will display a tree of all installed packages and their dependencies. Look for any packages that might conflict with the ones you're trying to use.

- **Ensure VSCode is Using the Correct Python Interpreter**: VSCode might be using a different Python interpreter than the one managed by Poetry. To ensure VSCode uses the correct interpreter, you can select it by clicking on the Python version in the bottom-left corner of the VSCode window or by using the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and searching for "Python: Select Interpreter". Choose the interpreter that corresponds to your Poetry-managed environment.

- **Reload VSCode**: Sometimes, simply reloading VSCode can resolve import issues. You can do this by closing and reopening VSCode or by using the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and searching for "Developer: Reload Window".

- **Check for Typos in Import Statements**: Although it might seem basic, ensure that there are no typos in your import statements. A common mistake is misspelling package names or module names.

- **Update Poetry**: If you're using an older version of Poetry, consider updating it to the latest version. Newer versions might have bug fixes or improvements that resolve your issue. You can update Poetry by running `poetry self update`.
