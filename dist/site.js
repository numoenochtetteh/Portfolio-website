const menuButton = document.querySelector(".menu-toggle");
const menu = document.querySelector("#main-nav");

if (menuButton && menu) {
  menuButton.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
    menuButton.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
  });
  menu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      menu.classList.remove("open");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Open navigation");
    });
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      menu.classList.remove("open");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Open navigation");
    }
  });
}

const filters = document.querySelectorAll(".filter");
const cards = document.querySelectorAll(".project-index .project-card");
const emptyState = document.querySelector(".empty-state");

filters.forEach((button) => {
  button.addEventListener("click", () => {
    const selected = button.dataset.filter;
    filters.forEach((filter) => {
      const active = filter === button;
      filter.classList.toggle("active", active);
      filter.setAttribute("aria-pressed", String(active));
    });
    let visibleCount = 0;
    cards.forEach((card) => {
      const visible = selected === "All" || card.dataset.category === selected;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });
    if (emptyState) emptyState.hidden = visibleCount !== 0;
  });
});

const previewLinks = document.querySelectorAll(".preview-link");
if (previewLinks.length) {
  const card = document.createElement("div");
  card.className = "hover-preview";
  card.setAttribute("aria-hidden", "true");
  card.innerHTML = '<div class="hover-preview-media"><img alt=""><span class="preview-mark"></span></div><div class="hover-preview-copy"><strong></strong><span></span></div>';
  document.body.append(card);

  const media = card.querySelector(".hover-preview-media");
  const image = media.querySelector("img");
  const mark = media.querySelector(".preview-mark");
  const title = card.querySelector(".hover-preview-copy strong");
  const detail = card.querySelector(".hover-preview-copy span");
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");
  let activeLink = null;

  const position = (x, y) => {
    const width = card.offsetWidth;
    const height = card.offsetHeight;
    let left = x + 20;
    if (left + width > window.innerWidth - 12) left = x - width - 20;
    let top = y - height - 18;
    if (top < 12) top = y + 20;
    card.style.left = `${Math.max(12, Math.min(left, window.innerWidth - width - 12))}px`;
    card.style.top = `${Math.max(12, Math.min(top, window.innerHeight - height - 12))}px`;
  };

  const show = (link, x, y) => {
    activeLink = link;
    media.className = `hover-preview-media ${link.dataset.previewTheme || "stone"} ${link.dataset.previewFit || "cover"}`;
    title.textContent = link.dataset.previewTitle || link.textContent;
    detail.textContent = link.dataset.previewDetail || "";
    if (link.dataset.previewImage) {
      image.src = `assets/${link.dataset.previewImage}`;
      image.hidden = false;
      mark.hidden = true;
    } else {
      image.removeAttribute("src");
      image.hidden = true;
      mark.textContent = link.dataset.previewMark || "";
      mark.hidden = false;
    }
    card.classList.add("visible");
    position(x, y);
  };
  const hide = () => {
    activeLink = null;
    card.classList.remove("visible");
  };

  previewLinks.forEach((link) => {
    link.addEventListener("pointerenter", (event) => {
      if (finePointer.matches) show(link, event.clientX, event.clientY);
    });
    link.addEventListener("pointermove", (event) => {
      if (finePointer.matches && activeLink === link) position(event.clientX, event.clientY);
    });
    link.addEventListener("pointerleave", hide);
    link.addEventListener("focusin", () => {
      if (!link.matches(":focus-visible")) return;
      const box = link.getBoundingClientRect();
      show(link, box.left + box.width / 2, box.top);
    });
    link.addEventListener("focusout", hide);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") hide();
  });
  window.addEventListener("scroll", hide, { passive: true });
}

