# password-generator

Generate strong random passwords and passphrases.

## Usage

```bash
python3 password_generator.py
python3 -c "from password_generator import generate; print(generate(24))"
python3 -c "from password_generator import generate_pin; print(generate_pin(6))"
python3 -c "from password_generator import entropy; print(entropy('aB3!aB3!'))"
python3 -c "from password_generator import strength_label; print(strength_label('aB3!aB3!aB3!aB3!'))"
```

## Features

- Cryptographically secure passwords via secrets
- Configurable length and character sets
- Numeric PINs with generate_pin(length=6)
- Word-based passphrases with generate_passphrase()
- Entropy estimates in bits with entropy(password)
- Strength labels with strength_label(password)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
