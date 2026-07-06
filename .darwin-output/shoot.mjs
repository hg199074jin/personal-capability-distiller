// Darwin Skill 高清截图脚本（Windows 兼容版）
// 用法: node shoot.mjs <html路径> <png输出路径>
import { chromium } from 'playwright';

const [, , htmlPath, outputPath] = process.argv;

async function run() {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: 960, height: 1400 },
    deviceScaleFactor: 2,
  });
  const page = await ctx.newPage();
  // 用 file:// 前缀转本地路径
  const url = htmlPath.startsWith('file:') ? htmlPath : `file:///${htmlPath.replace(/\\/g, '/')}`;
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(2000);
  const card = page.locator('.card');
  await card.screenshot({ path: outputPath, type: 'png' });
  const box = await card.boundingBox();
  console.log(`[ok] saved ${outputPath}`);
  console.log(`[info] card CSS: ${Math.round(box.width)}x${Math.round(box.height)}`);
  console.log(`[info] PNG: ${Math.round(box.width * 2)}x${Math.round(box.height * 2)} (2x)`);
  await browser.close();
}

run().catch((e) => {
  console.error('[fail]', e.message);
  process.exit(1);
});
