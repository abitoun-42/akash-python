from dataclasses import dataclass
from typing import List
import subprocess

from akash.deploy import Deploy
from akash.tx import Tx
from akash.query import Query


@dataclass
class Akash:
    deploy = Deploy()  # handle deploy module of the CLI
    tx = Tx()  # handle tx module of the CLI
    query = Query()  # handle query module of the CLI

    @staticmethod
    def add_genesis_account(
            address: str,
            coin: List,
            home: str = None,
            height: int = None,
            keyring_backend_string: str = None,
            output: str = None,
            node: str = None,
            vesting_amount: str = None,
            vesting_end_time: int = None,
            vesting_start_time: int = None) -> str:
        """
        :param address: akash public wallet address
        :param coin: List of initial coin, The list of initial tokens must contain valid denominations.
        :param home: The application home directory (default "/home/ericu/.akash")
        :param keyring_backend_string: Select keyring's backend (os|file|kwallet|pass|test) (default "os")
        :param height: Use a specific height to query state at (this can error if the node is pruning state)
        :param output: Output format (text|json) (default "text")
        :param node: <host>:<port> to Tendermint RPC interface for this chain (default "tcp://localhost:26657")
        :param vesting_amount: amount of coins for vesting accounts
        :param vesting_start_time: schedule end time (unix epoch) for vesting accounts
        :param vesting_end_time: schedule start time (unix epoch) for vesting accounts
        :return:
        """
        flags = []

        flags.extend(["--home", home] if home else [])
        flags.extend(["--keyring-backend-string", keyring_backend_string] if keyring_backend_string else [])
        flags.extend(["--height", height] if height else [])
        flags.extend(["--output", output] if output else [])
        flags.extend(["--node", node] if node else [])
        flags.extend(["--vesting-amount", vesting_amount] if vesting_amount else [])
        flags.extend(["--vesting-start-time", vesting_start_time] if vesting_start_time else [])
        flags.extend(["--vesting-end-time", vesting_end_time] if vesting_end_time else [])

        cmd = ["akash", "add-genesis-account", address]
        cmd.extend(coin)
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def collect_gentxs(home: str = None) -> str:
        flags = []

        flags.extend(["--home", home] if home else [])

        cmd = ["akash", "collect-gentxs"]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')
