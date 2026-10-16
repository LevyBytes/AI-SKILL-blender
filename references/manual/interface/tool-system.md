# Tool System

## Tool System

### Tool System

The Toolbar is where you get at tools.

What follows is a broad introduction to tools; each individual tool keeps its own documentation.

Only one tool can be active per Workspace and mode, and it's remembered: pick Extrude in Edit Mode, hop over to Object Mode (where no Extrude tool exists) and back again, and Extrude is still waiting.

LMB drives most tools, though a few also carry modifier keys (shown in the Status Bar while the tool is in use). All of this is customizable in the Keymap Preferences.

A handful of tools (Shear and Spin, for instance) define gizmos to help steer them.

### Toolbar
Reference

Shortcut :

T

Expanded tool group.

Buttons for the assorted tools fill the Toolbar. A small triangle in a button's bottom right corner marks a tool group, which opens if you hold LMB on it briefly (or drag LMB to pop it open at once).

Hover briefly over a tool and its name appears; linger and the full tooltip shows.

Widen the Toolbar and the icons spread into two columns. Stretch it further and each icon gains its text.

### Pop-Up Toolbar
Reference

Shortcut :

Shift - Spacebar

Hit Shift - Spacebar and a compact toolbar pops up right under your cursor for quicker reach. Selection shortcuts for the tools sit on the right.

You can instead bind this to Spacebar in the Keymap Preferences. Then Spacebar works like a modifier key (much as holding Ctrl or Shift does). For instance, Spacebar T gives Transform, Spacebar D gives Annotate, Spacebar M gives Measure, and so on. See Spacebar Action.

### Quick Favorites
Reference

Shortcut :

Q

Your go-to tools collect in the Quick Favorites menu. Through its context menu, any tool or menu item can be added to this pop-up.

### Changing Tools
With Alt Click Tool Prompt switched on in the Keymap Preferences, a tap of Alt brings up a tool prompt in the Status Bar. Press a key to pick the matching tool, or tap Alt once more to back out.

### Fallback Tool
Selected by default — sitting at the top of the Toolbar — is the fallback tool. Change it by holding LMB on the toolbar button or pressing Alt - W for a pie menu.

### Cycling Tools
Bind a key to a tool that belongs to a group, then switch on the Cycle option in the keymap editor. Each further press then steps through the tools in that group.

The selection tools in the 3D Viewport ship with this on by default, for instance: press W and it cycles between Select Box, Select Circle and so on.

### Properties
Settings of their own can belong to tools, reachable from several spots:

- The Tool ‣ Active Tool panel in the Sidebar N .

- The Active Tool tab in the Properties editor.

- The Tool Settings region below the area header.

[Related references](INDEX.md).
