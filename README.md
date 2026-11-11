# password-generator

Generate strong random passwords and passphrases.

## Usage

```bash
python3 password_generator.py
python3 -c "from password_generator import generate; print(generate(24))"
```

## Features

- Cryptographically secure passwords via secrets
- Configurable length and character sets
- Word-based passphrases with generate_passphrase()

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
