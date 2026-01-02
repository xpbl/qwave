<details>
<summary><h2>Authentication</h2></summary>

<h3><code>POST /auth/register</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{"username": "string", "password": "string"}</td></tr>
    <tr><td>Response</td><td>{"user_id": int, "username": "string", "created_at": "timestamp"}</td></tr>
    <tr><td>Actions </td><td>Hash password (bcrypt), add db entry, return info (not session)</td></tr>
</tbody></table>

<h3><code>POST /auth/login</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{"username": "string", "password": "string"}</td></tr>
    <tr><td>Response</td><td>{"token": "uuid", "user_id": int, "expires_at": "timestamp"}</td></tr>
    <tr><td>Actions </td><td>Verify hash, generate token, create 30d db entry, return token</td></tr>
</tbody></table>

<h3><code>POST /auth/logout</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Token in header</td></tr>
    <tr><td>Response</td><td>{"message": "message"}</td></tr>
    <tr><td>Actions </td><td>Delete token from db</td></tr>
</tbody></table>

<h3><code>GET /auth/me</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Response</td><td>{"user_id": int, "username": "string", "created_at": "timestamp"}</td></tr>
    <tr><td>Actions </td><td>Lookup token in db</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Tracks</h2></summary>

<h3><code>GET /tracks</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Params  </td><td>artist_id (int), album_id (int), genre_id (int), added_by (int), date_from (ISO), date_to (ISO), limit (int, default 100), offset (int, default 0)</td></tr>
    <tr><td>Response</td><td>{"tracks": [{"id": int, "title": "string", "duration": intm "artists": [{"id": int, "name": "string", "is_primary": bool}], "album": {"id": int, "title": "string"} or null, "added_date": "timestamp"}], "total": int}</td></tr>
    <tr><td>Actions </td><td>Query and filter db, join artist and album tables, return results. use /search for specific songs</td></tr>
</tbody></table>

<h3><code>GET /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Response</td><td>{"id": int, "title": "string", "duration": int, "track_number": int or null, "artists": [{"id": int, "name": "string", "is_primary": bool}], "album": {"id": int, "title": "string", "release_date": "date"} or null, "genres": [{"id": int, "name": "string"}], "lyrics": "string" or null, "added_date": "timestamp", "added_by": {"id": int, "username": "string"}}</td></tr>
    <tr><td>Actions </td><td>query db for track</td></tr>
</tbody></table>

<h3><code>POST /tracks/upload</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Body    </td><td>Audio file, max 200MB</td></tr>
    <tr><td>Response</td><td>{"job_id": int, "Track_id": int, "status": "pending"}</td></tr>
    <tr><td>Actions </td><td>Validate file type and size, save to temp, extract metadata (`mutagen`), search MusicBrainz, create track record and file paths, create job record, return job ID</td></tr>
</tbody></table>

<h3><code>PATCH /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Body    </td><td>all optional fields like {"title": "string"} to update</td></tr>
    <tr><td>Response</td><td>(full track object as in GET /tracks/{id})</td></tr>
    <tr><td>Actions </td><td>patch it lmao</td></tr>
</tbody></table>

<h3><code>DELETE /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Uploader</td></tr>
    <tr><td>Response</td><td>{"message": "status", "id": int}</td></tr>
    <tr><td>Actions </td><td>delete both files and all related db records, delete related jobs</td></tr>
</tbody></table>

<h3><code>GET /tracks/{id}/artists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Response</td><td>{"artists": [{"id": int, "name": "string", "is_primary": bool}]}</td></tr>
    <tr><td>Actions </td><td>query db</td></tr>
</tbody></table>

<h3><code>POST /tracks/{id}/artists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Body    </td><td>{"artist_id": int, "is_primary": bool}</td></tr>
    <tr><td>Response</td><td>{"message": "artist added", "track_id": int, "artist": {"id": int, "name": "string"}}</td></tr>
    <tr><td>Actions </td><td>add entry</td></tr>
</tbody></table>

<h3><code>DELETE /tracks/{id}/artists/{artist_id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Response</td><td>{"message": "status"}</td></tr>
    <tr><td>Actions </td><td>delete entry from track_artsts junction table</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Albums</h2></summary>

<h3><code>GET /albums</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Params  </td><td>artist_id (int), year (int), limit (int), offset (int)</td></tr>
    <tr><td>Response</td><td>{"albums": [{"id": int, "title": "string", "release_date": "date" or null, "album_artist": {"id": int, "name": "string"} or null, "track_count": int}], "total": int}</td></tr>
    <tr><td>Actions </td><td>query db</td></tr>
</tbody></table>

<h3><code>GET /albums/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Response</td><td>{"id": int, "title": "string", "release_date": "date" or null, "album_artist": {"id": "name": "string"} or null, "tracks": [{"id": int, "title": "string", "track_number": int, "duration": int, "artists": [...]}]}</td></tr>
    <tr><td>Actions </td><td>query db</td></tr>
</tbody></table>

<h3><code>PATCH /albums/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>Yes</td></tr>
    <tr><td>Body    </td><td>{"title": "string", "release_date": "date"} (optional)</td></tr>
    <tr><td>Response</td><td>{"id": int, "updated_fields": ["title", ...], "album": {...album object...}}</td></tr>
    <tr><td>Actions </td><td>update db</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Artists</h2></summary>

<h3><code>GET /artists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /artists/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /artists/{id}/tracks</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /artists/{id}/albums</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Genres</h2></summary>

<h3><code>GET /genres</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /genres</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /genres/{id}/tracks</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /tracks/{id}/genres</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>DELETE /tracks/{id}/genres/{genre_id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Playlists</h2></summary>

<h3><code>GET /playlists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /playlists/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /playlists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>PATCH /playlists/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>DELETE /playlists/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /playlists/id/{tracks}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>DELETE /playlists/{id}/tracks/{track_id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>PUT /playlists/{id}/reorder</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Search</h2></summary>

<h3><code>GET /search</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Streaming</h2></summary>

<h3><code>GET /stream/{track_id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Jobs</h2></summary>

<h3><code>GET /jobs/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /jobs</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>DELETE /jobs/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Import Review</h2></summary>

<h3><code>GET /import/pending</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>PATCH /import/pending/{track_id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Server Details</h2></summary>

<h3><code>GET /server/info</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /server/config</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Params  </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>