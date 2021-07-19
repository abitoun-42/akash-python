from dataclasses import dataclass
import subprocess


@dataclass
class Bank:
    @staticmethod
    def balances(address: str,
                 count_total: str = None,
                 denom: str = None,
                 height: int = None,
                 limit: int = None,
                 node: str = None,
                 offset: int = None,
                 output: str = None,
                 page: int = None,
                 page_key: str = None) -> str:
        """
        Query the total balance of an account or of a specific denomination.

        :param address: akash public wallet address
        :param count_total: count total number of records in all balances to query for
        :param denom: The specific balance denomination to query for
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param limit: pagination limit of all balances to query for (default 100)
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :param offset: pagination offset of all balances to query for
        :param output: Output format (text|json) (default "text")
        :param page: pagination page of all balances to query for. This sets offset to a multiple of limit (default 1)
        :param page_key: pagination page-key of all balances to query for
        :return:
        """
        flags = []

        flags.extend(["--count-total", count_total] if count_total else [])
        flags.extend(["--denom", denom] if denom else [])
        flags.extend(["--limit", limit] if limit else [])
        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])
        flags.extend(["--offset", offset] if offset else [])
        flags.extend(["--page", page] if page else [])
        flags.extend(["--page-key", page_key] if page_key else [])

        cmd = ["akash", "query", "bank", "balances", address]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def denom_metadata(denom: str = None,
                       height: int = None,
                       output: str = None,
                       node: str = None) -> str:
        """
        Query the client metadata for all the registered coin denominations

        :param denom: The specific denomination to query client metadata for
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param output: Output format (text|json) (default "text")
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :return:
        """
        flags = []

        flags.extend(["--denom", denom] if denom else [])
        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])

        cmd = ["akash", "query", "bank", "denom-metadata"]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def total(denom: str = None,
              height: int = None,
              output: str = None,
              node: str = None) -> str:
        """
        Query total supply of coins that are held by accounts in the chain.

        :param denom: The specific denomination to query client metadata for
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param output: Output format (text|json) (default "text")
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :return:
        """
        flags = []

        flags.extend(["--denom", denom] if denom else [])
        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])

        cmd = ["akash", "query", "bank", "total"]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')
