from dataclasses import dataclass
from akash.bank import Bank
from akash.auth import Auth


@dataclass
class Query:
    bank: callable = Bank()
    auth: callable = Auth()
