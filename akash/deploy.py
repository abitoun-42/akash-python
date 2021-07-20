from dataclasses import dataclass
import subprocess


@dataclass
class Deploy:
    @staticmethod
    def create(sdl_file: str,
               account_number: int = None,
               broadcast_mode: str = None,
               chain_id: str = None,
               deposit: str = None,
               dry_run: str = None,
               dseq: int = None,
               fees: int = None,
               froms: str = None,
               gas: str = None,
               gas_adjustment: str = None,
               gas_price: str = None,
               generate_only: str = None,
               keyring_backend: str = None,
               keyring_dir: str = None,
               ledger: bool = None,
               memo: str = None,
               offline: bool = None,
               owner: str = None,
               sequence: int = None,
               sign_mode: str = None,
               tick: str = None,
               timeout: str = None,
               timeout_height: int = None,
               yes: bool = None) -> str:
        """
        Create a deployment on the akash network

        :param sdl_file: the path to the .yaml deploy file
        :param account_number: The account number of the signing account (offline mode only)
        :param broadcast_mode: Transaction broadcasting mode (sync|async|block) (default "sync")
        :param chain_id: The network chain ID
        :param deposit: Deposit amount (default "5000000uakt")
        :param dry_run: ignore the --gas flag and perform a simulation of a transaction, but don't broadcast it
        :param dseq: Deployment Sequence
        :param fees: Fees to pay along with transaction; eg: 10uatom
        :param froms: Name or address of private key with which to sign
        :param gas: gas limit to set per-transaction; set to "auto" to calculate sufficient gas automatically (default 200000)
        :param gas_adjustment: adjustment factor to be multiplied against the estimate returned by the tx simulation; if the gas limit is set manually this flag is ignored  (default 1)
        :param gas_price: Gas prices in decimal format to determine the transaction fee (e.g. 0.1uatom)
        :param generate_only: Build an unsigned transaction and write it to STDOUT (when enabled, the local Keybase is not accessible)
        :param keyring_backend: Select keyring's backend (os|file|kwallet|pass|test) (default "os")
        :param keyring_dir: The client Keyring directory; if omitted, the default 'home' directory will be used
        :param ledger: Use a connected Ledger device
        :param memo: Memo to send along with transaction
        :param offline: Offline mode (does not allow any online functionality)
        :param owner: Deployment Owner
        :param sequence: The sequence number of the signing account (offline mode only)
        :param sign_mode: Choose sign mode (direct|amino-json), this is an advanced feature
        :param tick: The time interval at which deployment status is checked (default 500ms)
        :param timeout: The max amount of time to wait for deployment status checking process (default 2m30s)
        :param timeout_height: Set a block timeout height to prevent the tx from being committed past a certain height
        :param yes: Skip tx broadcasting prompt confirmation
        :return:
        """
        flags = []

        flags.extend(["--account-number", account_number] if account_number else [])
        flags.extend(["--broadcast-mode", broadcast_mode] if broadcast_mode else [])
        flags.extend(["--chain-id", chain_id] if chain_id else [])
        flags.extend(["--deposit", deposit] if deposit else [])
        flags.extend(["--dry-run", dry_run] if dry_run else [])
        flags.extend(["--dry-run", dry_run] if dry_run else [])
        flags.extend(["--dseq", dseq] if dseq else [])
        flags.extend(["--fees", fees] if fees else [])
        flags.extend(["--from", froms] if froms else [])
        flags.extend(["--gas", gas] if gas else [])
        flags.extend(["--gas-adjustment", gas_adjustment] if gas_adjustment else [])
        flags.extend(["--gas-price", gas_price] if gas_price else [])
        flags.extend(["--generate-only", generate_only] if generate_only else [])
        flags.extend(["--keyring-backend", keyring_backend] if keyring_backend else [])
        flags.extend(["--keyring-dir", keyring_dir] if keyring_dir else [])
        flags.extend(["--ledger"] if ledger else [])
        flags.extend(["--memo", memo] if memo else [])
        flags.extend(["--offline"] if offline else [])
        flags.extend(["--owner", owner] if owner else [])
        flags.extend(["--sequence", sequence] if sequence else [])
        flags.extend(["--sign-mode", sign_mode] if sign_mode else [])
        flags.extend(["--tick", tick] if tick else [])
        flags.extend(["--timeout", timeout] if timeout else [])
        flags.extend(["--timeout-height", timeout_height] if timeout_height else [])
        flags.extend(["--yes"] if yes else [])

        cmd = ["akash", "deploy", "create", sdl_file]
        cmd.extend(flags)

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise ValueError(stderr.decode('utf8'))

        return stdout.decode('utf8')
