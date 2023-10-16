// Плавная прокрутка при клике на меню
const menuLinks = document.querySelectorAll('.nav-link[href^="#"]');

menuLinks.forEach(link => {
  link.addEventListener('click', smoothScroll);
});

function smoothScroll(e) {
  e.preventDefault();

  const targetId = e.target.getAttribute('href');
  const target = document.querySelector(targetId);

  target.scrollIntoView({
    behavior: 'smooth'
  });
}

// Выделяем активную ссылку меню
const sections = document.querySelectorAll('section[id]');

function setActiveMenuItem() {
  const currentSection = document.querySelector('section:nth-of-type(1)');

  for (let menuLink of menuLinks) {
    if (menuLink.getAttribute('href') === '#' + currentSection.id) {
      menuLink.classList.add('selected');
    } else {
      menuLink.classList.remove('selected');
    }
  }
}

setActiveMenuItem();

// Обновляем при скролле
window.addEventListener('scroll', setActiveMenuItem);