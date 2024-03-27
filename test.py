def print_colored(msg: str, color: str):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'black': '\033[30m',
            'reset': '\033[0m',
        }
        print(f'{colors[color]}{msg}{colors["reset"]}')

print_colored('Hello, world!', 'magenta')