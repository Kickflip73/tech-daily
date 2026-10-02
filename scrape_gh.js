JSON.stringify(
  Array.from(document.querySelectorAll('article.Box-row')).map(el => {
    const h1 = el.querySelector('h2 a');
    const name = h1 ? h1.textContent.trim().replace(/\s+/g, '') : null;
    const url = h1 ? 'https://github.com' + h1.getAttribute('href') : null;
    const desc = el.querySelector('p');
    const description = desc ? desc.textContent.trim() : null;
    const lang = el.querySelector('[itemprop="programmingLanguage"]');
    const language = lang ? lang.textContent.trim() : null;
    const starsMatch = el.textContent.match(/(\d[\d,]*)\s*stars today/);
    const starsToday = starsMatch ? parseInt(starsMatch[1].replace(/,/g, '')) : null;
    const totalMatch = el.textContent.match(/(\d[\d,]*)\s*stars\s*total/);
    const totalStars = totalMatch ? parseInt(totalMatch[1].replace(/,/g, '')) : null;
    return { name, url, description, language, stars_today: starsToday, total_stars: totalStars };
  })
)
