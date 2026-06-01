/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      colors: {
        background: '#faf9fd',
        surface: '#faf9fd',
        'surface-container-lowest': '#ffffff',
        'surface-container-low': '#f5f3f7',
        'surface-container': '#efedf1',
        'surface-container-high': '#e9e7ec',
        'outline-variant': '#cbc3d9',
        'on-surface': '#1b1b1f',
        'on-surface-variant': '#494456',
        outline: '#7a7488',
        primary: '#5800d8',
        'primary-strong': '#4300a8',
        'primary-fixed': '#e8ddff',
        'primary-soft': '#e6daff',
        secondary: '#5740d8',
        tertiary: '#5817cc',
        error: '#ba1a1a',
        success: '#10b981',
      },
      maxWidth: {
        container: '1280px',
      },
      backgroundImage: {
        'map-pattern': 'radial-gradient(circle at 20% 20%, rgba(16, 185, 129, 0.24), transparent 28%), radial-gradient(circle at 78% 30%, rgba(88, 0, 216, 0.20), transparent 30%), linear-gradient(135deg, #eef2ff 0%, #f8fafc 52%, #ecfdf5 100%)',
      },
      borderRadius: {
        xl: '0.75rem',
      },
    },
  },
  plugins: [],
}
