#!/usr/bin/env python3
"""
Portfolio Deployment Helper Script
This script helps you prepare your portfolio for deployment.
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_git_status():
    """Check if git is initialized and has commits."""
    try:
        result = subprocess.run("git status", shell=True, capture_output=True, text=True)
        return "not a git repository" not in result.stderr
    except:
        return False

def main():
    print("🚀 Portfolio Deployment Helper")
    print("=" * 40)
    
    # Check if git is installed
    if not run_command("git --version", "Checking Git installation"):
        print("❌ Git is not installed. Please install Git first.")
        return
    
    # Initialize git if not already done
    if not check_git_status():
        print("\n📁 Initializing Git repository...")
        if not run_command("git init", "Initializing Git repository"):
            return
        
        if not run_command("git add .", "Adding files to Git"):
            return
        
        if not run_command('git commit -m "Initial portfolio commit"', "Making initial commit"):
            return
    
    print("\n✅ Your portfolio is ready for deployment!")
    print("\n📋 Next steps:")
    print("1. Create a GitHub repository")
    print("2. Add your GitHub repository as remote:")
    print("   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git")
    print("3. Push your code:")
    print("   git push -u origin main")
    print("4. Deploy using one of the options in DEPLOYMENT.md")
    
    print("\n🌐 Deployment Options:")
    print("- Streamlit Cloud: For your main AI app")
    print("- GitHub Pages: For your static portfolio")
    print("- Render: For your demo projects")
    
    print("\n📖 See DEPLOYMENT.md for detailed instructions!")

if __name__ == "__main__":
    main() 