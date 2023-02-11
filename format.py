
import os

def main():
    for root, dirs, filenames in os.walk('notes'):
        for filename in filenames:
            if not filename.endswith('md'):
                continue

            name, _ = os.path.splitext(filename)

            frontmatter = '---\ntitle: ' + name + '\nlayout: default\n---\n\n# ' + name + '\n\n'
            with open(os.path.join(root, filename), 'r+') as f:
                data = f.read()

                # Add empty lines for display math
                data = data.replace('$$', '\n\n$$\n\n')

                # Remove extra whitespace
                while '\n\n\n$$' in data:
                    data = data.replace('\n\n\n$$', '\n\n$$')
                while '$$\n\n\n' in data:
                    data = data.replace('$$\n\n\n', '$$\n\n')

                # Change header size
                data = data.replace('\n#', '\n##')

                # Overwrite current file
                f.seek(0)
                f.write(frontmatter + data)
                f.truncate()


if __name__ == '__main__':
    inp = input('Running this formatter will overwrite all markdown files in the notes directory. Are you sure? (Y/N) ')
    if inp == 'Y':
        main()
