import random

from Crypto.Hash import keccak


def kecakk256(value: str):
    return keccak.new(data=bytes.fromhex(value), digest_bits=256).hexdigest()


bytecode = "0x"
sender = "0x"

prefix_constraint = "0000"
suffix_constraint = ""
max_trials = 1_000_000_000_000

sender_bytes = sender[2:]
bytecode_hash = kecakk256(bytecode[2:])
file_name = f"{prefix_constraint}-{suffix_constraint}.txt"

if __name__ == "__main__":
    for step in range(max_trials):
        salt = "%062x" % random.randrange(16 ** 62)
        contract_address = kecakk256(f"ff{sender}{salt}{bytecode_hash}")[-40:]

        if step % 50000 == 0:
            print("🔎 {:,}".format(step).replace(",", " "))

        if contract_address.startswith(prefix_constraint) and contract_address.endswith(
            suffix_constraint
        ):
            print(f"🎉 Hash found after {step} tries: {salt} => 0x{contract_address}")
            with open(file_name, "a") as file:
                file.write(f"{step} 0x{contract_address} {salt}\n")
