import tomllib
import subprocess
from typing import Dict, List


def parse_toml_config(config_path: str) -> Dict[str, str]:
    """Parses a TOML configuration file."""
    config = {}
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)["config"]
        return config
    except FileNotFoundError as ex:
        print(f"Config file not found: {ex}")
    except tomllib.TOMLDecodeError as ex:
        print(f"Error decoding TOML file: {ex}")


def get_dependencies(package_name: str) -> List[str]:
    """Returns a list of dependencies for a given pip package."""
    try:
        result = subprocess.run(
            ["pip", "show", package_name], capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print(f"Error: Could not fetch dependencies for {package_name}")
        return []

    dependencies = []
    for line in result.stdout.splitlines():
        if line.startswith("Requires:"):
            dependencies = line.split(": ")[1].split(", ")

    dependencies = [dep.strip() for dep in dependencies if dep]

    return dependencies


def main():
    config_path = "config.toml"
    config = parse_toml_config(config_path)
    dependencies = get_dependencies(config["package_name"])


if __name__ == "__main__":
    main()
