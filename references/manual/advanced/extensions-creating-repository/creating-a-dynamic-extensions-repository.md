# Creating a Dynamic Extensions Repository

## Creating a Dynamic Extensions Repository

A dynamic extensions repository serves a smaller JSON file holding only the latest version of the extensions compatible with the query parameters; it's only relevant when a repository holds multiple versions of multiple extensions, and for small or personal repositories a static repository is simpler and recommended. Listing: set one up by following the static-repository steps, since the format and listing are identical. Query parameters: when fetching the listing, Blender passes "platform" and "blender_version" so only compatible extensions are listed, sent as query-URL parameters — the base URL `https://extensions.blender.org/api/v1/extensions/` becomes, for example, `https://extensions.blender.org/api/v1/extensions/?blender_version=4.2.0&platform=linux-x64`. Access token: a repository may require authentication, so the user can give it an access token that Blender sends in an Authorization header:
```text
curl -i https://extensions.blender.org/api/v1/extensions/ \
-H "Accept: application/json" \
-H "Authorization: Bearer abc29832befb92983423abcaef93001"
```

[Related references](INDEX.md).
