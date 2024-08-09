document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu_toggle');
  const menuMob = document.getElementById('menu_mob');
  menuToggle.addEventListener('click', function () {
    if (menuMob.classList.contains('open')) {
      menuMob.classList.remove('open');
      setTimeout(() => {
        menuMob.style.display = 'none';
      }, 500);
    } else {
      menuMob.style.display = 'block';
      setTimeout(() => {
        menuMob.classList.add('open');
      }, 10);
    }
  });

});
