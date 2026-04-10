# PyGit (Python)

A small, readable Git-like version control system built from scratch in Python.

PyGit is designed for learning and experimentation. It implements core ideas behind Git objects, branches, commits, and working directory restoration while keeping the codebase easy to follow.

---

## Highlights

- Content-addressed object storage (SHA-1)
- `blob`, `tree`, and `commit` object models
- Staging via index file
- Commit creation with parent linkage
- Branch creation, listing, checkout, and deletion (with current-branch safety check)
- Recursive tree restore on checkout
- Modular architecture for easier maintenance

---

## Project Layout

```text
python-git/
├── main.py         # Entry point
├── cli.py          # Command parsing + dispatch
├── repository.py   # Repository behavior (init/add/commit/checkout/branch)
├── git_objects.py  # Blob/Tree/Commit and object serialization logic
└── .pygit/         # Created after init
```

---

## Quick Start

### 1. Initialize repository

```bash
python3 main.py init
```

### 2. Stage files

```bash
python3 main.py add main.py
python3 main.py add .
```

### 3. Commit changes

```bash
python3 main.py commit -m "first commit"
python3 main.py commit -m "update" --author "Nguyen <you@example.com>"
```

### 4. Branch operations

```bash
# list branches
python3 main.py branch

# create branch
python3 main.py branch feature-x

# checkout branch
python3 main.py checkout feature-x

# create + checkout
python3 main.py checkout feature-y -b

# delete branch
python3 main.py branch feature-x -d
```

---

## CLI Reference

### `init`

Create `.pygit/` with object store, refs, HEAD, and index.

```bash
python3 main.py init
```

### `add`

Hash file content into blob objects and update index mapping path -> object hash.

```bash
python3 main.py add <path> [<path> ...]
```

### `commit`

Build tree from index, create commit object, advance current branch ref.

```bash
python3 main.py commit -m "message" [--author "Name <email>"]
```

### `checkout`

Switch branch and restore working directory from target commit tree.

```bash
python3 main.py checkout <branch>
python3 main.py checkout <branch> -b
```

### `branch`

List, create, or delete branches.

```bash
python3 main.py branch
python3 main.py branch <name>
python3 main.py branch <name> -d
```

---

## How It Works (Short Version)

1. File bytes are wrapped into a Git-like object format:
   `<type> <size>\0<content>`
2. The byte stream is SHA-1 hashed.
3. Compressed data is stored in `.pygit/objects/aa/bbbbb...`.
4. The index records staged file paths and blob hashes.
5. Commit points to a tree hash and optional parent commit.
6. Branch refs point to commit hashes.

---

## Current Limitations

This is an educational implementation, so some advanced Git behavior is intentionally out of scope for now:

- No merge/rebase
- No remote support
- No diff engine
- Minimal conflict handling
- No file mode variations beyond basic tree entries

---

## Design Goals

- Keep code understandable for learners
- Mirror real Git concepts where possible
- Prefer explicit logic over heavy abstraction
- Make extension points obvious for future features

---

## Suggested Next Steps

- Add a `status` command
- Add `log` to display commit history
- Add basic `cat-file` and `ls-tree` inspection commands
- Add tests for object serialization and checkout correctness

---

## License

Use this project for learning and experimentation.
Add a `LICENSE` file if you plan to distribute it publicly.
