# Will's Garden

This is my solution for hosting Obsidian (markdown) notes online. Check out the website [here](https://willjhliang.github.io/public-garden/).

## My Setup

I didn't find that many customizable options for publishing Obsidian notes, so I decided to build my own. The big idea is that since markdown is so versatile, we can publish it on Github Pages using Jekyll; the crucial component is `format.py`, which converts the Obsidian format into kramdown. The crucial changes are as follows.
1. Replace wikilinks with standard markdown links with absolute path; I also include support for header links.
2. Replace image links with HTML tags, include width information if necessary.
3. Add empty lines below and above `$$` for display (block) math.
4. Replace inline math delimeters `$` with `$$`.
5. (Optional) Add frontmatter for Jekyll, add title as H1 and reduce other header sizes, form organizational hierarchy for Just the Docs.

> Note that `format.py` will OVERWRITE all `.md` files in its directory. Be careful if you use it as it is not reversible.

You can manually deploy a site by running the Python script (I used Python 3.10.10) and putting all the files into the [Just the Docs template](https://github.com/just-the-docs/just-the-docs-template). I went a bit further and automated everything; the automated pipeline from Obsidian to publish is three-fold.
1. Set up a git repository in your vault and link it to Github. Install the Obsidian Git plugin for automatic commits and pushes. For reference, my repository is [here](https://github.com/willjhliang/notes).
2. Add that repository as a submodule in your Jekyll repository. Set up Github Actions in this repository and your notes repository for automatic syncing. My examples are in `.github/workflows`; you can copy those files and replace the relevant information.  

    For the workflow id, reference [this documentation](https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28). In summary, make a Github Personal Access Token, then run the following.
    ```
    curl \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer <YOUR-TOKEN>"\
      -H "X-GitHub-Api-Version: 2022-11-28" \
      https://api.github.com/repos/OWNER/REPO/actions/workflows
    ```
    You'll also need a secret token called CI_TOKEN for each repository. You can make one by making a Personal Access Token (with read/write permissions) and adding it to (repository) Settings > Secrets and variables > Actions > New repository secret.

3. The Just the Docs template includes an automated workflow for publishing to Github Pages. This needs to be modified to include `format.py`, and you can copy my workflow in `sync.yml`.

> Depending on your Obsidian usecase, you might need to modify `format.py` to modify some other markdown components.
