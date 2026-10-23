# Introduction

Python is an interpreted, interactive, object-oriented language featuring modules, exceptions, dynamic typing, high-level built-in data structures, and classes, pairing considerable power with clear syntax. Scripts are a flexible way to extend Blender — most areas can be scripted, including animation, rendering, import/export, object creation, and automating repetitive work — and they reach Blender through its tightly integrated API. General information, useful while scripting: Python.org (about Python), the Blender Python API (the official reference to consult while writing), and the API Introduction (a short, example-filled starter); for distribution, Creating Add-ons (encapsulating and sharing scripts) and Creating Extensions (sharing on the Blender Extensions platform). Getting started: the manual's Text Editor, Python Console, and Info Editor pages take you from basics to advanced scripting, and external resources include the Python API Quickstart, "CG Cookie: Blender 2.8 Python Scripting Superpowers for Non-Programmers," "Olav3D: 3D Programming for Beginners Using Python," and the Blender Artists Python Support forum. Extending Blender — add-ons: scripts that give Blender extra functionality, enabled in the Preferences; beyond the executable, many people have written hundreds of them, with officially supported ones bundled with Blender and others provided through Blender Extensions (not part of official releases, often reliable and useful but not yet guaranteed stable) — see the Add-ons docs for those included with Blender. Scripts: besides add-ons, other script types extend Blender — Modules (utility libraries imported by other scripts), Presets (settings for tools and key configurations), Startup (imported when Blender starts; they define most of the UI and some core operators), and Custom Scripts (typically run once from the Text Editor). Saving your own scripts — file location: scripts load from the scripts folder of the local, system, and user paths, and you can add another search path in Preferences ‣ File Paths; installation: add-ons install conveniently through Preferences via the Install… button and selecting the .zip.

Animation is making an object move or change shape over time, which can happen several ways: moving the whole object (changing its position, orientation, or size over time), deforming it (animating its vertices or control points), or inherited animation (moving based on another object such as a parent, hook, or armature). This chapter covers the first two, whose basics also underpin later chapters, and animation is usually done with keyframes (see also Physical Simulation and Motion Tracking). State colors: properties take different colors and menu items per state — Gray (not animated), Yellow (keyframed on the current frame), Green (keyframed on a different frame), Orange (changed from the keyframed value), and Purple (driven) — though the changed-value highlight currently doesn't work with NLA. Rigging is the general term for adding controls to objects, typically for animation, often using one or more of: Armatures (flexible joints for mesh objects, common for skeletal animation), Constraints (to control which motions make sense and add rig functionality), Object Modifiers (several help control mesh deformation), Shape Keys (to control target shapes such as facial expressions), and Drivers (so the rig controls many values at once and updates some properties automatically from changes elsewhere). Rigging can be as advanced as the project needs — a rig effectively defines a UI for the animator without exposing the underlying mechanisms. Examples: an armature is often paired with a modifier to deform a mesh for character animation; and a camera rig can replace animating the camera directly, simulating real-world rigs (a boom arm on a rotating pedestal, with effects like camera jitter). This chapter is a reference and pairs well with resources such as Nathan Vegdahl's character-rigging introduction, Humane Rigging.

