const loadTheme = () => {
  let theme = localStorage.getItem('theme');
  sessionStorage.setItem('availableThemes', '{available_themes}');
  sessionStorage.setItem('defaultTheme', '{default_theme}');

  if (theme !== null) {
    if (theme !== 'light')
      document.documentElement.setAttribute('data-theme-enabled', 'true');

    document.documentElement.setAttribute('data-theme', theme);
  } else {
    localStorage.setItem('theme', '{default_theme}');
    document.documentElement.setAttribute('data-theme', '{default_theme}');
    document.documentElement.setAttribute(
      'data-theme-enabled',
      '{default_theme_enabled}'
    );
  }
};

loadTheme();
