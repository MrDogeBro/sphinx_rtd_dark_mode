const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

const createThemeSwitcher = () => {
  const availableThemes = JSON.parse(sessionStorage.getItem('availableThemes'));

  let btn = document.createElement('BUTTON');
  btn.className = 'theme-switcher-btn';
  btn.id = 'themeSwitcherBtn';
  btn.innerHTML = '<i class="fa fa-paint-brush"></i>';
  document.body.appendChild(btn);

  let themes = document.createElement('DIV');
  themes.className = 'theme-switcher';
  themes.id = 'themeSwitcher';
  themeSwitcherHtml = '';

  for (i = 0; i < availableThemes.length; i++) {
    let themeName = capitalize(availableThemes[i]);

    themeSwitcherHtml += '<p id="theme' + themeName + '">' + themeName + '</p>';
  }

  themes.innerHTML = themeSwitcherHtml;
};

$(document).ready(() => {
  createThemeSwitcher();
  $('#themeSwitcherBtn').click(switchTheme);

  $('footer').html(
    $('footer').html() +
      'Dark theme provided by <a href="https://github.com/MrDogeBro">MrDogeBro</a>.'
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
