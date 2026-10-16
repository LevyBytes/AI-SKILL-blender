# Adding a Language

## Adding a Language

This page walks through starting a new translation language. Preparations — if no one has started your target language and you want to create a new set of files for, say, 'fr' (French), first build the environment described in Getting Started, particularly the Installing Dependencies and Building the Manual sections. That foundation lets you create a new translation language from the English source, run make to turn translated po-file text into HTML for local testing, and pull in English-text changes added by other contributors. The examples below show creating a new French file set (language code fr) on Linux; other platforms vary slightly but are mostly the same. Steps: create a Blender ID if you don't have one; log into projects.blender.org and create an issue requesting commit access to push changes to the translation team's central repository; open a console; and change the working directory to the blender-manual directory where the Makefile lives. Trying the make process to create English HTML files — remove any previous build directory:
```console
make clean
```
convert all rst files into pot translation files:
```console
make gettext
```
create HTML files:
```console
make html
```
then view the result locally by opening blender-manual/build/html/index.html. Creating the language entry in the HTML menu — open ./build_files/theme/js/version_switch.js (from the blender-manual subdirectory), find the language table in `var all_langs = {..};`, add the entry `"fr": "Français",` (i.e. `"fr": "Français"`, noting the Unicode characters), then commit and push:
```console
git add ./build_files/theme/js/version_switch.js
git commit -m "HTML: Add French to language menu"
```
```console
git push
```
Generating the file set for the target language — check out the current translation repository:
```console
git clone https://projects.blender.org/blender/blender-manual-translations.git locale
```
This downloads all available language sets into the locale directory (where you'll see the hidden .git subdirectory alongside the language directories), and you add your own set for the language you're translating. From the blender-manual directory, generate the fr file set:
```console
make update_po
```
These files are still English-only, with all msgstr entries blank. Submit the new set to the central repository:
```console
cd locale
git add fr
git commit -m "Initial commit language set of files for French"
```
Tips: for convenience in scripting batch/shell translation and review commands, define two environment variables in .bashrc:
```text
export BLENDER_MAN_EN=$HOME/<path>/blender-manual
export BLENDER_MAN_FR=$BLENDER_MAN_EN/locale
```
Newly generated files contain placeholders for authors, revision dates, and the like; if replacing them is tedious, copy the change_placeholders.sh script from ~/blender-manual/tools/util_maintenance into your local bin directory, replace its values with your details, then after each file change run it to update your personal details and revision date/time and build your language's HTML for browser viewing:
```console
$HOME/bin/change_placeholders.sh $BLENDER_MAN_FR
make -d --trace -w -B -e SPHINXOPTS="-D language='fr'" 2>&1
```

[Related references](INDEX.md).
