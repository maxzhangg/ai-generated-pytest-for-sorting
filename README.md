# AI-Generated Pytest Test Suite for Sorting Algorithms

This project provides a full suite of **Pytest test cases** for the classic sorting algorithms originally implemented by [Tarcisio Marinho](https://github.com/tarcisio-marinho) in the repository:  
🔗 https://github.com/tarcisio-marinho/sorting-algorithms

The tests were automatically generated using **ChatGPT (Generative AI)** to ensure correctness, structural coverage, and robustness. A full **HTML coverage report** is also included.

## 📌 About the Original Project

The sorting algorithms in `sorting_algorithms/` are sourced directly from the original repository. It includes:

- Bubble Sort  
- Insertion Sort  
- Selection Sort  
- Merge Sort  
- Quick Sort  
- Heap Sort  
- Radix Sort  
- Shell Sort  
- TimSort

All implementations are clean, educational, and ideal for practicing algorithm understanding.

## ⚠️ Code Fix Notice

The original sorting implementations contained a few bugs (e.g., float indexing, incorrect list assignments) that have been fixed to make them compatible with modern Python and Pytest testing.  
👉 You can view the exact changes in this diff file:  
[📄 sorting_algorithms/diff.txt](https://github.com/maxzhangg/ai-generated-pytest-for-sorting/blob/master/sorting_algorithms/diff.txt)


## ✅ What This Project Adds

- ✔️ AI-generated Pytest test cases for **each algorithm**
- ✔️ Test coverage for:
  - Empty arrays
  - Single elements
  - Sorted and reversed arrays
  - Arrays with duplicates
  - Large arrays
- ✔️ `pytest-cov` integrated HTML coverage report
- ✔️ Clean, ready-to-run Python testing structure

## 🧪 Run the Tests

Install dependencies:

```bash
pip install pytest pytest-cov
```

Run all tests with coverage:

```bash
pytest --cache-clear --cov=sorting_algorithms --cov-report=html:coverage-report/htmlcov
```

Then open this file in your browser to view the coverage report:

```
coverage-report/htmlcov/index.html
```

## 📁 Project Structure

```
python-alogrithm-testing/
├── sorting_algorithms/        # Original sorting implementations
│   ├── bubblesort.py
│   ├── insertionsort.py
│   ├── selectionsort.py
│   ├── mergesort.py
│   ├── quicksort.py
│   ├── heap_sort.py
│   ├── radix_sort.py
│   ├── shellsort.py
│   ├── timsort.py
│   └── __init__.py
│
├── tests/                     # Pytest test cases (AI-generated)
│   ├── test_bubble_sort.py
│   ├── test_insertion_sort.py
│   ├── test_selection_sort.py
│   ├── test_merge_sort.py
│   ├── test_quick_sort.py
│   ├── test_heap_sort.py
│   ├── test_radix_sort.py
│   ├── test_shell_sort.py
│   ├── test_tim_sort.py
│   └── __pycache__/
│
├── coverage-report/
│   └── htmlcov/
│       └── index.html (open this in browser to view report)
│
├── .gitignore
└── README.md
```

## 📈 Coverage Report

This project aims for **100% test coverage** across all sorting functions.

To explore the detailed report, open:
```
coverage-report/htmlcov/index.html
```

You’ll see per-function line-by-line coverage with visualization.

## 🤖 Test Generation with ChatGPT

All test files were created using prompts in [ChatGPT](https://chat.openai.com/), such as:

> "Write Pytest test cases for a selection sort function in Python. Include edge cases, sorted input, reversed input, and duplicates."

Tests were reviewed and adapted where needed. This demonstrates how generative AI can assist in software testing and engineering workflows.

## 📝 License & Credits

- Sorting algorithm implementations © [Tarcisio Marinho](https://github.com/tarcisio-marinho)
- Test suite and documentation generated for educational use with ChatGPT
- This repository is shared for demonstration and learning purposes only

## 🔗 Related Resources

- Original code: https://github.com/tarcisio-marinho/sorting-algorithms  
- Pytest: https://docs.pytest.org/  
- ChatGPT: https://chat.openai.com/  
- Coverage tool: https://github.com/pytest-dev/pytest-cov
