# Portfolio Deployment Guide

This guide will help you deploy your portfolio so you can share it with others.

## Option 1: Streamlit Cloud (Recommended for Main App)

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code to the repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and main branch
5. Set the file path to `app.py`
6. Click "Deploy"

Your app will be available at: `https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app`

## Option 2: GitHub Pages (For Static Portfolio)

### Step 1: Enable GitHub Pages

1. Go to your repository settings
2. Scroll down to "Pages" section
3. Select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click "Save"

Your portfolio will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## Option 3: Render (For Demo Projects)

### Deploy Computer Vision Demo

1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r demos/computer_vision/requirements.txt`
5. Set start command: `cd demos/computer_vision && gunicorn app:app`
6. Deploy

### Deploy NLP Demo

1. Create another Web Service on Render
2. Set build command: `pip install -r demos/nlp/requirements.txt`
3. Set start command: `cd demos/nlp && gunicorn app:app`
4. Deploy

## Option 4: Heroku (Alternative)

### Step 1: Install Heroku CLI

Download and install from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

### Step 2: Deploy

```bash
heroku create your-app-name
git push heroku main
```

## Quick Deployment Commands

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## Update Portfolio Links

After deployment, update the links in your `index.html` file to point to your deployed applications.

## Troubleshooting

### Common Issues:

1. **Import errors**: Make sure all dependencies are in requirements.txt
2. **Port issues**: Use `os.environ.get('PORT', 5000)` for port configuration
3. **File paths**: Use relative paths for deployment
4. **Memory limits**: Some platforms have memory restrictions for free tiers

### Support:

- Streamlit Cloud: [docs.streamlit.io](https://docs.streamlit.io/streamlit-community-cloud)
- GitHub Pages: [pages.github.com](https://pages.github.com)
- Render: [render.com/docs](https://render.com/docs)
