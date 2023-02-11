
import os

def main():
    for root, dirs, filenames in os.walk('.'):
        for filename in filenames:
            if not filename.endswith('md'):
                continue

            parsed = ''
            with open(os.path.join(root, filename), 'r+') as f:
                original = '\n\n\n' + f.read() + '\n\n\n'

                i = 1
                while i < len(original) - 1:
                    if original[i:i+2] == '$$':
                        if original[i-2:i] != '\n\n':
                            parsed += '\n' if original[i-1] == '\n' else '\n\n'
                        parsed += '$$'
                        if original[i+2:i+4] != '\n\n':
                            parsed += '\n'if original[i+2] == '\n' else '\n\n'
                        i += 2
                    else:
                        parsed += original[i]
                        i += 1

                f.seek(0)
                f.write(parsed)
                f.truncate()


if __name__ == '__main__':
    inp = input('Running this formatter will overwrite all markdown files in this directory. Are you sure? (Y/N) ')
    if inp == 'Y':
        main()
