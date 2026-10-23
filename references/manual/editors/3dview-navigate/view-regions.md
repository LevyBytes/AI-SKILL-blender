# View Regions

## View Regions

Clipping Region — Reference: Mode: All modes; Menu: View ‣ View Regions ‣ Clipping Region…; Shortcut: Alt-B. Lets you carve out a clipping region that restricts the 3D Viewport's display to a slice of 3D space, which helps when wrangling complex models and scenes. After activating it, drag a rectangle with the mouse; that becomes a four-plane clipping volume — a right-angled parallelepiped of infinite length under an orthographic view, or a rectangular-based pyramid of infinite height under perspective. With clipping on, only what's inside the volume shows, and tools like paint, sculpt, selection, and transform snapping ignore geometry beyond the bounds too. Press Alt-B again to clear it.

Example: the region/volume clipping illustration shows the tool used on a cube. Start it with Alt-B to get a dashed cross-hair cursor, then LMB-drag a rectangular region; clipping now applies to that slice of 3D space. Rotate with MMB and you'll see only what lies inside the clipping volume, with every editing tool still working but only within that volume. The dark gray area is the clipping volume itself, and once you deactivate it with another Alt-B, all of 3D space returns.

Render Region - Reference: Mode: All modes; Menu: View ‣ View Regions ‣ Render Region…, View ‣ View Regions ‣ Clear Render Region; Shortcut: Mark: Ctrl-B, Clear: Ctrl-Alt-B. Confines rendering to a rectangular 2D area. When you're tweaking just a small part of a scene, putting the whole viewport in Rendered shading or making full-frame renders wastes effort, so this saves time. You can define Render Regions in two contexts: set one while in Camera View and it applies both to the viewport and to the final render (to suspend it without clearing, use the Output tab of the Properties editor); set one outside Camera View and it applies to the viewport only (suspend it without clearing via the Sidebar). Both Render Regions can coexist. Note: under Cycles render regions affect the viewport, but under EEVEE they don't; either way they always affect the final render. See also Zoom Region.

[Related references](INDEX.md).
