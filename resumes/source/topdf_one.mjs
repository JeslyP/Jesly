import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [,, src, out] = process.argv;
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`file://${src}`, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
await p.pdf({ path: out, format: 'A4', preferCSSPageSize: true, printBackground: true });
await b.close();
