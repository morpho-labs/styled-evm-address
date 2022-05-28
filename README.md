# Styled EVM address miner

Get your own 0x0000...0000 EVM contract address by mining a CREATE2 salt!

## Installation

- `pip install -r requirements.txt`

## Usage

The script will automatically save the salt and associated contract address to a .txt file everytime it finds a valid hash.

- Populate main.py with your contract's bytecode and the address prefix & suffix constraints
- `python main.py`

## Example

The following configuration will mine a salt giving a contract address starting with 0x0000, testing maximum 1T hashes and printing progression every 100k hashes:

```python
prefix_constraint = "0000"
suffix_constraint = ""
deployer_address = "0x..."
bytecode = "0x..."

print_interval = 100_000
max_trials = 1_000_000_000_000
```
