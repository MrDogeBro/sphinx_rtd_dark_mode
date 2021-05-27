const createThemeSwitcher = () => {
  let btn = document.createElement('BUTTON');
  btn.className = 'theme-switcher';
  btn.id = 'themeSwitcher';
  btn.innerHTML = '<i class="fa fa-paint-brush"></i>';
  document.body.appendChild(btn);
};

$(document).ready(() => {
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
    document.documentElement.setAttribute('data-theme-enabled', 'false');
  } else {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
    document.documentElement.setAttribute('data-theme-enabled', 'true');
  }
};
