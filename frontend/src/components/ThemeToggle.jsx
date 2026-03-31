function ThemeToggle({ theme, setTheme }) {
  return (
    <div className="themeToggle" role="group" aria-label="Theme toggle">
      <button
        type="button"
        className={theme === 'fog' ? 'themeToggleButton isActive fog' : 'themeToggleButton fog'}
        onClick={() => setTheme('fog')}
      >
        fog
      </button>
      <button
        type="button"
        className={theme === 'blossom' ? 'themeToggleButton isActive blossom' : 'themeToggleButton blossom'}
        onClick={() => setTheme('blossom')}
      >
        blossom
      </button>
    </div>
  )
}

export default ThemeToggle
