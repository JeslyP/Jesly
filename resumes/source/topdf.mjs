import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [,, S] = process.argv;
const b = await chromium.launch();
const p = await b.newPage();
for (const v of ['full','web']) {
  await p.goto(`file://${S}/resume-${v}.html`, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  const fam = await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight+' '+f.style).join(', '));
  console.log(v, 'fonts loaded:', fam);
  await p.pdf({ path: `${S}/resume-${v}.pdf`, format: 'A4', preferCSSPageSize: true, printBackground: true });
}
await b.close();
