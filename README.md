# Modern Portfolio Website

A clean, responsive portfolio website built with HTML, CSS, and JavaScript. This template is designed to showcase your projects and skills in a modern, professional way.

## Features

- Responsive design that works on all devices
- Smooth scrolling navigation
- Animated project cards
- Contact form
- Social media links
- Modern UI with clean typography
- Optimized performance

## Getting Started

1. Clone this repository or download the files
2. Open `index.html` in your browser to view the website
3. Customize the content in `index.html` with your information
4. Modify the styles in `styles.css` to match your preferences
5. Update the JavaScript functionality in `script.js` if needed

## Customization

### Personal Information

Edit the following sections in `index.html`:

- Your name and title in the hero section
- About me section
- Skills list
- Project cards
- Contact information
- Social media links

### Styling

The website uses CSS variables for easy customization. Edit the following in `styles.css`:

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #1e40af;
  --text-color: #1f2937;
  --light-text: #6b7280;
  --background: #ffffff;
  --section-bg: #f3f4f6;
}
```

### Projects

Add your projects by duplicating the project card structure in `index.html`:

```html
<div class="project-card">
  <div class="project-image">
    <img src="path-to-your-image" alt="Project Name" />
  </div>
  <div class="project-info">
    <h3>Project Name</h3>
    <p>Project description</p>
    <div class="project-links">
      <a href="#" class="btn small">View Demo</a>
      <a href="#" class="btn small">Source Code</a>
    </div>
  </div>
</div>
```

## Deployment

To deploy your portfolio website:

1. Choose a hosting service (GitHub Pages, Netlify, Vercel, etc.)
2. Upload your files to the hosting service
3. Configure your domain name if needed

## Contributing

Feel free to fork this project and customize it for your needs. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
