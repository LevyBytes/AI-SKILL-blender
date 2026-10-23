# Cache

## Cache

The Cache keeps preview frames in memory so they display far faster during playback instead of being re-rendered each frame, which is especially useful for keeping things smooth while editing or scrubbing. The overall cache memory limit is set in the Preferences' System tab. See also: which frames are cached can be shown by enabling Show Cache in the Timeline overlay settings.

Cache Settings - Reference: Panel: Sidebar ‣ Cache ‣ Cache Settings. This panel configures how and when image data is cached during editing; the settings apply globally to every strip in the Video Sequence Editor.
Prefetch Frames: when on, Blender prefetches and caches frames ahead of the current one in the background, which can smooth playback. Note: prefetching isn't currently supported for Scene strips.
Cache:
Raw: caches raw image data right after it's read from disk, speeding up tweaks to strip parameters like color correction at the cost of more memory.
Final: caches each frame's final composited image, giving faster playback of fully processed strips.
Display: visual cues in the Timeline marking cached frames.
Cache:
Raw: draws a red bar in the Timeline beneath frames cached in their raw state.
Final: draws a blue bar along the Timeline's top wherever frames are cached in final composited form.
A readout at the panel's bottom gives live cache statistics: Current Cache Size (the total memory the cache system is using now), Raw (memory used by the raw image cache), and Final (memory used by the final rendered-frame cache).

[Related references](INDEX.md).
