from __future__ import annotations

import argparse
import sys

from repository import Repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PyGit: A simple Git implementation in Python")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("init", help="Initialize a new repository")

    add_parser = subparsers.add_parser(
        "add", help="Add files and directiories to the staging area"
    )
    add_parser.add_argument("paths", nargs="+", help="Files and dirs to add")

    commit_parser = subparsers.add_parser("commit", help="Commit changes to the repository")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
    commit_parser.add_argument("--author", help="Author name and email")

    checkout_parser = subparsers.add_parser("checkout", help="Move/Create branch")
    checkout_parser.add_argument("branch", help="Switch to existing branch")
    checkout_parser.add_argument(
        "-b", "--create-branch", action="store_true", help="Create and switch to a new branch"
    )

    branch_parser = subparsers.add_parser(
        "branch", help="List, create, or delete branches"
    )
    branch_parser.add_argument("name", nargs="?")
    branch_parser.add_argument(
        "-d", "--delete", action="store_true", help="Delete the specified branch"
    )

    return parser


def run(argv: list[str] | None = None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return

    repo = Repository()

    try:
        if args.command == "init":
            if repo.init() is False:
                print("Repository already exists")
                return

        elif args.command == "add":
            if not repo.git_dir.exists():
                print("Not a git repository")
                return

            for path in args.paths:
                repo.add_path(path)

        elif args.command == "commit":
            if not repo.git_dir.exists():
                print("Not a git repository")
                return

            author = args.author or "Pygit user"
            repo.commit(args.message, author)

        elif args.command == "checkout":
            if not repo.git_dir.exists():
                print("Not a git repository")
                return

            repo.checkout(args.branch, args.create_branch)

        elif args.command == "branch":
            if not repo.git_dir.exists():
                print("Not a git repository")
                return

            repo.branch(args.name, args.delete)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    run()
