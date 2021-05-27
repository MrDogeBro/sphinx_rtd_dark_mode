const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

const createThemeSwitcher = () => {
  const availableThemes = JSON.parse(sessionStorage.getItem('availableThemes'));
  const defaultTheme = sessionStorage.getItem('defaultTheme');
  let themeIDs = [];

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
    let themeName =
      capitalize(availableThemes[i]) +
      (defaultTheme === availableThemes[i] ? ' (default)' : '');
    let themeID = 'theme' + capitalize(availableThemes[i]);

    themeSwitcherHtml +=
      '<p data-name="' +
      availableThemes[i] +
      '" id="' +
      themeID +
      '">' +
      themeName +
      '</p>';
    themeIDs.push(themeID);
  }

  themes.innerHTML = themeSwitcherHtml;
  document.body.appendChild(themes);
  $('#themeSwitcher').hide();

  for (i = 0; i < themeIDs.length; i++) {
    $('#' + themeIDs[i]).click(switchTheme);
  }
};

$(document).ready(() => {
  createThemeSwitcher();
  $('#themeSwitcherBtn').click(toggleThemeSwitcher);

  $('footer').html(
    $('footer').html() +
      'Dark theme provided by <a href="https://github.com/MrDogeBro">MrDogeBro</a>.'
  );
});

const toggleThemeSwitcher = () => {
  $('#themeSwitcher').toggle();
};

const switchTheme = (e) => {
  const theme = e.target.dataset.name;

  localStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-theme', theme);
  toggleThemeSwitcher();

  if (theme === 'light')
    return document.documentElement.setAttribute('data-theme-enabled', 'false');
  document.documentElement.setAttribute('data-theme-enabled', 'true');
};
