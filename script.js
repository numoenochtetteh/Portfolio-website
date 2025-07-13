// // =================== YOUR OLD TAB CODE ===================
// // Keep this if you have other tabs elsewhere
// const tabs = document.querySelectorAll(".project-tabs button");
// const content = document.querySelector(".project-content");

// tabs.forEach(btn => {
//   btn.addEventListener("click", () => {
//     tabs.forEach(b => b.classList.remove("active"));
//     btn.classList.add("active");

//     // You can expand this part to switch tab-specific content
//   });
// });

// // =================== NEW PROJECT SWITCHING ===================
// // Your project data
// const projects = {
//   elegante: {
//     title: "Eleganté Shop",
//     description: "E-commerce app with seamless shopping experience, lightning-fast performance, secure authentication and a sleek design ensuring a hassle-free journey for users.",
//     image: "chpic.jpg",
//     badges: ["NEXT.JS", "REACT HOOKS", "NEXT AUTH", "MONGODB", "TAILWIND CSS"],
//     liveSite: "#",
//     codeLink: "#"
//   },
//   tourbuddy: {
//     title: "Tour Buddy",
//     description: "Tour Buddy helps travelers plan trips with smart itineraries and recommendations.",
//     image: "conpic.jpg",
//     badges: ["REACT", "NODE.JS", "EXPRESS", "MONGODB"],
//     liveSite: "#",
//     codeLink: "#"
//   },
//   churchblog: {
//     title: "Church Blog",
//     description: "A blog platform for church communities to share news and events easily.",
//     image: "fopic.jpg",
//     badges: ["HTML", "CSS", "JAVASCRIPT"],
//     liveSite: "#",
//     codeLink: "#"
//   },
//   triciakissi: {
//     title: "Tricia Kissi",
//     description: "Personal portfolio website for showcasing projects and skills.",
//     image: "barberingweb.jpg",
//     badges: ["HTML", "CSS", "JAVASCRIPT"],
//     liveSite: "#",
//     codeLink: "#"
//   }
// };

// // Sidebar nav items
// const navItems = document.querySelectorAll(".nav-item");

// // Get elements to update
// const projectImage = document.getElementById("project-image");
// const projectTitle = document.getElementById("project-title");
// const projectDescription = document.getElementById("project-description");
// const techBadges = document.getElementById("tech-badges");
// const liveSite = document.getElementById("live-site");
// const codeLink = document.getElementById("code-link");

// // Handle sidebar clicks
// navItems.forEach(item => {
//   item.addEventListener("click", () => {
//     // Remove active from all, add to clicked
//     navItems.forEach(i => i.classList.remove("active"));
//     item.classList.add("active");

//     // Get project key
//     const projectKey = item.getAttribute("data-project");
//     const project = projects[projectKey];

//     // Update content
//     projectImage.src = project.image;
//     projectTitle.textContent = project.title;
//     projectDescription.textContent = project.description;

//     // Update badges
//     techBadges.innerHTML = "";
//     project.badges.forEach(badge => {
//       const span = document.createElement("span");
//       span.textContent = badge;
//       span.className = "badge";
//       techBadges.appendChild(span);
//     });

//     // Update links
//     liveSite.href = project.liveSite;
//     codeLink.href = project.codeLink;
//   });
// });





// // =================== Initialize on page load ===================
// // Find the nav-item that is active by default
// const defaultActive = document.querySelector(".nav-item.active");

// if (defaultActive) {
//   const projectKey = defaultActive.getAttribute("data-project");
//   const project = projects[projectKey];

//   // Update image & text on page load
//   projectImage.src = project.image;
//   projectTitle.textContent = project.title;
//   projectDescription.textContent = project.description;

//   techBadges.innerHTML = "";
//   project.badges.forEach(badge => {
//     const span = document.createElement("span");
//     span.className = "badge";
//     span.textContent = badge;
//     techBadges.appendChild(span);
//   });

//   liveSite.href = project.liveSite;
//   codeLink.href = project.codeLink;
// }























































