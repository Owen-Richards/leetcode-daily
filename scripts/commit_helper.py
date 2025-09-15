#!/usr/bin/env python3
"""
Commit Message Helper Script

Generates descriptive commit messages for LeetCode solutions.
"""

import sys
import argparse
from pathlib import Path

class CommitHelper:
    def __init__(self):
        self.complexity_keywords = {
            "O(1)": "constant time",
            "O(log n)": "logarithmic",
            "O(n)": "linear",
            "O(n log n)": "linearithmic", 
            "O(n²)": "quadratic",
            "O(2^n)": "exponential"
        }
        
        self.approach_keywords = {
            "hash": "hash map",
            "map": "hash map",
            "dict": "hash map",
            "two": "two pointers",
            "pointer": "two pointers", 
            "slide": "sliding window",
            "window": "sliding window",
            "dp": "dynamic programming",
            "dynamic": "dynamic programming",
            "binary": "binary search",
            "search": "binary search",
            "bfs": "breadth-first search",
            "dfs": "depth-first search",
            "tree": "tree traversal",
            "graph": "graph traversal",
            "sort": "sorting",
            "greedy": "greedy algorithm",
            "divide": "divide and conquer"
        }
        
    def title_case(self, text):
        """Convert snake_case or kebab-case to Title Case"""
        return " ".join(word.capitalize() for word in text.replace("_", " ").replace("-", " ").split())
        
    def detect_approach(self, problem_name):
        """Try to detect the approach from problem name"""
        name_lower = problem_name.lower()
        
        for keyword, approach in self.approach_keywords.items():
            if keyword in name_lower:
                return approach
                
        return None
        
    def generate_commit_message(self, problem_name, languages, approach=None, complexity=None, difficulty=None):
        """Generate a descriptive commit message"""
        title_name = self.title_case(problem_name)
        
        # Format languages
        if len(languages) == 1:
            lang_str = languages[0].capitalize()
        elif len(languages) == 2:
            lang_str = f"{languages[0].capitalize()} and {languages[1].capitalize()}"
        else:
            lang_str = f"{', '.join(lang.capitalize() for lang in languages[:-1])}, and {languages[-1].capitalize()}"
            
        # Base message
        message = f"Add {title_name} solution in {lang_str}"
        
        # Add approach if provided or detected
        if not approach:
            approach = self.detect_approach(problem_name)
            
        details = []
        
        if approach:
            details.append(approach)
            
        if complexity:
            if complexity in self.complexity_keywords:
                details.append(f"{complexity} {self.complexity_keywords[complexity]}")
            else:
                details.append(complexity)
                
        if difficulty:
            details.append(f"{difficulty.lower()} level")
            
        if details:
            message += f" ({', '.join(details)})"
            
        return message
        
    def generate_multiple_formats(self, problem_name, languages, approach=None, complexity=None, difficulty=None):
        """Generate multiple commit message formats"""
        title_name = self.title_case(problem_name)
        lang_str = " and ".join(lang.capitalize() for lang in languages)
        
        formats = []
        
        # Format 1: Standard
        standard = self.generate_commit_message(problem_name, languages, approach, complexity, difficulty)
        formats.append(("Standard", standard))
        
        # Format 2: Short
        short = f"Solve {title_name} - {lang_str}"
        formats.append(("Short", short))
        
        # Format 3: Detailed
        detailed = f"Implement {title_name} solution"
        if approach:
            detailed += f" using {approach}"
        if languages:
            detailed += f" in {lang_str}"
        if complexity:
            detailed += f" with {complexity} complexity"
        formats.append(("Detailed", detailed))
        
        # Format 4: Emoji style
        emoji_map = {
            "easy": "🟢",
            "medium": "🟡", 
            "hard": "🔴"
        }
        emoji = emoji_map.get(difficulty.lower() if difficulty else "", "✨")
        emoji_format = f"{emoji} {title_name} - {lang_str}"
        if complexity:
            emoji_format += f" ({complexity})"
        formats.append(("Emoji", emoji_format))
        
        return formats

def main():
    parser = argparse.ArgumentParser(description="Generate commit messages for LeetCode solutions")
    parser.add_argument("problem_name", help="Name of the problem (e.g., 'two_sum' or 'Two Sum')")
    parser.add_argument("languages", help="Comma-separated list of languages (e.g., 'python,javascript')")
    parser.add_argument("--approach", "-a", help="Solution approach (e.g., 'hash map', 'two pointers')")
    parser.add_argument("--complexity", "-c", help="Time complexity (e.g., 'O(n)', 'O(log n)')")
    parser.add_argument("--difficulty", "-d", choices=["easy", "medium", "hard"], help="Problem difficulty")
    parser.add_argument("--format", "-f", choices=["standard", "short", "detailed", "emoji", "all"], 
                       default="standard", help="Commit message format")
    
    args = parser.parse_args()
    
    languages = [lang.strip() for lang in args.languages.split(",")]
    
    # Validate languages
    valid_languages = ["python", "javascript", "java", "cpp", "rust"]
    invalid_languages = [lang for lang in languages if lang not in valid_languages]
    if invalid_languages:
        print(f"❌ Warning: Unknown languages: {invalid_languages}")
        print(f"Valid languages: {valid_languages}")
        
    helper = CommitHelper()
    
    if args.format == "all":
        print(f"🎯 Commit message options for '{args.problem_name}':")
        print()
        
        formats = helper.generate_multiple_formats(
            args.problem_name, languages, args.approach, args.complexity, args.difficulty
        )
        
        for i, (format_name, message) in enumerate(formats, 1):
            print(f"{i}. {format_name}:")
            print(f"   {message}")
            print()
            
        print("💡 Copy the message you prefer!")
        
    else:
        message = helper.generate_commit_message(
            args.problem_name, languages, args.approach, args.complexity, args.difficulty
        )
        print(message)

if __name__ == "__main__":
    main()
