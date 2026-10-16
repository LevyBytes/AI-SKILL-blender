# Introduction

Introduction to UV Unwrapping

Begin unwrapping when only minor geometry adjustments remain. Adding or subdividing faces after unwrapping is possible, but may require additional mapping or editing. You can use the UV texture image to guide further geometry changes.

Understanding UVs

Each UV map point corresponds to a mesh vertex. Lines between UVs correspond to mesh edges. Each UV face corresponds to a mesh face. UV mapping projects your 3D model's surface onto a 2D image.

A mesh face can have multiple UV textures, each with its own image. When you unwrap a face to a UV texture, the face gains four UV coordinates defining the image mapping. U and V axes distinguish these from 3D XYZ coordinates, hence "UV unwrapping". These coordinates work for rendering and real-time viewport display.

Each mesh face links to a potentially different image. UV coordinates control how that image maps to the face. A 3D Viewport requires Face Select mode to assign images or modify UV coordinates of the active mesh. This allows a face to participate in multiple UV textures — for example, a character's hairline face might use both facial and scalp/hair textures.

Getting Started

The default UV Editing workspace setup divides the screen between the UV Editor and 3D Viewport.

By default, meshes lack UVs. You must first map the faces, then edit them. Unwrapping happens in Edit Mode within the 3D Viewport, creating one or more UV Islands in the UV Editor.

Choose the UV Editing workspace from the top-screen selection list.

Enter Edit Mode (all unwrapping occurs in Edit Mode). You can work in vertex, face, or edge selection mode.

General Workflow

Different models may require different unwrapping approaches, but this is the general process:

Mark Seams if necessary.

Select mesh faces in the 3D Viewport.

Pick a UV mapping method from UV ‣ Unwrap or the 3D Viewport UV menu.

Adjust unwrap settings in the Adjust Last Operation panel.

Add a test image to check for distortion. See Applying Images to UVs.

Refine UVs in the UV Editor. See Editing UVs.

[Related references](INDEX.md).
