#!/usr/bin/env python3
"""Build the dependency-free portfolio into dist/."""
from datetime import date
from html import escape
from pathlib import Path
from shutil import copy2
import json

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
ASSETS = DIST / "assets"
data = json.loads((SRC / "content.json").read_text(encoding="utf-8"))
projects = data["projects"]


def h(value):
    return escape(str(value), quote=True)


def project_url(project):
    return f"project-{h(project['slug'])}.html"


def figure(project, size=""):
    is_mockup = project["image"].endswith("-mockup.png")
    label = f"{project['name']} illustrative mobile mockup" if is_mockup else f"{project['name']} project preview"
    if project["image"]:
        visual = f'<img src="assets/{h(project["image"])}" alt="{h(label)}" loading="lazy">'
    else:
        visual = (
            '<div class="power-art" aria-label="Power Electrode project graphic">'
            '<span class="power-art-mark">PE<span>®</span></span>'
            '<strong>Power<br>Electrode</strong>'
            '<span class="power-art-caption">Made for the work that holds.</span>'
            '<i class="rod rod-one"></i><i class="rod rod-two"></i><i class="rod rod-three"></i>'
            '</div>'
        )
    return f'<div class="project-visual {h(project["tone"])} {"mockup" if is_mockup else ""} {size}">{visual}</div>'


def card(project, index=0):
    return f"""
      <article class="project-card" data-category="{h(project['category'])}">
        <a class="project-card-link" href="{project_url(project)}" aria-label="View {h(project['name'])} project">
          <div class="project-card-top"><span>{h(project['name'])}</span><span>{h(project['type'])}</span></div>
          {figure(project)}
          <div class="project-card-bottom"><span>{h(project['summary'])}</span></div>
        </a>
      </article>
    """


def header(active):
    nav = [
        ("Projects", "projects.html", "projects"),
        ("About", "about.html", "about"),
        ("Contact", "contact.html", "contact"),
    ]
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if active == key else ""}>{label}</a>'
        for label, href, key in nav
    )
    return f"""
      <header class="site-header">
        <div class="container header-inner">
          <a class="brand" href="index.html" aria-label="Coded by Enoch, home"><span class="brand-prefix">coded by</span> <span class="brand-person">Enoch</span></a>
          <button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="main-nav" aria-expanded="false">
            <span></span><span></span>
          </button>
          <nav class="nav" id="main-nav" aria-label="Main navigation">
            {links}
            <a class="nav-social" href="{h(data['github'])}" target="_blank" rel="noopener noreferrer" aria-label="GitHub, opens in a new tab">GitHub <span class="link-arrow" aria-hidden="true">↗</span></a>
            <a class="nav-cta" href="contact.html">Start a project <span class="link-arrow" aria-hidden="true">↗</span></a>
          </nav>
        </div>
      </header>
    """


def footer():
    return f"""
      <footer class="site-footer">
        <div class="container footer-cta">
          <div class="footer-cta-copy">
            <h2>Have a project in mind?<br><span>Let's talk.</span></h2>
            <a class="text-link" href="contact.html">Get in touch <span class="link-arrow" aria-hidden="true">↗</span></a>
          </div>
        </div>
        <div class="container footer-main">
          <div class="footer-identity">
            <a class="footer-brand" href="index.html" aria-label="Enoch Numo Tetteh, home">Enoch<span>®</span></a>
            <p>Frontend Developer &amp; Designer<br>Accra, Ghana</p>
          </div>
          <nav class="footer-column" aria-label="Footer navigation">
            <h3>Navigate</h3>
            <a href="index.html">Home</a>
            <a href="projects.html">Projects</a>
            <a href="shelf.html">My shelf</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
          </nav>
          <div class="footer-column">
            <h3>Connect</h3>
            <a href="{h(data['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
            <a href="{h(data['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
            <a href="mailto:{h(data['email'])}">Email ↗</a>
          </div>
          <div class="footer-column footer-location">
            <h3>Based in</h3>
            <p>Accra, Ghana<br>Working remotely</p>
          </div>
        </div>
        <div class="container footer-bottom">
          <small>© {date.today().year} Enoch Numo Tetteh <span>· Coded by Enoch</span></small>
          <a href="#main">Back to top ↑</a>
        </div>
      </footer>
    """


