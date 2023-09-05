$(document).ready(function () {
  console.log(window.location.pathname)
  // Home animation
  gsap.registerPlugin(ScrollTrigger, TextPlugin);

  let t2 = gsap.timeline({
    scrollTrigger: {
      trigger: '.eslogan-mb',
    },
  });


  // Shape Morph Anime.js
  {
    class MorphingBG {
      constructor(el) {
        this.DOM = {};
        this.DOM.el = el;
        this.DOM.paths = Array.from(this.DOM.el.querySelectorAll('path'));
        this.animate();
      }
      animate() {
        this.DOM.paths.forEach((path) => {
          setTimeout(
            () => {
              anime({
                targets: path,
                duration: anime.random(3000, 5000),
                easing: [0.5, 0, 0.5, 1],
                d: path.getAttribute('pathdata:id'),
                loop: true,
                direction: 'alternate',
              });
            },
            anime.random(0, 1000),
          );
        });
      }
    }

    new MorphingBG(document.querySelector('svg.scene'));
  }


  // Portafolio Gallería
  if (window.location.pathname == '/') {
    let proxy = { skew: 0 },
      skewSetter = gsap.quickSetter('.item-portafolio-home-image', 'skewY', 'deg'), // fast
      clamp = gsap.utils.clamp(-20, 20); // don't let the skew go beyond 20 degrees.

    ScrollTrigger.create({
      onUpdate: (self) => {
        let skew = clamp(self.getVelocity() / -300);
        // only do something if the skew is MORE severe. Remember, we're always tweening back to 0, so if the user slows
        // their scrolling quickly, it's more natural to just let the tween handle that smoothly rather than jumping to
        // the smaller skew.
        if (Math.abs(skew) > Math.abs(proxy.skew)) {
          proxy.skew = skew;
          gsap.to(proxy, {
            skew: 0,
            duration: 0.8,
            ease: 'power3',
            overwrite: true,
            onUpdate: () => skewSetter(proxy.skew),
          });
        }
      },
    });

    // make the right edge "stick" to the scroll bar. force3D: true improves performance
    gsap.set('.item-portafolio-home-image', { transformOrigin: 'right center', force3D: true });
  }


  // Media Queries
  if (window.matchMedia('(min-width: 926px)').matches) {
    t2.from('#eslogan-text', {
      duration: 1,
      text: {
        value: '',
      },
    });
  }


  // Text Reveal
  gsap.utils.toArray('.revealUp').forEach(function (elem) {
    ScrollTrigger.create({
      trigger: elem,
      start: 'top 80%',
      end: 'bottom 20%',
      markers: false,
      onEnter: function () {
        gsap.fromTo(
          elem,
          { y: 100, autoAlpha: 0 },
          {
            duration: 1.25,
            y: 0,
            autoAlpha: 1,
            ease: 'back',
            overwrite: 'auto',
          },
        );
      },
      onLeave: function () {
        gsap.fromTo(elem, { autoAlpha: 1 }, { autoAlpha: 0, overwrite: 'auto' });
      },
      onEnterBack: function () {
        gsap.fromTo(
          elem,
          { y: -100, autoAlpha: 0 },
          {
            duration: 1.25,
            y: 0,
            autoAlpha: 1,
            ease: 'back',
            overwrite: 'auto',
          },
        );
      },
      onLeaveBack: function () {
        gsap.fromTo(elem, { autoAlpha: 1 }, { autoAlpha: 0, overwrite: 'auto' });
      },
    });
  });
});
