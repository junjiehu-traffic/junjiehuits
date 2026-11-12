'use strict';
const root = document.documentElement;
const zh = root.lang === 'zh-CN';
root.classList.add('js-ready');
const themeToggle = document.querySelector('#theme-toggle');
function updateTheme() {
  const dark = root.dataset.theme === 'dark';
  themeToggle.setAttribute('aria-pressed', String(dark));
  themeToggle.setAttribute('aria-label', zh ? (dark ? '切换至浅色主题' : '切换至深色主题') : (dark ? 'Switch to light theme' : 'Switch to dark theme'));
}
updateTheme();
themeToggle.addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem('theme', root.dataset.theme); } catch (_) { /* Optional preference. */ }
  updateTheme();
});

const menuToggle = document.querySelector('#menu-toggle');
const menu = document.querySelector('#mobile-nav');
function closeMenu() { menu.hidden = true; menuToggle.setAttribute('aria-expanded', 'false'); }
menuToggle.addEventListener('click', () => { menu.hidden = !menu.hidden; menuToggle.setAttribute('aria-expanded', String(!menu.hidden)); });
menu.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
document.addEventListener('click', e => { if (!e.target.closest('.site-header')) closeMenu(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { closeMenu(); menuToggle.focus(); } });
matchMedia('(min-width:901px)').addEventListener('change', e => { if (e.matches) closeMenu(); });

// Keep a tall desktop profile readable while scrolling long publication lists.
const profile = document.querySelector('.profile');
function positionProfile() {
  const top = Math.min(document.querySelector('.site-header').offsetHeight + 28, innerHeight - profile.offsetHeight - 24);
  profile.style.setProperty('--profile-top', `${top}px`);
}
new ResizeObserver(positionProfile).observe(profile);
window.addEventListener('resize', positionProfile);
positionProfile();

// Both editions use identical paper IDs, topic IDs and filter semantics.
const papers = [...document.querySelectorAll('.paper')];
const publicationGroups = [...document.querySelectorAll('.publication-group')].map(element => ({
  element, papers: [...element.querySelectorAll('.paper')], count: element.querySelector('.publication-group-count')
}));
const search = document.querySelector('#publication-search');
const year = document.querySelector('#year-filter');
const topicButtons = [...document.querySelectorAll('[data-filter]')];
const resultCount = document.querySelector('#result-count');
const reset = document.querySelector('#reset-filters');
let topic = 'all';
const normalize = text => text.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
const index = papers.map(paper => ({paper, text: normalize(paper.textContent)}));
function applyFilters() {
  const terms = normalize(search.value).split(' ').filter(Boolean);
  let visible = 0;
  index.forEach(({paper, text}) => {
    const matches = (topic === 'all' || paper.dataset.topic === topic) &&
      (year.value === 'all' || paper.dataset.year === year.value) && terms.every(term => text.includes(term));
    paper.hidden = !matches;
    if (matches) visible++;
  });
  publicationGroups.forEach(group => {
    const matches = group.papers.filter(paper => !paper.hidden).length;
    group.element.hidden = matches === 0;
    const count = matches === group.papers.length ? String(matches) : `${matches} / ${group.papers.length}`;
    group.count.textContent = zh ? `${count} 篇论文` : `${count} ${group.papers.length === 1 ? 'publication' : 'publications'}`;
  });
  resultCount.textContent = zh ? `显示 ${visible} / ${papers.length} 篇论文` : `Showing ${visible} of ${papers.length} publications`;
  document.querySelector('#empty-results').hidden = visible !== 0;
  reset.hidden = topic === 'all' && year.value === 'all' && !search.value;
  topicButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === topic)));
  const url = new URL(location.href);
  ['topic', 'year', 'q'].forEach(key => url.searchParams.delete(key));
  if (topic !== 'all') url.searchParams.set('topic', topic);
  if (year.value !== 'all') url.searchParams.set('year', year.value);
  if (search.value) url.searchParams.set('q', search.value);
  if (location.protocol !== 'file:') history.replaceState(null, '', url);
}
search.addEventListener('input', applyFilters);
year.addEventListener('change', applyFilters);
topicButtons.forEach(button => button.addEventListener('click', () => { topic = button.dataset.filter; applyFilters(); }));
reset.addEventListener('click', () => { topic = 'all'; year.value = 'all'; search.value = ''; applyFilters(); search.focus(); });
document.querySelectorAll('[data-research]').forEach(link => link.addEventListener('click', () => {
  topic = link.dataset.research; year.value = 'all'; search.value = ''; applyFilters();
}));
const params = new URLSearchParams(location.search);
if (topicButtons.some(button => button.dataset.filter === params.get('topic'))) topic = params.get('topic');
if ([...year.options].some(option => option.value === params.get('year'))) year.value = params.get('year');
search.value = params.get('q') || '';
applyFilters();
document.querySelectorAll('.language-link').forEach(link => link.addEventListener('click', () => {
  const destination = new URL(link.getAttribute('href'), location.href);
  if (topic !== 'all') destination.searchParams.set('topic', topic);
  if (year.value !== 'all') destination.searchParams.set('year', year.value);
  if (search.value) destination.searchParams.set('q', search.value);
  destination.hash = location.hash;
  link.href = destination.pathname + destination.search + destination.hash;
}));

