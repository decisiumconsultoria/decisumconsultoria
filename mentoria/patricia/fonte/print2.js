const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve('Guia_da_Aluna.html'), { waitUntil: 'networkidle' });
  await p.pdf({ path: process.argv[2], preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7px;width:100%;text-align:center;color:#888;font-family:Arial">Guia da Aluna · Patrícia de Miranda Oliveira · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  await b.close(); })();
