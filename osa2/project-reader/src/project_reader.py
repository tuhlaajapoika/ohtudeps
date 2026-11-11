import re
import tomllib
from urllib import request
from project import Project


def _strip_deps_versions(dependencies: list[str]) -> list[str]:
    """Palauta lista riippuvuuksista ilman versiointia."""
    pkg_list: list[str] = []
    for dep in dependencies:
        name = re.split(r"[<>=!~]", dep, maxsplit=1)[0].strip()
        pkg_list.append(name)
    return pkg_list


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta
        # Project-olio sen tietojen perusteella
        try:
            toml_data = tomllib.loads(content)
            t_proj = toml_data["project"]
            t_authors = [a["name"] for a in t_proj["authors"]]

            # parsi versionumerot
            t_proj_deps = _strip_deps_versions(t_proj["dependencies"])
            t_dev_deps = _strip_deps_versions(
                toml_data["dependency-groups"]["dev"]
            )

            # lisää python projektin riippuvuudeksi, jos määritelty
            try:
                if t_proj["requires-python"]:
                    t_proj_deps.insert(0, "python")
            except KeyError:
                pass  # jatka nostamatta poikkeusta

            return Project(
                name=t_proj["name"],
                authors=t_authors,
                project_license=t_proj["license"],
                description=t_proj["description"],
                dependencies=t_proj_deps,
                dev_dependencies=t_dev_deps
            )
        except KeyError as e:
            raise KeyError(f"Error parsing TOML: {e}") from e
        except ValueError as e:
            raise ValueError(f"Error with TOML data: {e}") from e
