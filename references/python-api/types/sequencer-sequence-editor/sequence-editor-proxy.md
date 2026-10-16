# bpy.types.SequenceEditor: proxy_dir, proxy_storage

proxy_dir

(default “”, never None, blend relative // prefix supported)

Type :

str
proxy_storage

Where proxies for this project are kept (default '`PER_STRIP`' )

- `PER_STRIP`
Per Strip – Keep proxies according to each strip's own settings.

- PROJECT
Project – Keep proxies in the project directory.

Type :

Literal[‘`PER_STRIP`’, ‘PROJECT’]

[Related references](INDEX.md).
