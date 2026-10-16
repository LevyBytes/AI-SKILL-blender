# Blender release history 2011 2024

Blender 2.6x to 2.7x – Improvements & Stabilizing.

- 2.60 – October 2011: UI internationalization, gains in the animation system and the GE, vertex weight group modifiers, 3D audio and video, and bug fixes.
- 2.61 – December 2011: the Cycles renderer landed in trunk; a camera tracker; dynamic paint for altering textures via mesh contact/proximity; the Ocean modifier for ocean and foam; new add-ons; bug fixes; and more Python API extensions.
- 2.62 – February 2012: the Carve library for better Boolean operations, object-tracking support, the Remesh modifier, many GE gains, improved matrices and vectors in the Python API, new add-ons, and many bug fixes.
- 2.63 – April 2012: Bmesh merged into trunk with full n-sided polygon support, sculpt hiding, a panoramic Cycles camera, mirror-ball environment textures and float-precision textures, render-layer mask layers, ambient occlusion, and viewport display of background images and render layers; new import/export add-ons; and 150 bug fixes.
- 2.64 – October 2012: a mask editor, an improved motion tracker, OpenColorIO, Cycles gains, Sequencer gains, better mesh tools (Inset and Bevel improved), new keying nodes, sculpt masking, COLLADA gains, a new Skin modifier, a new compositing-nodes backend, and many bug fixes.
- 2.65 – December 2012: fire and smoke gains, an anisotropic Cycles shader, modifier gains, rounding added to the Bevel tool, new add-ons, and 200+ bug fixes.
- 2.66 – February 2013: dynamic topology, rigid-body simulation, UI and usability gains (retina-display support included), Cycles hair support, per-vertex beveling in the Bevel tool, the new Mesh Cache and UV Warp modifiers, and a new SPH particle fluid solver; 250+ bug fixes.
- 2.67 – May 2013: Freestyle, paint-system gains, Cycles subsurface scattering, the Ceres library in the motion tracker, custom Python nodes, new mesh-modeling tools, better UTF-8 text support and Text-editor gains, 3D-printing add-ons, and 260+ bug fixes.
- 2.68 – July 2013: new and improved modeling tools, three new Cycles nodes, big motion-tracker gains, Python scripts and drivers disabled by default on file load for security, and 280+ bug fixes.
- 2.69 – October 2013: still more modeling tools, Cycles gains across many areas, plane tracking in the motion tracker, better FBX import/export, and 270+ bug fixes.
- 2.70 – March 2014: basic CPU volumetrics in Cycles, more motion-tracker gains, two new modeling modifiers, some UI-consistency gains, and 560+ bug fixes.
- 2.71 – June 2014: deformation motion blur and fire/smoke in Cycles, draggable UI pop-ups, sculpt-mode performance work, new animation interpolation types, many GE gains, and 400+ bug fixes.
- 2.72 – October 2014: GPU volume and SSS in Cycles, pie menus, much-improved tooltips, the Intersection modeling tool, a new Sun Beam Compositor node, Freestyle working with Cycles, a better texture-painting workflow, and 220+ bug fixes.
- 2.73 – January 2015: better Cycles volumetrics, a major Grease Pencil upgrade, Input Method Editors (IMEs) on Windows, and general gains to painting, Freestyle, the Sequencer, and add-ons.
- 2.74 – March 2015: custom-normal support, viewport compositing, and hair-dynamics gains.
- 2.75 – July 2015: an integrated stereo/multi-view pipeline, the Smooth Corrective modifier, and a new developmental dependency graph.
- 2.76 – November 2015: Pixar OpenSubdiv support, a Viewport and File Browser speed boost, node auto-offset, and a Sequencer text-effect strip.
- 2.77 – March 2016: OpenVDB caching for smoke/volumetric sims, better Cycles subsurface scattering, Grease Pencil stroke sculpting and workflow gains, and reworked library handling for missing/deleted data-blocks.
- 2.78 – September 2016: Cycles spherical-stereo images for VR, Grease Pencil behaving more like other 2D drawing software, Alembic import/export, and Bendy Bones gains for simpler rigging.
- 2.79 – September 2017: new Cycles features (Denoising, Shadow Catcher, the new Principled shader), more Grease Pencil and Alembic gains, and application-template support.

