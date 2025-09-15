#!/usr/bin/env python3
"""
LeetCode Problem Generator Script

Usage:
    python new_problem.py "Two Sum" "easy" "python,javascript"
    python new_problem.py "Longest Substring" "medium" "python,java,cpp"
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

class ProblemGenerator:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.templates_dir = self.root_dir / "templates"
        self.language_extensions = {
            "python": ".py",
            "javascript": ".js", 
            "java": ".java",
            "cpp": ".cpp",
            "rust": ".rs"
        }
        
    def snake_case(self, text):
        """Convert text to snake_case for filenames"""
        return text.lower().replace(" ", "_").replace("-", "_")
        
    def title_case(self, text):
        """Convert text to Title Case"""
        return " ".join(word.capitalize() for word in text.split())
        
    def camel_case(self, text):
        """Convert text to CamelCase for class names"""
        words = text.replace("_", " ").replace("-", " ").split()
        return "".join(word.capitalize() for word in words)
        
    def function_name(self, text):
        """Convert to camelCase for function names"""
        words = text.replace("_", " ").replace("-", " ").split()
        if not words:
            return "solution"
        return words[0].lower() + "".join(word.capitalize() for word in words[1:])
        
    def load_template(self, language):
        """Load template for specific language"""
        template_file = self.templates_dir / f"template.{self.language_extensions[language].lstrip('.')}"
        if not template_file.exists():
            raise FileNotFoundError(f"Template not found: {template_file}")
        return template_file.read_text()
        
    def replace_placeholders(self, template, problem_name, difficulty, language):
        """Replace placeholders in template with actual values"""
        snake_name = self.snake_case(problem_name)
        title_name = self.title_case(problem_name)
        class_name = self.camel_case(problem_name)
        func_name = self.function_name(problem_name)
        
        replacements = {
            "{PROBLEM_NAME}": title_name,
            "{DIFFICULTY}": difficulty.capitalize(),
            "{DATE}": datetime.now().strftime("%Y-%m-%d"),
            "{APPROACH}": "TODO: Define approach",
            "{TIME_COMPLEXITY}": "TODO: Analyze time complexity", 
            "{SPACE_COMPLEXITY}": "TODO: Analyze space complexity",
            "{FUNCTION_NAME}": func_name,
            "{CLASS_NAME}": class_name,
            "{PARAMETERS}": "TODO: Define parameters",
            "{PARAM_TYPE}": "TODO: Define parameter type",
            "{PARAMETER}": "TODO: Define parameter",
            "{RETURN_TYPE}": "TODO: Define return type",
            "{PROBLEM_DESCRIPTION}": "TODO: Add problem description",
            "{ARGS_DESCRIPTION}": "TODO: Describe arguments",
            "{RETURN_DESCRIPTION}": "TODO: Describe return value",
            "{PARAM_DESCRIPTION}": "TODO: Describe parameter",
            "{INPUT}": "TODO: Add test input",
            "{EXPECTED_OUTPUT}": "TODO: Add expected output"
        }
        
        result = template
        for placeholder, value in replacements.items():
            result = result.replace(placeholder, value)
            
        return result
        
    def generate_code_file(self, problem_name, difficulty, language):
        """Generate code file for specific language"""
        template = self.load_template(language)
        content = self.replace_placeholders(template, problem_name, difficulty, language)
        
        snake_name = self.snake_case(problem_name)
        filename = snake_name + self.language_extensions[language]
        
        # Special case for Java - use PascalCase for class files
        if language == "java":
            class_name = self.camel_case(problem_name)
            filename = class_name + ".java"
            
        output_dir = self.root_dir / language
        output_dir.mkdir(exist_ok=True)
        
        output_file = output_dir / filename
        output_file.write_text(content)
        
        return output_file
        
    def generate_markdown_file(self, problem_name, difficulty):
        """Generate markdown explanation file"""
        template_file = self.templates_dir / "template.md"
        if not template_file.exists():
            raise FileNotFoundError(f"Markdown template not found: {template_file}")
            
        template = template_file.read_text()
        
        title_name = self.title_case(problem_name)
        snake_name = self.snake_case(problem_name)
        
        replacements = {
            "{PROBLEM_NAME}": title_name,
            "{DIFFICULTY}": difficulty.capitalize(),
            "{DATE}": datetime.now().strftime("%Y-%m-%d"),
            "{LEETCODE_URL}": f"https://leetcode.com/problems/{snake_name.replace('_', '-')}/",
            "{PROBLEM_DESCRIPTION}": "TODO: Add problem description",
            "{APPROACH_1_NAME}": "Brute Force",
            "{TIME_COMPLEXITY_1}": "n²",
            "{SPACE_COMPLEXITY_1}": "1",
            "{APPROACH_1_EXPLANATION}": "TODO: Explain brute force approach",
            "{APPROACH_2_NAME}": "Optimized",
            "{TIME_COMPLEXITY_2}": "n",
            "{SPACE_COMPLEXITY_2}": "n",
            "{APPROACH_2_EXPLANATION}": "TODO: Explain optimized approach",
            "{NOTE_1}": "TODO: Add implementation note",
            "{NOTE_2}": "TODO: Add implementation note",
            "{EDGE_CASE_1}": "TODO: Add edge case",
            "{EDGE_CASE_2}": "TODO: Add edge case",
            "{LEARNING_1}": "TODO: Add key learning",
            "{LEARNING_2}": "TODO: Add key learning", 
            "{LEARNING_3}": "TODO: Add key learning",
            "{RELATED_PROBLEM_1}": "TODO: Add related problem",
            "{RELATED_URL_1}": "#",
            "{RELATED_PROBLEM_2}": "TODO: Add related problem",
            "{RELATED_URL_2}": "#"
        }
        
        content = template
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
            
        notes_dir = self.root_dir / "notes"
        notes_dir.mkdir(exist_ok=True)
        
        output_file = notes_dir / f"{snake_name}.md"
        output_file.write_text(content)
        
        return output_file
        
    def generate_problem(self, problem_name, difficulty, languages):
        """Generate all files for a problem"""
        generated_files = []
        
        # Generate code files for each language
        for language in languages:
            try:
                code_file = self.generate_code_file(problem_name, difficulty, language)
                generated_files.append(str(code_file))
                print(f"✅ Generated {language}: {code_file}")
            except Exception as e:
                print(f"❌ Error generating {language}: {e}")
                
        # Generate markdown file
        try:
            md_file = self.generate_markdown_file(problem_name, difficulty)
            generated_files.append(str(md_file))
            print(f"✅ Generated notes: {md_file}")
        except Exception as e:
            print(f"❌ Error generating markdown: {e}")
            
        return generated_files
        
    def suggest_commit_message(self, problem_name, languages):
        """Suggest a commit message"""
        title_name = self.title_case(problem_name)
        lang_str = " and ".join(languages)
        return f"Add {title_name} solution in {lang_str}"

def main():
    parser = argparse.ArgumentParser(description="Generate LeetCode problem files")
    parser.add_argument("problem_name", help="Name of the problem (e.g., 'Two Sum')")
    parser.add_argument("difficulty", choices=["easy", "medium", "hard"], 
                       help="Problem difficulty")
    parser.add_argument("languages", help="Comma-separated list of languages (e.g., 'python,javascript,java')")
    
    args = parser.parse_args()
    
    # Find repository root
    current_dir = Path.cwd()
    root_dir = current_dir
    
    # Look for templates directory to confirm we're in the right place
    while not (root_dir / "templates").exists() and root_dir.parent != root_dir:
        root_dir = root_dir.parent
        
    if not (root_dir / "templates").exists():
        print("❌ Error: Could not find templates directory. Run this script from within the leetcode-daily repository.")
        sys.exit(1)
        
    languages = [lang.strip() for lang in args.languages.split(",")]
    
    # Validate languages
    valid_languages = ["python", "javascript", "java", "cpp", "rust"]
    invalid_languages = [lang for lang in languages if lang not in valid_languages]
    if invalid_languages:
        print(f"❌ Error: Invalid languages: {invalid_languages}")
        print(f"Valid languages: {valid_languages}")
        sys.exit(1)
        
    generator = ProblemGenerator(root_dir)
    
    print(f"🚀 Generating problem: {args.problem_name}")
    print(f"📊 Difficulty: {args.difficulty}")
    print(f"💻 Languages: {', '.join(languages)}")
    print()
    
    generated_files = generator.generate_problem(args.problem_name, args.difficulty, languages)
    
    print()
    print("🎉 Generation complete!")
    print(f"📁 Generated {len(generated_files)} files")
    print()
    print("💡 Suggested commit message:")
    print(f"   {generator.suggest_commit_message(args.problem_name, languages)}")
    print()
    print("📝 Next steps:")
    print("   1. Implement the solution in each language file")
    print("   2. Fill in the problem description and notes in the markdown file")
    print("   3. Test your solutions")
    print("   4. Commit and push your changes")

if __name__ == "__main__":
    main()
