import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
const [,, src, out] = process.argv;
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(pathToFileURL(resolve(src)).href, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
await p.pdf({ path: out, format: 'A4', preferCSSPageSize: true, printBackground: true });
await b.close();
