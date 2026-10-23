# Get Extensions

## Get Extensions

The Get Extensions section lets you install and manage extension preferences. See also the Extensions page to learn what extensions are and how to make them.

Installing Extensions - a few routes:
Install from the Website: drag the install URL into Blender.
Install from Blender: search for the extension's name and click Install.
Install from Disk: use the top-right drop-down, or drop an extension .zip package onto Blender.
Note: any installed extension can be removed, but that's permanent; to stop one temporarily, Disable it instead.
Hint: see network troubleshooting for trouble reaching remote repositories.

Updating Extensions: you check for updates yourself; once one is found, Blender lets you update any available extension, and if updates exist an Update All button appears to install them all at once. Whatever version the repository currently offers is always treated as the latest.

Enable/Disable: once installed, an extension can be disabled (or re-enabled) through the user preferences; some types don't support this and always read as enabled. Tip: if an Add-on doesn't activate when enabled, check the Console window for errors.

Extension Settings:
Visit Extensions Platform: opens extensions.blender.org in a browser.
Refresh Remote: manually checks the online repositories for updates.
Refresh Local: rescans extension and legacy add-ons for changes to modules and metadata (much like a restart); issues come back as warnings.
Install Available Updates: updates every extension that has one waiting.
Install from Disk: installs an extension from a .zip package into a Local Repository, with no updates available; it also installs legacy Add-ons (see Installing Legacy Add-ons).

Filter by Type: or narrow to a single type: All (every extension), Add-ons (only add-ons), Themes (only themes).

Repositories: out of the box Blender has one Remote Repository aimed at the Official Blender Extensions Platform plus two Local Repositories. When you need more (to reach third-party platforms, say), you can add them. Click the + icon to add: Add Remote Repository (from a URL) or Add Local Repository (user-managed, for use with Install from Disk). Click the - icon to remove: Remove Repository, or Remove Repository & Files (which also deletes all associated files). These changes are permanent and can't be undone.
Remote Repository: a remote repository that supports listing and updating extensions. Options: Check for Updates on Startup (lets Blender look for updates at launch, with a status-bar notification when any exist) and Access Token (a personal access token some repositories require).
Local Repository: a repository you manage by hand. There are two kinds; new local repositories default to User, which is what you want most of the time. After creating one you can switch it to a System source in the Advanced options; System repositories are meant to bundle extensions with Blender to keep it portable.

[Related references](INDEX.md).
