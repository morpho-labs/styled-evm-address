# Styled EVM address miner

Get your own 0x0000...0000 EVM contract address by mining a CREATE2 salt!

## Installation

- `pip install -r requirements.txt`

## Usage

- Populate main.py with your contract's bytecode and the address prefix & suffix constraints
- `python main.py`

## Example

The following configuration will mine a salt giving a contract address starting with 0x0000:

```python
bytecode = "0x"
sender = "0x"

prefix_constraint = "0000"
suffix_constraint = ""
max_trials = 1_000_000_000_000
```
