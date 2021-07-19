from dataclasses import dataclass


@dataclass
class Tx:
    def audit(self, chain_id: str) -> dict:
        """
        :param chain_id: The network chain ID
        :return:
        """

        return {}

    def update(self):
        self.context["dseq"] = "update"
