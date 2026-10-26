const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const out = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage();
  for (const [f, land] of [['01_Guia_da_Aluna',false],['02_Cronograma_26_Semanas',true],['03_Checklists',false]]) {
    await p.goto('file://' + path.resolve(f + '.html'), { waitUntil: 'networkidle' });
    await p.pdf({ path: path.join(out, f + '.pdf'), preferCSSPageSize: true, printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: '<div style="font-size:7px;width:100%;text-align:center;color:#888;font-family:Arial">Mentoria · Patrícia de Miranda Oliveira · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
    console.log('pdf', f);
  }
  await b.close();
})();
