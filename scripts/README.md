# LeetCode Daily - Helper Scripts

This directory contains utility scripts to streamline your LeetCode practice workflow.

## Scripts Overview

### 1. `new_problem.py` - Problem Generator
Creates boilerplate code and documentation for new LeetCode problems.

**Usage:**
```bash
python scripts/new_problem.py "Two Sum" "easy" "python,javascript"
python scripts/new_problem.py "Longest Substring" "medium" "python,java,cpp"
```

**Features:**
- Generates code files from templates for multiple languages
- Creates markdown documentation with structured sections
- Handles naming conventions (snake_case, PascalCase, camelCase)
- Suggests commit messages

### 2. `stats.py` - Repository Statistics
Analyzes your repository and shows comprehensive statistics.

**Usage:**
```bash
python scripts/stats.py
```

**Features:**
- Problems solved by language
- Difficulty distribution
- Monthly progress tracking
- Language completion matrix
- Git commit activity stats
- Progress toward 6-month goals

### 3. `commit_helper.py` - Commit Message Generator
Generates descriptive commit messages for your solutions.

**Usage:**
```bash
python scripts/commit_helper.py "two_sum" "python,javascript"
python scripts/commit_helper.py "binary_search" "java" --approach "binary search" --complexity "O(log n)" --difficulty "easy"
```

**Options:**
- `--approach, -a`: Solution approach (e.g., "hash map", "two pointers")
- `--complexity, -c`: Time complexity (e.g., "O(n)", "O(log n)")  
- `--difficulty, -d`: Problem difficulty (easy/medium/hard)
- `--format, -f`: Message format (standard/short/detailed/emoji/all)

## Quick Examples

### Generate a new problem with multiple languages:
```bash
python scripts/new_problem.py "Valid Palindrome" "easy" "python,javascript,java"
```

### Check your progress:
```bash
python scripts/stats.py
```

### Generate commit message options:
```bash
python scripts/commit_helper.py "valid_palindrome" "python,javascript" --format all
```

## Tips

1. **Run scripts from repository root** - They automatically detect the correct directory structure
2. **Use descriptive problem names** - The scripts handle naming convention conversions
3. **Specify multiple languages** - Helps maintain consistent multi-language practice
4. **Check stats regularly** - Motivates consistent progress and identifies gaps

## Error Handling

All scripts include error handling for:
- Invalid language names
- Missing template files
- Git repository issues
- File permission problems

If you encounter issues, ensure you're running the scripts from within the leetcode-daily repository.