// Native dialogs supply keyboard focus containment and Escape handling.
const paperDialog = document.querySelector('#paper-dialog');
const wechatDialog = document.querySelector('#wechat-dialog');
let dialogTrigger;
function openDialog(dialog, trigger) {
  dialogTrigger = trigger;
  dialog.showModal();
  document.body.classList.add('dialog-open');
  dialog.scrollTop = 0;
  dialog.querySelector('.dialog-close').focus();
}
for (const dialog of [paperDialog, wechatDialog]) {
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('dialog-open');
    if (dialogTrigger?.isConnected) dialogTrigger.focus();
  });
}
function showPaper(paper, trigger) {
  const body = paperDialog.querySelector('.dialog-body');
  body.replaceChildren();
  const title = document.createElement('h2');
  title.id = 'dialog-paper-title';
  title.textContent = paper.querySelector('.paper-title').textContent;
  body.append(paper.querySelector('.paper-venue').cloneNode(true), title, paper.querySelector('.paper-authors').cloneNode(true));
  for (const selector of ['.paper-bibliographic', '.paper-status']) {
    const element = paper.querySelector(selector);
    if (element) body.append(element.cloneNode(true));
  }
  const actions = paper.querySelector('.paper-actions').cloneNode(true);
  actions.querySelector('.copy-citation').addEventListener('click', event => copyCitation(paper, event.currentTarget));
  body.append(actions, paper.querySelector('.detail-content').cloneNode(true));
  openDialog(paperDialog, trigger);
}
papers.forEach(paper => {
  paper.querySelector('summary').addEventListener('click', event => { event.preventDefault(); showPaper(paper, event.currentTarget); });
  paper.querySelector('.paper-thumbnail')?.addEventListener('click', event => { event.preventDefault(); showPaper(paper, event.currentTarget); });
  paper.querySelector('.copy-citation').addEventListener('click', event => copyCitation(paper, event.currentTarget));
});
document.querySelector('.wechat-link').addEventListener('click', event => { event.preventDefault(); openDialog(wechatDialog, event.currentTarget); });
let toastTimer;
function toast(message) {
  const el = document.querySelector('#toast');
  el.textContent = message; el.classList.add('visible');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('visible'), 2600);
}
async function copyCitation(paper, button) {
  const text = paper.dataset.citation;
  try {
    await navigator.clipboard.writeText(text);
    const label = button.innerHTML;
    button.textContent = zh ? '引用已复制' : 'Citation copied';
    setTimeout(() => { button.innerHTML = label; }, 2400);
    toast(zh ? '引用已复制' : 'Citation copied');
  } catch (_) {
    // Allow manual copying when file:// or browser policy blocks the clipboard.
    const parent = button.closest('.dialog-body') || paper.querySelector('.paper-content');
    let field = parent.querySelector('.citation-fallback');
    if (!field) {
      field = document.createElement('textarea'); field.className = 'citation-fallback'; field.readOnly = true;
      field.setAttribute('aria-label', zh ? '论文引用' : 'Publication citation'); parent.append(field);
    }
    field.value = text; field.focus(); field.select();
    toast(zh ? '请选中并复制下方引用。' : 'Select and copy the citation below.');
  }
}
const anchors = [...document.querySelectorAll('.desktop-nav a')];
const sections = anchors.map(a => document.querySelector(a.getAttribute('href')));
const back = document.querySelector('.back-to-top');
let scrolling = false;
function updateScroll() {
  let active = sections[0];
  for (const section of sections) if (section.getBoundingClientRect().top < 180) active = section;
  for (const anchor of anchors) {
    if (anchor.hash === `#${active.id}`) anchor.setAttribute('aria-current', 'location');
    else anchor.removeAttribute('aria-current');
  }
  back.hidden = scrollY < 500; scrolling = false;
}
window.addEventListener('scroll', () => { if (!scrolling) { scrolling = true; requestAnimationFrame(updateScroll); } }, {passive:true});
updateScroll();
back.addEventListener('click', () => window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'}));
