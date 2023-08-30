$(document).ready(function () {
  // Home animation
  gsap.registerPlugin(ScrollTrigger);
  gsap.registerPlugin(TextPlugin);

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

  // t2.from('#eslogan-text', {
  //   duration: 1,
  //   text: {
  //     value: '',
  //   },
  // });

  // if (window.matchMedia('(min-width: 846px)').matches) {
  //   t1.from('.welcome-content-image', { x: 600, duration: 1 }).from(
  //     '.anim1',
  //     { y: -50, opacity: 0, duration: 1, stagger: 0.2 },
  //     '-=1',
  //   );
  // }

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
  const imgzoom2 = document.querySelectorAll('.portafolio-home .item-portafolio-home');

  // imgzoom2.forEach((element) => {
  //   const contents = element.querySelectorAll('.item-portafolio-home-image');

  //   gsap.set(contents, { scale: 0 });
  //   gsap.to(contents, {
  //     duration: 1.2,
  //     autoAlpha: 1,
  //     scale: 1,
  //     ease: 'power2.out',
  //     scrollTrigger: {
  //       trigger: element,
  //       start: 'top bottom-=100',
  //       end: 'bottom top+=100',
  //       toggleActions: 'play reverse play reverse',
  //     },
  //   });
  // });

  // Media Queries
  if (window.matchMedia('(min-width: 846px)').matches) {
    t1.from('.welcome-content-image', { x: 600, duration: 1 }).from(
      '.anim1',
      { y: -50, opacity: 0, duration: 1, stagger: 0.2 },
      '-=1',
    );
  }

  if (window.matchMedia('(min-width: 926px)').matches) {
    t2.from('#eslogan-text', {
      duration: 1,
      text: {
        value: '',
      },
    });

    imgzoom2.forEach((element) => {
      const contents = element.querySelectorAll('.item-portafolio-home-image');

      gsap.set(contents, { scale: 0 });
      gsap.to(contents, {
        duration: 1.2,
        autoAlpha: 1,
        scale: 1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: element,
          start: 'top bottom-=100',
          end: 'bottom top+=100',
          // toggleActions: 'play reverse play reverse',
          toggleActions: 'play',
        },
      });
    });
  }
});
