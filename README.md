# 🧑‍💻 LeetCode Daily - Structured Practice Repository

[![GitHub stars](https://img.shields.io/github/stars/Owen-Richards/leetcode-daily?style=social)](https://github.com/Owen-Richards/leetcode-daily)
[![GitHub forks](https://img.shields.io/github/forks/Owen-Richards/leetcode-daily?style=social)](https://github.com/Owen-Richards/leetcode-daily)
[![Last commit](https://img.shields.io/github/last-commit/Owen-Richards/leetcode-daily)](https://github.com/Owen-Richards/leetcode-daily)

A comprehensive, multi-language repository for daily LeetCode practice with automated progress tracking and consistent commit history for building an impressive GitHub profile.

## 🎯 Goals

- **📈 A+ GitHub Activity**: Consistent daily commits for 6 months
- **🌐 Multi-Language Mastery**: Solutions in Python, JavaScript, Java, C++, and Rust
- **📚 Knowledge Building**: System design and finance learning notes
- **🏆 Interview Ready**: Structured problem-solving with multiple approaches

## 📂 Repository Structure

```
leetcode-daily/
├── python/                 # Python solutions
├── javascript/             # JavaScript solutions  
├── java/                   # Java solutions
├── cpp/                    # C++ solutions
├── rust/                   # Rust solutions
├── notes/                  # Problem explanations (Markdown)
├── system-design/          # System design case studies
├── finance-learning/       # Finance and investment notes
├── templates/              # Code templates for each language
├── scripts/               # Utility scripts
├── .github/workflows/     # GitHub Actions
└── Progress.md           # Monthly progress tracking
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Owen-Richards/leetcode-daily.git
cd leetcode-daily
```

### 2. Set Up GitHub Action (Optional)
To auto-update your profile README with latest progress:

1. Create a Personal Access Token with `repo` scope
2. Add it as `PROFILE_README_TOKEN` in repository secrets
3. The workflow will run daily and after each push

### 3. Start Solving Problems

Use the helper script to generate new problem files:
```bash
# Python script to generate problem files
python scripts/new_problem.py "Problem Name" "easy" "python,javascript"
```

Or manually copy from templates:
```bash
cp templates/template.py python/new_problem.py
cp templates/template.md notes/new_problem.md
```

## 📝 Templates & Examples

Each language has a structured template with:
- **Problem metadata** (difficulty, date, complexity)
- **Comprehensive docstrings**
- **Test cases**
- **Multiple approach sections**

### Example: Two Sum Problem
- **Implementations**: [Python](python/two_sum.py) | [JavaScript](javascript/two_sum.js) | [Java](java/TwoSum.java) | [C++](cpp/two_sum.cpp) | [Rust](rust/two_sum.rs)
- **Explanation**: [Notes](notes/two_sum.md)

## 📊 6-Month Practice Schedule

### Daily (Monday-Friday) - 1 Hour
- ✅ Solve **1 LeetCode problem**
- ✅ Implement in **2+ languages** (rotate weekly)
- ✅ Write explanation in markdown
- ✅ Commit with descriptive message

### Weekly (Weekends)
- 📚 Write **1 system design note**
- 💰 Add **1 finance learning note**
- 🔄 Review and refactor code

### Monthly
- 📈 Update `Progress.md`
- 🎯 Set next month's goals
- 📝 Reflect on learnings

## 🎨 Language Rotation Schedule

| Week | Primary | Secondary | Focus Area |
|------|---------|-----------|------------|
| 1    | Python  | JavaScript| Syntax & Idioms |
| 2    | Java    | C++       | Memory & Performance |
| 3    | Python  | Rust      | Safety & Concurrency |
| 4    | JavaScript | Java   | Web & Enterprise |

## 📈 Expected GitHub Stats (6 Months)

- **~150 problems solved** across 5 languages
- **~300 commits** (daily coding + weekend notes)
- **Consistent green squares** for 6 months
- **Portfolio-ready repository** for interviews

## 🔧 Utility Scripts

### Generate New Problem
```bash
python scripts/new_problem.py "Two Sum" "easy" "python,javascript,java"
```

### Language Statistics
```bash
python scripts/stats.py
```

### Commit Message Generator
```bash
python scripts/commit_helper.py "two_sum" "python,javascript"
# Output: "Add Two Sum solution in Python and JavaScript (O(n) hash map)"
```

## 🏆 Problem Categories & Progress

### Arrays & Hashing
- [x] Two Sum (Easy)
- [ ] Valid Anagram (Easy)
- [ ] Group Anagrams (Medium)

### Two Pointers
- [ ] Valid Palindrome (Easy)
- [ ] Two Sum II (Medium)
- [ ] 3Sum (Medium)

### Sliding Window
- [ ] Best Time to Buy and Sell Stock (Easy)
- [ ] Longest Substring Without Repeating Characters (Medium)

### Stack & Queue
- [ ] Valid Parentheses (Easy)
- [ ] Min Stack (Medium)

### Binary Search
- [ ] Binary Search (Easy)
- [ ] Search in Rotated Sorted Array (Medium)

### Linked Lists
- [ ] Reverse Linked List (Easy)
- [ ] Merge Two Sorted Lists (Easy)

### Trees & Graphs
- [ ] Invert Binary Tree (Easy)
- [ ] Maximum Depth of Binary Tree (Easy)

### Dynamic Programming
- [ ] Climbing Stairs (Easy)
- [ ] House Robber (Medium)

## 🎓 Learning Resources

### System Design
- Load Balancers & Reverse Proxies
- Database Design (SQL vs NoSQL)
- Caching Strategies (Redis, Memcached)
- Message Queues & Event Streaming
- Microservices & API Design

### Finance & Investment
- Portfolio Theory & Diversification
- Risk Management Strategies
- Market Analysis & Technical Indicators
- Options & Derivatives
- Cryptocurrency & DeFi

## 🤝 Contributing

Feel free to:
- 🐛 Report bugs in templates
- 💡 Suggest new features
- 📝 Improve documentation
- 🔀 Submit alternative solutions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- LeetCode for providing excellent practice problems
- The programming community for inspiration and best practices
- GitHub for enabling awesome automation with Actions

---

**⭐ Star this repository if you find it helpful for your coding journey!**

*Last updated: September 14, 2025*
