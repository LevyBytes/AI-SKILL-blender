# Pull Requests

## Pull Requests

This page covers the tooling for contributing and reviewing code. Reviews are a key safeguard for change quality — they help catch bugs, design inconsistencies, and potential maintenance problems, and having your work reviewed also keeps you sharp. (Writers granted commit access can commit to the main repository without forking; see Commit Guidelines if that's you.) One-time setup assumes you've already checked out the manual repository per the install instructions. Fork: go to the Blender repository, click Fork, confirm with the default settings, then add your personal fork as a remote in your local git repository — click SSH for the correct URL and add it like:
```console
git remote add me git@git.blender.org:<username>/blender-manual.git
```
Pushing to the fork needs an SSH key; if you lack ~/.ssh/id_rsa.pub, generate one (works on Linux, macOS, and Git Bash on Windows):
```text
ssh-keygen
```
This makes a private key id_rsa and a public key id_rsa.pub in ~/.ssh — never reveal or send the private key, but the public one is safe to share. Paste the contents of ~/.ssh/id_rsa.pub into your projects.blender.org account settings via "Add Key" (any key name is fine). Workflow: the pull-request workflow is in the Blender Developer's Documentation — some of it targets the main Blender repository, but the workflow is identical for any Blender project. Guidelines for reviewers: the pull-request text should serve as the git commit message (see the guidelines); be explicit about changes to address before committing, without forcing a review iteration; if the PR isn't approved, the author should make another iteration; if the design needs agreement on a task first, put the PR on hold by prefixing the title with WIP:, signaling it isn't ready to merge (no review expected unless the author asks); writers should reply to PRs within 3 working days; add relevant modules/projects to the labels; and encourage new writers to review, since it's a good way to learn and to grow the project. Tips: append .patch to a PR's URL to get its patch file, e.g.:
```text
https://projects.blender.org/blender/blender-manual/pulls/104892.patch
```
Check out a PR into a detached head (leaving no branch behind), e.g.:
```console
git fetch -q origin +refs/pull/104892/head: ; git checkout -qf FETCH_HEAD
```

[Related references](INDEX.md).
