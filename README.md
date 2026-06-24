# Modular Geometry Backend Application

A structured Python backend application demonstrating modular architecture, isolated environment management, and automated test-driven development (TDD) principles.

## 🚀 Key Engineering Features

*   **Decoupled Architecture:** Separated core algorithmic and calculation workflows (`source/geometry.py`) from the main application execution engine (`source/main.py`) to maximize code reusability and maintainability.
*   **Automated Testing Suite:** Implemented dedicated unit testing pipelines under `/test` using standard assertion frameworks (`test_geometry.py`) to rigorously validate functional backend stability.
*   **Isolated Dependency Management:** Maintained strict local runtime isolation using Python virtual environments (`virtenv`), explicitly locking all external utility frameworks inside targeted production and testing manifests (`requirements.txt`).
*   **Repository Hygiene:** Applied version control discipline by configuring a `.gitignore` baseline to prevent compiled local runtime artifacts (`__pycache__`) and local hardware dependencies from leaking into the public version history.

## 📂 Project Structure

```text
├── source/                  # Production Backend Modules
│   ├── main.py              # Application Entry Point
│   └── geometry.py          # Functional & Algorithmic Logic
├── test/                    # Automated QA / Testing Subsystem
│   ├── requirements.txt     # Test-specific dependencies
│   └── test_geometry.py     # Functional Validation Unit Tests
├── .gitignore               # Environment Isolation Filters
└── requirements.txt         # Global Backend Dependencies