Blender 2.8 – Revamped UI
- 2.80 – July 2019: a fully redesigned UI for easier navigation; an improved viewport, gizmos, and tools; EEVEE, a new physically based real-time render engine; a big Grease Pencil overhaul, now a full 2D drawing and animation system; collections (replacing the old layers) as a powerful way to organize objects; plus gains to Cycles, Modeling, Animation, Import/Export, and the Dependency Graph.
- 2.81 – November 2019: revamped sculpting tools, Cycles OptiX-accelerated rendering, denoising, many EEVEE gains, library overrides, UI gains, and much more.
- 2.82 – February 2020: UDIM and USD support, Mantaflow for fluid and smoke simulation, AI denoising, Grease Pencil gains, and much more.
- 2.83 LTS – June 2020: 3D-Viewport VR scene inspection, a new Volume object type, Cycles adaptive sampling, Cycles viewport denoising, sculpting gains, and much more; the first LTS release, meant for studios and long-lifecycle projects.

Blender 2.9 – Refining 2.8
- 2.90 – August 2020: an improved sky texture, EEVEE motion blur, sculpting gains, a revamped modifier UI, better modeling tools, and faster Cycles motion blur.
- 2.91 – November 2020: Outliner gains, property search, better mesh Boolean operations, animation curves, Volume-object and display gains, and more refined sculpting tools.
- 2.92 – February 2021: geometry nodes, the primitive Add tool, sculpting gains, Grease Pencil curve editing, Cycles Color Attribute baking, APIC fluid sims, Video Sequencer gains, and much more.
- 2.93 LTS – June 2021: new geometry nodes, sculpting gains, the Grease Pencil Line Art modifier and other gains, an improved EEVEE DOF, a redesigned Cryptomatte workflow, and more; the LTS release for the 2.9 series.

Blender 3.0 – Optimizing Performance
- 3.0 – December 2021: the Asset Browser, Cycles X, EEVEE Attributes, new geometry nodes, an animation update, Grease Pencil Line Art gains, a pose library, Open Image Denoising 2–8× faster, and added AMD-on-Linux support.

- 3.1 – March 2022: major point-cloud gains, Cycles Apple Metal GPU support, GPU subdivision support, larger-image handling in the image editor, big geometry-nodes performance gains, and context-aware geometry-node search.
- 3.2 – June 2022: Cycles light groups, true shadow caustics, volume motion blur, glTF gains, AMD GPU rendering on Linux, painting in sculpt mode, and WebP image support.
- 3.3 LTS – September 2022: a new Hair object, procedural UV nodes, Line Art shadow and contour, Intel GPU rendering via oneAPI, and library-override gains; the first LTS of the 3.0 series.
- 3.4 – December 2022: Cycles path guiding, sculpting auto-masking gains, still more geometry nodes, UV-editing gains, and Wayland support on Linux.
- 3.5 – March 2023: new generative hair assets, vector displacement maps for sculpting, the viewport compositor, and Cycles light trees.
- 3.6 LTS – June 2023: Simulation Nodes added to Geometry Nodes, Cycles hardware ray-tracing for AMD and Intel, UV island packing, a bundled asset pack from Blender Studio and community artists, and a new retopology overlay; the final LTS of the 3.0 series.

Blender 4.0 – A Major Leap For Rendering, Creating Tools, and More
- 4.0 – November 2023: a new Principled BSDF shader with coat and sheen layers, the AgX view transform, Voronoi Texture fractal noise, light linking for selective lighting, running Geometry Nodes as Node Tools, snapping gains including Snap Base, type-to-search for menus and modifier types, the new Inter typeface, a streamlined keymap, bone collections, the Hydra Storm USD renderer, a larger asset library, and alignment to the VFX Reference Platform 2023.
- 4.1 – March 2024: Geometry Nodes baking, the Menu Switch node, OpenImageDenoise GPU acceleration, more real-time viewport-compositor functions, simpler animation-keyframe insertion, hierarchical bone collections, graph-editor click-and-slide, Video Sequencer performance and color-scope gains, alignment to the VFX Reference Platform 2024, and armature and shape-key export to USD.
- 4.2 LTS – July 2024: the next generation of EEVEE with major upgrades to lighting, sun lights, displacement, subsurface, volumetrics, and motion blur; Cycles gains a Ray Portal BSDF and Thin-Film Interference, plus better low-noise soft-volume rendering and blue-noise sampling; the Blender Extensions platform launches; the Khronos PBR Neutral Tone Mapper; sculpting-selection gains; matrix inputs for nodes; Node Tools that can use mouse position and viewport; a Video Sequencer graphical overhaul; more USD export options; and native portable-installation support. The first LTS of the 4.0 series.
- 4.3 – November 2024: light linking and shadow linking in EEVEE, the Metallic BSDF, the Gabor noise texture, EEVEE render passes in the compositor, minimum-stretch (SLIM) UV unwrapping, many Geometry Nodes updates including the For-Each zone, physics nodes, a Grease Pencil engine rewritten for speed and features, 100+ default brushes for painting and sculpting, and UI area docking.

[Related references](INDEX.md).
