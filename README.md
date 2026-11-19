# Enoch Numo Tetteh portfolio

An original static portfolio starter built around a quiet, content-first visual style. It was inspired by the Formo screenshot shared in the conversation. This is **not** a Framer project export or the original template source.

## Run it in VS Code

Extract this ZIP to a **new folder**. Open that folder in VS Code and check that `package.json` is directly inside it. Open a terminal there and run:

```powershell
npm install
npm run dev
```

Visit `http://localhost:5173` in your browser. The site has no external npm dependencies; `npm install` just prepares the normal Node project files.

The updated Home page begins **“Engineering modern solutions for real-world impact.”** Hover the highlighted **MadeBySebi**, **Lucenex Corp**, or **GitHub** words in the story on a desktop to see the floating previews. The MadeBySebi card is green and the GitHub card shows Enoch's photo. If you still see an older headline, your browser is showing an earlier extracted folder. Stop that server, run the commands above from this new folder, and refresh the page.

## Open it without npm

Double-click `index.html` in this folder, or open `dist/index.html` in a browser. No package install or server is needed.

The ZIP includes the prebuilt website, source, project images, brand logos, Enoch's portrait for the GitHub preview, frontend tool icons, a self-hosted Geist font, and a PDF CV. The project pages, filtering, mobile navigation, links, and contact email work without a backend. Inline story links show image or branded preview cards on desktop hover and keyboard focus; they remain normal links on touch devices. The clients section displays the supplied logos in color; a compact toolkit sits below it. All pages share a footer with navigation, social links, and a contact prompt. Main actions use simple link and button states, with no text scramble or audio. Motion is reduced when the visitor requests reduced motion.

## Edit it

1. Change your name, email, Home headline (`heroTitle` and `heroMuted`), story (`heroStory` and `aboutStory`), project details, brand logos, and tool list in `src/content.json`. In a story paragraph, plain strings are regular text; an object like `{ "text": "GitHub", "link": "github" }` inserts a link. Change its URL and hover-card details in `linkPreviews`. Other section headings are in `build.py`.
2. Replace project images or brand logos in `src/assets/` and update their filenames in `src/content.json`.
3. Change layout and typography in `src/styles.css`.
4. Run `python3 build.py` to regenerate `dist/`.

The project uses Python's standard library only for generation. The delivered website itself is plain HTML, CSS, and JavaScript.

## Deploy

For Vercel, import this folder as a new project, set the framework preset to **Other**, and use `dist` as the output directory. The included `vercel.json` declares it. Run `python3 build.py` locally before committing changes so `dist` stays up to date.

For another static host, upload the contents of `dist/`.

## Included pages

- Home with selected projects, an introduction, client logos, and a frontend toolkit
- Filterable Projects page
- Six project detail pages
- About page with CV download
- Contact page with working email and social links
- 404 page

## Before publishing

Review project wording and links for accuracy. The three phone visuals for FEMMORA, Forever Peng Hair, and Gas Safety & Plumbing are illustrative concepts based on the supplied screenshots; they do not represent exact shipped mobile screens. The original screenshots remain in `src/assets/`. The contact link uses the email from his current CV. There is no contact-form backend.

Geist is provided under the SIL Open Font License in `GEIST-LICENSE.txt`. The frontend tool marks come from Simple Icons; its license is in `SIMPLE-ICONS-LICENSE.md`.
