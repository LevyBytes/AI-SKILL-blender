# Commit Guidelines

## Commit Guidelines

Directly submitting changes is limited to people with commit access; once granted, you can commit directly rather than creating a patch file. Make commits from your Git client or the command line — this creates a commit and sends it to the central repository:
```console
git commit -m "This is what I did"
git push
```
Omitting -m "message" prompts you to type the message in a text editor. Tip: always be on the latest revision before committing, since conflicting changes in the latest revision can block a direct commit — update your local repository first (run make update). See also Blender's Git usage guide, and the release-branch documentation for committing to a specific release branch and creating merge commits. Writing a good commit message: when a manual change relates directly to a specific Blender commit, it helps to make the commit title match the Blender commit's, and you're asked to include the hash of the Blender source commit. For example, commit rBM8473 carries a descriptive title plus the hash rBa71d2b260170 — the hash comes from the URL in the Documentation task for an upcoming release. More general changes needn't follow that policy, but should still describe clearly what changed and why; prefixing the title with Cleanup: or Fix: helps for general cleanups or fixes. Good commit messages help administrators track changes and ensure new features are properly documented.

[Related references](INDEX.md).
