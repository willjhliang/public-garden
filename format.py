
import os
import re


def format_inline_math(data):
    ret, in_display = '', False

    i = 0
    while i < len(data):
        if i < len(data)-1 and data[i:i+2] == '$$':
            in_display = not in_display
            ret += '$$'
            i += 2
        else:
            if data[i] == '$':
                # Avoid edge case where $ occurs in display math
                # Ex: $$\text{$a$ is a variable}$$
                ret += '$$' if not in_display else '$'
            else:
                ret += data[i]
            i += 1
    return ret


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

                # Remove display math extra whitespace
                while '\n\n\n$$' in data:
                    data = data.replace('\n\n\n$$', '\n\n$$')
                while '$$\n\n\n' in data:
                    data = data.replace('$$\n\n\n', '$$\n\n')

                # Change $ to $$ for mathjax
                data = format_inline_math(data)

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
                data = re.sub(r'\[\[([^\]]+\/)*(.+?)\.(.+?)]]', r'[\2](/' + repo + r'/\1\2.html)', data)  # replaces .md with .html

                # Overwrite current file
                f.seek(0)
                f.write(frontmatter + data)
                f.truncate()


if __name__ == '__main__':
    inp = input('Running this formatter will overwrite all markdown files in the notes directory. Are you sure? (Y/N) ')
    if inp == 'Y':
        main()
