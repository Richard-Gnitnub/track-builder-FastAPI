# TODO List

## 1. Project Setup
- [x] Set up the project directory structure for a **FastAPI** application.  
- [x] Create a Python virtual environment (`venv` or `conda`) for isolated development.
- [x] Install FastAPI and essential dependencies.
- [x] Initialise a Git repository and push to GitHub using the desktop app.
- [x] Set up Docker for local deployment.

---

## 2. Core Functionality

### a. Database Models
- [x] Define models for track components in `models.py` using **SQLModel**:
  - Timbers: Include position, width, depth, and flange dimensions.
  - Chairs: Include groove dimensions, fit adjustment, and placement offset.
  - Tracks: Include length, timber spacing, and chair alignment.
- [x] Use **SQLModel** to implement the database schema.

### b. User Interface
- [ ] Create CRUD functionality for:
  - Timbers (with flange dimensions).
  - Chairs (with groove dimensions and fit adjustment).
  - Tracks (with relationships to timbers and chairs).
- [ ] Validate the UI for responsiveness and usability.

### c. Geometry and STL Export
- [ ] Implement a function to generate geometry for tracks with chairs and timbers.
- [ ] Integrate geometry generation with FastAPI routes.
- [ ] Use CadQuery to generate STL files based on user input.
- [ ] Validate STL file integrity and provide feedback if checks fail.
- [ ] Provide downloadable STL files through the FastAPI app.

---

## 3. Testing and Deployment
- [ ] Write unit tests for models and routes.
- [ ] Validate relationships between tracks, timbers, and chairs.
- [ ] Deploy the application locally using Docker Desktop for testing.

---

## 4. Documentation
- [ ] Update README with new schema and functionality.
- [ ] Provide usage examples for API endpoints.
- [ ] Create troubleshooting steps for common issues.
