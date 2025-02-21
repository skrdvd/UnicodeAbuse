# Unicode Variation Selector Text Encoder/Decoder

A Python tool for hiding text within Unicode variation selectors, making the text appear as a single character while containing hidden information. The tools currently supports only ONE base character, and unlimited payload character.

## Features

- Encode any text into Unicode variation selectors
- Decode hidden text from variation selectors
- Colorized command-line interface
- Detailed Unicode codepoint information
- Comprehensive error handling
- UTF-8 support

## Requirements

- Python 3.6+
- colorama package (`pip install colorama`)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd unicode-abuse
```

2. Install requirements using pip:
```bash
# Using requirements.txt
pip install -r requirements.txt

# Or install directly
pip install colorama>=0.4.6
```

## Usage

```bash
# Encode text (hide text behind a character)
python unicode_abuse.py encode -b <base_character> -p <payload/text_to_hide>

# Decode text (extract hidden text)
python unicode_abuse.py decode -t <text_with_hidden_content>
```

### Examples

1. **Encoding a simple message:**
```bash
python unicode_abuse.py encode -b A -p "Hello World"
```
Output:
```
╔══ ENCODED TEXT ══╗
A︀︁︂︃︄︅︆︇︈︉
Payload Length: 11 characters = 1 base character + 10 variation selector characters
Payload's Unicode Codepoints: U+0041 U+FE00 U+FE01 U+FE02 U+FE03 U+FE04 ...
```

2. **Decoding a message:**
```bash
python unicode_abuse.py decode -t "A︀︁︂︃︄︅︆︇︈︉"
```
Output:
```
╔══ DECODED TEXT ══╗
Hello World
Payload Length: 11 characters = 1 base character + 10 variation selector characters
Payload's Unicode Codepoints: U+0041 U+FE00 U+FE01 U+FE02 U+FE03 U+FE04 ...
```

## Technical Details

### Variation Selector Ranges
- Primary range: U+FE00 to U+FE0F (16 selectors)
- Extended range: U+E0100 to U+E01EF (240 selectors)

### Process
1. **Encoding:**
   - Converts input text to UTF-8 bytes
   - Maps bytes to variation selectors
   - Attaches selectors to base character

2. **Decoding:**
   - Extracts variation selectors
   - Converts back to original bytes
   - Reconstructs original text

## Limitations

- Some text editors may not display variation selectors
- Maximum payload size limited by available selectors
- Some systems may normalize or strip variation selectors
- Copy-paste might not work in all applications

## Command Line Arguments

```bash
encode:
  -b, --base BASE     Base character to attach selectors to
  -p, --payload TEXT  Text to encode

decode:
  -t, --text TEXT    Text to decode
```

## Error Handling

- Invalid input validation
- Empty payload checks
- Base character validation
- UTF-8 encoding/decoding errors
- Comprehensive error messages

## Security Notice

**DISCLAIMER AND WARNING:**

This tool is provided for STRICTLY EDUCATIONAL AND RESEARCH PURPOSES ONLY. By using this tool, you acknowledge and agree to the following:

- This tool should only be used in environments where you have explicit permission
- The author assumes NO RESPONSIBILITY for any misuse or illegal activities conducted with this tool
- Users are solely responsible for ensuring compliance with applicable laws and regulations
- Hidden text may be detected or stripped by security systems
- This tool should not be used for:
  - Bypassing security measures
  - Concealing malicious content
  - Any form of deception or fraud
  - Any illegal activities

USE AT YOUR OWN RISK.

## License

MIT License
