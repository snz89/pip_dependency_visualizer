# Python Package Dependency Graph Visualizer

Visualizing Python package dependencies, including transitive dependencies, using PlantUML

## Features

* Recursively explores package dependencies up to a configurable depth.
* Generates a PlantUML script representing the dependency graph.
* Supports visualization using a user-specified PlantUML jar file.
* Configuration via a TOML file.

## Prerequisites

* Python 3.11 or later (for `tomllib`)
* `pip` installed and accessible in your PATH.
* PlantUML jar file (e.g., `plantuml.jar`). You can download it from the [PlantUML website](https://plantuml.com/download).
* Java installed and accessible in your PATH (required to run the PlantUML jar).


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/snz89/pip_dependency_visualizer.git
   ```

## Configuration

Create a `config.toml` file in the project root directory with the following structure:

```toml
[config]
package_name = "your-package-name"  # Replace with the package you want to visualize
visualizer_path = "path/to/plantuml.jar" # Replace with the path to your PlantUML jar file
repository_url = "url-to-repository"
```

Replace `"your-package-name"` with the name of the pip package you want to analyze and `"path/to/plantuml.jar"` with the actual path to your PlantUML jar file.

## Usage

Run the script:

```bash
python .\src\dependency_visualizer.py  # Replace your_script_name.py with the actual script filename (e.g. visualize_dependencies.py)
```

This will generate a `dependency_graph.puml` file and then attempt to visualize it using the specified PlantUML jar. The resulting image will be saved in the same directory as the `.puml` file.  The default output image format is typically PNG.


## Example

To visualize the dependencies of the `requests` package, update your `config.toml` as follows:

```toml
[config]
visualizer_path = ".\\plantuml-1.2024.7.jar"
package_name = "requests"
repository_url = "https://github.com/psf/requests"
```

Then run the script as described above.
