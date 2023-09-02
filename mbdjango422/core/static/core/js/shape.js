$(document).ready(function () {
  // Home animation
  gsap.registerPlugin(ScrollTrigger, TextPlugin);
  // gsap.registerPlugin(TextPlugin);

  // Animación Intro
  let t1 = gsap.timeline({
    scrollTrigger: {
      trigger: '.welcome-content',
    },
  });

  let t2 = gsap.timeline({
    scrollTrigger: {
      trigger: '.eslogan-mb',
    },
  });

  // Shape Morph
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

  // Media Queries
  if (window.matchMedia('(min-width: 846px)').matches) {
    t1.from('.welcome-content-image', { x: 600, duration: 1.5 }).from(
      '.anim1',
      { y: -50, opacity: 0, duration: 1, stagger: 0.2 },
      '-=0.6',
    );
  }

  if (window.matchMedia('(min-width: 926px)').matches) {
    t2.from('#eslogan-text', {
      duration: 1,
      text: {
        value: '',
      },
    });
  }
});
