# bpy.types.SceneEEVEE: bokeh_max_size, bokeh_neighbor_max, bokeh_overblur, bokeh_threshold

bokeh_max_size

Largest the depth-of-field bokeh shape may grow; smaller is faster (in [0, 2000], default 100.0)

Type :

float
bokeh_neighbor_max

Upper brightness limit weighed when discarding bokeh sprites by their neighborhood; smaller is faster (in [0, 100000], default 10.0)

Type :

float
bokeh_overblur

Blur each jittered sample to cut down under-sampling artifacts (in [0, 100], default 5.0)

Type :

float
bokeh_threshold

Brightness cutoff above which sprite-based depth of field kicks in (in [0, 100000], default 1.0)

Type :

float

[Related references](INDEX.md).
