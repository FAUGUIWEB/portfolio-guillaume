const modal =
      document.getElementById(
        "videoModal"
      );

    const player =
      document.getElementById(
        "youtubePlayer"
      );

    function openVideo(videoId) {

      player.src =
        `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;

      modal.classList.add(
        "open"
      );

      document.body.style.overflow =
        "hidden";
    }

    function closeVideo(event) {

      if (
        event &&
        event.target !== modal
      ) {
        return;
      }

      modal.classList.remove(
        "open"
      );

      player.src = "";

      document.body.style.overflow = "";
    }

    document.addEventListener(
      "keydown",
      function(event) {

        if (
          event.key === "Escape"
        ) {
          closeVideo();
        }

      }
    );

    function scrollToNewDrop() {

      const target =
        document.getElementById(
          "new-drop"
        );

      if (!target) {
        return;
      }

      const header =
        document.querySelector(
          ".header-glass"
        );

      const headerHeight =
        header
          ? header.getBoundingClientRect().height
          : 60;

      const targetPosition =
        target.getBoundingClientRect().top +
        window.scrollY;

      window.scrollTo({
        top:
          targetPosition -
          headerHeight -
          35,
        behavior:
          "smooth"
      });
    }

    const projects =
      document.querySelectorAll(
        ".project"
      );

    const observer =
      new IntersectionObserver(

        function(entries) {

          entries.forEach(
            function(entry) {

              if (
                entry.isIntersecting
              ) {

                entry.target.classList.add(
                  "visible"
                );

                observer.unobserve(
                  entry.target
                );
              }

            }
          );

        },

        {
          threshold: 0.12
        }

      );

    projects.forEach(
      function(project) {

        observer.observe(
          project
        );

      }
    );

    const siteHeader =
      document.querySelector(
        ".site-header"
      );

    function updateHeader() {

      siteHeader.classList.toggle(
        "scrolled",
        window.scrollY > 40
      );

    }

    window.addEventListener(
      "scroll",
      updateHeader,
      {
        passive: true
      }
    );

    updateHeader();

    const heroParallaxArea =
      document.getElementById(
        "home"
      );

    const heroTitleStage =
      document.getElementById(
        "heroTitleStage"
      );

    const heroCassetteLayer =
      document.getElementById(
        "heroCassetteLayer"
      );

    const canUseMainHeroParallax =
      window.matchMedia(
        "(hover: hover) and (pointer: fine)"
      );

    if (
      heroParallaxArea &&
      heroTitleStage &&
      heroCassetteLayer &&
      canUseMainHeroParallax.matches
    ) {

      heroParallaxArea.addEventListener(
        "mousemove",
        function(event) {

          const rect =
            heroParallaxArea
              .getBoundingClientRect();

          const nx =
            (
              (event.clientX - rect.left) /
              rect.width
            ) - .5;

          const ny =
            (
              (event.clientY - rect.top) /
              rect.height
            ) - .5;

          heroTitleStage.style.setProperty(
            "--hero-text-x",
            `${nx * 12}px`
          );

          heroTitleStage.style.setProperty(
            "--hero-text-y",
            `${ny * 7}px`
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-x",
            `${nx * 72}px`
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-y",
            `${ny * 40}px`
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-ry",
            `${nx * 11}deg`
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-rx",
            `${ny * -8}deg`
          );
        }
      );

      heroParallaxArea.addEventListener(
        "mouseleave",
        function() {

          heroTitleStage.style.setProperty(
            "--hero-text-x",
            "0px"
          );

          heroTitleStage.style.setProperty(
            "--hero-text-y",
            "0px"
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-x",
            "0px"
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-y",
            "0px"
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-ry",
            "0deg"
          );

          heroCassetteLayer.style.setProperty(
            "--cassette-rx",
            "0deg"
          );
        }
      );
    }

    const heroShowreelTilt =
      document.getElementById(
        "heroShowreelTilt"
      );

    const heroShowreelArea =
      document.querySelector(
        ".hero-showreel"
      );

    const canUseHeroParallax =
      window.matchMedia(
        "(hover: hover) and (pointer: fine)"
      );

    if (
      heroShowreelTilt &&
      heroShowreelArea &&
      canUseHeroParallax.matches
    ) {

      heroShowreelArea.addEventListener(
        "mousemove",
        function(event) {

          const rect =
            heroShowreelArea.getBoundingClientRect();

          const x =
            (event.clientX - rect.left) /
            rect.width;

          const y =
            (event.clientY - rect.top) /
            rect.height;

          const rotateY =
            -7 + ((x - .5) * 3.2);

          const rotateX =
            1.5 - ((y - .5) * 2.4);

          heroShowreelTilt.style.setProperty(
            "--hero-ry",
            `${rotateY}deg`
          );

          heroShowreelTilt.style.setProperty(
            "--hero-rx",
            `${rotateX}deg`
          );
        }
      );

      heroShowreelArea.addEventListener(
        "mouseleave",
        function() {

          heroShowreelTilt.style.setProperty(
            "--hero-ry",
            "-8deg"
          );

          heroShowreelTilt.style.setProperty(
            "--hero-rx",
            "2deg"
          );
        }
      );
    }

    const heroSection =
      document.getElementById(
        "home"
      );

    const floatingShowreel =
      document.getElementById(
        "floatingShowreel"
      );

    if (heroSection && floatingShowreel) {

      const heroObserver =
        new IntersectionObserver(

          function(entries) {

            entries.forEach(
              function(entry) {

                floatingShowreel.classList.toggle(
                  "visible",
                  !entry.isIntersecting
                );
              }
            );
          },
          {
            threshold: 0.12
          }
        );

      heroObserver.observe(
        heroSection
      );
    }

    const newDropGrid =
      document.getElementById(
        "newDropGrid"
      );

    const newDropPrev =
      document.getElementById(
        "newDropPrev"
      );

    const newDropNext =
      document.getElementById(
        "newDropNext"
      );

    function updateNewDropArrows() {

      if (!newDropGrid) {
        return;
      }

      const maxScroll =
        newDropGrid.scrollWidth -
        newDropGrid.clientWidth;

      const currentScroll =
        newDropGrid.scrollLeft;

      newDropPrev
        .classList
        .toggle(
          "disabled",
          currentScroll <= 5
        );

      newDropNext
        .classList
        .toggle(
          "disabled",
          currentScroll >= maxScroll - 5
        );
    }

    function getNewDropStep() {

      const card =
        newDropGrid.querySelector(
          ".new-drop-card"
        );

      if (!card) {
        return 0;
      }

      const style =
        window.getComputedStyle(
          newDropGrid
        );

      const gap =
        parseFloat(
          style.columnGap
        ) || 18;

      return (
        card.offsetWidth +
        gap
      );
    }

    newDropPrev.addEventListener(
      "click",
      function() {

        newDropGrid.scrollBy({
          left:
            -getNewDropStep() * 4,
          behavior:
            "smooth"
        });
      }
    );

    newDropNext.addEventListener(
      "click",
      function() {

        newDropGrid.scrollBy({
          left:
            getNewDropStep() * 4,
          behavior:
            "smooth"
        });
      }
    );

    newDropGrid.addEventListener(
      "scroll",
      updateNewDropArrows,
      {
        passive: true
      }
    );

    window.addEventListener(
      "resize",
      updateNewDropArrows
    );

    let isDragging = false;
    let dragStartX = 0;
    let dragScrollLeft = 0;

    newDropGrid.addEventListener(
      "mousedown",
      function(event) {

        isDragging = true;

        newDropGrid.classList.add(
          "dragging"
        );

        dragStartX =
          event.pageX -
          newDropGrid.offsetLeft;

        dragScrollLeft =
          newDropGrid.scrollLeft;
      }
    );

    newDropGrid.addEventListener(
      "mouseleave",
      stopDragging
    );

    newDropGrid.addEventListener(
      "mouseup",
      stopDragging
    );

    function stopDragging() {

      isDragging = false;

      newDropGrid.classList.remove(
        "dragging"
      );
    }

    newDropGrid.addEventListener(
      "mousemove",
      function(event) {

        if (!isDragging) {
          return;
        }

        event.preventDefault();

        const x =
          event.pageX -
          newDropGrid.offsetLeft;

        const walk =
          (
            x -
            dragStartX
          ) * 1.2;

        newDropGrid.scrollLeft =
          dragScrollLeft -
          walk;
      }
    );

    const aboutSection = document.querySelector(".about");
    const aboutLiquid = document.getElementById("aboutLiquid");

    if (aboutSection) {
      const aboutRevealObserver =
        new IntersectionObserver(
          function(entries) {
            entries.forEach(
              function(entry) {
                if (entry.isIntersecting) {
                  aboutSection.classList.add("is-visible");
                  aboutRevealObserver.unobserve(aboutSection);
                }
              }
            );
          },
          {
            threshold: 0.28
          }
        );

      aboutRevealObserver.observe(aboutSection);
    }

    if (aboutSection && aboutLiquid && window.matchMedia("(min-width: 801px)").matches) {
      aboutSection.addEventListener("mousemove", function(event) {
        const rect = aboutSection.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;

        aboutLiquid.style.setProperty("--about-x", `${x * 26}px`);
        aboutLiquid.style.setProperty("--about-y", `${y * 18}px`);
      });

      aboutSection.addEventListener("mouseleave", function() {
        aboutLiquid.style.setProperty("--about-x", "0px");
        aboutLiquid.style.setProperty("--about-y", "0px");
      });
    }

    updateNewDropArrows();