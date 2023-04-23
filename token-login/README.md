# Copy the token to the clipboard

```
window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getToken !== undefined) {return copy(m.default.getToken())}if (m.getToken !== undefined) {return copy(m.getToken())}}}]); console.log("%cSuccessfully!", "font-size: 50px"); console.log(`%cYou now have your token successfully in the clipboard`, "font-size: 16px")
```

# Login with token

```js
function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 200);
}


token = "TOKEN HERE" // Paste the copied token into the string;
login(token)
```
