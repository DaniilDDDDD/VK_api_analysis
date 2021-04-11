module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
   darkMode: false, 
   theme: {
     extend: {
      spacing: {
        '72': '18rem',
        '84': '21rem',
        '96': '24rem',
        '120' : '40rem',
      }
     },
   },
   variants: {
     extend: {},
   },
   plugins: [],
 }