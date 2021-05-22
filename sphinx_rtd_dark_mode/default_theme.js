const loadTheme = () => {
  let theme = localStorage.getItem('theme');

  if (theme !== null) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      document.documentElement.setAttribute('data-theme-enabled', 'true');
    }
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
