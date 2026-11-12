"""Build both static language editions. Python 3, no third-party dependencies."""
from pathlib import Path
from html import escape, unescape
from datetime import date
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'frontend/data/content.json').read_text(encoding='utf-8'))
UPDATED = date.fromisoformat(DATA['updated'])
BASE = 'https://junjiehu-traffic.github.io/junjiehuits/frontend/'
CAST = 'https://www.cast.org.cn/rc2/fwyfz/zgkxqnkjrcpygc/bsszxjh/xgtz/art/2026/art_552cec3bc26248d1a475b98727df804f.html'
UI = {
    'en': {
        'name': 'Junjie Hu', 'other': '胡俊杰', 'title': 'Junjie Hu | Transportation Research · Tsinghua University',
        'about': 'About', 'news': 'News', 'research': 'Research', 'publications': 'Publications', 'experience': 'Experience', 'honors': 'Honors',
        'role': 'Ph.D. Student', 'university': 'Tsinghua University', 'department': 'Department of Civil Engineering',
        'intro': 'Understanding mobility.<br><span>Connecting data and dynamics.</span>',
        'eyebrow': 'TRANSPORTATION RESEARCH', 'profile_label': 'Academic profile',
        'updated': 'Last updated', 'date': UPDATED.strftime('%B %d, %Y').replace(' 0', ' '),
        'lang': '中文', 'lang_code': 'zh-CN', 'other_page': 'index_cn.html',
        'email': 'Email', 'scholar': 'Google Scholar', 'cv': 'Curriculum vitae', 'wechat': 'WeChat',
        'wechat_title': 'Connect on WeChat', 'wechat_hint': 'Scan the QR code to add me on WeChat.',
        'nav': 'Main navigation', 'menu': 'Open navigation', 'theme': 'Switch color theme', 'skip': 'Skip to content',
        'close': 'Close', 'top': 'Back to top', 'view': 'Explore papers', 'all': 'All research', 'year': 'Year', 'all_years': 'All years',
        'search': 'Search publications', 'placeholder': 'Search title, author, journal or keyword…', 'reset': 'Reset filters',
        'result': 'Showing all {count} publications', 'empty': 'No publications match your filters.',
        'note': '* Corresponding author. Years follow the assigned journal issue; online-first status is shown separately. Abstract-based schematics are labeled.',
        'preview': 'Research overview', 'contribution': 'Research summary', 'figure': 'Research figure', 'original': 'Open full-size figure',
        'paper': 'Paper', 'cite': 'Copy citation', 'copied': 'Citation copied', 'copy_failed': 'Select and copy the citation below.',
        'honor_label': 'Selected · October 2026',
        'honor': 'CAST Young Science and Technology Talent Cultivation Program',
        'honor_sub': 'Special Program for Doctoral Students',
        'honor_org': 'China Association for Science and Technology (CAST)',
        'news_honor': 'Selected for the CAST Young Science and Technology Talent Cultivation Program — Special Program for Doctoral Students.',
        'news_phd': 'Began Ph.D. studies in the <strong>Department of Civil Engineering, Tsinghua University</strong>, advised by Prof. Ruimin Li.',
        'news_grad': 'Named an <strong>Outstanding Graduate of Hunan Province</strong>.',
        'topics_short': ['Traffic modeling', 'Traffic safety', 'Driving behavior', 'Other explorations'],
        'topic_desc': ['Modeling spatiotemporal structure in traffic flow and crash events, including state reconstruction, data imputation, regional risk prediction and dynamic crash associations.', 'Assessing traffic conflicts and crash severity through safety indicators, heterogeneous statistical models and structured data augmentation.', 'Understanding car-following dynamics, driving styles and trajectory patterns through complex networks, residual analysis and physics-informed learning.', 'Exploratory work on urban road-network structure, dynamic regionalization and public electric-vehicle charging.'],
        'contact': 'Let’s connect', 'contact_text': 'For academic discussions and research exchanges, please get in touch.',
        'footer': 'Transportation research · Tsinghua University', 'inspired': 'Design inspiration',
    },
    'zh': {
        'name': '胡俊杰', 'other': 'Junjie Hu', 'title': '胡俊杰 | 交通运输研究 · 清华大学',
        'about': '关于', 'news': '动态', 'research': '研究', 'publications': '论文', 'experience': '经历', 'honors': '荣誉',
        'role': '博士研究生', 'university': '清华大学', 'department': '土木工程系',
        'intro': '理解交通运行，<br><span>连接数据与动力学。</span>',
        'eyebrow': 'TRANSPORTATION RESEARCH · 交通运输研究', 'profile_label': '学术主页',
        'updated': '最近更新', 'date': f'{UPDATED.year}年{UPDATED.month}月{UPDATED.day}日',
        'lang': 'English', 'lang_code': 'en', 'other_page': 'index.html',
        'email': '电子邮箱', 'scholar': '谷歌学术', 'cv': '个人简历', 'wechat': '微信',
        'wechat_title': '微信联系', 'wechat_hint': '扫描二维码添加微信，交流研究与想法。',
        'nav': '主导航', 'menu': '展开导航', 'theme': '切换明暗主题', 'skip': '跳转至正文',
        'close': '关闭', 'top': '返回顶部', 'view': '查看相关论文', 'all': '全部方向', 'year': '年份', 'all_years': '全部年份',
        'search': '检索学术论文', 'placeholder': '搜索论文标题、作者、期刊或关键词…', 'reset': '重置筛选',
        'result': '显示全部 {count} 篇论文', 'empty': '没有符合当前筛选条件的论文。',
        'note': '* 通讯作者。年份按正式卷期列示，在线预发表另行注明；依据摘要绘制的图示均有标注。',
        'preview': '研究概览', 'contribution': '研究概述', 'figure': '研究图示', 'original': '查看完整图示',
        'paper': '论文链接', 'cite': '复制引用', 'copied': '引用已复制', 'copy_failed': '请选中并复制下方引用。',
        'honor_label': '2026年10月 · 入选',
        'honor': '中国科协青年科技人才培育工程', 'honor_sub': '博士生专项计划',
        'honor_org': '中国科学技术协会',
        'news_honor': '入选中国科协青年科技人才培育工程博士生专项计划。',
        'news_phd': '进入<strong>清华大学土木工程系</strong>攻读博士学位，师从李瑞敏教授。',
        'news_grad': '获评<strong>湖南省优秀毕业生</strong>。',
        'topics_short': ['交通时空数据建模', '交通安全', '驾驶行为', '其他研究尝试'],
        'topic_desc': ['面向交通流与事故事件的时空结构，研究状态重构、缺失数据插补、区域风险预测及事故动态关联。', '围绕交通冲突与事故严重程度，开展安全指标分析、异质性统计建模及结构化数据增强。', '结合复杂网络、残差分析与物理信息融合学习，研究跟驰动力学、驾驶风格及轨迹行为表征。', '探索城市道路网络结构、动态区域划分与公共电动汽车充电等相关问题。'],
        'contact': '学术交流', 'contact_text': '欢迎就交通数据、交通安全与驾驶行为等方向交流研究。',
        'footer': '交通运输研究 · 清华大学', 'inspired': '设计参考',
    }
}
ICONS = {
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'file': '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    'scholar': '<path d="m2 9 10-6 10 6-10 6zM6 12v5c4 3 8 3 12 0v-5M22 9v7"/>',
    'chat': '<path d="M21 11a9 9 0 0 1-9 9 11 11 0 0 1-4-.8L3 21l1.8-5A9 9 0 1 1 21 11Z"/><path d="M8 11h.01M12 11h.01M16 11h.01"/>',
    'moon': '<path d="M20.8 13A9 9 0 0 1 11 3.2 9 9 0 1 0 20.8 13Z"/>',
    'arrow': '<path d="M5 12h14m-5-5 5 5-5 5"/>',
    'search': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
    'close': '<path d="m6 6 12 12M6 18 18 6"/>',
    'award': '<circle cx="12" cy="8" r="5"/><path d="m8 12-2 9 6-3 6 3-2-9"/>',
    'copy': '<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V3H3v13h5"/>',
    'link': '<path d="M14 3h7v7M21 3 10 14M10 3H4v17h17v-6"/>',
    'github': '<path d="M9 19c-4 1-4-2-6-2m12 4v-4a3 3 0 0 0-1-2c3 0 6-1 6-5a4 4 0 0 0-1-3 4 4 0 0 0 0-4s-1 0-3 1a11 11 0 0 0-6 0C8 3 7 3 7 3a4 4 0 0 0 0 4 4 4 0 0 0-1 3c0 4 3 5 6 5a3 3 0 0 0-1 2v4"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def heading(key, number, u, extra=''):
    return f'<div class="section-heading"><h2 id="heading-{key}"><span class="section-number" aria-hidden="true">{number}</span>{u[key]}</h2>{extra}</div>'

def paper(p, u, topics):
    authors = escape(p['authors'])
    # The original page explicitly marks this person in bold; preserve those positions.
    if p['id'] == 14:
        authors = authors.replace('Hu, J.', '<strong>Hu, J.</strong>')
    else:
        authors = authors.replace('Hu, J.', '<strong>Hu, J.</strong>', 1)
    figure = ''
    thumbnail = ''
    if p['image']:
        source = p.get('figure_source', '')
        source_link = f' <a href="{escape(source)}" target="_blank" rel="noopener">{"Source" if u["name"] == "Junjie Hu" else "来源"}</a>' if source.startswith('https:') else ''
        label = ('Research schematic' if u['name'] == 'Junjie Hu' else '研究示意图') if p.get('figure_kind') == 'schematic' else u['figure']
        figure = f'<figure><a href="{p["image"]}" target="_blank" rel="noopener" title="{u["original"]}"><img src="{p["image"]}" alt="{escape(p["image_alt"])}" loading="lazy"></a><figcaption>{escape(p["caption"])}{source_link}</figcaption></figure>'
        thumbnail = f'<a class="paper-thumbnail" href="{p["image"]}" data-preview="{p["id"]}" aria-label="{u["preview"]}: {escape(p["title"])}"><img src="{p["image"]}" alt="{escape(p["image_alt"])}" loading="lazy" decoding="async"><span>{label} {icon("arrow")}</span></a>'
    else:
        thumbnail = f'<div class="paper-typography" aria-hidden="true"><span>{p["year"]}</span><strong>{escape(p["journal"])}</strong><i>JH / {p["id"]:02}</i></div>'
    link = f'<a href="{escape(p["url"])}" target="_blank" rel="noopener">{icon("link")}{u["paper"]}</a>' if p['url'] else ''
    issue = p.get('issue', '')
    volume = p.get('volume', '') + ((f', {issue}' if issue.startswith('Part ') else f'({issue})') if issue else '')
    locator = ', '.join(x for x in [volume, p.get('page', '')] if x)
    bibliographic = f'<p class="paper-bibliographic">{escape(locator)}</p>' if locator else ''
    status = f'<p class="paper-status">{escape(p["status"])}</p>' if p.get('status') else ''
    citation = f'{p["authors"]} ({p["year"]}). {p["title"].rstrip(".")}. {p["journal"]}' + (f', {locator}' if locator else '') + f'. {p["url"]}'
    return f'''<article class="paper" id="paper-{p['id']}" data-topic="{p['topic']}" data-year="{p['year']}" data-citation="{escape(citation)}">
      {thumbnail}<div class="paper-content">
        <div class="paper-venue"><span>{escape(p['journal'])}</span><time>{p['year']}</time></div>
        <h3><a href="{escape(p['url'])}" target="_blank" rel="noopener">{escape(p['title'])}</a></h3>
        <p class="paper-authors">{authors}</p>
        {bibliographic}{status}
        <p class="paper-topic">{escape(topics[p['topic']])}</p>
        <div class="paper-actions">{link}<button class="copy-citation enhanced" type="button">{icon('copy')}{u['cite']}</button></div>
        <details class="paper-details"><summary>{u['preview']} {icon('arrow')}</summary><div class="detail-content"><h4>{u['contribution']}</h4><p>{p['contribution_html']}</p>{figure}</div></details>
      </div></article>'''

def build(lang):
    u, d = UI[lang], DATA['languages'][lang]
    html_lang, filename = ('en', 'index.html') if lang == 'en' else ('zh-CN', 'index_cn.html')
    desc = ' '.join(unescape(re.sub('<[^>]+>', '', d['bio_html'])).split())
    nav = ''.join(f'<a href="#{key}">{u[key]}</a>' for key in ('about','news','research','publications','experience','honors'))
    nav_mobile = nav + f'<a href="{u["other_page"]}" hreflang="{u["lang_code"]}" class="language-link">{u["lang"]}</a>'
    topics = ''.join(f'<a class="research-item" href="#publications" data-research="{i}"><span class="research-index">0{i+1}</span><div><h3>{escape(title)}</h3><p>{u["topic_desc"][i]}</p><span class="research-link">{u["view"]} {icon("arrow")}</span></div></a>' for i,title in enumerate(d['topics']))
    count = len(d['publications'])
    years = ''.join(f'<option>{year}</option>' for year in sorted({p['year'] for p in d['publications']}, reverse=True))
    filters = f'<button type="button" data-filter="all" aria-pressed="true">{u["all"]}<span>{count}</span></button>'
    for i, topic in enumerate(u['topics_short']):
        topic_count = sum(p['topic'] == i for p in d['publications'])
        filters += f'<button type="button" data-filter="{i}" aria-pressed="false">{topic}<span>{topic_count}</span></button>'
    pubs = ''.join(paper(p, u, d['topics']) for p in sorted(d['publications'], key=lambda p:p['sort_date'], reverse=True))
    honors = d['honors_html'].replace('<h3>Scholarships</h3>', '<h3>Scholarships &amp; distinctions</h3>').replace('<h3>奖学金</h3>', '<h3>奖学金与综合荣誉</h3>')
    person = {'@context':'https://schema.org','@type':'Person','name':'Junjie Hu','alternateName':'胡俊杰','url':BASE,'image':BASE+'profile-anime.png','jobTitle':'Ph.D. Student','affiliation':{'@type':'CollegeOrUniversity','name':'Tsinghua University'},'sameAs':['https://scholar.google.com/citations?user=2Irk2E4AAAAJ','https://github.com/junjiehu-traffic']}
    page = f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{u['title']}</title><meta name="description" content="{escape(desc)}">
  <meta name="theme-color" content="#5b6096"><meta property="og:type" content="profile">
  <meta property="og:title" content="{u['title']}"><meta property="og:description" content="{escape(desc)}">
  <meta property="og:image" content="{BASE}profile-anime.png"><meta property="og:url" content="{BASE}{filename}">
  <meta property="og:locale" content="{'en_US' if lang == 'en' else 'zh_CN'}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{BASE}{filename}">
  <link rel="alternate" hreflang="en" href="{BASE}index.html"><link rel="alternate" hreflang="zh-CN" href="{BASE}index_cn.html"><link rel="alternate" hreflang="x-default" href="{BASE}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="css/style.css?v={DATA['revision']}">
  <script src="js/theme.js?v={DATA['revision']}"></script>
  <script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
  <script src="js/main.js?v={DATA['revision']}" defer></script>
</head>
<body>
<a class="skip-link" href="#main">{u['skip']}</a>
<header class="site-header"><div class="header-inner">
  <a class="wordmark" href="#about" aria-label="{u['name']} · {u['profile_label']}"><span class="monogram">jh<span>.</span></span><span class="wordmark-label">{u['profile_label']}</span></a>
  <nav class="desktop-nav" aria-label="{u['nav']}">{nav}</nav>
  <div class="header-actions"><a class="language-link" href="{u['other_page']}" hreflang="{u['lang_code']}" lang="{u['lang_code']}">{u['lang']}</a><button class="icon-button enhanced" id="theme-toggle" type="button" aria-label="{u['theme']}" aria-pressed="false">{icon('moon')}</button><button class="icon-button menu-toggle enhanced" id="menu-toggle" type="button" aria-label="{u['menu']}" aria-expanded="false" aria-controls="mobile-nav">{icon('menu')}</button></div>
</div><nav id="mobile-nav" class="mobile-nav" aria-label="{u['nav']}" hidden>{nav_mobile}</nav></header>
<div class="page-layout">
  <aside class="profile" aria-label="{u['profile_label']}">
    <div class="portrait-frame"><img class="portrait" src="profile-anime.png" alt="{'Anime portrait of Junjie Hu in graduation attire' if lang == 'en' else '胡俊杰身着学位服的动漫风格肖像'}" width="1122" height="1402" fetchpriority="high"></div>
    <div class="profile-info"><p class="profile-kicker">{u['university']}</p><h1>{u['name']}<span>{u['other']}</span></h1><p class="profile-role">{u['role']}</p><p class="profile-department">{u['department']}</p>
    <div class="profile-topics"><span>{u['topics_short'][0]}</span><span>{u['topics_short'][1]}</span><span>{u['topics_short'][2]}</span></div>
    <a class="cv-link" href="JunjieHu_CV.pdf" target="_blank" rel="noopener">{icon('file')}{u['cv']}{icon('link')}</a>
    <div class="social-links"><a href="mailto:junjiehuits@gmail.com" aria-label="{u['email']}" title="{u['email']}">{icon('mail')}</a><a href="https://scholar.google.com/citations?hl={'en' if lang == 'en' else 'zh-CN'}&amp;user=2Irk2E4AAAAJ" target="_blank" rel="noopener" aria-label="{u['scholar']}" title="{u['scholar']}">{icon('scholar')}</a><a href="https://github.com/junjiehu-traffic" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">{icon('github')}</a><a href="wechat.jpg" class="wechat-link" aria-label="{u['wechat']}" title="{u['wechat']}">{icon('chat')}</a></div>
    <a class="profile-email" href="mailto:junjiehuits@gmail.com">junjiehuits@gmail.com</a><p class="last-updated">{u['updated']}<time datetime="{DATA['updated']}">{u['date']}</time></p></div>
  </aside>
  <main id="main">
    <section id="about" aria-labelledby="about-title" class="about-section"><p class="eyebrow">{u['eyebrow']}</p><h2 id="about-title">{u['intro']}</h2><div class="biography"><p>{d['bio_html']}</p></div><div class="affiliation">{d['affiliation_html']}</div></section>
    <section id="news" aria-labelledby="heading-news">{heading('news','01',u)}<ol class="news-list"><li><time datetime="2026-10">2026.10</time><p>{u['news_honor']}</p></li><li><time datetime="2026">2026</time><p>{u['news_phd']}</p></li><li><time datetime="2026">2026</time><p>{u['news_grad']}</p></li></ol></section>
    <section id="research" aria-labelledby="heading-research">{heading('research','02',u)}<div class="research-grid">{topics}</div></section>
    <section id="publications" aria-labelledby="heading-publications">{heading('publications','03',u,f'<span class="section-count">{count}</span>')}
      <div class="publication-tools enhanced"><div class="search-row"><label class="search-field">{icon('search')}<span class="sr-only">{u['search']}</span><input id="publication-search" type="search" placeholder="{u['placeholder']}" autocomplete="off"></label><label class="year-field"><span class="sr-only">{u['year']}</span><select id="year-filter" aria-label="{u['year']}"><option value="all">{u['all_years']}</option>{years}</select></label></div>
      <div class="topic-filters" role="group" aria-label="{u['research']}">{filters}</div><div class="results-row"><p id="result-count" role="status" aria-live="polite">{u['result'].format(count=count)}</p><button id="reset-filters" type="button" hidden>{u['reset']}</button></div></div>
      <p class="publication-note">{u['note']}</p><div class="publications-list">{pubs}</div><p id="empty-results" hidden>{u['empty']}</p>
    </section>
    <section id="experience" aria-labelledby="heading-experience">{heading('experience','04',u)}<div class="experience-list">{d['experience_html']}</div></section>
    <section id="honors" aria-labelledby="heading-honors">{heading('honors','05',u)}
      <div class="honors-grid">{honors}</div>
    </section>
    <section class="contact-section" aria-labelledby="contact-title"><div><p class="eyebrow">{u['contact']}</p><h2 id="contact-title">{u['contact_text']}</h2><a href="mailto:junjiehuits@gmail.com">junjiehuits@gmail.com {icon('arrow')}</a></div></section>
  </main>
</div>
<footer><div><p>© {UPDATED.year} {u['name']}<span>{u['footer']}</span></p><p>{u['updated']} <time datetime="{DATA['updated']}">{u['date']}</time> · <a href="https://github.com/Anleeno/anleeno-academic" target="_blank" rel="noopener">{u['inspired']}</a></p></div></footer>
<dialog id="paper-dialog" aria-labelledby="dialog-paper-title"><div class="dialog-top"><span>{u['preview']}</span><button class="icon-button dialog-close" aria-label="{u['close']}">{icon('close')}</button></div><div class="dialog-body"></div></dialog>
<dialog id="wechat-dialog" aria-labelledby="wechat-title"><div class="dialog-top"><h2 id="wechat-title">{u['wechat_title']}</h2><button class="icon-button dialog-close" aria-label="{u['close']}">{icon('close')}</button></div><div class="wechat-body"><img src="wechat.jpg" alt="{u['wechat_title']}" width="400" height="400" loading="lazy"><p>{u['wechat_hint']}</p></div></dialog>
<div id="toast" role="status" aria-live="polite"></div><button class="back-to-top icon-button enhanced" type="button" aria-label="{u['top']}" hidden>{icon('arrow')}</button>
</body></html>
'''
    with (ROOT / 'frontend' / filename).open('w', encoding='utf-8', newline='\n') as output:
        output.write(page)
    print(f'Built {filename}: {len(d["publications"])} publications; updated {DATA["updated"]}')

if __name__ == '__main__':
    build('en')
    build('zh')
