# bpy.types.PreferencesView: pie_animation_timeout, pie_initial_timeout, pie_menu_confirm, pie_menu_radius, pie_menu_threshold, pie_tap_timeout

pie_animation_timeout 

How long it takes to animate the pie fully open (measured in hundredths of a second) (in [0, 1000], default 6)

Type :

int
pie_initial_timeout 

Span during which the pie keeps the starting mouse position as its center (measured in hundredths of a second) (in [0, 1000], default 0)

Type :

int
pie_menu_confirm 

Travel distance past which a choice is committed (set to zero to turn off) (in [0, 1000], default 0)

Type :

int
pie_menu_radius 

Size of the pie menu, in pixels (in [0, 1000], default 100)

Type :

int
pie_menu_threshold 

How far from the center the pointer must move before a choice can register (in [0, 1000], default 12)

Type :

int
pie_tap_timeout 

Holding the pie button past this duration dismisses the menu when released (measured in hundredths of a second) (in [0, 1000], default 20)

Type :

int

[Related references](INDEX.md).