def shell(title, description, body, active=""):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fbfbf8">
  <meta name="description" content="{h(description)}">
  <title>{h(title)} — Enoch Numo Tetteh</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="assets/Geist-Variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="styles.css">
  <script src="site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {header(active)}
  <main id="main">{body}</main>
  {footer()}
</body>
</html>"""


def rich_paragraph(segments, lead=False, outro=False):
    parts = []
    for segment in segments:
        if isinstance(segment, str):
            parts.append(h(segment))
            continue
        preview = data["linkPreviews"][segment["link"]]
        url = preview["url"]
        external = url.startswith(("https://", "http://"))
        attributes = (
            f'data-preview-title="{h(preview["title"])}" '
            f'data-preview-detail="{h(preview["detail"])}" '
            f'data-preview-image="{h(preview.get("image", ""))}" '
            f'data-preview-mark="{h(preview.get("mark", ""))}" '
            f'data-preview-theme="{h(preview.get("theme", "stone"))}" '
            f'data-preview-fit="{h(preview.get("fit", "cover"))}"'
        )
        target = ' target="_blank" rel="noopener noreferrer"' if external else ""
        icon = preview.get("icon")
        icon_html = f'<img class="inline-link-icon" src="assets/{h(icon)}" alt="" aria-hidden="true">' if icon else ''
        parts.append(f'<a class="preview-link preview-{h(segment["link"])}" href="{h(url)}" {attributes}{target}>{icon_html}{h(segment["text"])}</a>')
    klass = ' class="lead"' if lead else ' class="story-outro"' if outro else ''
    return f'<p{klass}>{"".join(parts)}</p>'


def brands_section():
    items = []
    for brand in data["brands"]:
        content = (f'<span class="brand-logo"><img src="assets/{h(brand["logo"])}" '
                   f'alt="" loading="lazy"></span><span class="brand-name">{h(brand["name"])}</span>')
        theme = f'brand-tile brand-{h(brand.get("theme", "neutral"))}'
        if brand.get("project"):
            items.append(f'<a class="{theme}" href="project-{h(brand["project"])}.html" '
                         f'aria-label="View {h(brand["name"])} project">{content}</a>')
        elif brand.get("url"):
            items.append(f'<a class="{theme}" href="{h(brand["url"])}" target="_blank" rel="noopener noreferrer" '
                         f'aria-label="Visit {h(brand["name"])} website">{content}</a>')
        else:
            items.append(f'<div class="{theme}">{content}</div>')
    return f"""
      <section class="brands-section container" aria-labelledby="brands-title">
        <div class="section-rail"><h2 id="brands-title"><span class="plus" aria-hidden="true">+</span> Clients</h2><p>Brands and businesses I've worked with.</p></div>
        <div class="brand-grid">{''.join(items)}</div>
      </section>
    """


def tools_section():
    tiles = "".join(
        f'<div class="tool-tile"><span class="tool-icon"><img src="assets/{h(item["icon"])}" alt="" loading="lazy"></span>'
        f'<span>{h(item["name"])}</span></div>'
        for item in data["tools"]
    )
    return f"""
      <section class="tools-section container" aria-labelledby="tools-title">
        <div class="section-rail"><h2 id="tools-title"><span class="plus" aria-hidden="true">+</span> My toolkit</h2><p>Tools I use to make things work.</p></div>
        <div class="tools-body">
          <p class="tools-intro">The tools behind the things I make<span aria-hidden="true"> ✳</span></p>
          <div class="tool-grid" role="group" aria-label="Frontend tools and platforms">{tiles}</div>
        </div>
      </section>
    """


def home():
    selected = projects[:3]
    items = "".join(card(p, n) for n, p in enumerate(selected))
    story = "".join(rich_paragraph(p, outro=i == len(data["heroStory"]) - 1) for i, p in enumerate(data["heroStory"]))
    return f"""
      <section class="hero story-hero container">
        <div class="hero-copy">
          <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> Frontend Developer &amp; Designer · Accra, Ghana</p>
          <h1>{h(data['heroTitle'])} <span>{h(data['heroMuted'])}</span></h1>
          <div class="hero-story">{story}</div>
        </div>
      </section>
      <section class="work-section container" id="work" aria-labelledby="work-title">
        <div class="section-rail">
          <h2 id="work-title"><span class="plus" aria-hidden="true">+</span> Selected work</h2>
          <p>Sites and products I have built.</p>
        </div>
        <div class="work-list">
          {items}
          <a class="all-work-link" href="projects.html">View all projects <span class="link-arrow" aria-hidden="true">↗</span></a>
        </div>
      </section>
      <section class="about-strip container">
        <div class="section-rail"><h2><span class="plus" aria-hidden="true">+</span> A little about me</h2></div>
        <div class="about-strip-copy">
          <p>From small experiments to real client work, I keep coming back to the same thing: making the web clearer and more useful for people.</p>
          <a class="text-link" href="about.html">More about me <span class="link-arrow" aria-hidden="true">↗</span></a>
        </div>
      </section>
      {brands_section()}
      {tools_section()}
    """


def shelf_item(item, kind):
    title = item["title"]
    creator = item["creator"]
    label = f"{title} by {creator}" if creator != "Cover artwork" else f"Cover artwork: {title}"
    return f'''<figure class="shelf-item {kind}" title="{h(label)}">
      <img src="assets/{h(item['image'])}" alt="{h(label)}" loading="lazy" decoding="async">
      <figcaption class="visually-hidden">{h(label)}</figcaption>
    </figure>'''


def shelf_row(items, kind):
    covers = "".join(shelf_item(item, kind) for item in items)
    return f'<div class="shelf-row {kind}-row">{covers}</div>'


def shelf_layout(items, kind):
    layouts = []
    for size, name in ((4, "desktop"), (2, "mobile")):
        rows = "".join(shelf_row(items[i:i + size], kind) for i in range(0, len(items), size))
        layouts.append(f'<div class="shelf-layout shelf-layout-{name}">{rows}</div>')
    return "".join(layouts)


def shelf_page():
    books = shelf_layout(data["books"], "book")
    records = shelf_layout(data["records"], "record")
    return f"""
      <section class="page-intro shelf-intro container">
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> A few favourites</p>
        <h1>My shelf<span class="period">.</span></h1>
        <p>Books and records I keep coming back to.</p>
      </section>
      <section class="shelf-section container" aria-labelledby="books-title">
        <div class="shelf-heading"><h2 id="books-title">Books</h2><span>01 / 02</span></div>
        {books}
      </section>
      <section class="shelf-section record-section container" aria-labelledby="records-title">
        <div class="shelf-heading"><h2 id="records-title">Records</h2><span>02 / 02</span></div>
        {records}
        <a class="shelf-home-link text-link" href="index.html">Back to my work <span class="link-arrow" aria-hidden="true">↗</span></a>
      </section>
    """


def projects_page():
    cards = "".join(card(p, n) for n, p in enumerate(projects))
    return f"""
      <section class="page-intro container">
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> Work</p>
        <h1>Selected projects<span class="period">.</span></h1>
        <p>A mix of client websites, product flows and ideas I have built for the web.</p>
      </section>
      <section class="container project-index" aria-label="Project gallery">
        <div class="filter-bar" role="group" aria-label="Filter projects">
          <button type="button" class="filter active" data-filter="All" aria-pressed="true">All <span>{len(projects):02}</span></button>
          <button type="button" class="filter" data-filter="Product" aria-pressed="false">Product</button>
          <button type="button" class="filter" data-filter="Commerce" aria-pressed="false">Commerce</button>
          <button type="button" class="filter" data-filter="Website" aria-pressed="false">Websites</button>
        </div>
        <div class="project-grid">{cards}</div>
        <p class="empty-state" hidden>No projects in this category yet.</p>
      </section>
    """


def about_page():
    story = "".join(rich_paragraph(p, i == 0) for i, p in enumerate(data["aboutStory"]))
    return f"""
      <section class="page-intro container">
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> About</p>
        <h1>Hi, I'm Enoch<span class="period">.</span></h1>
        <p>Frontend developer &amp; designer based in Accra, Ghana.</p>
      </section>
      <section class="about-page-grid container">
        <div class="section-rail"><h2><span class="plus" aria-hidden="true">+</span> My story</h2></div>
        <div class="about-page-copy">
          {story}
          <a class="text-link" href="assets/Enoch_Numo_Tetteh_CV.pdf" download>Download my CV <span class="link-arrow" aria-hidden="true">↓</span></a>
        </div>
      </section>
      <section class="principles container">
        <div class="section-rail"><h2><span class="plus" aria-hidden="true">+</span> How I work</h2></div>
        <div class="principle-grid">
          <div><h3>Start with the person</h3><p>I try to understand what someone needs to do before deciding what the screen should look like.</p></div>
          <div><h3>Make the path clear</h3><p>Good structure, readable content and straightforward interactions matter as much as the final visual polish.</p></div>
          <div><h3>Build for real use</h3><p>I pay attention to the small screens, slow connections and edge cases a polished mockup can miss.</p></div>
          <div><h3>Keep improving</h3><p>I test what I build, work through feedback and refine the details after the first version is live.</p></div>
        </div>
      </section>
      <section class="about-page-grid container toolkit">
        <div class="section-rail"><h2><span class="plus" aria-hidden="true">+</span> Tools I use</h2></div>
        <div class="tool-list">React <span>·</span> Next.js <span>·</span> TypeScript <span>·</span> JavaScript <span>·</span> Tailwind CSS <span>·</span> WordPress <span>·</span> Git</div>
      </section>
    """


def contact_page():
    return f"""
      <section class="contact-hero container">
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> Contact</p>
        <h1>Tell me what you're<br><span>working on.</span></h1>
        <p>For a project, a role or a conversation about a website, send me an email. I am based in Accra and work with people remotely.</p>
        <a class="contact-email" href="mailto:{h(data['email'])}?subject=Hello%20Enoch">{h(data['email'])}</a>
      </section>
      <section class="contact-bottom container">
        <div><span class="small-label">Elsewhere</span><a href="{h(data['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a><a href="{h(data['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn</a></div>
        <div><span class="small-label">Location</span><p>Accra, Ghana<br>Working remotely</p></div>
      </section>
    """


def detail_page(project, next_project):
    return f"""
      <section class="project-detail-intro container">
        <a class="back-link" href="projects.html">All projects</a>
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> {h(project['category'])} / {h(project['type'])}</p>
        <h1>{h(project['name'])}<span class="period">.</span></h1>
        <p class="detail-summary">{h(project['summary'])}</p>
      </section>
      <section class="container detail-hero">{figure(project, "detail-visual")}</section>
      <section class="container detail-content">
        <div class="detail-facts">
          <div><span>Contribution</span><strong>{h(project['contribution'])}</strong></div>
          <div><span>Built with</span><strong>{h(project['stack'])}</strong></div>
          <div><span>Explore</span><a href="{h(project['url'])}" target="_blank" rel="noopener noreferrer">Visit live project</a></div>
        </div>
        <div class="detail-story">
          <div class="section-rail"><h2><span class="plus" aria-hidden="true">+</span> The work</h2></div>
          <p>{h(project['approach'])}</p>
        </div>
      </section>
      <section class="next-project container">
        <span class="small-label">Next project</span>
        <a href="{project_url(next_project)}">{h(next_project['name'])}</a>
      </section>
    """


def not_found_page():
    return """
      <section class="contact-hero container">
        <p class="eyebrow"><span class="plus" aria-hidden="true">+</span> Page not found</p>
        <h1>That page isn't here<span class="period">.</span></h1>
        <p>Let's get you back to the work.</p>
        <a class="pill-link" href="index.html">Go home</a>
      </section>
    """


def write(name, title, description, body, active=""):
    (DIST / name).write_text(shell(title, description, body, active), encoding="utf-8")


def main():
    DIST.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    for asset in (SRC / "assets").iterdir():
        if asset.is_file():
            copy2(asset, ASSETS / asset.name)
    for filename in ("styles.css", "site.js", "favicon.svg"):
        source = SRC / filename
        target = ASSETS / filename if filename.endswith(".svg") else DIST / filename
        copy2(source, target)
    write("index.html", "Frontend Developer and Designer", data["intro"], home(), "home")
    write("shelf.html", "My shelf", "Books and records Enoch Numo Tetteh loves.", shelf_page(), "shelf")
    write("projects.html", "Projects", "Selected websites and web products by Enoch Numo Tetteh.", projects_page(), "projects")
    write("about.html", "About", "About Enoch Numo Tetteh, frontend developer and designer in Accra.", about_page(), "about")
    write("contact.html", "Contact", "Contact Enoch Numo Tetteh about frontend development and web projects.", contact_page(), "contact")
    write("404.html", "Page not found", "Page not found.", not_found_page())
    for i, project in enumerate(projects):
        next_project = projects[(i + 1) % len(projects)]
        write(
            f"project-{project['slug']}.html",
            project["name"],
            project["summary"],
            detail_page(project, next_project),
            "projects",
        )
    print(f"Built {len(list(DIST.glob('*.html')))} pages in {DIST}")


if __name__ == "__main__":
    main()