// =================== YOUR OLD TAB CODE ===================
// Keep this if you have other tabs elsewhere
const tabs = document.querySelectorAll(".project-tabs button");
const content = document.querySelector(".project-content");

tabs.forEach(btn => {
  btn.addEventListener("click", () => {
    tabs.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    // You can expand this part to switch tab-specific content
  });
});

// =================== NEW PROJECT SWITCHING ===================
// Your project data
const projects = {
  elegante: {
    title: "eCommerce Website",
    description: "A modern e-commerce website with smooth navigation, fast loading, secure authentication, and a clean, user-friendly design for an easy and enjoyable shopping experience.",
    image: "mix.jpg",
    badges: ["NEXT.JS", "REACT HOOKS", "NEXT AUTH", "MONGODB", "TAILWIND CSS"],
    liveSite: "#",
    codeLink: "#"
  },
  tourbuddy: {
    title: "Barbering Shop Website",
    description: "A clean and fast-loading website that highlights services, prices, and gallery with easy booking and smooth navigation.",
    image: "mixx.jpg",
    badges: ["REACT", "NODE.JS", "EXPRESS", "MONGODB"],
    liveSite: "#",
    codeLink: "#"
  },
  churchblog: {
    title: "WordPress E-Commerce Website",
    description: "E-commerce website built with WordPress to showcase products, manage orders, and support customer interactions.",
    image: "mix22.jpg",
    badges: ["HTML", "CSS", "JAVASCRIPT"],
    liveSite: "#",
    codeLink: "#"
  },
  triciakissi: {
    title: "Supermarket Website",
    description: "Supermarket website built for a local business to display products, share store info, and enable customer contact.",
    image: "mixx1.jpg",
    badges: ["HTML", "CSS", "JAVASCRIPT"],
    liveSite: "#",
    codeLink: "#"
  }
};

// Sidebar nav items
const navItems = document.querySelectorAll(".nav-item");

// Get elements to update
const projectImage = document.getElementById("project-image");
const projectTitle = document.getElementById("project-title");
const projectDescription = document.getElementById("project-description");
const techBadges = document.getElementById("tech-badges");
const liveSite = document.getElementById("live-site");
const codeLink = document.getElementById("code-link");

// Handle sidebar clicks
navItems.forEach(item => {
  item.addEventListener("click", () => {
    // Remove active from all, add to clicked
    navItems.forEach(i => i.classList.remove("active"));
    item.classList.add("active");

    // Get project key
    const projectKey = item.getAttribute("data-project");
    const project = projects[projectKey];

    // Update content
    projectImage.src = project.image;
    projectTitle.textContent = project.title;
    projectDescription.textContent = project.description;

    // Update badges
    techBadges.innerHTML = "";
    project.badges.forEach(badge => {
      const span = document.createElement("span");
      span.textContent = badge;
      span.className = "badge";

      // Add color class based on badge text
      const className = badge.toLowerCase().replace(/\s+/g, '-').replace(/\./g, '');
      span.classList.add(className);

      techBadges.appendChild(span);
    });

    // Update links
    liveSite.href = project.liveSite;
    codeLink.href = project.codeLink;
  });
});

// =================== Initialize on page load ===================
// Find the nav-item that is active by default
const defaultActive = document.querySelector(".nav-item.active");

if (defaultActive) {
  const projectKey = defaultActive.getAttribute("data-project");
  const project = projects[projectKey];

  // Update image & text on page load
  projectImage.src = project.image;
  projectTitle.textContent = project.title;
  projectDescription.textContent = project.description;

  techBadges.innerHTML = "";
  project.badges.forEach(badge => {
    const span = document.createElement("span");
    span.textContent = badge;
    span.className = "badge";

    // Add color class based on badge text
    const className = badge.toLowerCase().replace(/\s+/g, '-').replace(/\./g, '');
    span.classList.add(className);

    techBadges.appendChild(span);
  });

  liveSite.href = project.liveSite;
  codeLink.href = project.codeLink;
}
