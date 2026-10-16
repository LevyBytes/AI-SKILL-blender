# bpy.types.Depsgraph: debug_relations_graphviz, debug_stats_gnuplot, debug_tag_update, debug_stats

debug_relations_graphviz ( * , filepath = '' )

debug_relations_graphviz

Parameters :

filepath ( str ) – File Name, Optional output path for the graphviz debug file (optional, never None)

Returns :

Dot Graph, Graph in dot format

Return type :

str
debug_stats_gnuplot ( filepath , output_filepath )

debug_stats_gnuplot

Parameters :

- filepath ( str ) – File Name, Output path for the gnuplot debug file (never None)

- output_filepath ( str ) – Output File Name, File name where gnuplot script will save the result (never None)
debug_tag_update ( )

debug_tag_update
debug_stats ( )

Report the number of elements in the Dependency Graph

Returns :

result, (never None)

Return type :

str

[Related references](INDEX.md).