A keyframe is a time marker storing a property's value — for example, that a cube's horizontal position is 3 m on frame 1. Its purpose is interpolated animation: add another key on frame 10 putting the cube at 20 m, and Blender computes the cube's position for every frame between, per the chosen interpolation (Linear, Bézier, Quadratic, etc.). An overview of existing keyframes is in the Dope Sheet. Visualization: in the 3D Viewport, when the current frame is a keyframe for the active object, that object's name (upper-left) turns yellow. Interpolation: keyframe interpolation is shown and controlled by animation curves (F-Curves), viewable and editable in the Graph Editor, where the curve's X axis is time and Y is the property value, keyframes define points, and interpolation is set by extra parameters. The Interpolation Mode is the main per-keyframe setting for how the curve runs from that key to the next, with fixed-shape modes (Constant, Linear, Quadratic, etc.) and a free-form Bézier mode. Extrapolation sets how the curve extends before the first and after the last key, mainly Constant and Linear, and it can also loop. Bézier interpolation uses handles with a type and position: Free and Aligned handles are positioned manually in the Graph editor, while Vector, Automatic, and Auto Clamped handles are computed from keyframe values; Interpolation, Extrapolation, and Handle Type can also be changed in the Dope Sheet. The three automatic handle types are computed per the per-curve Auto Handle Smoothing setting: None resembles most software, considering only the immediately adjacent keys, while Continuous Acceleration considers the whole curve's shape for smoother out-of-the-box results, though changes to one key then affect a larger section and Automatic handles tend to overshoot more. Keyframe types: keyframes can be colored to distinguish regular keys from animation events or states — Keyframe (white/yellow diamond, normal), Breakdown (small cyan diamond, e.g. transitions between key poses), Moving Hold (dark gray/orange diamond, a key adding slight motion around a holding pose, with a bar shown between them in the Dope Sheet), Extreme (big pink diamond, an "extreme" state or other use), Jitter (tiny green diamond, a filler or baked key for keying on ones or other use), and Generated (dark diamond, made by a tool such as Copy Global Transform: Fix to Camera — this type tells Blender and add-ons it's safe to remove and regenerate, so mark hand-made animation with it carefully). Handles & interpolation display: the Dope Sheet can show a keyframe's Bézier handle type and flag segments with non-Bézier interpolation, for basic interpolation editing without the Graph Editor — the icon shape is the handle type: Circle (Auto Clamped, default), Circle With Dot (Automatic), Square (Vector), Clipped Diamond (Aligned), Diamond (Free); when a keyframe's handles differ, or for summary rows over multiple curves, the icon furthest down that list is used (so a circle on a grouped row guarantees no grouped channel has a non-auto key). Horizontal green lines mark non-Bézier interpolation (dimmed in summary rows where not all grouped channels share it), and this display can be turned off via the Dope Sheet's View menu "Show Handles and Interpolation".

The Dope Sheet gives a bird's-eye view of the keyframes in the scene. It draws on classical hand-drawn animation, where animators used a chart marking exactly when each drawing, sound, and camera move happens and for how long. You can also bring up Playback Controls to drive the playhead.

Dope Sheet Modes: the editor has several modes, picked from a header dropdown. The default Dope Sheet mode surveys most kinds of animatable data; for others, such as masks, you switch to a more specific mode. They are:
Dope Sheet, Action Editor, Shape Key Editor, Grease Pencil, Mask, and Cache File (originally intended to display baked animation data from Alembic files, though it was never implemented).

Main Region: the Dope Sheet Editor presents a stack of channels (animatable properties), and for each channel a row of keyframes spread along the time axis. Keyframes vary in color and shape:
  Gray: unselected.
  Yellow: selected.
  Other colors: a custom keyframe tag you set (Key ‣ Keyframe Type).
  Diamond: Free Keyframe Handle (Key ‣ Handle Type).
  Round: Auto-Clamped Keyframe Handle.
  Circle: Automatic Keyframe Handle.
  Square: Vector Keyframe Handle.
  Rhombus: Aligned Keyframe Handle.
  Gray bar between keys: a held key, meaning the pair of keyframes match.
  Green line between keys: that curve segment runs on custom interpolation (Key ‣ Interpolation Mode).
  Upwards arrow: a local maximum in the curve (shown when View ‣ Show Curve Extremes is on).
  Downwards arrow: a local minimum in the curve.
Click to select a keyframe and drag to move it; the Select and Key menus hold more options.

Channels Region: sits down the left side of time-based editors such as the Dope Sheet and the Graph Editor. It lists a tree of items (objects, bones…) and their animated properties, the latter also called "channels," each with an F-curve that describes how its value changes over time.

The rows carry color codes:
Dark blue: scenes, objects.
Light blue: actions, shape keys, and the like.
Green: channel groups.
Gray: channels.
Search (Ctrl-F): filters the channels by part of their name; click Invert to instead show channels that lack the search text.

Channels: the headers hold these toggle buttons:
/ Pin — keeps the row and its children visible even after you select a different object.
/ Hide — hides the keyframes and curve tied to the channel.
/ Modifiers — switches off the curve's modifiers.
/ Mute — switches off the curve, so the animation acts as if it isn't there.
/ Lock (Tab) — stops the curve from being edited.
Note: this works in the Nonlinear Animation Editor too, but there it only locks the strips, not the underlying F-curves.

Selection:
Select single header: LMB.
Add/Remove single header: Ctrl-LMB.
Select range: Shift-LMB.
Select All: A.
Deselect All: Alt-A, or double-tap A.
Box Select: drag LMB.
Box Add: drag Shift-LMB.
Box Remove: drag Ctrl-LMB.
Select all keyframes in the channel: double-click LMB on its header.

Editing:
Rename (anything but a channel): double-click LMB.
Delete selected: X or Delete.
Lock selected: Tab.
Sliders: turning on View ‣ Show Sliders adds a value slider beside each channel; changing one alters the curve's value at the current frame, inserting a keyframe if none exists yet.

The Outliner shows the blend-file's content as a tree, which you can use to survey the scene's data; pick and unpick objects; render objects unselectable or hidden in the 3D Viewport; keep objects out of the render; duplicate and delete objects; and manage parent/child relationships and collections. Items with a left-hand arrow expand: LMB it to expand one, drag LMB to expand several, or Shift-LMB to expand recursively.

[Related references](INDEX.md).
