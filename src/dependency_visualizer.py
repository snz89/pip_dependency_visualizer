import tomllib
from typing import Dict


def parse_toml_config(config_path: str) -> Dict[str, str]:
    """Parses a TOML configuration file."""
    config = {}
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)["general"]
        return config
    except FileNotFoundError as ex:
        print(f"Config file not found: {ex}")
    except tomllib.TOMLDecodeError as ex:
        print(f"Error decoding TOML file: {ex}")


def main():
    config_path = "config.toml"
    config = parse_toml_config(config_path)


if __name__ == "__main__":
    main()
