
import os
import re

def main():
    repo = 'public-garden'
    attachment_folder = 'Attachments/'

    paths = {}
    for root, dirs, filenames in os.walk('notes'):
        for filename in filenames:
            name, _ = os.path.splitext(filename)
            paths[name] = os.path.join(root, filename)


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
                data = data.replace('\n#######', '\n######')

                # Replace local image links
                data = re.sub(r'!\[\[([^\]]+)(\.\D{3,4})\]\]', r'![\1](\1\2)', data)

                # Replace resized image links
                data = re.sub(r'!\[\[(?:([^\]]+)(\.\D{3,4}))\|(\d+)\]\]', r'<div>\n<img src="attachment:notes/' + attachment_folder + r'\1\2" width="\3"/>\n</div>', data)

                # Replace wikilinks
                for note in paths:
                    data = data.replace(note, paths[note])
                data = re.sub(r'\[\[([^\]]+\/)*(.+?)\.(.+?)]]', r'[\2](/' + repo + r'/\1\2.\3)', data)

                # Overwrite current file
                f.seek(0)
                f.write(frontmatter + data)
                f.truncate()


if __name__ == '__main__':
    inp = input('Running this formatter will overwrite all markdown files in the notes directory. Are you sure? (Y/N) ')
    if inp == 'Y':
        main()
