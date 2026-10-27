import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
const S = resolve(process.argv[2] || '.');
const b = await chromium.launch();
const p = await b.newPage();
for (const v of ['full','web']) {
  await p.goto(pathToFileURL(join(S, `resume-${v}.html`)).href, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  const fam = await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight+' '+f.style).join(', '));
  console.log(v, 'fonts loaded:', fam);
  await p.pdf({ path: join(S, `resume-${v}.pdf`), format: 'A4', preferCSSPageSize: true, printBackground: true });
}
await b.close();
