const createThemeSwitcher = () => {
  let btn = document.createElement('BUTTON');
  btn.className = 'theme-switcher';
  btn.id = 'themeSwitcher';
  btn.innerHTML =
    '<i id=themeMoon class="fas fa-moon"></i><i id=themeSun class="fas fa-sun"></i>';
  document.body.appendChild(btn);

  if (localStorage.getItem('theme') === 'dark') $('#themeMoon').hide(0);
  else $('#themeSun').hide(0);
};

$(document).ready(() => {
  $('head').append(
    '<script src="https://kit.fontawesome.com/ea3a6b8494.js" crossorigin="anonymous"></script>'
  );
  createThemeSwitcher();

  $('#themeSwitcher').click(switchTheme);

  $('footer').html(
    $('footer').html() +
      'Dark theme provided by <a href="http://mrdogebro.com">MrDogeBro</a>.'
  );
});

const switchTheme = () => {
  if (localStorage.getItem('theme') === 'dark') {
    localStorage.setItem('theme', 'light');
    document.documentElement.setAttribute('data-theme', 'light');

    $('#themeSun').fadeOut(200, () => {
      $('#themeMoon').fadeIn(200);
    });
  } else {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');

    $('#themeMoon').fadeOut(200, () => {
      $('#themeSun').fadeIn(200);
    });
  }
};
