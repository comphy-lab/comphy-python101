function prepareCourseControls() {
  const controls = [
    {
      selector: ".md-header label[for='__drawer']",
      label: "Open navigation",
      toggleId: "__drawer",
      region: ".md-sidebar--primary",
      regionId: "course-navigation",
    },
    {
      selector: ".md-header label[for='__search']",
      label: "Open search",
      toggleId: "__search",
      region: "[data-md-component='search']",
      regionId: "course-search",
    },
    {
      selector: ".md-search label.md-search__icon[for='__search']",
      label: "Close search",
      toggleId: "__search",
      region: "[data-md-component='search']",
      regionId: "course-search",
      closeControl: true,
    },
  ];

  for (const config of controls) {
    const { selector, label, toggleId, regionId, closeControl } = config;
    const control = document.querySelector(selector);
    if (!control || control.dataset.courseControlReady) continue;
    const toggle = document.getElementById(toggleId);
    const region = document.querySelector(config.region);
    if (region && !region.id) region.id = regionId;
    const controlledId = region?.id || regionId;
    control.dataset.courseControlReady = "true";
    control.setAttribute("role", "button");
    control.setAttribute("tabindex", "0");
    control.setAttribute("aria-label", label);
    control.setAttribute("aria-controls", controlledId);
    const syncState = () => {
      if (!toggle) return;
      if (closeControl) {
        control.setAttribute("tabindex", toggle.checked ? "0" : "-1");
      } else {
        control.setAttribute("aria-expanded", String(toggle.checked));
      }
    };
    syncState();
    toggle?.addEventListener("change", syncState);
    control.addEventListener("keydown", (event) => {
      if (event.key !== "Enter" && event.key !== " ") return;
      event.preventDefault();
      event.stopPropagation();
      control.click();
    });
  }

  const query = document.querySelector("[data-md-component='search-query']");
  if (query && !query.dataset.courseInputReady) {
    query.dataset.courseInputReady = "true";
    query.addEventListener("input", () => {
      query.dispatchEvent(new KeyboardEvent("keyup", { bubbles: true }));
    });
  }
}

prepareCourseControls();
if (typeof document$ !== "undefined") document$.subscribe(prepareCourseControls);
