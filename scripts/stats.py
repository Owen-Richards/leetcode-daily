#!/usr/bin/env python3
"""
LeetCode Repository Statistics Script

Generates statistics about solved problems, languages used, and progress.
"""

import os
import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

class LeetCodeStats:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.language_dirs = ["python", "javascript", "java", "cpp", "rust"]
        self.language_extensions = {
            "python": ".py",
            "javascript": ".js",
            "java": ".java", 
            "cpp": ".cpp",
            "rust": ".rs"
        }
        
    def count_problems_by_language(self):
        """Count problems solved in each language"""
        stats = {}
        
        for lang in self.language_dirs:
            lang_dir = self.root_dir / lang
            if lang_dir.exists():
                files = list(lang_dir.glob(f"*{self.language_extensions[lang]}"))
                # Filter out template files
                problem_files = [f for f in files if not f.name.startswith("template")]
                stats[lang] = len(problem_files)
            else:
                stats[lang] = 0
                
        return stats
        
    def get_problem_list(self):
        """Get list of all problems with metadata"""
        problems = []
        notes_dir = self.root_dir / "notes"
        
        if notes_dir.exists():
            for md_file in notes_dir.glob("*.md"):
                if md_file.name.startswith("template"):
                    continue
                    
                problem_name = md_file.stem.replace("_", " ").title()
                
                # Try to extract metadata from markdown file
                try:
                    content = md_file.read_text()
                    lines = content.split('\n')
                    
                    difficulty = "Unknown"
                    date = "Unknown"
                    
                    for line in lines:
                        if line.startswith("**Difficulty:**"):
                            difficulty = line.split("**Difficulty:**")[1].strip()
                        elif line.startswith("**Date:**"):
                            date = line.split("**Date:**")[1].strip()
                            
                    # Check which languages this problem is solved in
                    languages_solved = []
                    for lang in self.language_dirs:
                        lang_dir = self.root_dir / lang
                        problem_file = None
                        
                        # Check different possible filename formats
                        snake_name = md_file.stem
                        
                        if lang == "java":
                            # Java uses PascalCase class names
                            class_name = "".join(word.capitalize() for word in snake_name.split("_"))
                            problem_file = lang_dir / f"{class_name}.java"
                        else:
                            problem_file = lang_dir / f"{snake_name}{self.language_extensions[lang]}"
                            
                        if problem_file and problem_file.exists():
                            languages_solved.append(lang)
                            
                    problems.append({
                        "name": problem_name,
                        "difficulty": difficulty,
                        "date": date,
                        "languages": languages_solved,
                        "file": str(md_file)
                    })
                    
                except Exception as e:
                    print(f"Warning: Could not parse {md_file}: {e}")
                    
        return problems
        
    def calculate_difficulty_distribution(self, problems):
        """Calculate distribution of problems by difficulty"""
        difficulties = [p["difficulty"] for p in problems]
        return Counter(difficulties)
        
    def calculate_monthly_progress(self, problems):
        """Calculate problems solved per month"""
        monthly_stats = defaultdict(int)
        
        for problem in problems:
            try:
                date_str = problem["date"]
                if date_str != "Unknown":
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    month_key = date_obj.strftime("%Y-%m")
                    monthly_stats[month_key] += 1
            except Exception:
                continue
                
        return dict(sorted(monthly_stats.items()))
        
    def generate_language_completion_matrix(self, problems):
        """Generate matrix showing which problems are solved in which languages"""
        matrix = []
        
        for problem in problems:
            row = {
                "problem": problem["name"],
                "difficulty": problem["difficulty"]
            }
            
            for lang in self.language_dirs:
                row[lang] = "✅" if lang in problem["languages"] else "❌"
                
            matrix.append(row)
            
        return matrix
        
    def calculate_streak_stats(self):
        """Calculate commit streaks and activity (requires git)"""
        try:
            import subprocess
            
            # Get commit dates for the last 3 months
            result = subprocess.run([
                "git", "log", "--since=3.months.ago", "--pretty=format:%ad", "--date=short"
            ], capture_output=True, text=True, cwd=self.root_dir)
            
            if result.returncode == 0:
                commit_dates = result.stdout.strip().split('\n')
                commit_dates = [date for date in commit_dates if date]
                
                # Count commits per date
                date_counts = Counter(commit_dates)
                
                # Calculate current streak
                today = datetime.now().date()
                current_streak = 0
                
                current_date = today
                while current_date.strftime("%Y-%m-%d") in commit_dates:
                    current_streak += 1
                    current_date = current_date.replace(day=current_date.day - 1)
                    
                return {
                    "total_commits_3m": len(commit_dates),
                    "unique_days_3m": len(date_counts),
                    "current_streak": current_streak,
                    "avg_commits_per_day": len(commit_dates) / max(len(date_counts), 1)
                }
            else:
                return None
                
        except Exception:
            return None
            
    def print_stats(self):
        """Print comprehensive statistics"""
        print("📊 LeetCode Repository Statistics")
        print("=" * 50)
        print()
        
        # Language statistics
        lang_stats = self.count_problems_by_language()
        total_solutions = sum(lang_stats.values())
        
        print("💻 Solutions by Language:")
        for lang, count in sorted(lang_stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / max(total_solutions, 1)) * 100
            print(f"   {lang.ljust(12)}: {count:3d} solutions ({percentage:5.1f}%)")
        print(f"   {'Total'.ljust(12)}: {total_solutions:3d} solutions")
        print()
        
        # Problem statistics
        problems = self.get_problem_list()
        unique_problems = len(problems)
        
        print(f"🎯 Problems Solved: {unique_problems}")
        print()
        
        if problems:
            # Difficulty distribution
            difficulty_dist = self.calculate_difficulty_distribution(problems)
            print("📈 Difficulty Distribution:")
            for difficulty, count in sorted(difficulty_dist.items()):
                percentage = (count / unique_problems) * 100
                print(f"   {difficulty.ljust(8)}: {count:3d} problems ({percentage:5.1f}%)")
            print()
            
            # Monthly progress
            monthly_progress = self.calculate_monthly_progress(problems)
            if monthly_progress:
                print("📅 Monthly Progress:")
                for month, count in monthly_progress.items():
                    print(f"   {month}: {count} problems")
                print()
            
            # Language completion matrix (show first 10 problems)
            print("✅ Language Completion Matrix (Recent Problems):")
            matrix = self.generate_language_completion_matrix(problems)
            
            if matrix:
                # Header
                header = "Problem".ljust(25) + "Diff".ljust(8)
                for lang in self.language_dirs:
                    header += lang[:3].upper().ljust(4)
                print(f"   {header}")
                print(f"   {'-' * len(header)}")
                
                # Show last 10 problems
                for row in matrix[-10:]:
                    line = row["problem"][:24].ljust(25) + row["difficulty"][:7].ljust(8)
                    for lang in self.language_dirs:
                        line += row[lang].ljust(4)
                    print(f"   {line}")
                print()
        
        # Git statistics
        streak_stats = self.calculate_streak_stats()
        if streak_stats:
            print("🔥 Commit Activity (Last 3 Months):")
            print(f"   Total commits: {streak_stats['total_commits_3m']}")
            print(f"   Active days: {streak_stats['unique_days_3m']}")
            print(f"   Current streak: {streak_stats['current_streak']} days")
            print(f"   Avg commits/day: {streak_stats['avg_commits_per_day']:.1f}")
            print()
        
        # Goals and recommendations
        print("🎯 Progress Toward Goals:")
        target_problems = 150  # 6 months * 25 problems/month
        target_languages = 5
        
        progress_percentage = (unique_problems / target_problems) * 100
        languages_used = len([lang for lang, count in lang_stats.items() if count > 0])
        
        print(f"   Problems: {unique_problems}/{target_problems} ({progress_percentage:.1f}%)")
        print(f"   Languages: {languages_used}/{target_languages}")
        
        if unique_problems < target_problems:
            remaining = target_problems - unique_problems
            print(f"   🎯 {remaining} more problems to reach goal!")
            
        if languages_used < target_languages:
            missing_langs = [lang for lang, count in lang_stats.items() if count == 0]
            print(f"   💡 Try these languages: {', '.join(missing_langs)}")
            
        print()
        print("🚀 Keep up the great work!")

def main():
    # Find repository root
    current_dir = Path.cwd()
    root_dir = current_dir
    
    # Look for known directories to confirm we're in the right place
    while not (root_dir / "templates").exists() and root_dir.parent != root_dir:
        root_dir = root_dir.parent
        
    if not (root_dir / "templates").exists():
        print("❌ Error: Could not find leetcode-daily repository. Run this script from within the repository.")
        return
        
    stats = LeetCodeStats(root_dir)
    stats.print_stats()

if __name__ == "__main__":
    main()
