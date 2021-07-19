from dataclasses import dataclass
import subprocess


@dataclass
class Debug:
    @staticmethod
    def addr(address: str) -> str:
        """
        Convert an address between hex encoding and bech32.

        :param address: akash public wallet address
        :return:
        """
        flags = []

        cmd = ["akash", "debug", "addr", address]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def pubkey(pubkey: str) -> str:
        """
        Decode a pubkey from hex, base64, or bech32.

        :param pubkey: pubkey from a cosmos ecosystem wallet
        :return:
        """
        flags = []

        cmd = ["akash", "debug", "pubkey", pubkey]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')

    @staticmethod
    def raw_bytes(raw_bytes: str) -> str:
        """
        Convert raw-bytes to hex.

        :param raw_bytes: bytes string
        :return:
        """
        flags = []

        cmd = ["akash", "debug", "raw-bytes", raw_bytes]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')
