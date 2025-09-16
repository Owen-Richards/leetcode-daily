#!/bin/bash
# GitHub Repository Setup Script
# Run this script after creating the repository on GitHub

echo "🚀 LeetCode Daily - GitHub Setup Script"
echo "======================================"
echo

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "templates" ]; then
    echo "❌ Error: Please run this script from the leetcode-daily directory"
    exit 1
fi

echo "📊 Repository Status:"
git status --short
echo

echo "🔗 Remote Configuration:"
git remote -v
echo

echo "📤 Attempting to push to GitHub..."
echo "If this fails, make sure you've created the repository on GitHub first!"
echo

# Try to push
if git push -u origin main; then
    echo
    echo "🎉 SUCCESS! Repository pushed to GitHub!"
    echo
    echo "🌐 Your repository is now available at:"
    echo "   https://github.com/Owen-Richards/leetcode-daily"
    echo
    echo "📋 Next Steps:"
    echo "   1. Visit your repository on GitHub to see your code"
    echo "   2. Star your own repository (optional but fun!)"
    echo "   3. Set up GitHub Action secrets for auto-updates:"
    echo "      - Go to Settings → Secrets and variables → Actions"
    echo "      - Add secret: PROFILE_README_TOKEN"
    echo "   4. Start your daily practice:"
    echo "      python scripts/new_problem.py \"Problem Name\" \"difficulty\" \"languages\""
    echo
    echo "🚀 Happy coding!"
else
    echo
    echo "❌ Push failed. Please make sure:"
    echo "   1. You've created the 'leetcode-daily' repository on GitHub"
    echo "   2. The repository is public"
    echo "   3. You didn't initialize it with README, .gitignore, or license"
    echo "   4. You're authenticated with GitHub (git credentials)"
    echo
    echo "🔧 To create the repository:"
    echo "   1. Go to https://github.com/Owen-Richards"
    echo "   2. Click 'New repository'"
    echo "   3. Name it 'leetcode-daily'"
    echo "   4. Make it public"
    echo "   5. DON'T check any initialization options"
    echo "   6. Click 'Create repository'"
    echo "   7. Run this script again"
fi
