from dataclasses import dataclass


@dataclass
class Deploy:

    def create(self):
        self.context["dseq"] = "create"

    def update(self):
        self.context["dseq"] = "update"
