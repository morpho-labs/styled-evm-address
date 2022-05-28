import random

from Crypto.Hash import keccak

MIN_SALT_INT = 16 ** 64


def kecakk256(value: str):
    return keccak.new(data=bytes.fromhex(value), digest_bits=256).hexdigest()


prefix_constraint = "0000"
suffix_constraint = ""
deployer_address = "0x"
bytecode = "0x"

print_interval = 100_000
max_trials = 1_000_000_000_000


deployer_address_hex = deployer_address[2:]
bytecode_hash_hex = kecakk256(bytecode[2:])
file_name = f"{prefix_constraint}-{suffix_constraint}.txt"

if __name__ == "__main__":
    for step in range(max_trials):
        salt_hex = "%064x" % random.randrange(MIN_SALT_INT)
        input_hex = f"ff{deployer_address_hex}{salt_hex}{bytecode_hash_hex}"

        contract_address = kecakk256(input_hex)[-40:]

        if step % print_interval == 0:
            print("🔎 {:,}".format(step).replace(",", " "))

        if contract_address.startswith(prefix_constraint) and contract_address.endswith(
            suffix_constraint
        ):
            print(
                f"🎉 Hash found after {step} tries: {salt_hex} => 0x{contract_address}"
            )
            with open(file_name, "a") as file:
                file.write(f"{step} 0x{contract_address} {salt_hex}\n")
