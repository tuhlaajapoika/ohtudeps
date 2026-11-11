class Project:
    def __init__(self, name, authors, project_license, description, dependencies, dev_dependencies):
        self.name = name
        self.authors = authors
        self.license = project_license
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    @staticmethod
    def _dashify_list(data_list):
        if not data_list:
            return " -"
        return "\n" + "\n".join(f"- {item}" for item in data_list)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or "-"}"
            f"\nLicense: {self.license or "-"}"

            f"\n\nAuthors:"
            f"{self._dashify_list(self.authors)}"

            f"\n\nDependencies:"
            f"{self._dashify_list(self.dependencies)}"

            f"\n\nDevelopment dependencies:"
            f"{self._dashify_list(self.dev_dependencies)}"
        )
