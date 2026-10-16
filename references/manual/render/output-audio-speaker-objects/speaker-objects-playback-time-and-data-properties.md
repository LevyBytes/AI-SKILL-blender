# Speaker Objects: Playback Time, Data Properties, Sound, Distance

## Speaker Objects

### Speaker Objects 

Speaker objects are designed to emit audio within the 3D Viewport. They enable spatial audio playback, making them ideal for animated projects and real-time environments. Speaker configuration is managed through the Properties editor.

Speaker object. 

### Playback Time 

Unlike other objects, speaker timing is not set directly via properties. The NLA editor manages speaker playback instead, utilizing Sound Strips:

- Sound strips in the NLA editor govern when playback begins.

- When a new speaker is created, a sound strip is automatically assigned at the current frame.

- Separate sound strips allow the same speaker to play at different times.

- Audio plays for the full file duration regardless of the sound strip length.

### Data Properties 

Reference

Panel :

Properties editor ‣ Data

Speaker properties. 

### Sound 

Open
The Data-Block Menu for importing audio files. Two audio-loading properties are available:

Cache
Converts sound to memory storage for quicker playback. Best for brief, frequently-used sounds but unsuitable for lengthy audio.

Mono
Restricts audio to a single channel. Necessary for spatial audio and directional effects since multi-channel files assume pre-mixed spatial information.

Mute
Toggles audio output off.

Volume
Adjusts speaker loudness.

Pitch
Changes playback speed and pitch. Increasing values accelerates playback and raises pitch; decreasing values slow it down and lower pitch.

### Distance 

Distance-dependent attenuation manages how speaker volume decays with listener distance. This emulates natural sound behavior, enhancing spatial audio realism by creating louder nearby sounds and quieter distant ones.

These options fine-tune volume falloff over distance:

Volume Min, Max
Sets minimum and maximum volume limits based on distance. Volume will not fall below or rise above these thresholds regardless of listener proximity.

Attenuation
Determines how quickly volume drops with increasing distance. Behavior depends on the scene's Distance Model.

Max Distance
The farthest point where attenuation is computed. Beyond this distance, volume stays constant.

Distance Reference
The distance at which volume reaches full (1.0). Should correspond to the recording distance for accurate playback.

[Related references](INDEX.md).
