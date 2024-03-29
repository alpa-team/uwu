import subprocess

import toml

pyproject = toml.load("pyproject.toml")
version = pyproject["tool"]["poetry"]["version"]
minor = int(version.split(".")[1])
new_version = f"0.{minor + 1}.0"
pyproject["tool"]["poetry"]["version"] = new_version

with open("pyproject.toml", "w") as f:
    toml.dump(pyproject, f)


subprocess.run(["git", "config", "--global", "user.name", "github-actions"])
subprocess.run(["git", "config", "--global", "user.email", "github-actions@github.com"])
subprocess.run(["git", "add", "pyproject.toml"])
subprocess.run(
    ["git", "commit", "-m", f"release of package uwu to version {new_version}"]
)
subprocess.run(["git", "push", "origin", "main"])
subprocess.run(["git", "tag", new_version])
subprocess.run(["git", "push", "origin", "--tags"])
