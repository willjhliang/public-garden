
import os
import re


def simplify(str, allowed=['.', '/']):
    str = str.replace(' ', '-')
    str = ''.join(c.lower() for c in str if c.isalnum() or c in allowed or c == '-')
    return str.strip('-')


def format_display_math(data):
    ret = ''

    for line in data.splitlines():
        if re.match(r'\d+\. \$\$.+\$\$$', line):  # Only display math in list
            ret += line + '\n'
        elif re.match(r'\s*\d+\. .*\$\$.+\$\$.*$', line):  # Display math in list with other content
            ret += re.sub(r'(\s*)(\d+\. )(.*)(\$\$.+\$\$)(.*)$', r'\1\2\3\n\n\1    \4\n\n\1    \5\n', line)
        elif re.match(r'\s*> .*\$\$.+\$\$.*$', line):
            ret += re.sub(r'(\s*)> (.*)(\$\$.+\$\$)(.*)$', r'\1> \2\n\1>\n\1> \3\n\1>\n\1> \4\n', line)
        else:
            ret += line.replace('$$', '\n\n$$\n\n') + '\n'

    # Remove display math extra whitespace
    while '\n\n\n$$' in ret:
        ret = ret.replace('\n\n\n$$', '\n\n$$')
    while '$$\n\n\n' in ret:
        ret = ret.replace('$$\n\n\n', '$$\n\n')

    return ret


def format_inline_math(data):
    ret, in_display = '', False

    i = 0
    while i < len(data):
        if i < len(data) - 1 and data[i:i+2] == '$$':
            in_display = not in_display
            ret += '$$'
            i += 2
        else:
            if data[i] == '$':
                # Avoid edge case where $ occurs in display math Ex: $$\text{$a$ is a variable}$$
                ret += '$$' if not in_display else '$'
            else:
                ret += data[i]
            i += 1

    return ret


def format_wikilink_header(data):
    ret, in_header = '', False

    i = 0
    while i < len(data):
        if i - 6 >= 0 and data[i-6:i] == '.html#':
            in_header = True
        if in_header and data[i] == ')':
            in_header = False

        if in_header:
            if data[i] == ' ':
                ret += '-'
            elif data[i].isalnum():
                ret += data[i].lower()
        else:
            ret += data[i]
        i += 1

    return ret


def format_blockquote(data):
    ret, continuing = '', False

    for line in data.splitlines():
        if re.match(r'\s*> .*$', line):
            if continuing:
                ret += re.sub(r'(\s*)> (.*)$', r'\1>\n\1> \2\n', line)
            else:
                ret += line + '\n'
                continuing = True
        else:
            ret += line + '\n'
            continuing = False

    return ret


def main():
    names = {}  # Maps note title to simplified name
    paths = {}  # Maps note name with path to file
    parents = {}  # Tracks parent notes for folders
    for root, dirs, filenames in os.walk('notes'):
        for dir in dirs:
            names[dir] = simplify(dir)
        for filename in filenames:
            if filename.endswith('md'):
                name, _ = os.path.splitext(filename)
                names[name] = simplify(filename)
                paths[name] = simplify(os.path.join(root, names[name]))

                # Just the Docs only support 2 levels of folders, we only use the first
                if f'{os.path.basename(root)}.md' in filename and root.count('/') == 1:
                    parents[os.path.basename(root)] = name


    for root, _, filenames in os.walk('notes'):
        for filename in filenames:
            if not filename.endswith('md'):
                continue

            name, _ = os.path.splitext(filename)
            frontmatter = f'---\ntitle: {name}\nlayout: default\n'
            if name in parents.values():
                frontmatter += 'has_children: true\n'
            else:
                for parent in parents:
                    if parent in root:
                        frontmatter += f'parent: {parents[parent]}\n'
            frontmatter += '---\n\n'
            title = '# ' + name + '\n\n'

            with open(os.path.join(root, filename), 'r+') as f:
                data = '\n' + f.read()

                # Enforce new lines in blockquotes
                data = format_blockquote(data)

                # Add empty lines for display math, process list edge case
                data = format_display_math(data)

                # Change $ to $$ for mathjax, process display math edge case
                data = format_inline_math(data)

                # Reduce header size
                data = data.replace('\n#', '\n##')
                if len(data) > 0 and data[0] == '#':
                    data = '#' + data
                data = data.replace('\n#######', '\n######')

                # Replace local image links
                data = re.sub(r'\n(\s*)!\[\[([^\]]+)(\.\D{3,4})\]\]', r'\n\1<div style="text-align:center">\n\1<img src="{{ site.url }}{{ site.baseurl }}/notes/attachments/\2\3?raw=true"/>\n\1</div>', data)

                # Replace resized image links
                data = re.sub(r'\n(\s*)!\[\[(?:([^\]]+)(\.\D{3,4}))\|(\d+)\]\]', r'\n\1<div style="text-align:center">\n\1<img src="{{ site.url }}{{ site.baseurl }}/notes/attachments/\2\3?raw=true" width="\4"/>\n\1</div>', data)

                # Replace wikilinks
                for note in paths:
                    data = data.replace(f'[[{note}', f'[[{note} -> {paths[note]}')
                data = re.sub(r'\[\[([^\]]+) -> ([^\]]+\/)*(.+?)\.md(.+?)??]]', r'[\1#>\4](/public-garden/\2\3.html\4)', data)  # Replace .md with .html
                data = format_wikilink_header(data)  # Change header anchor to html anchor
                data = data.replace('#>#', ' > ')  # Change # to > for header links
                data = data.replace('#>', '')

                # Replace callouts
                data = re.sub(r'^> \[!(\w+)\]$', r'{: .\1 }', data, flags=re.M)

                # Overwrite current file
                f.seek(0)
                f.write(frontmatter + title + data)
                f.truncate()

                print(f'Formatted {filename}')

    for root, dirs, filenames in os.walk('notes', topdown=False):
        for filename in filenames:
            name, _ = os.path.splitext(filename)
            if name in names:
                os.rename(os.path.join(root, filename), os.path.join(root, names[name]))

        for dir in reversed(dirs):
            if dir in names:
                os.rename(os.path.join(root, dir), os.path.join(root, names[dir]))


if __name__ == '__main__':
    main()
