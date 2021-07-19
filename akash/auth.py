from dataclasses import dataclass
import subprocess


@dataclass
class Auth:
    @staticmethod
    def account(address: str,
                height: int = None,
                node: str = None,
                output: str = None) -> str:
        """
        :param address: akash public wallet address
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param output: Output format (text|json) (default "text")
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :return:
        """
        flags = []

        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])

        cmd = ["akash", "query", "auth", "account", address]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def params(height: int = None,
               node: str = None,
               output: str = None) -> str:
        """
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param output: Output format (text|json) (default "text")
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :return:
        """
        flags = []

        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])

        cmd = ["akash", "query", "auth", "account"]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')
