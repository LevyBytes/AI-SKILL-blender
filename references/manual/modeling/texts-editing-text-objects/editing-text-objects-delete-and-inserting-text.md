# Editing Text Objects: Delete, Inserting Text, Accent Characters, Converting to a Mesh or Curve, Assigning Materials

### Delete

Reference

Editor :

3D Viewport

Mode :

Edit Mode

Menu :

Header ‣ Text ‣ Delete

Previous/Next Character
Wipes out the character sitting before or after the cursor.

Previous/Next Word
Wipes out the word sitting before or after the cursor.

### Inserting Text

Text can come in two ways: out of the internal text buffer, or out of a text file.

Take an existing text data-block and turn it into an object from the Text editor's header by
choosing Edit ‣ Text to 3D Object ,
then One Object or One Object per Line as your needs dictate.

You can also paste in from the clipboard or a file while editing 3D text.

### Accent Characters

A lot of special characters — accented letters and the like, which your keyboard doesn't provide directly —
can be "composed" out of two other characters. The recipe:
type the base character, press Alt - Backspace ,
then press the chosen "modifier" to form the special character.
A few examples follow:

| Description | Description |
| --- | --- |
| ã: A , Alt - Backspace , ~ á: A , Alt - Backspace , ' à: A , Alt - Backspace , \ â: A , Alt - Backspace , ^ å: A , Alt - Backspace , O æ: A , Alt - Backspace , E ª: A , Alt - Backspace , - ë: E , Alt - Backspace , " ç: C , Alt - Backspace , , ¢: C , Alt - Backspace , / | ø: O , Alt - Backspace , / §: S , Alt - Backspace , S †: / , Alt - Backspace , - ‡: / , Alt - Backspace , = ©: O , Alt - Backspace , C ®: O , Alt - Backspace , R ™: T , Alt - Backspace , M ½: 1 , Alt - Backspace , 2 ÷: - , Alt - Backspace , : ±: - , Alt - Backspace , + |

### Converting to a Mesh or Curve

Over in Object Mode, a text object can be turned into a mesh or a curve — see Convert.

Tip

Because the resulting topology tends to be a little messy,
running a Limited Dissolve deletion or applying a
Remesh modifier
at a low threshold can help tidy up your mesh.

### Assigning Materials

Reference

Mode :

Edit

Panel :

Properties ‣ Materials

Giving individual characters their own Material index lets you put different materials
on different characters.

Assign those indices as you type, or do it afterward by selecting blocks of text and
hitting the Assign button in the Materials panel.

Red Green Blue text example.

[Related references](INDEX.md).
