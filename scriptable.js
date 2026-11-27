const request = new Request("https://raw.githubusercontent.com/ragingfromyt/Flappy/main/index.html?v=" + Date.now());
const html = await request.loadString();
const web = new WebView();
await web.loadHTML(html);
await web.present(true);
Script.complete();
