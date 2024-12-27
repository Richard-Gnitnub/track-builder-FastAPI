# PROJECT: 

Lightweight Track Builder (Rewrite of Templot by Martin Wynne)

## GOAL:

Develop a lightweight Python-based application to design accurate model railway track for 3D printing, focusing on **COT (Chairs on Timbers) track**. This MVP will prioritise straight track generation adhering to bullhead rail standards based on REA specifications. The generated STL files will include timbers with integrated chairs, and the rail will be manually added post-printing. The MVP serves as a foundation for a modular and extensible track design tool.

---

## KEY INSIGHTS:

- Legacy `dxf_unit.pas` (Pascal) code is pivotal, containing the original 2D DXF and 3D STL export logic.
- The codebase’s monolithic design relies heavily on global variables for geometry, tolerances, and track parameters.
- Decades of incremental updates have resulted in intertwined 2D and 3D logic, complicating direct porting.
- **COT Track Discoveries**:
  - **Integrated Chairs and Timbers**: COT tracks combine chairs and timbers into a single printable unit.
  - **Chair Data**: Groove dimensions (width, depth, tolerance) are crucial for rail fit.
  - **Timber Data**: Includes flange dimensions for stability during FDM printing.
  - **Alignment Patterns**: Chairs can be aligned symmetrically or staggered based on track design.

---

## MVP PLAN:

1. **Framework**:
   - Build the MVP using **FastAPI** for its performance, API-first design, and type validation capabilities.
   - Use **SQLModel** for database interactions, ensuring type safety and simplicity.

2. **Core Features**:
   - **STL Generation**:
     - Parameterised straight track geometry.
     - Includes chairs with grooves for rail placement and timbers with optional flanges.
   - **Database Integration**:
     - Use SQLite to store dynamic track configurations and eliminate hardcoded values.
   - **Admin Panel**:
     - Provide CRUD operations for timbers, chairs, and track settings via a user-friendly web interface.

3. **Design Elements**:
   - **Timbers**: Base structure with configurable dimensions (length, width, depth, flanges).
   - **Chairs**: Integrated into timbers with configurable groove dimensions for rail fit.
   - **Rails**: Added manually by the user after 3D printing.

4. **Validation**:
   - Ensure STL files are watertight and structurally sound.
   - Provide error feedback for invalid configurations or failed exports.

5. **Excluded from MVP**:
   - **Curved Tracks** and **Turnouts**: Deferred for future enhancements.
   - **Mesh Inspection and Repair**: Planned for post-MVP development.

---

## WORKING ENVIRONMENT REQUIREMENTS:

- Development will use **VS Code** on a Windows machine.
- **GitHub Desktop** will manage version control.
- The CLI will use **Command Prompt** on Windows.
- Explicit instructions will ensure clarity for contributors, detailing file placements and commands.

---

## REFACTORING OUTLINE:

- **Separation of Concerns**: Replace global variables with structured classes (e.g., `TrackSettings`) for better modularity.
- **Database Integration**: Dynamically retrieve values using SQLModel to allow flexibility and scalability.
- **Decoupled Geometry**: Keep geometry logic in standalone modules, independent of the UI.
- **3D Export**: Leverage CadQuery for generating native STL files directly.
- **Modular Design**: Ensure timbers, chairs, and tracks are modularly designed for reusability and scalability.

---

## ATTRIBUTION:
To comply with GNU GPLv3, include prominent attribution in the code comments and documentation to Martin Wynne for his original work on Templot.

---

## FUTURE ENHANCEMENTS:

1. **Advanced Track Designs**:
   - Add curved tracks, turnout angles, and complex geometries (e.g., snap-fit designs).
2. **Enhanced Validation**:
   - Include STL inspection workflows for watertightness, inverted normals, and repair options.
3. **Programmatic Access**:
   - Introduce a REST API for automated track generation and configuration.
4. **Cloud Deployment**:
   - Plan for hosting and deploying the application on cloud platforms (e.g., AWS, DigitalOcean).

---

## END STATE:

A FastAPI-based, modular, and maintainable track design engine capable of generating STL files for REA-standard bullhead rail track. This includes integrated timbers and chairs, with the rail added manually post-printing. The SQLModel-backed database ensures flexibility in track configurations, forming the foundation for future enhancements.

---

## REFERENCES:
- [Templot GitHub Reference](https://github.com/Richard-Gnitnub/Templot5/blob/main/dxf_unit.pas)
- [FastAPI Documentation](https://fastapi.tiangolo.com/reference/templating/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/intro/)

---

## NOTES:

- Develop using Python 3.12.3 (latest version as of October 2023).
- Ensure proper attribution to Martin Wynne in compliance with GNU GPLv3.


---
## Core Application Functionality (MVP)
```
flowchart TD
    A[User Input] -->|Track Parameters| B[Input Validation]
    B -->|Check for Errors| C{Valid Input?}
    C -->|Yes| D[Fetch Data from Database]
    C -->|No| E[Return Error Message]
    D -->|Configurations Loaded| F[Process Geometry]
    F -->|Generate Timbers and Chairs| G[Create 3D Model with CadQuery]
    G -->|Convert to STL| H[STL Export]
    H -->|Save File| I[Provide Download Link]
    I -->|User Access| J[Download STL File]

    subgraph FastAPI Workflow
        B --> C --> D --> F
    end

    subgraph External Logic
        G --> H
    end

    subgraph Final Output
        I --> J
    end

```
---
## Future Enhancements 
```
flowchart TD
    A[User Input] -->|Advanced Parameters| B[Enhanced Validation]
    B -->|Check for Errors| C{Valid Input?}
    C -->|Yes| D[Fetch Advanced Data from Database]
    C -->|No| E[Return Error Message]
    D -->|Configurations Loaded| F[Process Advanced Geometry]
    F -->|Generate Curves, Turnouts, and Alternate Track Types| G[Create Advanced 3D Model with CadQuery]
    G -->|Convert to STL| H[STL Export]
    H --> I[Inspect STL File]
    I -->|Check for Issues| J{Issues Found?}
    J -->|Yes| K[Generate Inspection Report]
    K -->|User Opts to Repair| L[Run Mesh Repair Workflow]
    L --> M[Save Repaired STL File]
    J -->|No| N[Save Original STL File]
    M --> O[Provide Download Link]
    N --> O
    O --> P[User Access STL File or Report]

    subgraph Advanced Workflow
        F --> G --> H --> I --> J
        J --> K --> L --> M
        J --> N
    end

    subgraph Final Output
        O --> P
    end
```
---
## Core App Directory Structure

```
project/
├── track_app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # Database connection and session
│   ├── models.py            # SQLModel definitions
│   ├── routes/              # Modular route files
│   │   ├── chair_routes.py
│   │   ├── track_routes.py
│   │   ├── timber_routes.py
│   │   ├── stl_routes.py
│   ├── static/              # Static assets
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── admin_dashboard.html
│   │   ├── chairs_list.html
│   │   ├── chairs_form.html
│   │   ├── tracks_list.html
│   │   ├── tracks_form.html
│   │   ├── ...
│   ├── database.db          # SQLite database file (moved here)
├── alembic/                 # Alembic migrations
│   ├── versions/            # Migration scripts
│   ├── env.py               # Alembic environment file
│   ├── script.py.mako       # Migration script template
│   └── alembic.ini          # Alembic configuration file (root reference)
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose
└── .gitignore               # Files and folders to ignore

```
---