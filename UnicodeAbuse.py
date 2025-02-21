import sys
from typing import List
from colorama import init, Fore, Style

# Initialize colorama
init()

class UnicodeAbuse:
    """Class for encoding and decoding text using Unicode variation selectors."""
    
    @staticmethod
    def text_to_bytes(text: str) -> list:
        """Convert text to list of bytes.
        
        Args:
            text: Input text to convert
            
        Returns:
            List of bytes representing the text
            
        Raises:
            ValueError: If text is empty or invalid
        """
        try:
            if not text:
                raise ValueError("Input text cannot be empty")
            return list(text.encode('utf-8'))
        except Exception as e:
            raise ValueError(f"Failed to convert text to bytes: {str(e)}")

    @staticmethod
    def convert_bytes_to_variation_selectors(bytes_list: list) -> list:
        """Convert bytes to Unicode variation selectors.
        
        Args:
            bytes_list: List of bytes to convert
            
        Returns:
            List of Unicode variation selectors
            
        Raises:
            ValueError: If bytes_list is empty or invalid
        """
        try:
            if not bytes_list:
                raise ValueError("Bytes list cannot be empty")
            # Placeholder - will implement actual conversion later
            encoded_list = []
            for b in bytes_list:
                if b < 16:
                    encoded_list.append( chr(0xFE00 + (b)) )
                else:
                    encoded_list.append( chr(0xE0100 + (b - 16)) )
        
            return list(encoded_list)
        
        except Exception as e:
            raise ValueError(f"Failed to convert bytes to variation selectors: {str(e)}")

    def encoder(self, base: str, payload: str) -> str:
        """Encode payload into Unicode variation selectors after base character.
        
        Args:
            base: Base Unicode character
            payload: Text to encode
            
        Returns:
            Encoded string with variation selectors
            
        Raises:
            ValueError: If base or payload is invalid
        """
        try:
            if not base or len(base) != 1:
                raise ValueError("Base must be a single character")
            if not payload:
                raise ValueError("Payload cannot be empty")
                
            bytes_list = self.text_to_bytes(payload)
            variations = self.convert_bytes_to_variation_selectors(bytes_list)
            
            return base + ''.join(variations)
        except Exception as e:
            raise ValueError(f"Failed to encode payload: {str(e)}")

    @staticmethod
    def decoder(encoded_payload: str) -> str:
        """Remove variation selectors from encoded text.
        
        Args:
            encoded_payload: Text with variation selectors
            
        Returns:
            Original text without variation selectors
            
        Raises:
            ValueError: If encoded_payload is invalid
        """
        try:
            if not encoded_payload:
                raise ValueError("Encoded payload cannot be empty")
                
            # Remove variation selectors (U+FE00 to U+FE0F and U+E0100 to U+E01EF)
            result = ''
            for char in encoded_payload:
                cp = ord(char)
                if (0xFE00 <= cp <= 0xFE0F or 0xE0100 <= cp <= 0xE01EF):
                    result += chr(cp - 0xFE00) if cp < 0xE0100 else chr(cp - 0xE0100 + 16)
            return result
        except Exception as e:
            raise ValueError(f"Failed to decode payload: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Unicode Variation Selector Text Encoder/Decoder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
                Examples:
                Encode text:
                    python unicode_abuse.py encode -b A -p "Hello World"
                    
                Decode text:
                    python unicode_abuse.py decode -t "A︀︁︂︃"
                    
                Note: The encoded text might not display correctly in all terminals.
                """
                    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    subparsers.required = True
    
    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encode text using variation selectors')
    encode_parser.add_argument('-b', '--base', required=True, help='Base character to attach selectors to')
    encode_parser.add_argument('-p', '--payload', required=True, help='Text to encode')
    
    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decode text with variation selectors')
    decode_parser.add_argument('-t', '--text', required=True, help='Text to decode')
    
    args = parser.parse_args()
    
    abuser = UnicodeAbuse()
    
    try:
        if args.command == 'encode':
            result = abuser.encoder(args.base, args.payload)
            print(f"{Fore.YELLOW}╔══ ENCODED TEXT ══╗{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{result}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}Payload Length: {Style.RESET_ALL}{len(result)} characters = 1 base character + {len(result) - 1} variation selector characters")
            print(f"{Fore.GREEN}Payload's Unicode Codepoints: {Style.RESET_ALL}{' '.join(f'U+{ord(c):04X}' for c in result)}\n")
        else:  # decode
            result = abuser.decoder(args.text)
            print(f"\n{Fore.YELLOW}╔══ DECODED TEXT ══╗{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}{result}{Style.RESET_ALL}\n")
            print(f"{Fore.GREEN}Payload Length: {Style.RESET_ALL}{len(result) + 1} characters = 1 base character + {len(result)} variation selector characters")
            print(f"{Fore.GREEN}Payload's Unicode codepoints: {Style.RESET_ALL}{' '.join(f'U+{ord(c):04X}' for c in args.text)}\n")
            
    except ValueError as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}", file=sys.stderr)
        sys.exit(1)
