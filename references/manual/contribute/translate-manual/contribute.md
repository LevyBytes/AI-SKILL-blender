# Contribute

## Contribute

This guide uses French (fr) as an example, but any language code works — replace /fr throughout with your desired language's code. Check the currently available languages on the online translation interface or in the underlying git repository. Simple contribution — the preferred way to contribute translations is the web-based interface, currently hosted on Weblate; suggestions can be contributed without logging in and are reviewed by the translation team before publishing, and Weblate also offers tools like the glossary to improve consistency. Advanced operations — if the web interface doesn't suit you, PO files can be downloaded, edited locally, and uploaded back. Warning: conflicts can arise if updates occur while you edit locally, requiring manual resolution, and direct commits to the translation repository are no longer permitted. Note: uploading or integrating PO files can take several minutes — if a server timeout appears after ten minutes, refresh the page to confirm whether it succeeded. Installing — before translating, confirm the manual builds correctly per Getting Started. Language files — from the manual's root directory run:
```console
make checkout_locale
```
You'll be prompted for the language folder to download (e.g. type fr for French and press Return), which creates a locale/fr subdirectory after downloading. Example directory layout:
```text
blender-manual
|- locale/
|  |- fr/
|  |  |- LC_MESSAGES/
|- manual/
```
Note: with command-line Git, switch to the locale directory for updates rather than the blender-manual directory. Alternatively, download the PO files directly from Weblate via the Files menu on the language's page. PO-file editor — install a PO-file editor to modify the translation files; Poedit is recommended, but others work too. Building with translations — to build the manual with translations applied:
```console
make -e BF_LANG=fr
```
On Windows:
```console
set BF_LANG=fr
make html
```
Editing translation files — the PO files in `LC_MESSAGES` include blender_manual.po (the main user-manual translations) and sphinx.po (a smaller file for the website theme); open them in the PO editor (each entry is a manual section), translate the untranslated strings in the provided input field, then save and upload the modified .po files back to Weblate. Tip: sort entries by source or translation status for easier navigation. Important: build the manual after translating to surface syntax errors, which appear as warnings during the build. Maintenance — keeping track of fuzzy strings: when the manual updates, outdated translations are marked fuzzy; to track them:
```console
make report_po_progress
```
For a detailed report:
```console
python tools/translations/report_translation_progress.py locale/fr/
```
which lists files with fuzzy or empty strings; for more options:
```console
python tools/translations/report_translation_progress.py --help
```
Updating PO files: administrators regularly update PO files to match the latest English manual (typically weekly), and the last update is shown on the Blender Manual Translations project page; translators can update locally with:
```console
make update_po
```
though uploading these to Weblate is not permitted. See also Adding a Language.

[Related references](INDEX.md).
