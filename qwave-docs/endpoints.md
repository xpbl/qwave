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
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /auth/logout</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /auth/me</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>
</details>

<details>
<summary><h2>Tracks</h2></summary>

<h3><code>GET /tracks</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>POST /tracks/upload</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>PATCH /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>DELETE /tracks/{id}</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>GET /tracks/{id}/artists</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

<h3><code>t</code></h3>
<table><tbody>
    <tr><td>Auth    </td><td>None</td></tr>
    <tr><td>Body    </td><td>{}</td></tr>
    <tr><td>Response</td><td>{}</td></tr>
    <tr><td>Actions </td><td>a</td></tr>
</tbody></table>

</details>